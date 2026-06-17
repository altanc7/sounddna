from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
        redirect_uri=os.getenv("REDIRECT_URI"),
        scope="user-top-read user-read-private user-read-email"
    )
)

def get_top_artists():
    results = sp.current_user_top_artists(limit=10)

    artists = []

    for artist in results["items"]:
        artists.append(artist["name"])

    return artists

def get_top_tracks():
    results = sp.current_user_top_tracks(limit=10)

    return [
        track["name"] + " - " + track["artists"][0]["name"]
        for track in results["items"]
    ]

def get_user_profile():
    return sp.current_user()

def get_top_genres():
    results = sp.current_user_top_artists(limit=20)

    genres = []

    for artist in results["items"]:
        genres.extend(artist["genres"])

    return genres