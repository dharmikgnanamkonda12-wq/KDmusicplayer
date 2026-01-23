import requests

class Song:
    def paginate_songs(self, query):

        API_URL = ""          # ADD API URL HERE
        API_KEY = ""          # ADD API KEY HERE (IF REQUIRED)

        headers = {
            # ADD REQUIRED HEADERS HERE
        }

        params = {
            # ADD REQUIRED QUERY PARAMS HERE (example: "q": query)
        }

        response = requests.get(
            API_URL,
            headers=headers,
            params=params,
            timeout=10
        )

        data = response.json()

        batch = []

        for item in []:       # REPLACE [] WITH SONG LIST FROM API RESPONSE
            batch.append({
                "item": {
                    "data": {
                        "name": "",       # MAP SONG NAME HERE
                        "artist": "",     # MAP ARTIST NAME HERE
                        "audio_url": ""   # MAP PLAYABLE AUDIO / EMBED URL HERE
                    }
                }
            })

        yield batch
