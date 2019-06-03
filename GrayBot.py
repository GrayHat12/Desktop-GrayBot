import sys
import os

print('Welcome User ....')
print('yt : for browsing youtube\n'+
      'news : for browsing Google News\n'+
      #'run : for running codes on GeeksforGeeks Online IDE\n'+
      'shuffle : to shuffle play the songs of your favorite artists\n'+
      'play : to shuffle play songs from your playlist\n'+
      'artist : to go to your favorite artist menu\n'+
      'lyrics : to go to lyrics menu\n'+
      'maps : to use Google Maps\n'+
      'exit : to exit')
while True:
      choice = input('...$ ')
      if choice.lower() == 'yt':
            os.system("start cmd /C python yt.py")
      elif choice.lower() == 'news':
            os.system("start cmd /K python driver.py")
      elif choice.lower() == 'shuffle':
            os.system("start cmd /C python favart.py")
      elif choice.lower() == 'play':
            os.system("start cmd /C python playlist.py")
      elif choice.lower() == 'artist':
            os.system("start cmd /C python artist.py")
      elif choice.lower() == 'exit':
            sys.exit('USER CHOSE TO QUIT')
      elif choice.lower() == 'lyrics':
            os.system("start cmd /K python lyrics.py")
      elif choice.lower() == 'maps':
            os.system("start cmd /C python maps.py")