import streamlit as st

# ===============================
# Import prediction functions
# ===============================

from model import (
    predict_jumlah,
    predict_worker_on_time,
    predict_worker_quantity,
)

# ===============================
# Page configuration
# ===============================

st.set_page_config(
    page_title="📈 Koperasi Prediction",
    layout="wide"
)

# ===============================
# Custom tab styling
# ===============================

st.markdown("""
<style>
/* Tab container */
div[data-testid="stTabs"] {
    width: 100%;
    margin-top: 0.5rem;
}

/* Tab list */
div[data-testid="stTabs"] > div > div {
    gap: 0.25rem;
}

/* Individual tab buttons */
button[data-testid="stTab"] {
    flex: 1;
    padding: 0.6rem 1rem;
    font-size: 15px;
    font-weight: 600;
    border-radius: 8px 8px 0 0;
    background-color: #1f2937; /* dark gray */
    color: #d1d5db;
    border: 1px solid #374151;
}

/* Hover */
button[data-testid="stTab"]:hover {
    background-color: #374151;
    color: white;
}

/* Active tab */
button[data-testid="stTab"][aria-selected="true"] {
    background-color: #f97316; /* orange */
    color: black;
    border-bottom: none;
}

/* Reduce top padding so orange bar feels secondary */
div.block-container {
    padding-top: 3rem;
}
</style>
""", unsafe_allow_html=True)


# ===============================
# Tabs
# ===============================

tabs = st.tabs([
    "💰 Revenue Prediction",
    "⏱️ On-Time Reliability",
    "📦 Quantity Reliability"
])

# ---------- Dropdown options ----------

KECAMATAN_OPTIONS = [
    "Kenjeran", "Simokerto", "Semampir", "Sukolilo", "Krembangan",
    "Rungkut", "Sukomanunggal", "Bulak", "Sawahan", "Mulyorejo",
    "Gubeng", "Tambak Sari", "Pabean Cantian", "Unknown"
]

STATUS_MISKIN_OPTIONS = [
    "Miskin Non Ekstrem",
    "Non Miskin",
    "Pramiskin",
    "Unknown"
]

SPESIALIS_OPTIONS = [
    "Semua",
    "Seragam",
    "Unknown"
]


# ======================================================
# TAB 1 — Revenue Prediction
# ======================================================

with tabs[0]:
    st.markdown(
    "<div style='font-size:13px; color:#9ca3af;'>Current module</div>"
    "<div style='font-size:20px; font-weight:600;'>💰 Revenue Prediction</div>",
    unsafe_allow_html=True
)
    
    # st.header("💰 Revenue Prediction")
    # st.write("Estimate expected transaction revenue based on order details.")

    with st.form("revenue_form"):
        qty = st.number_input("Quantity (QTY)", min_value=1, value=100)
        harga = st.number_input("Unit Price (HARGA)", min_value=1, value=10_000)
        satuan = st.selectbox("Unit (SATUAN)", ["pcs", "stell", "paket"])

        submitted = st.form_submit_button("Predict Revenue")

    if submitted:
        pred = predict_jumlah(
            qty=qty,
            harga=harga,
            satuan=satuan
        )

        st.success(f"💰 **Predicted Revenue:** Rp {pred:,.0f}")


# ======================================================
# TAB 2 — Worker On-Time Reliability
# ======================================================

with tabs[1]:
    st.markdown(
    "<div style='font-size:13px; color:#9ca3af;'>Current module</div>"
    "<div style='font-size:20px; font-weight:600;'>⏱️ On-Time Reliability</div>",
    unsafe_allow_html=True
)

    # st.header("⏱️ On-Time Reliability Prediction")
    # st.write("Assess the likelihood that a worker delivers on time.")

    with st.form("ontime_form"):
        usia = st.number_input("Age (Usia)", min_value=18, max_value=70, value=35)

        kerapian_bool = st.selectbox("Tidiness (Kerapian)", [True, False])
        komitmen_bool = st.selectbox("Commitment (Komitmen)", [True, False])

        kecamatan = st.selectbox("Kecamatan", KECAMATAN_OPTIONS)
        status_keluarga_miskin = st.selectbox(
            "Status Keluarga Miskin",
            STATUS_MISKIN_OPTIONS
        )

        submitted = st.form_submit_button("Evaluate On-Time Risk")

    if submitted:
        result = predict_worker_on_time(
            usia=usia,
            kerapian=int(kerapian_bool),
            komitmen=int(komitmen_bool),
            kecamatan=kecamatan,
            status_keluarga_miskin=status_keluarga_miskin,
        )

        st.subheader(f"{result['icon']} {result['category']}")
        st.metric(
            "Probability On-Time",
            f"{result['probability'] * 100:.1f}%"
        )



# ======================================================
# TAB 3 — Worker Quantity Reliability
# ======================================================

with tabs[2]:
    st.markdown(
    "<div style='font-size:13px; color:#9ca3af;'>Current module</div>"
    "<div style='font-size:20px; font-weight:600;'>📦 Quantity Reliability Prediction</div>",
    unsafe_allow_html=True
)
    # st.header("📦 Quantity Reliability Prediction")
    # st.write("Assess the likelihood that a worker delivers the right quantity.")

    with st.form("quantity_form"):
        usia = st.number_input("Age (Usia)", min_value=18, max_value=70, value=35)

        kerapian_bool = st.selectbox("Tidiness (Kerapian)", [True, False])
        komitmen_bool = st.selectbox("Commitment (Komitmen)", [True, False])
        ketepatan_waktu_bool = st.selectbox("On-Time History", [True, False])

        kecamatan = st.selectbox("Kecamatan", KECAMATAN_OPTIONS)
        status_keluarga_miskin = st.selectbox(
            "Status Keluarga Miskin",
            STATUS_MISKIN_OPTIONS
        )
        spesialis = st.selectbox("Specialisation", SPESIALIS_OPTIONS)

        submitted = st.form_submit_button("Evaluate Quantity Risk")

    if submitted:
        result = predict_worker_quantity(
            usia=usia,
            kerapian=int(kerapian_bool),
            komitmen=int(komitmen_bool),
            ketepatan_waktu=int(ketepatan_waktu_bool),
            kecamatan=kecamatan,
            status_keluarga_miskin=status_keluarga_miskin,
            spesialis=spesialis,
        )

        st.subheader(f"{result['icon']} {result['category']}")
        st.metric(
            "Probability Correct Quantity",
            f"{result['probability'] * 100:.1f}%"
        )

