import streamlit as st
import requests

# Page config
st.set_page_config(
    page_title="KD Music Player",
    page_icon="🎵",
    layout="centered"
)

st.title("🎵 KD Music Player")
st.write("Search and play songs (30-second previews)")

# User input
song_name = st.text_input("Enter song name")

# Search button
if st.button("Search") and song_name:
    st.write("Searching...")

    try:
        # iTunes Search API (OFFICIAL & FREE)
        url = f"https://itunes.apple.com/search?term={song_name}&media=music&limit=10"
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()
            songs = data.get("results", [])

            if not songs:
                st.warning("No songs found")
            else:
                for song in songs:
                    st.markdown(
                        f"**{song.get('trackName', 'Unknown')}** — {song.get('artistName', 'Unknown')}"
                    )

                    # Album art
                    if song.get("artworkUrl100"):
                        st.image(song["artworkUrl100"], width=150)

                    # 30-second preview audio
                    if song.get("previewUrl"):
                        st.audio(song["previewUrl"])
                    else:
                        st.info("No preview available")

                    st.divider()
        else:
            st.error("Failed to fetch songs")

    except Exception as e:
        st.error("Network error or API unavailable")
