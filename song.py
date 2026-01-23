import requests

class Song:
    def paginate_songs(self, query):

        API_URL = "https://example-api.com/search"
        API_KEY = "YOUR_API_KEY"

        headers = {
            "Authorization": f"Bearer {API_KEY}"
        }

        params = {
            "query": query,
            "limit": 10
        }

        response = requests.get(
            API_URL,
            headers=headers,
            params=params,
            timeout=10
        )

        data = response.json()

        batch = []

        for item in data["results"]:
            batch.append({
                "item": {
                    "data": {
                        "name": item["title"],
                        "artist": item["artist"],
                        "audio_url": item["audio"]
                    }
                }
            })

        yield batch
