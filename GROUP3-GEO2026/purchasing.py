import streamlit as st
import numpy as np
import pandas as pd
from pathlib import Path
from datetime import date

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
    "Pre-Order",
    "Receive Item",
    "Purchase Invoice",
    "Purchase Payment",
    "Supplier"
])

with tabs[0]:
    menu = st.selectbox(
       "", ["Bahan Baku Utama (Kain)", "Bahan Pendukung (Perintilan, Kancing, Benang, Retsleting, RIB DLL)", 
            "Jasa Bordir", "Jasa Printing", "Jasa DTF Sablon", "Jasa Sublim", "Jasa Distribusi", "ATK"], key="preorder"
       ) 

    if menu == "Bahan Baku Utama (Kain)": 
      BASE_DIR = Path(__file__).resolve().parent.parent
      FILE_PATH = BASE_DIR / "DATA SUPPLIER KAIN.csv"
    
      data = pd.read_csv(FILE_PATH)
      st.write(data)

      st.divider()

      st.subheader("Add New Supplier Data")

      with st.form("add_purchase", clear_on_submit=True):
          tanggal = st.date_input("Tanggal Pembelian", date.today())
          supplier = st.text_input("Nama Supplier & Penyedia Jasa")
          item = st.text_input("Item")
          qty = st.text_input("Qty")
          harga = st.number_input("Harga", min_value=0, step=1000)
          keterangan = st.text_area("Keterangan")

          submitted = st.form_submit_button("Simpan")

      if submitted:
          if supplier.strip() == "" or item.strip() == "":
              st.error("Nama Supplier dan Item wajib diisi!")
          else:
              new_row = pd.DataFrame([[
                  tanggal.strftime("%Y-%m-%d"),
                  supplier,
                  item,
                  qty,
                  harga,
                  keterangan
              ]], columns=data.columns)  

              data = pd.concat([data, new_row], ignore_index=True)
              data.to_csv(FILE_PATH, index=False)

              st.rerun()

with tabs[1]:
    st.subheader("Receive Item")
    st.write("Receive Item content here")

with tabs[2]:
    st.subheader("Purchase Invoice")
    st.write("Purchase Invoice content here")

with tabs[3]:
    st.subheader("Purchase Payment")
    st.write("Purchase Payment content here")

with tabs[4]:
    menu = st.selectbox(
       "", ["Bahan Baku Utama (Kain)", "Bahan Pendukung (Perintilan, Kancing, Benang, Retsleting, RIB DLL)", 
            "Jasa Bordir", "Jasa Printing", "Jasa DTF Sablon", "Jasa Sublim", "Jasa Distribusi", "ATK"], key="supplier"
       ) 

    if menu == "Bahan Baku Utama (Kain)": 
      BASE_DIR = Path(__file__).resolve().parent.parent
      FILE_PATH = BASE_DIR / "Nama Supplier.csv"
    
      data = pd.read_csv(FILE_PATH)
      st.write(data)



    elif menu == "Bahan Pendukung (Perintilan, Kancing, Benang, Retsleting, RIB DLL)": 
      st.write("Inventory Taking Order content here")
  

    
    
