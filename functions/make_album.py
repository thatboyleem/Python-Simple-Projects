def make_album(artist_name, album_title, number_songs=None):
    """function to make an a dictionary of album titles"""
    album = {'name':artist_name, 'album': album_title}
    if number_songs:
       album ['songs'] = number_songs
    else:
        album = {'name': artist_name, 'album': album_title}
    return album

albums = []
while True:

    name = input("please enter artists name: ")
    if name == 'q':
        break

    al_name = input("please enter album name: ")
    if al_name == 'q':
        break

    album = make_album(name, al_name)
    albums.append(album)
for album in albums:
        print('\n----Album Created-----')
        print(albums)

ready_albums1 = make_album('saleem', 'african giant')
ready_albums2= make_album('big mike', 'shake the town', number_songs=20)
print(ready_albums1)
print(ready_albums2)
make_album('saleem', 'african giant')
