import streamlit as st
from pathlib import Path
import pandas as pd

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
    "Sales Order",
    "Delivery Order",
    "Sales Invoice",
    "Sales Receipt",
    "Customer"
])

with tabs[0]:
    st.subheader("Sales Order")
    st.write("Sales Order content here")

with tabs[1]:
    st.subheader("Delivery Order")
    st.write("Delivery Order content here")

with tabs[2]:
    st.subheader("Sales Invoice")
    st.write("Sales Invoice content here")

with tabs[3]:
    st.subheader("Sales Receipt")
    st.write("Sales Receipt content here")

with tabs[4]:
    BASE_DIR = Path(__file__).resolve().parent.parent
    FILE_PATH = BASE_DIR / "Customer.csv"
    
    data = pd.read_csv(FILE_PATH)
    data['Balance'] = pd.to_numeric(data['Balance'], errors='coerce')

    # buat copy untuk tampilan
    data_display = data.copy()
    data_display['Balance'] = data_display['Balance'].apply(
        lambda x: f"Rp {x:,.0f}".replace(',', '.') if not pd.isna(x) else "-"
    )

    st.write(data_display)


    st.subheader("Add New Customer Data")

    with st.form("add_cus", clear_on_submit=True):
        cus = st.text_input("Nama Customer")
        number = st.text_input("Contact Info")
        balance = st.number_input("Balance", step=1000)

        submitted = st.form_submit_button("Simpan")

    if submitted:
        if cus.strip() == "":
            st.error("Nama Customer Wajib diisi!")
        else:
            new_row = pd.DataFrame([[
                cus,
                number,
                balance
            ]], columns=data.columns)  

            data = pd.concat([data, new_row], ignore_index=True)
            data.to_csv(FILE_PATH, index=False)

            st.rerun()
