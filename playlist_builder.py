from spotify_client import search_spotify_track, create_playlist, add_to_playlist, get_user_id
from scrape import create_songs

def build_playlist(date):
    song_list = create_songs(date)
    user_id = get_user_id()
    print(user_id)
    track_uris = []

    for song in song_list:
        uri = search_spotify_track(song) #type:ignore
        if uri:
            track_uris.append(uri)
        else:
            print(f"Track not found: {song}")

    if not track_uris:
        print("No tracks found. Playlist not created.")
        return

    playlist_name = f"Billboard Hot 100 - {date}"
    playlist_id = create_playlist(user_id, playlist_name)
    add_to_playlist(playlist_id, track_uris)
    print(f"Playlist '{playlist_name}' created successfully!")
