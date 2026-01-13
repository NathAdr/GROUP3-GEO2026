import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import date

st.set_page_config(layout="wide")

st.markdown("""
<style>
button[data-testid="stTab"] {
    flex: 1;
    justify-content: center;
    font-size: 16px;
    font-weight: 600;
}
div.block-container { padding-top: 1rem; }
</style>
""", unsafe_allow_html=True)

def parse_rupiah(text):
    if not text:
        return 0
    try:
        cleaned = (
            text.replace("Rp", "")
                .replace("rp", "")
                .replace(".", "")
                .replace(",", "")
                .strip()
        )
        return int(cleaned)
    except ValueError:
        return None


def load_and_display_data(file_path, is_po=True):
    if Path(file_path).exists():
        df = pd.read_csv(file_path)
        df.columns = df.columns.str.strip()

        if is_po and "Harga" in df.columns:
            df["Harga"] = pd.to_numeric(df["Harga"], errors="coerce").fillna(0)

            st.dataframe(
                df,
                column_config={
                    "Harga": st.column_config.NumberColumn(
                        "Harga",
                        format="Rp %,.0f",
                        help="Harga dalam Rupiah"
                    )
                },
                hide_index=True,
                use_container_width=True
            )
        else:
            st.dataframe(df, hide_index=True, use_container_width=True)

        return df

    return pd.DataFrame()


tabs = st.tabs([
    "Purchase Order",
    "Receive Item",
    "Purchase Invoice",
    "Purchase Payment",
    "Supplier"
])

with tabs[0]:
    po_menu = st.selectbox(
        "Kategori PO",
        [
            "Bahan Baku Utama (Kain)",
            "Bahan Pendukung",
            "Jasa Bordir",
            "Jasa Printing",
            "Jasa DTF Sablon",
            "Jasa Sublim",
            "Jasa Distribusi",
            "ATK"
        ],
        key="sb_po"
    )

    po_files = {
        "Bahan Baku Utama (Kain)": "DATA SUPPLIER KAIN.csv",
        "Bahan Pendukung": "DATA SUPPLIER KAIN - Bahan Baku Pendukung PO.csv",
        "Jasa Bordir": "DATA SUPPLIER KAIN - Jasa Bordir PO.csv",
        "Jasa Printing": "DATA SUPPLIER KAIN - Jasa Printing PO.csv",
        "Jasa DTF Sablon": "DATA SUPPLIER KAIN - Jasa DTF Sablon PO.csv",
        "Jasa Sublim": "DATA SUPPLIER KAIN - Jasa Sublim PO.csv",
        "Jasa Distribusi": "DATA SUPPLIER KAIN - Jasa Distribusi PO.csv",
        "ATK": "DATA SUPPLIER KAIN - ATK PO.csv"
    }

    BASE_DIR = Path(__file__).resolve().parent.parent
    path_po = BASE_DIR / po_files[po_menu]
    data_po = load_and_display_data(path_po, is_po=True)

    st.divider()

    with st.form("form_po", clear_on_submit=True):
        col1, col2 = st.columns(2)

        tanggal = col1.date_input("Tanggal", date.today())
        supplier = col1.text_input("Supplier")
        item = col2.text_input("Item")
        qty = col2.text_input("Qty")

        harga_text = st.text_input(
            "Harga (Rp)",
            placeholder="Contoh: Rp 150.000 atau 150000"
        )

        ket = st.text_area("Keterangan")

        if st.form_submit_button("Simpan PO"):
            harga = parse_rupiah(harga_text)

            if not supplier or not item:
                st.error("Supplier dan Item harus diisi")
            elif harga is None:
                st.error("Format harga tidak valid")
            else:
                new_row = [
                    tanggal.strftime("%Y-%m-%d"),
                    supplier,
                    item,
                    qty,
                    harga,
                    ket
                ]

                new_data = pd.DataFrame([new_row], columns=data_po.columns)
                pd.concat([data_po, new_data], ignore_index=True).to_csv(path_po, index=False)
                st.rerun()

with tabs[4]:
    sup_menu = st.selectbox(
        "Kategori Supplier",
        [
            "Bahan Baku Utama (Kain)",
            "Bahan Pendukung",
            "Jasa Bordir",
            "Jasa Printing",
            "Jasa DTF Sablon",
            "Jasa Sublim",
            "Jasa Distribusi",
            "ATK"
        ],
        key="sb_sup"
    )

    sup_files = {
        "Bahan Baku Utama (Kain)": "Supplier Utama.csv",
        "Bahan Pendukung": "Supplier Pendukung.csv",
        "Jasa Bordir": "Jasa Bordir.csv",
        "Jasa Printing": "Jasa Printing.csv",
        "Jasa DTF Sablon": "Jasa DTF Sablon.csv",
        "Jasa Sublim": "Jasa Sublim.csv",
        "Jasa Distribusi": "Jasa Distribusi.csv",
        "ATK": "ATK.csv"
    }

    path_sup = BASE_DIR / sup_files[sup_menu]
    data_sup = load_and_display_data(path_sup, is_po=False)

    st.divider()

    with st.form("form_sup", clear_on_submit=True):
        s_nama = st.text_input("Nama Supplier")
        s_alamat = st.text_input("Alamat")

        if st.form_submit_button("Simpan Supplier"):
            if s_nama:
                new_sup = pd.DataFrame(
                    [[s_nama, s_alamat]],
                    columns=data_sup.columns
                )
                pd.concat([data_sup, new_sup], ignore_index=True).to_csv(path_sup, index=False)
                st.rerun()
