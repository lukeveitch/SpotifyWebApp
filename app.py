import flask
<<<<<<< HEAD:app.py
from SpotifyClient import SpotifyClient, client_id, client_secret
from ImageGenerator import ImageGenerator
import sys
sys.path.append('../')

=======
from flask import request, jsonify
from SpotifyClient import SpotifyClient, client_id, client_secret
from ImageGenerator import ImageGenerator
import os
>>>>>>> dev:api.py

app = flask.Flask(__name__)
app.config["DEBUG"] = True

<<<<<<< HEAD:app.py
playlist_id = '5AAD6wso6ksiY8V7yu6Gr2'
=======

playlist_id= '73KvoZbKdQSNonmuvKrUII'
>>>>>>> dev:api.py
dir_path = "\\PietMondrian\\"
script_name = "PietMondrian.pyde"

spotifyClient = SpotifyClient(client_id, client_secret)
is_success, playlist_image, track_ids = spotifyClient.getPlaylistInfo(playlist_id)
is_success, audio_features = spotifyClient.getFeatures(track_ids)
imageGenerator = ImageGenerator(dir_path, script_name)
<<<<<<< HEAD:app.py
image_art_url = imageGenerator.makeArt() 
#will want to pass in the audiofeatures eventually - use input() function in processing script, to then pass the inputs into the cli using os lib
=======
image_art_url = imageGenerator.makeArt() #will want to pass in the audiofeatures eventually - use input() function in processing script, to then pass the inputs into the cli using os lib

>>>>>>> dev:api.py

@app.route('/artImage', methods=['GET'])
def api_all():
    return image_art_url

if __name__ == "__main__":
    app.run()