import flask
from flask import request, jsonify
from SpotifyClient import SpotifyClient, client_id, client_secret
from ImageGenerator import ImageGenerator

app = flask.Flask(__name__)
app.config["DEBUG"] = True


playlist_id= '73KvoZbKdQSNonmuvKrUII'
dir_path = "C:\\Users\\Lenovo\\OneDrive\\Desktop\\PietMondrian\\"
script_name = "PietMondrian.pyde"


spotifyClient = SpotifyClient(client_id, client_secret)
is_success, playlist_image, track_ids = spotifyClient.getPlaylistInfo(playlist_id)
is_success, audio_features = spotifyClient.getFeatures(track_ids)
imageGenerator = ImageGenerator(dir_path, script_name)
image_art_url = imageGenerator.makeArt() #will want to pass in the audiofeatures eventually - use input() function in processing script, to then pass the inputs into the cli using os lib


@app.route('/artImage', methods=['GET'])
def api_all():
    return image_art_url

app.run()

