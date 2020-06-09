import json


class CreatePlaylist:

    def __init__(self):
        pass

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

    # search for the song
    def get_spotify_url(self):
        pass

    # add song into spotify playlist
    def add_song_to_playlist(self):
        pass
