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
    "Other Payment",
    "Other Deposit",
    "Bank Statement"
])

with tabs[0]:
    st.subheader("Other Payment")
    st.write("Other Payment content here")

with tabs[1]:
    st.subheader("Other Deposit")
    st.write("Other Deposit content here")

with tabs[2]:
    st.subheader("Bank Statement")
    st.write("Bank Statement content here")
