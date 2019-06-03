import gplaylist as gp
from os import system,name

help='show : to see the list of your favorite artists..\nadd : to add a name to your favorite artist list\nrem : to remove a name from your favorite artist list\nquit : to quitn\nclr : to clear screen\nhelp : for this menu'
print(help)
while True:
    inp=input('..>')
    inp=inp.lower()
    if inp == 'show':
        lst=gp.GetPlayList().getNames()
        for name in lst:
            print(name)
    elif inp == 'add':
        name=input('Name of Artist to add : ')
        ob=gp.AddPlayList(name)
        if ob.hasErr():
            print(ob.getError())
        else:
            print('Successfully added the artist')
    elif inp == 'rem':
        name=input('Name of Artist to remove : ')
        ob=gp.RemoveArtist(name)
        if ob.hasErr():
            print(ob.getError())
        elif ob.found:
            print('Successfully removed the artist')
        else :
            print('Artist not found in the List')
    elif inp == 'quit':
        break
    elif inp == 'clr':
        if name == 'nt': 
            _ = system('cls')
        elif name == 'posix':
            _ = system('clear')
        else:
            print('Sorry Clear Screen not supported for your OS : '+name)
    elif inp == 'help':
        print(help)