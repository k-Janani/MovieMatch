import streamlit as st
import streamlit_authenticator as stauth
import pickle
import pandas as pd
import requests
import numpy as np
import random
import time
import json
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
from PIL import Image
st.title("Feel The Reel")
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    

lottie_coding = load_lottiefile("music.json")  # replace link to local lottie file
lottie_hello = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_CTaizi.json")

st_lottie(
    lottie_hello,
    speed=1,
    reverse=False,
    loop=True,
    quality="high", # medium ; high
    height=200,
    width=200,
)
names = ['Kamkshi','John Smith','Rebecca Briggs','K Janani',]
usernames = ['kamakshi1','jsmith','rbriggs','janani']
passwords = ['111111','123','456','123456']
hashed_passwords = stauth.Hasher(passwords).generate()
authenticator = stauth.Authenticate(names,usernames,hashed_passwords,
    'some_cookie_name','some_signature_key',cookie_expiry_days=60)
name, authentication_status, username = authenticator.login('Login','main')
if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write('Welcome *%s*' % (name))
    
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=a2f46d8641f693a0e2859f61613f17ff&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from api
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters


movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))


def random_emoji():
    st.session_state.emoji = random.choice(emojis)

# initialize emoji as a Session State variable
if "emoji" not in st.session_state:
    st.session_state.emoji = "🍿🎞️"

emojis = ["📽️","🎬","🎼","🎞️"]

st.button(f"Getting Popcorn....{st.session_state.emoji}", on_click=random_emoji)

video_file = open('l3.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)

selected_movie_name = st.selectbox(
'Which Movie do you want to watch?',
movies['title'].values)

if st.button('Recommend'):
   names,posters = recommend(selected_movie_name)

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

st.subheader('Magazine Match')
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    

lottie_coding = load_lottiefile("m2.json")  # replace link to local lottie file
lottie_hello = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_96bovdur.json")

st_lottie(
    lottie_hello,
    speed=3,
    reverse=False,
    loop=True,
    quality="high", # medium ; high
    height=250,
    width=250,
)
st.write("Get updated with the recent releases, reviews and news about your favourite movies and cast. This website provides wonderful entertainment with the combination of movies and movie magazines making this as the BEST SITE FOR MOVIE INSIGHT. ")
st.write("Enjoy the Movie Zing with Magazine  [Click here](https://www.thefilmagazine.com/)") 
st.title("MMM:Movie Music Memes")
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    

lottie_coding = load_lottiefile("m1.json")  # replace link to local lottie file
lottie_hello = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_Z8msK0.json")

st_lottie(
    lottie_hello,
    speed=2,
    reverse=False,
    loop=True,
    quality="high", # medium ; high
    height=200,
    width=200,
)
st.write("Listen to one of the most beloved movie themes which will take to you back to the nostalgia accompanied by perfect chucklesome memes to refresh your mind which serves as an icing on the cake")
st.subheader("Harry Potter")
st.write("Hi there  Potter Heads groove to one of your favourite Harry potter tunes while going through the memes")
audio_file = open('a1.mp4', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='a1.mp4')
image = Image.open('g1.jpg')
st.image(image,width=350)
st.title(" ")
image = Image.open('g2.jpg')
st.image(image,width=350)
st.title(" ")
image = Image.open('g3.jpg')
st.image(image,width=350)
st.title(" ")
image = Image.open('g4.jpg')
st.image(image,width=350)
st.title(" ")
image = Image.open('g5.jpg')
st.image(image,width=350)
st.title(" ")
st.subheader("Avengers")
st.write("Hello there True Believers groove to one of your favourite Avenger tunes while going through the memes ")
audio_file = open('a2.mp4', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='a2.mp4')
image = Image.open('g6.jpg')
st.image(image,width=350)
st.title(" ")
image = Image.open('g7.jpg')
st.image(image,width=350)
st.title(" ")
st.subheader("Rush Hour")
st.write("Hello there groove to one of your favourite Rush Hour tunes while going through the memes ")
audio_file = open('a3.mp4', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='a3.mp4')
image = Image.open('g8.jpg')
st.image(image,width=350)
st.title(" ")
image = Image.open('g9.jpg')
st.image(image,width=350)
st.subheader("Spider Man")
st.write("Hello there groove to one of your favourite Spider Man tunes while going through the memes ")
audio_file = open('a4.mp4', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='a4.mp4')
image = Image.open('g10.jpg')
st.image(image,width=350)
st.title(" ")
image = Image.open('g11.jpg')
st.image(image,width=350)
st.subheader("Karate Kid")
st.write("Hello there groove to one of your favourite Karate Kid tunes while going through the memes ")
audio_file = open('a5.mp4', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='a5.mp4')
image = Image.open('g13.jpg')
st.image(image,width=350)
st.title(" ")
image = Image.open('g14.jpg')
st.image(image,width=350)
st.header("Slam Note")
st.title(" ")
age = st.slider('1. How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')
st.title(" ")
from datetime import time
movie_time = st.slider(
     "2. Your Movie time?",
     value=(time(11, 30), time(12, 45)))
st.write("You're selected time:", movie_time)

st.title(" ")

options = st.multiselect(
     '3. What are your favorite movie genre',
     ['Comedy','Drama','Action','Thriller','Horror','Fantasy','Fiction','Short','Musical'])

st.write('You selected:', options)

if st.button('Thank you'):
     st.write('Happy Days')
else:
     st.write('Have a nice day')
st.write("4. The number of different genre movies liked by watchers")
col1, col2, col3,col4,col5,col6 = st.columns(6)
col1.metric("Musical", "11%")
col2.metric("Comedy", "35%")
col3.metric("Action", "15%")
col4.metric("Thriller","20%")
col5.metric("Fantasy","14%")
col6.metric("Horror", "5%")
st.title("")
st.caption("The comparison of three different genre over a period of time")
chart_data = pd.DataFrame(
     np.random.randn(50, 3),
     columns=['Comedy', 'Musical', 'Thriller'])

st.area_chart(chart_data)
# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How do you rate our website?",
    ("1", "2", "3","4","5")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Would you like to recieve new updates from us?",
        ("Yes", "No","Only on weekends")
        
    )


with st.sidebar:
    with st.echo():
        "Buckle up, Enjoy The Reel Ride!!"



def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
st.subheader("Contact")    
st.write("Connect with us at:- klucse2000030403@gmail.com")
lottie_coding = load_lottiefile("m3.json")  # replace link to local lottie file
lottie_hello = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_cgbdcefj.json")

st_lottie(
    lottie_hello,
    speed=1,
    reverse=False,
    loop=True,
    quality="high", # medium ; high
    height=250,
    width=250,
)
