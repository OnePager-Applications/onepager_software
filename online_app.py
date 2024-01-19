
import streamlit as st
import login
import main_app

st.set_page_config(layout='wide')
hide_streamlit_style = """
            <style>
            [data-testid="stToolbar"] {visibility: hidden !important;}
            footer {visibility: hidden !important;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# Create login form
if not st.session_state['logged_in']:
    login.app()
else:
    main_app.app()