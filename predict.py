import streamlit as st
from model import predict_jumlah


st.markdown("""
<style>
div[data-testid="stTabs"] {
    width: 100%;
}

div[data-testid="stTabs"] > div > div {
    display: flex;
}

button[data-testid="stTab"] {
    flex: 1;
    justify-content: center;
    font-size: 16px;
    font-weight: 600;
}

div.block-container {
    padding-top: 1rem;
}
</style>
""", unsafe_allow_html=True)

tabs = st.tabs([
    "Overview",
    "Statistics",
    "Reports"
])

with tabs[0]:
    st.subheader("Overview")
    st.write("Overview content here")

with tabs[1]:
    st.subheader("Statistics")
    st.write("Statistics content here")

with tabs[2]:
    st.subheader("Reports")
    st.write("Reports content here")


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

