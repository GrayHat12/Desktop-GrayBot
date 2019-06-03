import pafy
import requests
import urllib
import vlc
import gplaylist as grayp
import random
import threading
import sys
import math
from os import system, name


class Player:

    def __init__(self):
        self.link = 'https://www.youtube.com/results?search_query='
        self.data = ''
        self.outlnk = 'https://www.youtube.com/'
        self.lnks = set()
        self.idn = 'watch?v='
        self.audvol = 100
        self.flag = True

    def setVol(self, vol):
        self.audvol = vol

    def getVol(self):
        return self.audvol

    def task(self,inp,lnk):
        while self.player.get_state() != vlc.State.Ended:
            if inp == 'pause':
                self.player.set_pause(1)
            elif inp == 'help':
                print('stop : for stopping playback\npause : for pausing playback\nresume : for resuming playback\nfff : to skip forward 5 seconds\nffb : to skip backwards 5 seconds\nvol <volume 0-100> : for setting desired volume\ngvol : to get current audio volume\nmute : to mute audio\nunmute : to unmute audio\nquit to quit code\ninfo for song info\nclr : to clear screen')
            elif inp == 'resume':
                self.player.set_pause(0)
            elif inp == 'clr':
                if name == 'nt': 
                    _ = system('cls')
                elif name == 'posix':
                    _ = system('clear')
                else:
                    print('Sorry Clear Screen not supported for your OS : '+name)
            elif inp == 'info':
                print(lnk.title)
                print(self.player.audio_get_track_description())
                ratio = (self.player.get_time()//1000)/lnk.length
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
                sec = lnk.length
                mint = sec//60
                sec = sec-mint*60
                print(str(mint)+':'+str(sec), end='')
                print()
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
            elif inp == 'quit':
                sys.exit(0)
            if(self.player.get_state() == vlc.State.Ended):
                self.player.stop()
                self.flag=False
                return False
            else:
                inp = self.getInp()
                if inp == 'stop':
                    self.player.stop()
                    self.flag=False
                    return False
        self.flag=False
        return False
                
    def examplea(self, lnk):
        self.flag=True
        print('help for CONTROLS')
        bestaudio = lnk.getbestaudio()
        Instance = vlc.Instance()
        self.player = Instance.media_player_new()
        Media = Instance.media_new(bestaudio.url)
        Media.get_mrl()
        self.player.set_media(Media)
        self.player.audio_set_volume(self.audvol)
        self.player.play()
        inp = '.'
        self.task(inp,lnk)
        while self.flag:
            pass
        return

    def examplev(self, lnk):
        print('help for CONTROLS')
        bestaudio = lnk.getbest()
        Instance = vlc.Instance()
        self.player = Instance.media_player_new()
        Media = Instance.media_new(bestaudio.url)
        Media.get_mrl()
        self.player.set_media(Media)
        self.player.audio_set_volume(self.audvol)
        self.player.play()
        inp = '.'
        while inp != 'stop':
            pass
            if inp == 'pause':
                self.player.set_pause(1)
            elif inp == 'help':
                print('stop : for stopping playback\npause : for pausing playback\nresume : for resuming playback\nfff : to skip forward 5 seconds\nffb : to skip backwards 5 seconds\nvol <volume 0-100> : for setting desired volume\ngvol : to get current audio volume\nmute : to mute audio\nunmute : to unmute audio')
            elif inp == 'resume':
                self.player.set_pause(0)
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
            if(self.player.get_state() == vlc.State.Ended):
                self.player.stop()
                return
            else:
                inp = input('..>')
                if inp == 'stop':
                    self.player.stop()
                    return

    def main(self, query):
        r = requests.get(self.link+urllib.parse.quote(query))
        self.data = r.text
        try:
            while(self.data.index(self.idn)):
                self.data = self.data[self.data.index(self.idn):]
                tmp = self.data[0:self.data.index('\"')]
                if (self.outlnk+tmp).find('&amp;list')==-1:
                    self.lnks.add(self.outlnk + tmp)
                self.data = self.data[len(tmp)+1:]
        except ValueError as ve:
            return True

    def getLinks(self):
        return self.link

    def showMenu(self):
        lines = len(self.lnks)
        print('D for Download\nI for Info\nN for Next\nE for exit\nP for audio playback\nV for video playback\nQ for adding all songs to audio queue')
        i = 0
        ti = True
        for lnk in self.lnks:
            if ti:
                ti = False
            else:
                i += 1
            dat = pafy.new(lnk)
            print(".> "+dat.title)
            while True:
                inp = input("....")
                if inp == 'D' or inp == 'd':
                    downloada(dat)
                elif inp == 'I' or inp == "i":
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
                        print(
                            'MAX YT LIMITS REACHED...\nTRY AGAIN AFTER SOME TIME FOR INFO')
                    stream = dat.getbestaudio()
                    print('______ AUDIO ______')
                    print('\nBITRATE : '+stream.bitrate)
                    print("DOWNLOAD Size : " +
                          str(int(stream.get_filesize()/1024))+' bytes')
                    print("EXTENSION : "+stream.extension)
                    print(stream.notes)
                    stream = dat.getbest()
                    print('______ VIDEO ______')
                    print('\nBITRATE : '+stream.bitrate)
                    print("DOWNLOAD Size : " +
                          str(int(stream.get_filesize()/1024))+' bytes')
                    print("EXTENSION : "+stream.extension)
                    print(stream.notes)
                elif inp == 'N' or inp == 'n':
                    break
                elif inp == 'E' or inp == 'e':
                    print('QUITTING')
                    return
                elif inp == 'p' or inp == 'P':
                    print('Playing ..')
                    self.examplea(dat)
                elif inp == 'q' or inp == 'Q':
                    print('Playing All Audio in queue..')
                    tmplst = list(self.lnks)[i:]
                    for lk in tmplst:
                        dat = pafy.new(lk)
                        self.examplea(dat)
                elif inp == 'v' or inp == 'V':
                    print('Playing ..')
                    self.examplev(dat)
                else:
                    print('WRONG INPUT')

    def downloada(self, dat):
        ba = dat.getbestaudio()
        print("Size : "+str(ba.get_filesize())+' bytes')
        filename = ba.download()

    def downloadv(self, dat):
        ba = dat.getbestaudio()
        print("Size : "+str(ba.get_filesize())+' bytes')
        filename = ba.download()


def func():
    el = input('TYPE YOUR SEARCH ELEMENT : ')
    if el.startswith('#GRAY#'):
        playlist(el)
        return
    ob = Player()
    ob.main(query=el)
    ob.showMenu()


def playlist(el):
    lst = grayp.GetPlayList().getNames()
    random.shuffle(lst)
    ob = GPlayer()
    lnks = ob.getLinks()
    t1 = threading.Thread(target=new, args=(ob,lst))
    t1.start()
    print('Playing All Audio in queue...')
    
    tmplst = list(lnks)
    random.shuffle(tmplst)
    ob.examplea(tmplst)
    t1.join()
    print('END')
    
def new(ob,lst):
    for ls in lst:
        ob.main(query=ls+' songs')
        grayp.AddPlayList(ob.getLinks(),False)
    print("==========>Done Updating Playlist<============")
        
class GPlayer:

    def __init__(self):
        self.link = 'https://www.youtube.com/results?search_query='
        self.data = ''
        self.outlnk = 'https://www.youtube.com/'
        self.lnks = set()
        self.isPlaying=False
        self.idn = 'watch?v='
        self.audvol = 150
        self.flag = True
        self.Instance=Instance = vlc.Instance('--input-repeat=-1', '--fullscreen', '--mouse-hide-timeout=0')
        self.player=Instance.media_player_new()
        self.lnks = grayp.GetPlayList().getLinks()
        self.t3=threading.Thread(target=self.getOptions)

    def setVol(self, vol):
        self.audvol = vol
        
    def setdat(self,lnk):
        dat=pafy.new(lnk)
        self.dat=dat
        self.setMedia(dat)
        
    def setMedia(self,dat):
        self.media=self.Instance.media_new(dat.getbestaudio().url)
        self.media.get_mrl()

    def getVol(self):
        return self.audvol
    
    def getOptions(self):
        while True:
            inp=input('...>')
            if inp == 'pause':
                self.player.set_pause(1)
            elif inp == 'help':
                print('skip : for next song\npause : for pausing playback\nresume : for resuming playback\nfff : to skip forward 5 seconds\nffb : to skip backwards 5 seconds\nvol <volume 0-100> : for setting desired volume\ngvol : to get current audio volume\nmute : to mute audio\nunmute : to unmute audio\nstop : to quit')
            elif inp == 'resume':
                self.player.set_pause(0)
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
            elif inp=='skip':
                self.player.stop()
                self.isPlaying=False
            elif inp == 'info':
                print(self.dat.title)
                ratio = (self.player.get_time()//1000)/self.dat.length
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
                sec = self.dat.length
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
                sys.exit('USER CHOSE TO QUIT')
                exit(0)
            
    def examplea(self,lnks):
        #print(lnks)
        self.flag=True
        print('help for CONTROLS')
        i=0
        for song in self.lnks:
            try:
                self.setdat(song)
                print('CURRENTLY PLAYING : ',)
                print(self.dat)
                print('FROM YOUR FAVORITE ARTISTS')
                if i==0:
                    self.t3.start()
                    i=1
                self.player.set_media(self.media)
                self.player.audio_set_volume(self.getVol())
                self.player.play()
                self.isPlaying=True
                #duration = player.get_length() / 1000
                #mm, ss = divmod(duration, 60)
                while self.isPlaying:
                    if self.player.get_state()==vlc.State.Ended:
                        self.isPlaying=False
                        self.player.stop()
                        break
                    if self.t3.isAlive() == False:
                        sys.exit('USER CHOSE TO EXIT')
                #print('CAME OUT WHILE')
                
            except Exception as ex:
                print(ex)
                continue
            #print('CAME OUT EXCEPT')
            continue
        self.t3._stop()
        self.t3.join()
        print('QUEUE ENDED')
        

    def main(self, query):
        r = requests.get(self.link+urllib.parse.quote(query))
        self.data = r.text
        try:
            while(self.data.index(self.idn)):
                self.data = self.data[self.data.index(self.idn):]
                tmp = self.data[0:self.data.index('\"')]
                if (self.outlnk+tmp).find('&amp;list')==-1:
                    self.lnks.append(self.outlnk + tmp)
                self.data = self.data[len(tmp)+1:]
        except ValueError as ve:
            return True

    def getLinks(self):
        return self.lnks

    def downloada(self, dat):
        ba = dat.getbestaudio()
        print("Size : "+str(ba.get_filesize())+' bytes')
        filename = ba.download()

    def downloadv(self, dat):
        ba = dat.getbestaudio()
        print("Size : "+str(ba.get_filesize())+' bytes')
        filename = ba.download()


print('WELCOME TO GRAYBOT\'s AUDIO SERVICE')
func()
