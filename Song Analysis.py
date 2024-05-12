import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
import streamlit as st 
import pandas as pd
import os 

load_dotenv()

CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
REDIRECT_URI = 'http://localhost:5000'

spot = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope='user-top-read'
    )
)  


st.set_page_config(page_title='Spotify Song Analysis', page_icon=':musical_note:')
st.title('Analysis for your Top Songs')
st.write('Discover insights about your epic Spotify listening habits.')