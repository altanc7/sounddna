from spotify_client import (
    get_top_artists,
    get_top_tracks,
    get_user_profile,
    get_top_genres
)
import streamlit as st

st.title("🎵 SoundDNA")

artists = get_top_artists()
tracks = get_top_tracks()
profile = get_user_profile()
genres = get_top_genres()

st.subheader("👤 Spotify Profil")
st.write("Name:", profile["display_name"])
st.write("Land:", profile["country"])
st.write("Abo:", profile["product"].capitalize())

st.subheader("🎧 Deine Top Artists")


if len(artists) == 0:
    st.warning("Noch keine Spotify-Hörhistorie vorhanden.")
else:
    for artist in artists:
        st.write("•", artist)

st.subheader("🎵 Deine Top Tracks")
if len(tracks) == 0:

    st.warning("Noch keine Spotify-Hörhistorie vorhanden.")

else:

    for track in tracks:

        st.write("•", track)

st.subheader("🎼 Top Genres")

if len(genres) == 0:
    st.warning("Keine Genre-Daten vorhanden.")
else:
    from collections import Counter

    genre_counts = Counter(genres)

    for genre, count in genre_counts.most_common():
        st.write(f"• {genre} ({count})")
    top_genre = genre_counts.most_common(1)[0][0]

    st.subheader("🏆 Dominantes Genre")
    st.success(top_genre)

st.subheader("🧬 Dein Music DNA Profil")

if len(artists) == 0:
    st.info("Noch nicht genug Daten für eine Analyse.")
else:
    if top_genre == "hip hop":
        dna = "🧬 The Visionary Rebel"

    elif "rock" in top_genre:
        dna = "🧬 The Fearless Explorer"

    else:
        dna = "🧬 The Music Nomad"

    st.success(dna)