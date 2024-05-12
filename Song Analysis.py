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


##returns top 10 tracks 

top_tracks = spot.current_user_top_tracks(limit=10,time_range='short_term')
track_ids = [track['id'] for track in top_tracks['items']]
audio_features = spot.audio_features(track_ids)


# Check if top_tracks['items'] is not empty
if top_tracks['items']:
    df = pd.DataFrame(audio_features)
    df['track_name'] = [track['name'] for track in top_tracks['items']]
    df = df[['track_name', 'danceability' , 'energy', 'valence']]
    df.set_index('track_name', inplace=True)

    # Print the first few rows of the DataFrame
    st.write("DataFrame:")
    st.write(df.head())

    st.subheader('Audio Feature for Top Tracks')
    st.bar_chart(df, height=500)
else:
    st.write('No top tracks found.')


