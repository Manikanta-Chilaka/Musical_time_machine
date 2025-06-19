import spotipy
from spotipy.oauth2 import SpotifyOAuth
import config
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id = config.SPOTIPY_CLIENT_ID,
        client_secret = config.SPOTIPY_CLIENT_SECRET,
        redirect_uri = config.SPOTIPY_REDIRECT_URI,
        scope = "playlist-modify-private"        
        ))
def get_user_id():
    return sp.current_user()['id'] #type: ignore

def search_spotify_track(song):
    result = sp.search(q=song, type="track", limit=1)
    tracks = result['tracks']['items'] #type: ignore
    if tracks:
        track = tracks[0]
        return track['uri']
    
def create_playlist(user_id, name):
    playlist = sp.user_playlist_create(user=user_id, name=name, public=False, description="growing")
    print("Playlist Created")
    print(playlist)
    return playlist['id'] #type: ignore

def add_to_playlist(playlist_id, track_uris):
    sp.playlist_add_items(playlist_id, track_uris)
    print("Track added to playlist")
