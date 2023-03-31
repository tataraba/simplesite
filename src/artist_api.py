import sys
import os
import dotenv
import discogs_client
import httpx
import app.crud as crud

dotenv.load_dotenv()
user_token = os.environ.get("DISCOGS_TOKEN")
d = discogs_client.Client('FastAPI-ArtistExplorer', user_token=user_token)


def get_artist(artist_name):
    """Get artist from discogs"""
    artist = d.search(artist_name, type='artist')[0]
    return httpx.get(f"https://api.discogs.com/artists/{artist.id}?token={user_token}").json()




if __name__ == "__main__":
    artist_name = sys.argv[1]
    artist = get_artist(artist_name)
    db = crud.CRUD().with_table("artist_details")
    db.insert(artist)