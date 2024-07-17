# login.py

import streamlit as st
from authentication import authenticate, init_session_state
from pages.Home import main as home_page  # Import the main function from Home.py

def main():
    st.markdown(
        """
        <style>
            [data-testid="collapsedControl"] {
                display: none
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Initialize session state
    init_session_state()

    st.title('User Login')

    username = st.text_input('Username')
    password = st.text_input('Password', type='password')

    if st.button('Login'):
        if username == "" or password == "":
            st.error("Please enter both username and password.")
        else:
            if authenticate(username, password):
                st.success(f'Logged in as {username}')

                # Update session state upon successful login
                st.session_state.authenticated = True
            else:
                st.error('Authentication failed. Please check your username and password.')

    # Check if user is authenticated before redirecting to home page
    if st.session_state.authenticated:
        st.switch_page("pages/Home.py")
        return  # Exit the function to prevent further execution

if __name__ == '__main__':
    main()