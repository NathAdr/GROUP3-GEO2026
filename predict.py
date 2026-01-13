import streamlit as st
from model import predict_jumlah

st.set_page_config(page_title="Revenue Prediction", layout="wide")

st.title("📊 Revenue Prediction Tool")

st.write("Enter order details to estimate expected revenue.")

# ---------- Input form ----------

with st.form("prediction_form"):
    qty = st.number_input("Quantity (QTY)", min_value=1, value=100)
    harga = st.number_input("Unit Price (HARGA)", min_value=1, value=10000)
    satuan = st.selectbox("Unit (SATUAN)", ["pcs", "stell", "paket"])

    submitted = st.form_submit_button("Predict Revenue")

# ---------- Prediction ----------

if submitted:
    pred = predict_jumlah(
        qty=qty if qty > 0 else None,
        harga=harga if harga > 0 else None,
        satuan=satuan
    )

    st.success(f"💰 Predicted Revenue: **Rp {pred:,.0f}**")

