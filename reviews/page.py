import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

from movies.service import MovieService
from reviews.service import ReviewService


def show_reviews():
    reviews_service = ReviewService()
    reviews = reviews_service.get_reviews()

    if reviews:
        st.write('Lista de avaliaçãoes')

        reviews_df = pd.json_normalize(reviews)
        AgGrid(
            data=pd.DataFrame(reviews_df),
            reload_data=True,
            key='reviews_grid',
        )
    else:
        st.warning('Nenhuma avaliação encontrada.')

    st.title('Cadastrar nova avaliação')
    movie_service = MovieService()
    movies = movie_service.get_movies() or []
    movie_titles = {movie['title']: movie['id'] for movie in movies}
    movie = st.selectbox('Filme', list(movie_titles.keys()))

    stars = st.number_input(
        label='Estrelas',
        min_value=0,
        max_value=5,
        step=1,
    )
    comment = st.text_area('Comentário')

    if st.button('Cadastrar'):
        new_review = reviews_service.create_review(
            movie=movie_titles[movie],
            stars=stars,
            comment=comment,
        )
        if new_review:
            st.success(f'Avaliação do filme: {movie}, cadastrada com sucesso!')
            st.rerun()
        else:
            st.error('Falha ao cadastrar a avaliação.')
