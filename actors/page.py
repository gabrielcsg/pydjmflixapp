import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

actors = [
    {
        'id': '1',
        'name': 'ator 1'
    },
    {
        'id': '2',
        'name': 'ator 2'
    },
    {
        'id': '3',
        'name': 'ator 3'
    },
    {
        'id': '4',
        'name': 'ator 4'
    },
    {
        'id': '5',
        'name': 'ator 5'
    }
]


def show_actors():
    st.write('Lista de atores')

    AgGrid(
        data=pd.DataFrame(actors),
        reload_data=True,
        key='actors_grid',
    )

    st.title('Cadastrar novo ator/atriz')
    name = st.text_input('Nome do ator/atriz')
    if st.button('Cadastrar'):
        st.success(f'Ator/Atriz de nome: ({name}), cadastrado com sucesso!')
