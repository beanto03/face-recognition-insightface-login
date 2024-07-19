# authentication.py

import streamlit as st

# Dummy user database (replace with actual user database in a real application)
users = {
    "amir": {
        "name": "Amir",
        "password": "123"  # Replace with hashed password in a real application
    }
}

def init_session_state():
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False

def authenticate(username, password):
    """ Function to authenticate user based on username and password. """
    if username in users:
        if password == users[username]["password"]:
            return True
    return False
