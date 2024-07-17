# Home.py

import streamlit as st

st.set_page_config(page_title='Login', page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)
# Dummy user database (replace with actual user database in a real application)
users = {
    "amir": {
        "name": "Amir",
        "password": "123"# Replace with hashed password in a real application
    }
}

def main():
    st.header('Attendance System using Face Recognition')

    with st.spinner("Loading Models and Connecting to Redis db ..."):
        # Perform operations needed for homepage after successful login
        import pages.face_rec  # You can import additional modules or perform operations here
        st.success('Model loaded successfully')
        st.success('Redis db successfully connected')

if __name__ == '__main__':
    main()
