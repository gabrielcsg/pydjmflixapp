import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

movies = [
    {
        'id': '1',
        'name': 'filme 1'
    },
    {
        'id': '2',
        'name': 'filme 2'
    },
    {
        'id': '3',
        'name': 'filme 3'
    },
    {
        'id': '4',
        'name': 'filme 4'
    },
    {
        'id': '5',
        'name': 'filme 5'
    }
]


def show_movies():
    st.write('Lista de filmees')

    AgGrid(
        data=pd.DataFrame(movies),
        reload_data=True,
        key='movies_grid',
    )
