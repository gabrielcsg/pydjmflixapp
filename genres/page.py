import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from genres.service import GenreService


def show_genres():
    genre_service = GenreService()
    genres = genre_service.get_genres()

    if genres:
        st.write('Lista de gêneros')
        genres_df = pd.json_normalize(genres)
        AgGrid(
            data=pd.DataFrame(genres_df),
            reload_data=True,
            key='genres_grid',
        )
    else:
        st.warning('Nenhum gênero encontrado.')

    st.title('Cadastrar novo gênero')
    name = st.text_input('Nome do gênero')
    if st.button('Cadastrar'):
        new_genre = genre_service.create_genre(name=name)
        if new_genre:
            st.success(f'Gênero: {name}, cadastrado com sucesso!')
            st.rerun()
        else:
            st.error('Falha ao cadastrar o gênero.')
