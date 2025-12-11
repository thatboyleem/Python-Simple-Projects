def make_album(artist, title, num_songs=None):
    """Build a dictionary describing a music album."""
    album = {'artist': artist, 'title': title}
    if num_songs:
        album['num_songs'] = num_songs
    return album

while True:
    print("\nPlease enter the album details:")
    print("(Type 'quit' to exit at any prompt)")

    artist = input("Enter the artist's name: ")
    if artist.lower() == 'quit':
        break

    title = input("Enter the album title: ")
    if title.lower() == 'quit':
        break

    num_songs = input("Enter the number of songs (optional): ")
    if num_songs.lower() == 'quit':
        break
    
    if num_songs:
        album = make_album(artist, title, int(num_songs))
    else:
        album = make_album(artist, title)
    
    print("\nAlbum created:")
    print(album)
