import streamlit as st
import pickle
import pandas as pd
import requests

# Function to return random image URLs
def get_poster(movie_id):
    # response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))
    # data = response.json()
    # return "https://image.tmdb.org/t/p/w500" + data['poster_path']
    return "https://images-cdn.ubuy.co.id/6352289f38bb253c44612d53-interstellar-movie-poster-24-x-36-inches.jpg"

def recommend(movie):
    """
    Recommend similar movies based on the selected movie.
    """
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    req_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    print(movies.columns)
    for i in req_list:
        print(movies.iloc[i[0]])
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(get_poster(1))
    return recommended_movies, recommended_movies_posters

# Load movie data and similarity matrix
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
print(movies.columns)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit UI
st.title('Movie Recommender System')

selectedMovie = st.selectbox(
    "Select a movie for recommendations:",
    movies['title'].values
)

if st.button('Show Recommendation'):
    names, posters = recommend(selectedMovie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
