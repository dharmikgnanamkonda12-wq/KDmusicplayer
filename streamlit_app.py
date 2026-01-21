import streamlit as st
import requests
import webbrowser

st.set_page_config(
    page_title="Campus Music Player",
    page_icon="🎵",
    layout="centered"
)

st.title("🎵 Campus Music Player")
st.write("Preview songs and open full music legally")

st.info("🔊 Previews play here. Full songs open in Spotify / YouTube.")

query = st.text_input("Enter song name")

if st.button("Search") and query:
    try:
        url = f"https://itunes.apple.com/search?term={query}&media=music&limit=10"
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

                    if song.get("artworkUrl100"):
                        st.image(song["artworkUrl100"], width=150)

                    # Preview (campus-safe)
                    if song.get("previewUrl"):
                        preview = requests.get(song["previewUrl"]).content
                        st.audio(preview, format="audio/mp3")

                    # Full song links
                    col1, col2 = st.columns(2)

                    with col1:
                        if song.get("trackViewUrl"):
                            st.link_button("▶ Open in Apple Music / iTunes", song["trackViewUrl"])

                    with col2:
                        search_q = f"{song.get('trackName')} {song.get('artistName')}"
                        yt_url = f"https://www.youtube.com/results?search_query={search_q.replace(' ', '+')}"
                        st.link_button("▶ Search on YouTube", yt_url)

                    st.divider()
        else:
            st.error("Failed to fetch songs")

    except Exception:
        st.error("Network issue or API blocked")
