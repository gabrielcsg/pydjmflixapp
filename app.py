import streamlit as st

from actors.page import show_actors
from genres.page import show_genres
from login.page import show_login
from login.service import logout
from movies.page import show_movies
from reviews.page import show_reviews


def main():
    if 'token' not in st.session_state:
        show_login()
    else:
        st.title('Flix APP')

        menu_option = st.sidebar.selectbox(
            'Selecione uma opção',
            [
                'Início',
                'Gêneros',
                'Atores/Atrizes',
                'Filmes',
                'Avaliações',
                'Sair'
            ]
        )

        if menu_option == 'Início':
            st.write('Bem-vindo ao Flix APP')
        if menu_option == 'Gêneros':
            show_genres()
        if menu_option == 'Atores/Atrizes':
            show_actors()
        if menu_option == 'Filmes':
            show_movies()
        if menu_option == 'Avaliações':
            show_reviews()
        if menu_option == 'Sair':
            logout()


if __name__ == '__main__':
    main()
