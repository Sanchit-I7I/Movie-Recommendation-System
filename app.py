import streamlit as st
import pickle
import pandas as pd

movies_dict=pickle.load(open('movie_dict.pkl','rb'))

movies=pd.DataFrame(movies_dict)


similarity=pickle.load(open('similarity.pkl','rb'))


st.title("Movie Recommendation System")

selected_movie_name=st.selectbox('What similar Movie would you like to watch?',movies['title'].values)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie = []
    for i in movies_list:
        recommended_movie.append(movies.iloc[i[0]].title)

    return recommended_movie

if st.button("Recommend"):
    recommendations=recommend(selected_movie_name)
    for i in recommendations:
                st.write(i)
