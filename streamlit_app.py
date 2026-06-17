import streamlit as st

st.title("🎵 SoundDNA")

artists = st.text_area(
    "Enter your favorite artists (one per line)"
)

if st.button("Analyze"):

    artist_list = [
        artist.strip()
        for artist in artists.split("\n")
        if artist.strip()
    ]

    st.subheader("Your Music DNA")

    if any("kanye" in artist.lower() for artist in artist_list):
        st.success("🧬 The Visionary Rebel")

        st.write("""
        Traits:
        - Creative
        - Ambitious
        - Independent
        - Reflective
        """)

    else:
        st.success("🧬 The Explorer")

        st.write("""
        Traits:
        - Curious
        - Open-minded
        - Adventurous
        """)