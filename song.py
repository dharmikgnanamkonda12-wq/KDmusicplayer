class Song:
    def paginate_songs(self, query):
        yield [
            {
                "item": {
                    "data": {
                        "name": f"{query} Song 1",
                        "audio_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
                    }
                }
            },
            {
                "item": {
                    "data": {
                        "name": f"{query} Song 2",
                        "audio_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"
                    }
                }
            }
        ]
