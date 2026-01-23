import streamlit as st
from song import Song

# Page config
st.set_page_config(
    page_title="Sai Ram Music Player",
    page_icon="🎵"
)

# Title
st.title("🎵 Sai Ram Music Player")
st.subheader("Listen to full songs")

# Search box
query = st.text_input("Search for a song or artist")

# Button logic
if st.button("Search") and query:
    try:
        song = Song()
        gen = song.paginate_songs(query)

        for batch in gen:
            for item in batch:
                data = item["item"]["data"]

                st.markdown(f"### 🎶 {data['name']}")
                st.audio(data["audio_url"])
            break

    except Exception as e:
        st.error("Something went wrong")
        st.exception(e)
