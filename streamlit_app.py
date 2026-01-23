import streamlit as st
from song import Song

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Sai Ram Music Player",
    page_icon="🎵",
    layout="centered"
)

# ------------------ HEADER ------------------
st.title("🎵 Sai Ram Music Player")
st.subheader("Listen to full songs")

st.info("Songs are streamed using the internal Song engine")

# ------------------ SEARCH INPUT ------------------
query = st.text_input("🔍 Search for a song or artist")

# ------------------ SEARCH LOGIC ------------------
if st.button("Search") and query:
    try:
        song = Song()
        generator = song.paginate_songs(query)

        found = False

        for batch in generator:
            for item in batch:
                found = True
                data = item["item"]["data"]

                st.markdown("---")
                st.markdown(f"### 🎶 {data['name']}")
                st.caption(f"👤 Artist: {data['artist']}")
                st.audio(data["audio_url"])

            break  # show only first page

        if not found:
            st.warning("No songs found.")

    except Exception as e:
        st.error("Failed to load songs.")
        st.exception(e)

# ------------------ FOOTER ------------------
st.markdown("---")
st.caption("Sai Ram Music Player | Full Song Streaming Demo")
