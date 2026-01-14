"""
model.py

This module trains and exposes 3 predictive models:

1. Transaction value prediction (JUMLAH) using Linear Regression
2. Worker on-time reliability prediction (Ketepatan Waktu)
3. Worker quantity reliability prediction (Quantity)

Each model is trained ONCE at import time and exposes
a clean prediction function for inference.
"""

# ======================================================
# Imports
# ======================================================

import pandas as pd
import numpy as np
from pathlib import Path

from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# ======================================================
# Base paths
# ======================================================

BASE_DIR = Path(__file__).resolve().parent.parent

# ======================================================
# 1️⃣ JUMLAH (Transaction Value) Model
# ======================================================

FILE_PATH_JUMLAH = "GEO_data.xlsx"
df_jumlah = pd.read_excel(FILE_PATH_JUMLAH)

# --- Clean numeric columns ---
for col in ["QTY", "HARGA", "JUMLAH"]:
    df_jumlah[col] = pd.to_numeric(df_jumlah[col], errors="coerce")

df_jumlah = df_jumlah[
    (df_jumlah["JUMLAH"] > 0) &
    (df_jumlah["QTY"] > 0)
].reset_index(drop=True)

# --- Encode SATUAN ---
df_jumlah = pd.get_dummies(df_jumlah, columns=["SATUAN"], drop_first=True)
satuan_columns = [c for c in df_jumlah.columns if c.startswith("SATUAN_")]

# --- Impute missing price ---
price_imputer = SimpleImputer(strategy="median")
df_jumlah["HARGA"] = price_imputer.fit_transform(df_jumlah[["HARGA"]])

# --- Log transform ---
df_jumlah["log_QTY"] = np.log(df_jumlah["QTY"])
df_jumlah["log_HARGA"] = np.log(df_jumlah["HARGA"])
df_jumlah["log_JUMLAH"] = np.log(df_jumlah["JUMLAH"])

X_jumlah = df_jumlah[["log_QTY", "log_HARGA"] + satuan_columns]
y_jumlah = df_jumlah["log_JUMLAH"]

# --- Train model ---
model_jumlah = LinearRegression()
model_jumlah.fit(X_jumlah, y_jumlah)

# --- Medians for inference fallback ---
log_qty_median = np.log(df_jumlah["QTY"].median())
log_harga_median = np.log(df_jumlah["HARGA"].median())


def predict_jumlah(qty=None, harga=None, satuan="pcs"):
    """
    Predict total transaction value (JUMLAH).
    """

    log_qty = np.log(qty) if qty is not None else log_qty_median
    log_harga = np.log(harga) if harga is not None else log_harga_median

    input_dict = {
        "log_QTY": log_qty,
        "log_HARGA": log_harga,
    }

    # Initialise SATUAN dummies
    for col in satuan_columns:
        input_dict[col] = 0

    if satuan != "pcs":
        col_name = f"SATUAN_{satuan}"
        if col_name in input_dict:
            input_dict[col_name] = 1

    input_df = pd.DataFrame([input_dict])
    log_pred = model_jumlah.predict(input_df)[0]

    return float(np.exp(log_pred))


# ======================================================
# 2️⃣ Worker On-Time Reliability Model
# ======================================================

FILE_PATH_WORKER = "Koperasi Sumber Mulia Barokah Mapping.csv"
df_worker = pd.read_csv(FILE_PATH_WORKER)

# --- Type casting ---
for col in ["Kerapian", "Komitmen", "Ketepatan Waktu"]:
    df_worker[col] = df_worker[col].astype(int)

# --- Handle missing categories ---
df_worker["Kecamatan"] = df_worker["Kecamatan"].fillna("Unknown")
df_worker["Status Keluarga Miskin"] = df_worker["Status Keluarga Miskin"].fillna("Unknown")

# --- One-hot encoding ---
df_worker = pd.get_dummies(
    df_worker,
    columns=["Kecamatan", "Status Keluarga Miskin"],
    drop_first=True
)

features_ontime = (
    ["Usia", "Kerapian", "Komitmen"]
    + [c for c in df_worker.columns if c.startswith("Kecamatan_")]
    + [c for c in df_worker.columns if c.startswith("Status Keluarga Miskin_")]
)

