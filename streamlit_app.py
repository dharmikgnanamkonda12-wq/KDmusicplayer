import streamlit as st
import requests

st.set_page_config(
    page_title="KD Music Player",
    page_icon="🎵"
)

st.title("🎵 KD Music Player")
st.write("Search and play songs (audio only)")

song_name = st.text_input("Enter song name")

if st.button("Search") and song_name:
    st.write("Searching...")

    try:
        url = f"https://saavn.dev/api/search/songs?query={song_name}"
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()
            songs = data.get("data", {}).get("results", [])

            if not songs:
                st.warning("No songs found")
            else:
                for song in songs[:10]:
                    st.markdown(
                        f"**{song['name']}** — {song['primaryArtists']}"
                    )
                    audio_url = song["downloadUrl"][-1]["url"]
                    st.audio(audio_url)
                    st.divider()
        else:
            st.error("Failed to fetch songs")

    except Exception:
        st.error("Network error or API blocked")
