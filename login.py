import streamlit as st
from pyrebase  import pyrebase

def app():
    firebase_config = {
        "apiKey": st.secrets["firebase"]["apiKey"],
        "authDomain": st.secrets["firebase"]["authDomain"],
        "databaseURL": st.secrets["firebase"]["databaseURL"],
        "projectId": st.secrets["firebase"]["projectId"],
        "storageBucket": st.secrets["firebase"]["storageBucket"],
        "messagingSenderId": st.secrets["firebase"]["messagingSenderId"],
        "appId": st.secrets["firebase"]["appId"]
    }

    firebase = pyrebase.initialize_app(firebase_config)
    auth = firebase.auth()
    st.image("onepager-logo.png")
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')

    if st.button('Log In'):
        try:
            user = auth.sign_in_with_email_and_password(username, password)
            st.session_state['logged_in'] = True
           
        except:
            st.error('Invalid username/password')    
