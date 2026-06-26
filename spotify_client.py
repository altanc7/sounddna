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
        scope="user-top-read user-read-private user-read-email playlist-read-private"
    )
)

def get_top_artists():
    results = sp.current_user_top_artists(limit=10)

    print(results["items"][0])

    artists = []

    for artist in results["items"]:
       artists.append({
    "name": artist["name"],
    "image": artist["images"][0]["url"] if artist["images"] else None,
    "genres": artist.get("genres", []),
    "popularity": artist.get("popularity", 0)
})

    return artists

def get_top_tracks():
    results = sp.current_user_top_tracks(limit=10)

    tracks = []

    for track in results["items"]:
        tracks.append({
    "name": track["name"],
    "artist": track["artists"][0]["name"],
    "image": track["album"]["images"][0]["url"],
    "album": track["album"]["name"],
    "release_date": track["album"]["release_date"],
    "url": track["external_urls"]["spotify"]
})

    return tracks

def get_user_profile():
    return sp.current_user()

def get_top_genres():
    results = sp.current_user_top_artists(limit=20)

    genres = []

    for artist in results["items"]:
       genres.extend(artist.get("genres", []))

    return genres

def get_playlists():
    playlists = sp.current_user_playlists(limit=20)

    return [
        playlist["name"]
        for playlist in playlists["items"]
    ]