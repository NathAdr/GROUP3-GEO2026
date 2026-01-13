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
    "Purchase Order",
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

        st.subheader("Add New Purchase Order Data")

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

    elif menu == "Bahan Pendukung (Perintilan, Kancing, Benang, Retsleting, RIB DLL)":
        BASE_DIR = Path(__file__).resolve().parent.parent
        FILE_PATH = BASE_DIR / "DATA SUPPLIER KAIN - Bahan Baku Pendukung PO.csv"
    
        data = pd.read_csv(FILE_PATH)
        st.write(data)

        st.divider()

        st.subheader("Add New Purchase Order Data")

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
    
    elif menu == "Jasa Bordir":
        BASE_DIR = Path(__file__).resolve().parent.parent
        FILE_PATH = BASE_DIR / "DATA SUPPLIER KAIN - Jasa Bordir PO.csv"
    
        data = pd.read_csv(FILE_PATH)
        st.write(data)

        st.divider()

        st.subheader("Add New Purchase Order Data")

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
    
    elif menu == "Jasa Printing":
        BASE_DIR = Path(__file__).resolve().parent.parent
        FILE_PATH = BASE_DIR / "DATA SUPPLIER KAIN - Jasa Printing PO.csv"
    
        data = pd.read_csv(FILE_PATH)
        st.write(data)

        st.divider()

        st.subheader("Add New Purchase Order Data")

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
    
    elif menu == "Jasa DTF Sablon":
        BASE_DIR = Path(__file__).resolve().parent.parent
        FILE_PATH = BASE_DIR / "DATA SUPPLIER KAIN - Jasa DTF Sablon PO.csv"
    
        data = pd.read_csv(FILE_PATH)
        st.write(data)

        st.divider()

        st.subheader("Add New Purchase Order Data")

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
    
    elif menu == "Jasa Sublim":
        BASE_DIR = Path(__file__).resolve().parent.parent
        FILE_PATH = BASE_DIR / "DATA SUPPLIER KAIN - Jasa Sublim PO.csv"
    
        data = pd.read_csv(FILE_PATH)
        st.write(data)

        st.divider()

        st.subheader("Add New Purchase Order Data")

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
    
    elif menu == "Jasa Distribusi":
        BASE_DIR = Path(__file__).resolve().parent.parent
        FILE_PATH = BASE_DIR / "DATA SUPPLIER KAIN - Jasa Distribusi PO.csv"
    
        data = pd.read_csv(FILE_PATH)
        st.write(data)

        st.divider()

        st.subheader("Add New Purchase Order Data")

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
    
    elif menu == "ATK":
        BASE_DIR = Path(__file__).resolve().parent.parent
        FILE_PATH = BASE_DIR / "DATA SUPPLIER KAIN - ATK PO.csv"
    
        data = pd.read_csv(FILE_PATH)
        st.write(data)

        st.divider()

        st.subheader("Add New Purchase Order Data")

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
      FILE_PATH = BASE_DIR / "Supplier Utama.csv"
    
      data = pd.read_csv(FILE_PATH)
      st.write(data)

      st.subheader("Add New Supplier Data")

      with st.form("add_utama", clear_on_submit=True):
          supplier = st.text_input("Nama Supplier & Penyedia Jasa")
          address = st.text_input("Alamat")

          submitted = st.form_submit_button("Simpan")

      if submitted:
          if supplier.strip() == "" or address.strip() == "":
              st.error("Nama Supplier dan Alamat wajib diisi!")
          else:
              new_row = pd.DataFrame([[
                  supplier,
                  address
              ]], columns=data.columns)  

              data = pd.concat([data, new_row], ignore_index=True)
              data.to_csv(FILE_PATH, index=False)

              st.rerun()

    elif menu == "Bahan Pendukung (Perintilan, Kancing, Benang, Retsleting, RIB DLL)": 
      BASE_DIR = Path(__file__).resolve().parent.parent
      FILE_PATH = BASE_DIR / "Supplier Pendukung.csv"
    
      data = pd.read_csv(FILE_PATH)
      st.write(data)

      st.subheader("Add New Supplier Data")

      with st.form("add_sup", clear_on_submit=True):
          supplier = st.text_input("Nama Supplier & Penyedia Jasa")
          address = st.text_input("Alamat")

          submitted = st.form_submit_button("Simpan")

      if submitted:
          if supplier.strip() == "" or address.strip() == "":
              st.error("Nama Supplier dan Alamat wajib diisi!")
          else:
              new_row = pd.DataFrame([[
                  supplier,
                  address
              ]], columns=data.columns)  

              data = pd.concat([data, new_row], ignore_index=True)
              data.to_csv(FILE_PATH, index=False)

              st.rerun()


    elif menu == "Jasa Bordir": 
      BASE_DIR = Path(__file__).resolve().parent.parent
      FILE_PATH = BASE_DIR / "Jasa Bordir.csv"
    
      data = pd.read_csv(FILE_PATH)
      st.write(data)

      st.subheader("Add New Supplier Data")

      with st.form("add_bor", clear_on_submit=True):
          supplier = st.text_input("Nama Supplier & Penyedia Jasa")
          address = st.text_input("Alamat")

          submitted = st.form_submit_button("Simpan")

      if submitted:
          if supplier.strip() == "" or address.strip() == "":
              st.error("Nama Supplier dan Alamat wajib diisi!")
          else:
              new_row = pd.DataFrame([[
                  supplier,
                  address
              ]], columns=data.columns)  

              data = pd.concat([data, new_row], ignore_index=True)
              data.to_csv(FILE_PATH, index=False)

              st.rerun()
    


    elif menu == "Jasa Printing": 
      BASE_DIR = Path(__file__).resolve().parent.parent
      FILE_PATH = BASE_DIR / "Jasa Printing.csv"
    
      data = pd.read_csv(FILE_PATH)
      st.write(data)

      st.subheader("Add New Supplier Data")

      with st.form("add_pri", clear_on_submit=True):
          supplier = st.text_input("Nama Supplier & Penyedia Jasa")
          address = st.text_input("Alamat")

          submitted = st.form_submit_button("Simpan")

      if submitted:
          if supplier.strip() == "" or address.strip() == "":
              st.error("Nama Supplier dan Alamat wajib diisi!")
          else:
              new_row = pd.DataFrame([[
                  supplier,
                  address
              ]], columns=data.columns)  

              data = pd.concat([data, new_row], ignore_index=True)
              data.to_csv(FILE_PATH, index=False)

              st.rerun()

    
    elif menu == "Jasa DTF Sablon": 
      BASE_DIR = Path(__file__).resolve().parent.parent
      FILE_PATH = BASE_DIR / "Jasa DTF Sablon.csv"
    
      data = pd.read_csv(FILE_PATH)
      st.write(data)

      st.subheader("Add New Supplier Data")

      with st.form("add_sab", clear_on_submit=True):
          supplier = st.text_input("Nama Supplier & Penyedia Jasa")
          address = st.text_input("Alamat")

          submitted = st.form_submit_button("Simpan")

      if submitted:
          if supplier.strip() == "" or address.strip() == "":
              st.error("Nama Supplier dan Alamat wajib diisi!")
          else:
              new_row = pd.DataFrame([[
                  supplier,
                  address
              ]], columns=data.columns)  

              data = pd.concat([data, new_row], ignore_index=True)
              data.to_csv(FILE_PATH, index=False)

              st.rerun()
    

    elif menu == "Jasa Sublim": 
      BASE_DIR = Path(__file__).resolve().parent.parent
      FILE_PATH = BASE_DIR / "Jasa Sublim.csv"
    
      data = pd.read_csv(FILE_PATH)
      st.write(data)

      st.subheader("Add New Supplier Data")

      with st.form("add_sub", clear_on_submit=True):
          supplier = st.text_input("Nama Supplier & Penyedia Jasa")
          address = st.text_input("Alamat")

          submitted = st.form_submit_button("Simpan")

      if submitted:
          if supplier.strip() == "" or address.strip() == "":
              st.error("Nama Supplier dan Alamat wajib diisi!")
          else:
              new_row = pd.DataFrame([[
                  supplier,
                  address
              ]], columns=data.columns)  

              data = pd.concat([data, new_row], ignore_index=True)
              data.to_csv(FILE_PATH, index=False)

              st.rerun()
    

    elif menu == "Jasa Distribusi": 
      BASE_DIR = Path(__file__).resolve().parent.parent
      FILE_PATH = BASE_DIR / "Jasa Distribusi.csv"
    
      data = pd.read_csv(FILE_PATH)
      st.write(data)

      st.subheader("Add New Supplier Data")

      with st.form("add_dis", clear_on_submit=True):
          supplier = st.text_input("Nama Supplier & Penyedia Jasa")
          address = st.text_input("Alamat")

          submitted = st.form_submit_button("Simpan")

      if submitted:
          if supplier.strip() == "" or address.strip() == "":
              st.error("Nama Supplier dan Alamat wajib diisi!")
          else:
              new_row = pd.DataFrame([[
                  supplier,
                  address
              ]], columns=data.columns)  

              data = pd.concat([data, new_row], ignore_index=True)
              data.to_csv(FILE_PATH, index=False)

              st.rerun()
    

    elif menu == "ATK": 
      BASE_DIR = Path(__file__).resolve().parent.parent
      FILE_PATH = BASE_DIR / "ATK.csv"
    
      data = pd.read_csv(FILE_PATH)
      st.write(data)

      st.subheader("Add New Supplier Data")

      with st.form("add_atk", clear_on_submit=True):
          supplier = st.text_input("Nama Supplier & Penyedia Jasa")
          address = st.text_input("Alamat")

          submitted = st.form_submit_button("Simpan")

      if submitted:
          if supplier.strip() == "" or address.strip() == "":
              st.error("Nama Supplier dan Alamat wajib diisi!")
          else:
              new_row = pd.DataFrame([[
                  supplier,
                  address
              ]], columns=data.columns)  

              data = pd.concat([data, new_row], ignore_index=True)
              data.to_csv(FILE_PATH, index=False)

              st.rerun()

    
    
