This project uses the Spotify API to analyze a user's top tracks. It utilizes Spotipy for Python to access the Spotify API, Streamlit for the web application interface, and Pandas for data manipulation.

The main features of the project include:

Authenticating with Spotify using OAuth2.0 to access user data
Displaying insights about the user's top 10 tracks, including danceability, energy, and valence
Visualizing the audio features of the top tracks using bar charts
Users can interact with the application by clicking a button to authenticate with Spotify and view the analysis of their top tracks.

Overall, this project provides a simple and interactive way for users to explore their Spotify listening habits and discover insights about their music preferences.

![Screenshot (27)](https://github.com/e-basi/Spotify-Song-Analysis/assets/93174387/12ae7a2d-6088-4823-91fe-3aa9f0447444)

Getting Started

1) Clone the repository:

git clone https://github.com/your-username/spotify-song-analysis.git


2) Install dependencies:

pip install -r requirements.txt


3) Set up environment variables:
Create a .env file in the root directory with your Spotify CLIENT_ID and CLIENT_SECRET:

export CLIENT_ID=your_client_id_here
export CLIENT_SECRET=your_client_secret_here

4) Run the application:
   
For Mac/Linux:

source .env && streamlit run main.py

For Windows:


.\.env && streamlit run main.py

5) Authenticate with Spotify:
Click the "Login to Spotify" button in the app and follow the instructions to authorize Spotify access.

View your top tracks:
Once authenticated, the app will display insights about your top Spotify tracks.

Technologies Used: 


Spotipy - Spotify API wrapper for Python
Streamlit - Web application framework for Python
Pandas - Data manipulation and analysis library for Python


