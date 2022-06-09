# ...... Creating Spotify Playlist using Musical Time Machine ............. #
# ...... Created and modified by N.S.Bhanuprakash on 29-04-2022 ........... #
# ... Note:- Paste the url that u were redirected to.. in the console,
# when u were first running the program in-order to generate an access token in a cache file

import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

# 1) Scraping Billboard website to get top 100 tracks of a particular date ............ #
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
URL = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(url=URL)
website_html = response.text

# ........ writing HTML to a file to view it properly ......... #
# with open("website.html", "w") as file:
#     file.write(soup.prettify())

# with open("website.html") as file:
#     local_html = file.read()
soup = BeautifulSoup(website_html, "html.parser")  # You can change website_html to the local_html
# if u want to minimise the number of times we scrape a particular site.

song_titles = soup.find_all(name="h3", class_="a-no-trucate")
titles = []
# Only 100 songs can be added to one single playlist. So,[0:99]
for title in song_titles[0:99]:
    titles.append(title.string.strip())
# ............ Other way of scraping .....................#
# song_titles = soup.select("li #title-of-a-story")
# titles = []
# for title in song_titles:
#     titles.append(title.string.strip())
# print(titles)
# ........................................................ #

# 2) Spotify Authentication and getting user_id ............................................ #

SPOTIFY_CLIENT_ID = os.getenv("spotify_client_id")
SPOTIFY_CLIENT_SECRET = os.getenv("spotify_client_secret")
SPOTIFY_REDIRECT_URI = os.getenv("spotify_redirect_uri")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET,
                                               redirect_uri=SPOTIFY_REDIRECT_URI, scope="playlist-modify-private"))
user_id = sp.current_user()["id"]

# 3) Getting URI's of the tracks, from spotify, that were scraped from Billboard ...................#
song_uris = []
year = date.split("-")[0]
for song in titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        song_uris.append(result["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
#         pass

# 4) Creating a playlist and getting it's ID ................................................#
playlist = sp.user_playlist_create(user=user_id, name=f"{date}:Billboard 100", public=False, collaborative=False,
                                   description=f'Top 100 tracks of {year}')
playlist_id = playlist["id"]
# 5) Adding the list of songs that were scraped to the above created playlist using their URI's .....#
playlist_items = sp.playlist_add_items(playlist_id=playlist_id, items=song_uris, position=None)

