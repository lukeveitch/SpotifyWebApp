# SpotifyWebApp

Creating the backend using Python and Flask.

References processing.py file to generate art. Path defined in SpotifyArt.


<hr>

  API make calls to Spotify API using the following endpoints: 
      https://api.spotify.com/v1/playlists/{playlist_id}
      https://api.spotify.com/v1/audio-features?ids={ids}
  It then generates a piece of art based on the audiofeatures of the playlist.
  
  API endpoint /api/v1/art_url/ returns the location of the piece of art that is generated for the front end.
  
  
  
