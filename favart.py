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

def playlist():
    lst = grayp.GetPlayList().getNames()
    random.shuffle(lst)
    ob = GPlayer()
    lnks = ob.getInitLinks()
    t1 = threading.Thread(target=new, args=(ob,lst))
    t1.start()
    print('Playing All Audio in queue...')
    tmplst = list(lnks)
    #print(tmplst)
    random.shuffle(tmplst)
    ob.examplea(tmplst)
    t1.join()
    print('END')

def new(ob,lst):
    for ls in lst:
        ob.main(query=ls+' songs')
        grayp.AddPlayList(ob.getSearchLinks(),False)
    print("==========>Done Updating Playlist<============")

class GPlayer:

    def __init__(self):
        self.link = 'https://www.youtube.com/results?search_query='
        self.data = ''
        self.outlnk = 'https://www.youtube.com/'
        self.lnks = set()
        self.isPlaying=False
        self.idn = 'watch?v='
        self.audvol = 100
        self.flag = True
        self.Instance=Instance = vlc.Instance('--input-repeat=-1', '--fullscreen', '--mouse-hide-timeout=0')
        self.player=Instance.media_player_new()
        self.inlnks = grayp.GetPlayList().getLinks()
        self.t3=threading.Thread(target=self.getOptions)
        self.repeat = False

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
    
    def getOptions(self):
        while True:
            inp=input('...>')
            if inp == 'pause':
                self.player.set_pause(1)
            elif inp == 'help':
                print('skip : for next song\npause : for pausing playback\nresume : for resuming playback\nfff : to skip forward 5 seconds\nffb : to skip backwards 5 seconds\nvol <volume 0-100> : for setting desired volume\ngvol : to get current audio volume\nmute : to mute audio\nunmute : to unmute audio\nstop : to quit'+
                      '\naud : to download audio\nvid : to download video\nl : to add song to liked song list\nu : to dislike song\nr to keep repeating current song')
            elif inp == 'resume':
                self.player.set_pause(0)
            elif inp == 'r':
                if self.repeat:
                    self.repeat = False
                    print('Repeat off')
                else:
                    self.repeat = True
                    print('Repeat on')
            elif inp == 'aud':
                audth=threading.Thread(target=self.downloada)
                audth.start()
            elif inp == 'vid':
                vidth=threading.Thread(target=self.downloadv)
                vidth.start()
            elif inp == 'l':
                    self.like("https://www.youtube.com/watch?v="+str(self.dat.videoid))
            elif inp == 'a':
                    self.addToPlaylist("https://www.youtube.com/watch?v="+str(self.dat.videoid))
            elif inp == 'u':
                    self.unlike("https://www.youtube.com/watch?v="+str(self.dat.videoid))
                    self.player.stop()
                    self.isPlaying=False
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
                self.setVol(vol)
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
                print(self.dat)
                ratio = (self.player.get_time()//1000)/self.dat.length
                ratio = ratio*10
                ratio = int(ratio)
                sec = self.player.get_time()//1000
                mint = sec//60
                sec = sec-mint*60
                print(str(mint)+':'+str(sec), end='')
                for i in range(10):
                    if i == ratio:
                        print('*.', end='')
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
                self.player.stop()
                sys.exit('USER CHOSE TO QUIT')
                exit(0)
            
    def examplea(self,lnks):
        #print('Started examplea')
        #print(lnks)
        self.flag=True
        print('help for CONTROLS')
        self.t3.start()
        unlked=grayp.GetUnliked().getList()
        for song in lnks:
            if song in unlked:
                continue
            try:
                cond = True
                self.setdat(song)
                while self.repeat or cond:
                    print('CURRENTLY PLAYING : ',)
                    print(self.dat)
                    print('FROM YOUR FAVORITE ARTISTS')
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
                            self.isPlaying=False
                            sys.exit('USER CHOSE TO EXIT..\n'+'Script might still wait for the download to finish...')
                            break
                        pass
                    cond = False
                    #print('CAME OUT WHILE')
            except Exception as ex:
                print(ex)
                continue
            #print('CAME OUT EXCEPT')
            continue
        self.t3.join()
        print('QUEUE ENDED')
        

    def main(self, query):
        self.lnks=set()
        r = requests.get(self.link+urllib.parse.quote(query))
        self.data = r.text
        try:
            while(self.data.index(self.idn)):
                self.data = self.data[self.data.index(self.idn):]
                tmp = self.data[0:11+len(self.idn)]
                self.lnks.add(self.outlnk + tmp)
                self.data = self.data[len(tmp)+1:]
        except ValueError as ve:
            return True

    def getInitLinks(self):
        return self.inlnks

    def downloada(self):
        ba = self.dat.getbestaudio()
        print("Size : "+str(ba.get_filesize())+' bytes')
        filename = ba.download()

    def downloadv(self):
        ba = self.dat.getbest()
        print("Size : "+str(ba.get_filesize())+' bytes')
        filename = ba.download()
        
    def getSearchLinks(self):
        return self.lnks

playlist()