import requests
from bs4 import BeautifulSoup

def create_songs(date):
    url = f"https://www.billboard.com/charts/hot-100/{date}"
    print(url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get(url, headers=headers)
    data = response.text

    soup = BeautifulSoup(data, "html.parser")
    title_of_the_songs = soup.select("li ul li h3.c-title")

    song_titles = [title.get_text().strip() for title in title_of_the_songs]
    song_title_final = [song for song in song_titles if song and not song.endswith(":")]

    return song_title_final