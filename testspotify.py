import spotipy
import spotipy.util as util

CLIENT_ID = '0d5ebd1360fa46b7a2184239e05041bf'
CLIENT_SECRET = 'b5ca94f4773348e594e714dd1e20e2d7'
username ="bNCOxCR6Qt6RfePqiaXQjw"
scope = "user-read-currently-playing user-library-modify streaming"

redirect_url="http://localhost:8888/callback/"
token = util.prompt_for_user_token(username, scope, CLIENT_ID, CLIENT_SECRET, redirect_url)



sp = spotipy.Spotify(token)
currentsong = sp.currently_playing()

song_name = currentsong['item']['name']
song_artist = currentsong['item']['artists'][0]['name']
# should get list of song artists not just one
song_id=currentsong['item']['id']
print(song_id)
print(currentsong)
print("Now playing {} by {}".format(song_name, song_artist))

#sp.current_user_saved_tracks_add(tracks=[song_id])
#print("added")
#sp.current_user_saved_tracks_delete(tracks=[song_id])
#print("deleted")

#shuffle
#turn on shuffle
#sp.shuffle(state=True)
print("shuffle on")
#turn of shuffle
sp.shuffle(state=False)
print("shuffle off")