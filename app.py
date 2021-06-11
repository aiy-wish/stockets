import about
import main
import streamlit as st

PAGES = {
    "About": about,
    "Stock Predictor": main
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
