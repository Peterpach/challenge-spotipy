import challenge

# Ask for the artist name
name = input("Introduce el nombre de un artista: ")

# Display the song list to the user and ask the user to select a song
selectSong = challenge.getArtistList(name)

# Add the selected song to the playlist and show the playlist duration
challenge.addSonToPlaylist(selectSong)

