from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

SPOTIPY_CLIENT_ID = os.environ["SPOTIPY_CLIENT_ID"]
SPOTIPY_CLIENT_SECRET = os.environ["SPOTIPY_CLIENT_SECRET"]
SPOTIPY_REDIRECT_URI = os.environ["SPOTIPY_REDIRECT_URI"]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope="playlist-modify-private",
        cache_path="token.txt",
        show_dialog=True
    )
)

user_id = sp.current_user()["id"]

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = int(date.split("-",1)[0])

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
billboard_webpage = response.text
soup = BeautifulSoup(billboard_webpage, "html.parser")

songs = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
top_songs = [song.getText() for song in songs]

song_uris = []
for song in top_songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

new_playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
tracks = sp.playlist_add_items(playlist_id=new_playlist["id"], items=song_uris)
