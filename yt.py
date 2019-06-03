import pafy
import requests
import urllib
import vlc
import gplaylist as grayp
import multiprocessing
import sys
from os import system, name
import threading

class Player:

    def __init__(self):
        self.link = 'https://www.youtube.com/results?search_query='
        self.data = ''
        self.outlnk = 'https://www.youtube.com/'
        self.lnks = set()
        self.idn = 'watch?v='
        self.audvol = 100
        self.curdat=None
        self.isPlaying=False
        self.Instance=Instance = vlc.Instance('--input-repeat=-1', '--fullscreen', '--mouse-hide-timeout=0')
        self.player=Instance.media_player_new()
        self.t3=[]
        self.auddth=[]
        self.vidth=[]
        self.threadind=0
        self.audthi=0
        self.vidthi=0

    def setVol(self, vol):
        self.audvol = vol

    def getVol(self):
        return self.audvol

    def main(self, query):
        r = requests.get(self.link+urllib.parse.quote(query))
        self.data = r.text
        try:
            while(self.data.index(self.idn)):
                self.data = self.data[self.data.index(self.idn):]
                tmp = self.data[0:11+len(self.idn)]
                self.lnks.add(self.outlnk+tmp)
                self.data = self.data[12:]
                #print(self.lnks)
        except ValueError as ve:
            return True

    def getLinks(self):
        return self.link
    
    def like(self,lnk):
        ob=grayp.Like(lnk)
        if ob.hasErr():
            print(ob.getError())
        else:
            print('Added to Liked Songs')
            
    def unlike(self,lnk):
        ob=grayp.UnLike(lnk)
        if ob.hasErr():
            print(ob.getError())
        else:
            print('Added to Unliked Songs')
        
    def addToPlaylist(self,lnk):
        grayp.AddQueue(lnk)
        print('Added to your Playlist')

    def showMenu(self):
        print('DA for Audio Download\nDV for video download\nI for Info\nN for Next\nE for exit\nP for audio playback\nV for video playback\nL to like \nU to dislike\nA for adding it to playlist')
        for lnk in self.lnks:
            dat = pafy.new(lnk)
            print("..# "+dat.title)
            while True:
                inp = input("..>")
                inp=inp.lower()
                if inp == 'da':
                    self.downloada(dat)
                elif inp == 'l':
                    self.like(lnk)
                elif inp == 'a':
                    self.addToPlaylist(lnk)
                elif inp == 'u':
                    self.unlike(lnk)
                elif inp == 'dv':
                    self.downloadv(dat)
                elif inp == "i":
                    try:
                        print("AUTHOR : "+dat.author)
                        print("CATEGORY : "+dat.category)
                        print("DESCRIPTION : "+dat.description)
                        print(str(dat.likes)+' Likes \t ' +
                              str(dat.dislikes)+' Dislikes')
                        print("LENGTH : "+str(dat.length) + ' seconds')
                        print("PUBLISHED : "+dat.published)
                        print("RATING : "+str(dat.rating))
                        print("VIEWS : "+str(dat.viewcount))
                    except Exception as ex:
                        print(dat)
                    stream = dat.getbestaudio()
                    print('______ AUDIO ______')
                    print('\nBITRATE : '+stream.bitrate)
                    print("DOWNLOAD Size : " +
                          str(int(stream.get_filesize()/1024))+' bytes')
                    print("EXTENSION : "+stream.extension)
                    stream = dat.getbest()
                    print()
                    print('______ VIDEO ______')
                    print('\nBITRATE : '+stream.bitrate)
                    print("DOWNLOAD Size : " +
                          str(int(stream.get_filesize()/1024))+' bytes')
                    print("EXTENSION : "+stream.extension)
                elif inp == 'n':
                    break
                elif inp == 'e':
                    print('QUITTING')
                    return
                elif inp == 'p':
                    print('Playing ..')
                    self.examplea(dat)
                elif inp == 'v':
                    print('Playing ..')
                    self.examplev(dat)
                else:
                    print('WRONG INPUT')

    def downloada(self, dat):
        ba = dat.getbestaudio()
        print("Size : "+str(ba.get_filesize())+' bytes')
        filename = ba.download()
    
    def downloa(self):
        ba = self.dat.getbestaudio()
        print("Size : "+str(ba.get_filesize())+' bytes')
        filename = ba.download()
    
    def downlov(self):
        ba = self.dat.getbest()
        print("Size : "+str(ba.get_filesize())+' bytes')
        filename = ba.download()

    def downloadv(self, dat):
        ba = dat.getbest()
        print("Size : "+str(ba.get_filesize())+' bytes')
        filename = ba.download()
        
    def examplea(self,dat):
        self.t3.append(threading.Thread(target=self.getOptions))
        print('help for CONTROLS')
        self.media=self.Instance.media_new(dat.getbestaudio().url)
        self.media.get_mrl()
        self.player.set_media(self.media)
        self.player.audio_set_volume(self.getVol())
        self.player.play()
        self.curdat=dat
        self.isPlaying=True
        print('Thread State : ',self.t3[0].is_alive())
        if self.t3[0].is_alive()==False:
            self.t3[self.threadind].start()
        while self.isPlaying:
            if self.player.get_state()==vlc.State.Ended:
                self.isPlaying=False
                self.player.stop()
                break
            if self.t3[self.threadind].is_alive() == False:
                print('USER CHOSE TO EXIT')
                self.player.stop()
                break
        self.t3[self.threadind]._stop()
        self.isPlaying=False
        self.t3[self.threadind].join()
        self.curdat=None
        print('SONG ENDED')
        self.threadind+=1
    
    def examplev(self,dat):
        self.t3.append(threading.Thread(target=self.getOptions))
        print('help for CONTROLS')
        self.media=self.Instance.media_new(dat.getbest().url)
        self.media.get_mrl()
        self.player.set_media(self.media)
        self.player.audio_set_volume(self.getVol())
        self.player.play()
        self.curdat=dat
        self.isPlaying=True
        print('Thread State : ',self.t3[0].is_alive())
        if self.t3[self.threadind].is_alive()==False:
            self.t3[self.threadind].start()
        while self.isPlaying:
            if self.player.get_state()==vlc.State.Ended:
                self.isPlaying=False
                self.player.stop()
                break
            if self.t3[self.threadind].is_alive() == False:
                print('USER CHOSE TO EXIT')
                break
        self.t3[self.threadind].join()
        self.isPlaying=False
        self.curdat=None
        print('SONG ENDED')
        self.threadind+=1
        
    def getOptions(self):
        vidstr=False
        audstr=False
        while self.isPlaying:
            inp=input('...>')
            if inp == 'pause':
                self.player.set_pause(1)
            elif inp == 'help':
                print('pause : for pausing playback\nresume : for resuming playback\nfff : to skip forward 5 seconds\nffb : to skip backwards 5 seconds\nvol <volume 0-100> : for setting desired volume\ngvol : to get current audio volume\nmute : to mute audio\nunmute : to unmute audio\nstop : to quit\naud : to download audio file\n vid : to download video file')
            elif inp == 'resume':
                self.player.set_pause(0)
            elif inp == 'aud' and not audstr:
                self.auddth.append(threadind.Thread(target=self.downloa))
                self.auddth[self.audthi].start()
                audstr=True
            elif inp == 'vid' and not vidstr:
                self.vidth.append(threadind.Thread(target=self.downlov))
                self.vidth[self.vidthi].start()
                vidstr=True
            elif inp == 'fff':
                c = self.player.get_time()
                self.player.set_time(c+1000*5)
            elif inp == 'ffb':
                c = self.player.get_time()
                if c-5000 < 0:
                    self.player.set_time(0)
                else:
                    self.player.set_time(c-1000*5)
            elif inp.startswith('vol'):
                vol = int(inp.split(' ')[1])
                self.audvol = vol
                self.player.audio_set_volume(self.audvol)
            elif inp == 'gvol':
                print(self.player.audio_get_volume())
            elif inp == 'mute':
                self.player.audio_set_mute(True)
            elif inp == 'unmute':
                self.player.audio_set_mute(False)
            elif inp == 'info':
                print(self.curdat)
                ratio = (self.player.get_time()//1000)/self.curdat.length
                ratio = ratio*10
                ratio = int(ratio)
                sec = self.player.get_time()//1000
                mint = sec//60
                sec = sec-mint*60
                print(str(mint)+':'+str(sec), end='')
                for i in range(10):
                    if i == ratio:
                        print('>.', end='')
                    else:
                        print('..', end='')
                sec = self.curdat.length
                mint = sec//60
                sec = sec-mint*60
                print(str(mint)+':'+str(sec), end='')
                print()
            elif inp == 'clr':
                if name == 'nt': 
                    _ = system('cls')
                elif name == 'posix':
                    _ = system('clear')
                else:
                    print('Sorry Clear Screen not supported for your OS : '+name)
            elif inp=='stop':
                print('Stopping the Script...')
                self.player.stop()
                self.isPlaying=False
                break
        sys.exit(0)
        print('Quit Thread')
        return
    
print('WELCOME TO GrayBot\'s YouTube SERVICE')
while True:
    el = input('TYPE YOUR SEARCH ELEMENT (q to quit) : ')
    if el=='q':
        break
    ob = Player()
    ob.main(query=el)
    ob.showMenu()