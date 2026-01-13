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
