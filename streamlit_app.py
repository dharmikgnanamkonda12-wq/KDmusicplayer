import streamlit as st

st.set_page_config(
    page_title="Campus Music Player",
    page_icon="🎵",
    layout="centered"
)

st.title("🎵 Campus Music Player")
st.write("Full song playback using Spotify (campus-safe)")

st.info("Click ▶️ to play the full song")

# Example Spotify Track ID (Ed Sheeran - Shape of You)
track_id = "7qiZfU4dY1lWllzX7mPBI3"

st.components.v1.html(
    f"""
    <iframe
      src="https://open.spotify.com/embed/track/{track_id}"
      width="100%"
      height="352"
      frameborder="0"
      allow="encrypted-media">
    </iframe>
    """,
    height=380
)
