import streamlit as st

# IMPORTANT: your existing import
# from your_module import Song

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Sai Ram Music Player",
    page_icon="🎵",
    layout="centered"
)

# ------------------ HEADER ------------------
st.title("🎵 Sai Ram Music Player")
st.subheader("Listen to full songs")

st.info(
    "🎧 Songs are streamed using the internal Song engine"
)

# ------------------ SEARCH INPUT ------------------
query = st.text_input("🔍 Search for a song or artist")

# ------------------ SEARCH LOGIC ------------------
if st.button("Search") and query:
    with st.spinner("Fetching songs..."):
        try:
            song = Song()
            gen = song.paginate_songs(query)

            found = False

            # Each batch contains ~100 songs
            for batch in gen:
                for idx, item in enumerate(batch):
                    found = True
                    st.markdown("---")

                    data = item["item"]["data"]

                    # Song title
                    st.markdown(f"### 🎶 {data.get('name', 'Unknown')}")

                    # Optional metadata
                    if "artist" in data:
                        st.caption(f"👤 Artist: {data['artist']}")

                    # FULL AUDIO URL (this depends on YOUR Song backend)
                    if "audio_url" in data:
                        st.audio(data["audio_url"])
                    else:
                        st.warning("Audio stream unavailable")

                # Stop after first page (remove this if you want infinite load)
                break

            if not found:
                st.warning("No songs found.")

        except Exception as e:
            st.error("Failed to load songs.")
            st.exception(e)

# ------------------ FOOTER ------------------
st.markdown("---")
st.caption(
    "Sai Ram Music Player | Full Song Streaming"
)
