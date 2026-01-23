class Song:
    def paginate_songs(self, query):
        """
        This simulates a song engine.
        Later you can replace this with a real API or embed logic.
        """

        yield [
            {
                "item": {
                    "data": {
                        "name": f"{query} - Sample Song 1",
                        "artist": "Demo Artist",
                        "audio_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
                    }
                }
            },
            {
                "item": {
                    "data": {
                        "name": f"{query} - Sample Song 2",
                        "artist": "Demo Artist",
                        "audio_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"
                    }
                }
            }
        ]
