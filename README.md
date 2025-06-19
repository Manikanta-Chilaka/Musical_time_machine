# Musical Time Machine: Spotify Billboard Playlist Generator

Travel back in time with music!  
This Python-based project allows you to generate a **Spotify playlist** of the **Billboard Top 100 songs** for any historical date. Simply enter a date, and the script will:

- Scrape the top 100 songs from [Billboard.com](https://www.billboard.com)
- Search for those songs on Spotify
- Create a new playlist in your Spotify account
- Automatically add available tracks to the playlist

---

## Features

- 🔍 Scrapes Billboard Top 100 for any valid date
- 🎧 Authenticates with your Spotify account
- 📃 Creates a neatly named playlist like `Billboard Top 100 - YYYY-MM-DD`
- 🎶 Adds matching tracks automatically
- ✅ Skips unavailable tracks with proper handling
- 🧠 Smart matching for track & artist names

---

## Requirements

- Python 3.7+
- Spotify Developer Account (for API keys)
- A Spotify account (Free or Premium)

## Python Libraries Used

```bash
requests
beautifulsoup4
spotipy
python-dotenv
