import kivy
import os
kivy.require('1.10.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
#from kivy.config import Config

#Config.set('kivy','window_icon','')

class MainScreen(GridLayout):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.cols = 1
        self.but1=Button(text='Youtube')
        self.but1.bind(on_press=self.runyt)
        self.add_widget(self.but1)
        self.but2=Button(text='GoogleNews')
        self.but2.bind(on_press=self.rungn)
        self.add_widget(self.but2)
        self.but3=Button(text='Shuffle')
        self.but3.bind(on_press=self.runfa)
        self.add_widget(self.but3)
        self.but4=Button(text='Playlist')
        self.but4.bind(on_press=self.runpl)
        self.add_widget(self.but4)
        self.but5=Button(text='Artist')
        self.but5.bind(on_press=self.runar)
        self.add_widget(self.but5)
        self.but6=Button(text='Lyrics')
        self.but6.bind(on_press=self.runlr)
        self.add_widget(self.but6)
        self.but7=Button(text='Maps')
        self.but7.bind(on_press=self.runlm)
        self.add_widget(self.but7)
        
    def runyt(self,instance):
        os.system("start cmd /C python yt.py")
    
    def rungn(self,instance):
        os.system("start cmd /K python driver.py")
    
    def runfa(self,instance):
        os.system("start cmd /C python favart.py")
    
    def runpl(self,instance):
        os.system("start cmd /K python playlist.py")
    
    def runar(self,instance):
        os.system("start cmd /C python artist.py")
    
    def runlr(self,instance):
        os.system("start cmd /K python lyrics.py")
    
    def runlm(self,instance):
        os.system("start cmd /C python maps.py")
    

class MyApp(App):

    def build(self):
        self.title='GrayBot'
        return MainScreen()


if __name__ == '__main__':
    MyApp().run()