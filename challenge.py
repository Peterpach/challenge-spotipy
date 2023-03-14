import settingEnvironment
import datetime
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=settingEnvironment.CLIENT_ID,
                                                           client_secret=settingEnvironment.CLIENT_SECRET))

# Display the song list to the user and ask the user to select a song
def getArtistList(name):
    
    print(f"Las 10 canciones más populares de {name.upper()} son: \n")
    
    # Get the list of songs from an artist (name)
    results = sp.search(q=name, limit=10)
    for idx, track in enumerate(results['tracks']['items']):
        print(f"{(idx)+1}._ {track['name']} - Popularidad: {track['popularity']}")
    
    print("\n")
    
    # Ask user to select a song
    getIdFromUser = int(input("Ingrese un número del 1 al 10 para agregar su canción a la playlist: "))
    
    # Get the ID of the selected song
    selectSong = results['tracks']['items'][getIdFromUser - 1]
    return selectSong



# Add the selected song to the playlist and show the playlist duration
def addSonToPlaylist(songId):
    songName = songId['name']
    artistName = songId['artists'][0]['name']
    newPlaylist = []
    millisecondsDuration = 0
    
    while True:
        
        # Add the song to the playlist
        newPlaylist.append(songName)
        print(f"'{songName}' se agregó a la lista de reproducción.")
        
        addAnotherSong = input("¿Desea agregar otra canción a la lista de reproducción? (S/N): ")
        
        if addAnotherSong.upper() == 'S':
            songId = getArtistList(artistName)
            # Reassigning the new name of the song
            songName = songId['name']
        else:    
            break
    
    
    print("\n")
    
    print("Lista de reproducción final: ")
    print(newPlaylist)
    
    # Get the playlist duration (in milliseconds)
    for song in newPlaylist:
        millisecondsDuration += songId['duration_ms']
    
    # Change the milliseconds format to hours, minutes and seconds format
    time = datetime.datetime.fromtimestamp(millisecondsDuration / 1000.0)
    timeFormat = time.strftime('%H:%M:%S')
    
    print(f"Duración total de la lista de reproducción: {timeFormat}")


