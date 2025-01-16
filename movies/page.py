from datetime import datetime
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

from actors.service import ActorService
from genres.service import GenreService
from movies.service import MovieService


def show_movies():
    movies_service = MovieService()
    movies = movies_service.get_movies()

    if movies:
        st.write('Lista de filmees')
        movies_df = pd.json_normalize(movies)
        movies_df = movies_df.drop(columns=['actors', 'genre.id'])
        AgGrid(
            data=pd.DataFrame(movies_df),
            reload_data=True,
            key='movies_grid',
        )
    else:
        st.warning('Nenhum filme encontrado.')

    st.title('Cadastrar novo filme')
    title = st.text_input('Título do filme')
    release_date = st.date_input(
        label='Data de lançamento',
        value=datetime.now(),
        min_value=datetime(1600, 1, 1).date(),
        max_value=datetime.today().date(),
        format='DD/MM/YYYY',
    )

    genres_service = GenreService()
    genres = genres_service.get_genres() or []
    genre_names = {genre['name']: genre['id'] for genre in genres}
    selected_genre_name = st.selectbox(
        label='Gênero',
        options=list(genre_names.keys()),
    )

    actors_service = ActorService()
    actors = actors_service.get_actors() or []
    actors_names = {actor['name']: actor['id'] for actor in actors}
    selected_actors_names = st.multiselect(
        label='Atores/Atrizes',
        options=list(actors_names.keys()),
    )
    selected_actors_ids = [
        actors_names[actor] for actor in selected_actors_names
    ]
    resume = st.text_area('Resumo do filme')

    if st.button('Cadastrar'):
        new_movie = movies_service.create_movie(
            title=title,
            release_date=release_date,
            genre=genre_names[selected_genre_name],
            actors=selected_actors_ids,
            resume=resume,
        )
        if new_movie:
            st.success(f'Filme: {title}, cadastrado com sucesso!')
            st.rerun()
        else:
            st.error('Falha ao cadastrar o filme.')
