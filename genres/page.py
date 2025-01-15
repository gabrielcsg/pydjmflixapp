import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

genres = [
    {
        'id': '1',
        'name': 'Genre 1'
    },
    {
        'id': '2',
        'name': 'Genre 2'
    },
    {
        'id': '3',
        'name': 'Genre 3'
    },
    {
        'id': '4',
        'name': 'Genre 4'
    },
    {
        'id': '5',
        'name': 'Genre 5'
    }
]


def show_genres():
    st.write('Lista de gêneros')

    AgGrid(
        data=pd.DataFrame(genres),
        reload_data=True,
        key='genres_grid',
    )

    st.title('Cadastrar novo gênero')
    name = st.text_input('Nome do gênero')
    if st.button('Cadastrar'):
        st.success(f'Gênero ({name}) cadastrado com sucesso!')
