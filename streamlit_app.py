import streamlit as st
import requests

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Sai Ram Full Music Player",
    page_icon="🎧",
    layout="centered"
)

# ------------------ HEADER ------------------
st.title("🎧 Sai Ram Full Music Player")
st.subheader("Stream full-length songs (Legal & Campus-Safe)")

st.info(
    "🎶 This player streams full songs from the Internet Archive "
    "(public domain & artist-uploaded content)."
)

# ------------------ SEARCH INPUT ------------------
query = st.text_input("🔍 Search song, artist, or album")

# ------------------ SEARCH LOGIC ------------------
if st.button("Search") and query:
    with st.spinner("Searching full songs..."):
        try:
            search_url = (
                "https://archive.org/advancedsearch.php"
                f"?q={query}"
                "&fl[]=identifier"
                "&fl[]=title"
                "&fl[]=creator"
                "&fl[]=year"
                "&rows=10"
                "&page=1"
                "&output=json"
            )

            response = requests.get(search_url, timeout=10)
            data = response.json()

            docs = data["response"]["docs"]

            if not docs:
                st.warning("No full songs found.")
            else:
                st.success(f"Found {len(docs)} full songs")

                for song in docs:
                    st.markdown("---")

                    col1, col2 = st.columns([1, 3])

                    # Album Art
                    with col1:
                        cover_url = (
                            f"https://archive.org/services/img/{song['identifier']}"
                        )
                        st.image(cover_url, width=120)

                    # Song Info
                    with col2:
                        st.markdown(
                            f"### {song.get('title', 'Unknown')}\n"
                            f"**Artist:** {song.get('creator', 'Unknown')}\n"
                            f"**Year:** {song.get('year', 'N/A')}"
                        )

                        # Full Audio URL
                        audio_url = (
                            f"https://archive.org/download/"
                            f"{song['identifier']}/"
                            f"{song['identifier']}.mp3"
                        )

                        st.audio(audio_url)

                        st.link_button(
                            "🌐 View on Internet Archive",
                            f"https://archive.org/details/{song['identifier']}"
                        )

        except Exception as e:
            st.error("Network error or Archive API unavailable.")

# ------------------ FOOTER ------------------
st.markdown("---")
st.caption(
    "⚡ Full-Length Music Streaming using Internet Archive\n"
    "📚 Legal | Free | Campus-Safe"
)