X_ontime = df_worker[features_ontime]
y_ontime = df_worker["Ketepatan Waktu"]

X_train, _, y_train, _ = train_test_split(
    X_ontime, y_ontime, test_size=0.2, stratify=y_ontime, random_state=42
)

model_ontime = Pipeline([
    ("scaler", StandardScaler()),
    ("clf", LogisticRegression(class_weight={0: 2, 1: 1}, max_iter=1000))
])

model_ontime.fit(X_train, y_train)


def predict_worker_on_time(
    usia, kerapian, komitmen, kecamatan, status_keluarga_miskin
):
    """
    Predict worker on-time reliability.
    """

    input_dict = {
        "Usia": usia,
        "Kerapian": int(kerapian),
        "Komitmen": int(komitmen),
    }

    # Initialise all dummy columns
    for col in features_ontime:
        if col not in input_dict:
            input_dict[col] = 0

    if f"Kecamatan_{kecamatan}" in input_dict:
        input_dict[f"Kecamatan_{kecamatan}"] = 1

    if f"Status Keluarga Miskin_{status_keluarga_miskin}" in input_dict:
        input_dict[f"Status Keluarga Miskin_{status_keluarga_miskin}"] = 1

    input_df = pd.DataFrame([input_dict])[features_ontime]
    prob = model_ontime.predict_proba(input_df)[0, 1]

    if prob >= 0.70:
        return {"category": "On Track", "icon": "🟢", "probability": round(prob, 3)}
    elif prob >= 0.40:
        return {"category": "Needs Attention", "icon": "🟡", "probability": round(prob, 3)}
    else:
        return {"category": "High Risk of Delay", "icon": "🔴", "probability": round(prob, 3)}


# ======================================================
# 3️⃣ Worker Quantity Reliability Model
# ======================================================

df_worker["Spesialis"] = df_worker["Spesialis"].fillna("Unknown")

df_worker = pd.get_dummies(
    df_worker,
    columns=["Spesialis"],
    drop_first=True
)

features_quantity = (
    ["Usia", "Kerapian", "Komitmen", "Ketepatan Waktu"]
    + [c for c in df_worker.columns if c.startswith("Kecamatan_")]
    + [c for c in df_worker.columns if c.startswith("Status Keluarga Miskin_")]
    + [c for c in df_worker.columns if c.startswith("Spesialis_")]
)

X_qty = df_worker[features_quantity]
y_qty = df_worker["Quantity"]

X_train, _, y_train, _ = train_test_split(
    X_qty, y_qty, test_size=0.2, stratify=y_qty, random_state=42
)

model_quantity = Pipeline([
    ("scaler", StandardScaler()),
    ("clf", LogisticRegression(class_weight={0: 2, 1: 1}, max_iter=1000))
])

model_quantity.fit(X_train, y_train)


def predict_worker_quantity(
    usia, kerapian, komitmen, ketepatan_waktu,
    kecamatan, status_keluarga_miskin, spesialis
):
    """
    Predict worker quantity reliability.
    """

    input_dict = {
        "Usia": usia,
        "Kerapian": int(kerapian),
        "Komitmen": int(komitmen),
        "Ketepatan Waktu": int(ketepatan_waktu),
    }

    for col in features_quantity:
        if col not in input_dict:
            input_dict[col] = 0

    for prefix, value in [
        ("Kecamatan", kecamatan),
        ("Status Keluarga Miskin", status_keluarga_miskin),
        ("Spesialis", spesialis),
    ]:
        col_name = f"{prefix}_{value}"
        if col_name in input_dict:
            input_dict[col_name] = 1

    input_df = pd.DataFrame([input_dict])[features_quantity]
    prob = model_quantity.predict_proba(input_df)[0, 1]

    if prob >= 0.75:
        return {"category": "Consistent Output", "icon": "🟢", "probability": round(prob, 3)}
    elif prob >= 0.45:
        return {"category": "Monitor Closely", "icon": "🟡", "probability": round(prob, 3)}
    else:
        return {"category": "High Quantity Risk", "icon": "🔴", "probability": round(prob, 3)}
