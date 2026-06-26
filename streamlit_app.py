from spotify_client import (
    get_top_artists,
    get_top_tracks,
    get_user_profile,
    get_top_genres,
    get_playlists
)

import streamlit as st

st.set_page_config(page_title="SoundDNA", page_icon="🎵", layout="wide")

st.markdown("""
<style>
:root {
    --bg: #f4f1ea;
    --card: #fffdf9;
    --border: #e5ddd0;
    --accent: #7c5cff;
    --text: #232323;
    --muted: #6b6b6b;
}

.stApp {
    background: var(--bg);
}

.block-container {
    max-width: 1180px;
    padding-top: 2.5rem;
}

section[data-testid="stSidebar"] {
    background: #ece7de;
    border-right: 1px solid var(--border);
}

h1,h2,h3 {
    color: var(--text);
    font-weight: 800;
    letter-spacing: -0.03em;
}

p, label, div {
    color: var(--text);
}

[data-testid="stMetric"] {
    background: var(--card);
    border-radius: 18px;
    border: 1px solid var(--border);
    padding: 18px;
    box-shadow: 0 8px 30px rgba(0,0,0,.05);
}

[data-testid="stVerticalBlockBorderWrapper"] {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 22px;
    padding: 20px;
    margin-bottom: 18px;
    box-shadow: 0 10px 30px rgba(0,0,0,.05);
}

img {
    border-radius: 18px !important;
}

.stLinkButton a,
.stButton button {
    background: var(--accent) !important;
    color: white !important;
    border: none !important;
    border-radius: 999px !important;
    padding: .55rem 1.2rem !important;
}
</style>
""", unsafe_allow_html=True)

st.title("SoundDNA")
st.caption("Discover your listening identity.")

artists = get_top_artists()
tracks = get_top_tracks()
profile = get_user_profile()
genres = get_top_genres()
playlists = get_playlists()

st.sidebar.title("🎵 SoundDNA")

page = st.sidebar.radio(

    "Navigation",

    [

        "🏠 Dashboard",

        "👤 Profil",

        "🎧 Top Artists",

        "🎵 Top Tracks",

        "🧬 Music DNA"

    ]

)

if page == "🏠 Dashboard":
    st.header("Dashboard")
    st.write("Willkommen bei SoundDNA!")
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("🎧 Top Artists", len(artists))

    with col2:
        st.metric("🎵 Top Tracks", len(tracks))

    col3, col4 = st.columns(2)

    with col3:
        st.metric("📂 Playlists", len(playlists))

    with col4:
        st.metric("🎼 Genres", len(set(genres)))

    st.markdown("---")

    st.subheader("Spotify Profile")
    st.info(
        f"""
**Name:** {profile['display_name']}

**Land:** {profile['country']}

**Abo:** {profile['product'].capitalize()}
"""
    )

    st.subheader("📂 Deine Playlists")

    if len(playlists) == 0:
        st.info("Keine Playlists gefunden.")
    else:
        for playlist in playlists:
            st.write("•", playlist)

elif page == "👤 Profil":
    st.subheader("Spotify Profile")
    st.write("Name:", profile["display_name"])
    st.write("Land:", profile["country"])
    st.write("Abo:", profile["product"].capitalize())

elif page == "🎧 Top Artists":
    st.subheader("Top Artists")

    if len(artists) == 0:
        st.warning("Noch keine Künstler gefunden.")
    else:
        for artist in artists:
            col1, col2 = st.columns([1, 4])

            with col1:
                st.image(artist["image"], width=70)

            with col2:
                st.subheader(artist["name"])

                if artist["genres"]:
                    st.caption(", ".join(artist["genres"][:2]))

                st.progress(artist["popularity"] / 100)
                st.caption(f'Popularität: {artist["popularity"]}/100')

elif page == "🎵 Top Tracks":
    st.subheader("Top Tracks")
    if len(tracks) == 0:

        st.warning("Noch keine Spotify-Hörhistorie vorhanden.")

    else:
        for track in tracks:
            st.container(border=True)

            col1, col2 = st.columns([1,5])

            with col1:
                st.image(track["image"], width=130)

            with col2:
                st.markdown(f"### {track['name']}")
                st.write(f"**🎤 Artist:** {track['artist']}")
                st.write(f"**💿 Album:** {track['album']}")
                st.write(f"**📅 Released:** {track['release_date'][:4]}")
                st.link_button("Open in Spotify", track["url"])

            st.markdown("")

elif page == "🧬 Music DNA":
    st.subheader("Top Genres")

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

    st.subheader("Music DNA")

    if len(artists) == 0 or len(genres) == 0:
        st.info("Noch nicht genug Daten für eine Analyse.")
    else:
        if top_genre == "hip hop":
            dna = "🧬 The Visionary Rebel"

        elif "rock" in top_genre:
            dna = "🧬 The Fearless Explorer"

        else:
            dna = "🧬 The Music Nomad"

        st.success(dna)