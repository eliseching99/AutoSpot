import speech_recognition as sr
import spotipy
import spotipy.util as util
import time
from os import environ
print(sr.__version__)

r = sr.Recognizer()
quitprogram=False
PHRASES = ["save song","delete song", "repeat", "skip", "shuffle on", "shuffle off","play song"]

CLIENT_ID=environ.get("SPOTIPY_CLIENT_ID")
CLIENT_SECRET=environ.get("SPOTIPY_CLIENT_SECRET")
username ="bNCOxCR6Qt6RfePqiaXQjw"
scope = "user-read-currently-playing user-library-modify streaming user-read-playback-state user-modify-playback-state"

redirect_url="http://localhost:8888/callback/"
token = util.prompt_for_user_token(username, scope, CLIENT_ID, CLIENT_SECRET, redirect_url)



while quitprogram==False:

    
    sp = spotipy.Spotify(token)
    print(sp.devices())
    devices=sp.devices()
    comp_id=devices['devices'][0]['id']
    try:
        currentsong = sp.currently_playing()

        song_name = currentsong['item']['name']
        song_artist = currentsong['item']['artists'][0]['name']
    # should get list of song artists not just one
        song_id=currentsong['item']['id']
        print(song_id)
        print(currentsong)
        print("Now playing {} by {}".format(song_name, song_artist))
    except:
        print('song not being currently played')
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

 

    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
        voiceinput=r.recognize_google(audio)
        if voiceinput.lower() in PHRASES:
            print(voiceinput)
            if voiceinput=="shuffle on":
                sp.shuffle(state=True)
                print("shuffle on")
            if voiceinput=="shuffle off":
                sp.shuffle(state=False)
                print("shuffle off")
            if voiceinput=="save song":
                sp.current_user_saved_tracks_add(tracks=[song_id])
                print("added")
            if voiceinput=="delete song":
                sp.current_user_saved_tracks_delete(tracks=[song_id])
                print("deleted")
            if voiceinput=="play song":
                sp.start_playback(device_id=comp_id)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials

# sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
# username = "bNCOxCR6Qt6RfePqiaXQjw"
# scope = "user-read-currently-playing"

# results = sp.search(q='BTS', limit=20)
# for idx, track in enumerate(results['tracks']['items']):
#     print(idx, track['name'])
