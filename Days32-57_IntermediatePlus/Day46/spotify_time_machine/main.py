import os
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
load_dotenv()
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def search_billboards():
    """Uses user input on a date to find the most popular billboard songs during that time. It then passes it to a
    function that will create a playlist."""

    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
    URL = f"https://www.billboard.com/charts/hot-100/{u_input}"
    response = requests.get(URL, headers=header)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Song names are located in this cell.
    song_names = soup.select('main ul li li h3')
    song_list = []
    for song_name in song_names:
        song_list.append(song_name.text.strip())
    create_playlist(song_list)

def create_playlist(song_list):
    """Creates a playlist from a list of song names. Uses spotipy library with spotify API."""
    scope = 'playlist-modify-private'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    #Creates the blank playlist using the user input as a name.
    create_playlist = sp.user_playlist_create(user='chjopa',name=f'{u_input} top 100',public=False)

    playlist_id = create_playlist['id']
    song_ids =[]
    #Searches spotify for the song names in the list and then adds them to the spotify playlist.
    for song in song_list:
        songs = sp.search(q=song,type='track')
        song_ids.append(songs['tracks']['items'][0]['uri'])
    add_song = sp.playlist_add_items(playlist_id=playlist_id, items=song_ids)
    print(add_song)

u_input = input("What year do you want to be transported to? Enter as YYYY-MM-DD: ")
search_billboards()