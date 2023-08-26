import streamlit as st
import pickle
import pandas as pd
st.title("Movie reccomendation system")
movie_dict=pickle.load(open('movies_dict.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
movies=pd.DataFrame(movie_dict)
selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values)

def fetch_poster(movie_id):
     pass
def reccomend(movie):
    # def recommend(movie):
        recomended_movies=[]
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
        for i in distances[1:6]:
            recomended_movies.append(movies.iloc[i[0]].title)
        return recomended_movies

# st.write('You selected:', selected_movie_name)

# st.button("Reset", type="primary")
if st.button('Recommend'):
    reccomendation=reccomend(selected_movie_name)
    for i in reccomendation:
        st.write(i)