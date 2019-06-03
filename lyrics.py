import lyricsgenius
import colorama

genius = lyricsgenius.Genius("---YOUR GENIUS API KEY HERE---")

genius.verbose = False # Turn off status messages
genius.remove_section_headers = True # Remove section headers (e.g. [Chorus]) from lyrics when searching
genius.skip_non_songs = False # Include hits thought to be non-songs (e.g. track lists)
genius.excluded_terms = ["(Remix)", "(Live)"] # Exclude songs with these words in their title

""",per_page=size"""

def byArtist():
    colorama.init(autoreset=True)
    name = input('Artist Name : ')
    size = int(input('Max Songs to search from(based on popularity) : '))
    print('Searching ....../',end='\r')
    artist = genius.search_artist(name,max_songs=size,sort='popularity')
    i,j=0,5
    print('Search Completed ...... )')
    while True:
        print('\n\n\n')
        for a in range(i,j):
            print(colorama.Fore.RED+colorama.Back.CYAN+str(str(a)+' : '+str(artist.songs[a])),end='\n\n')
        print('n : for more\nb : to move back\nsong number to get lyrics\ne : to quit')
        inp= input('..> ')
        if inp == 'n':
            i+=5
            j+=5
        elif inp == 'b':
            i-=5
            j-=5
        elif inp == 'e':
            break
        else:
            num=-1
            try:
                num=int(inp)
            except Exception as ex:
                num=-1
            if num >= i and num <j:
                showLyrics(artist.songs[num])
                break
            else:
                print('Invalid Song number')
                continue

def showLyrics(song):
    colorama.init(autoreset=True)
    print(colorama.Back.GREEN+colorama.Fore.BLUE+song.lyrics)
    
def searchbySong(song,artist=''):
    colorama.init(autoreset=True)
    sng=genius.search_song(title=song,artist=artist)
    print(colorama.Back.GREEN+colorama.Fore.BLUE+sng.lyrics)
    print('By : ',sng.artist)
    
print('a : for searching by artist name')
print('b : for searching by song name')

inp = input('...> ')

if inp == 'a':
    byArtist()
elif inp == 'b':
    song = input('Song Name : ')
    artist = input('Artist Name (Optional) : ')
    searchbySong(song,artist)