import streamlit as st

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
    st.subheader("Customer")
    st.write("Customer content here")
