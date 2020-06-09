import json
from secrets import spotify_user_id, spotify_token
import requests


class CreatePlaylist:

    def __init__(self):
        self.user_id = spotify_user_id

    # log into youtube

    def get_youtube_client(self):
        pass

    # grab our liked videos
    def get_liked_videos(self):
        pass

    # create a new playlist
    def create_playlist(self):
        request_body = json.dumps({
            "name": "Youtube songs",
            "description": "All liked videos from youtube",
            "public": True
        })

        query = "https://api.spotify.com/v1/users/{}/playlists".format(
            self.user_id)
        response = requests.post(
            query,
            data=request_body,
            header={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )
        response_json = response.json()

        # playlist id
        return response_json("id")

    # search for the song
    def get_spotify_url(self, song_name, artist):
        query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(
            song_name,
            artist
        )
        response = requests.get(
            query,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )
        response_json = response.json()

    # add song into spotify playlist

    def add_song_to_playlist(self):
        pass
