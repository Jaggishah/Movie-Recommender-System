import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=d9bfd9c04df4dc798cf9cba16a9bd9ae&language=en-US')
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances  = similarity[movie_index]
    movie_list  =sorted(list(enumerate(distances)),reverse =True,key = lambda x:x[1])[1:6]
    
    recommended_movies = [] 
    recommended_movies_poster = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movies.iloc[i[0]].movie_id))
    return recommended_movies,recommended_movies_poster

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity  = pickle.load(open('similariy.pkl','rb'))

st.title('Movie Recommender System')

options = st.selectbox(
    'How Would You Like To be contacted?',
    movies['title'].values
)

if st.button('Recommend'):
    recomandation,posters = recommend(options)
    # for i in recomandation:
    #     st.write(i)
    
    col1, col2, col3 , col4 ,col5 = st.columns(5)

    with col1:
        st.text(recomandation[0])
        st.image(posters[0])

    with col2:
        st.text(recomandation[1])
        st.image(posters[1])

    with col3:
        st.text(recomandation[2])
        st.image(posters[2])

    with col4:
        st.text(recomandation[3])
        st.image(posters[3])
    
    with col5:
        st.text(recomandation[4])
        st.image(posters[4])



# Add bottom chart