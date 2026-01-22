import streamlit as st
import requests

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Sai Ram Music Player",
    page_icon="⚡",
    layout="centered"
)

# ------------------ HEADER ------------------
st.title("⚡Sai Ram Music Player")
st.subheader("Preview songs and open full music legally")

st.info(
    "🔊 Due to campus network restrictions, full songs open on official platforms "
    "(Apple Music / YouTube). Previews play directly here."
)

# ------------------ SEARCH INPUT ------------------
query = st.text_input("🔍 Search for a song, artist, or album")

# ------------------ SEARCH LOGIC ------------------
if st.button("Search") and query:
    with st.spinner("Searching music..."):
        try:
            url = f"https://itunes.apple.com/search?term={query}&media=music&limit=10"
            response = requests.get(url, timeout=10)

            if response.status_code == 200:
                data = response.json()
                songs = data.get("results", [])

                if not songs:
                    st.warning("No songs found.")
                else:
                    st.success(f"Found {len(songs)} results")

                    # ------------------ SONG CARDS ------------------
                    for song in songs:
                        st.markdown("---")

                        col1, col2 = st.columns([1, 3])

                        # Album Art
                        with col1:
                            if song.get("artworkUrl100"):
                                st.image(song["artworkUrl100"], width=120)

                        # Song Info
                        with col2:
                            st.markdown(
                                f"### {song.get('trackName', 'Unknown')}\n"
                                f"**Artist:** {song.get('artistName', 'Unknown')}\n"
                                f"**Album:** {song.get('collectionName', 'Unknown')}"
                            )

                            # Preview Audio (Campus-safe)
                            if song.get("previewUrl"):
                                try:
                                    preview_audio = requests.get(
                                        song["previewUrl"], timeout=10
                                    ).content
                                    st.audio(preview_audio, format="audio/mp3")
                                except Exception:
                                    st.caption("🔇 Preview unavailable")
                            else:
                                st.caption("🔇 Preview unavailable")

                            # Action Buttons
                            b1, b2 = st.columns(2)

                            with b1:
                                if song.get("trackViewUrl"):
                                    st.link_button(
                                        "🎧 Open in Apple Music",
                                        song["trackViewUrl"]
                                    )

                            with b2:
                                search_text = f"{song.get('trackName')} {song.get('artistName')}"
                                yt_url = (
                                    "https://www.youtube.com/results?search_query="
                                    + search_text.replace(" ", "+")
                                )
                                st.link_button("📺 Search on YouTube", yt_url)

            else:
                st.error("Failed to fetch songs. Please try again.")

        except Exception:
            st.error("Network error or API unavailable.")

# ------------------ FOOTER ------------------
st.markdown("---")
st.caption(
    "Campus-Safe Music Player | Streamlit Project\n\n"
    "⚠️ Full songs are streamed only on official platforms due to legal and network policies."
)




