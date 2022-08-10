import flask
from SpotifyClient import SpotifyClient, client_id, client_secret
from ImageGenerator import ImageGenerator
import os

app = flask.Flask(__name__)
app.config["DEBUG"] = True

playlist_id= '73KvoZbKdQSNonmuvKrUII'
script_dir_name = "PietMondrian" # write the name of the directory with no leading or trailing slashes
sketch_name = "PietMondrian.pyde"

spotifyClient = SpotifyClient(client_id, client_secret)
is_success, playlist_image, track_ids = spotifyClient.getPlaylistInfo(playlist_id)
is_success, audio_features = spotifyClient.getFeatures(track_ids)
imageGenerator = ImageGenerator(script_dir_name, sketch_name)
image_art_url = imageGenerator.makeArt() #will want to pass in the audiofeatures eventually - use input() function in processing script, to then pass the inputs into the cli using os lib

@app.route('/artImage', methods=['GET'])
def api_all():
    return image_art_url

if __name__ == "__main__":
    app.run()