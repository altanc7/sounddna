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

user = sp.current_user()

print("Hallo", user["display_name"])

results = sp.current_user_top_artists(limit=10)

print("\nDeine Top Artists:")

for artist in results["items"]:
    print("-", artist["name"])