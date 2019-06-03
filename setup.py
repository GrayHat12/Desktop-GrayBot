import os
import platform
import sys
import socket

def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

if is_connected() == False:
    print('Try running the setup file again when you have an internet connection')
    sys.exit('No Network Connection Found')

t2=0
s4=0
if '32bit' in platform.architecture():
    t2+=1
    print('32-bit operating system detected.../')
elif '64bit' in platform.architecture():
    s4+=1
    print('64-bit operating system detected.../')
else : 
    print('Failed to detect Operating System Architectre')
if str(sys.maxsize) == str(2147483647):
    t2+=1
    print('32bit python detected.../')
elif str(sys.maxsize) == str(9223372036854775807):
    s4+=1
    print('64bit python detected.../')
else : 
    print('Failed to detect Python Architecture')

if t2 == 2 or s4 == 2:
    print('GrayBot should be supported by your Machine...\n')
else:
    print('Architectural Errors .... GrayBot might fail to run properly on your system')
    
print('Installing necessary modules .... ')
    

p1=os.system("pip3 install pafy")
p2=os.system("pip3 install python-vlc")
p3=os.system("pip3 install youtube_dl")
p4=os.system("pip3 install colorama")
p5=os.system("pip3 install requests")
#p6=os.system("pip3 install numpy")
#p7=os.system("pip3 install tensorflow")
p8=os.system("pip3 install lyricsgenius")

print('Do you want to install neccessary packages for the incomplete GUI ? GUI will hopefully be finished in the coming future.. (y/n)')
inp = input('..> ')
if inp == 'y' or inp == 'Y':
    p9=os.system("pip3 install --upgrade pip3 wheel setuptools")
    p10=os.system("pip3 install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew")
    p11=os.system("pip3 install kivy.deps.gstreamer")
    p12=os.system("pip3 install kivy.deps.angle")
    p13=os.system("pip3 install kivy")
    print('Setup Finished...\nNow you can launch GUI GrayBot from main.py\nCommand Line GrayBot can be launched from GrayBot.py')
else:
    print('Setup Finished...\nCommand Line GrayBot can be launched from GrayBot.py\nmain.py will not work since you chose not to install GUI dependencies')