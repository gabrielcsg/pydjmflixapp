import streamlit as st
from api.service import Auth


def login(username: str, password: str):
    auth_service = Auth()
    response = auth_service.get_token(username, password)

    if response.get('error'):
        st.error(f'Falha ao realizar o login: {response.get("error")}')
        return

    st.session_state.token = response.get('access')
    st.session_state.refresh_token = response.get('refresh')
    st.rerun()


def logout():
    for key in st.session_state.keys():
        del st.session_state[key]
    st.rerun()
