class AddPlayList:

    def __init__(self, name, nme=True):
        self.err=''
        self.haserr=False
        self.intl=GetPlayList().getLinks()
        if nme and len(name) == 43 :
            try:
                file = open('mem.ghh', 'a')
                file.write(name+'\n')
                file.close()
            except Exception as ex:
                self.haserr=True
                self.err=ex
        else :        
            try:
                file = open('tempplay.ghh', 'a')
                for nm in name:
                    if nm not in self.intl and len(nm) == 43:
                        file.write(nm+'\n')
                file.close()
            except Exception as ex:
                self.haserr=True
                self.err=ex
        #print('PLAYLIST WRITTEN')
    
    def hasErr(self):
        return self.haserr
    
    def getError(self):
        return self.err

class RemoveArtist:
    
    def __init__(self,name):
        self.err=None
        self.haserr=False
        self.names=GetPlayList().getNames()
        tok=name.split()
        tname=name.replace(' ','')
        tname=tname.lower()
        fnal=''
        self.found=False
        for nme in self.names:
            tmp=nme.replace(' ','')
            tmp=tmp.lower()
            if tmp==tname:
                self.found=True
            else:
                fnal+=nme+'\n'
        if self.found:
            try:
                file = open('mem.ghh','w')
                file.write(fnal)
                file.close()
            except Exception as ex:
                self.err=ex
                self.haserr=True
    
    def getError(self):
        return self.err
    
    def hasErr(self):
        return self.haserr

class GetPlayList:
    
    def __init__(self):
        self.names=set()
        self.links=set()
        self.haserr=False
        try:
            file = open('mem.ghh','r')
            for each in file:
                if each.lstrip() != '':
                    if each.endswith('\n'):
                        self.names.add(each[0:len(each)-1])
                    else:
                        self.names.add(each)
            file.close()
        except Exception as ex:
            self.err=ex
            self.haserr=True
        try:
            file = open('tempplay.ghh','r')
            for each in file:
                if each.lstrip() != '':
                    if each.find('&amp;list')==-1:
                        if each.endswith('\n'):
                            self.links.add(each[0:len(each)-1])
                        else:
                            self.links.add(each)
            file.close()
        except Exception as ex:
            self.err=ex
            self.haserr=True
    
    def getNames(self):
        if(self.haserr):
            return getError()
        else:
            return list(self.names)
        
    def getLinks(self):
        if(self.haserr):
            return getError()
        else:
            return list(self.links)
    
    def getError(self):
        return self.err
    
class Like:
    
    def __init__(self, link):
        self.haserr=False
        self.err=None
        self.names=set()
        try:
            file = open('liked.ghh', 'a')
            file.write(link+'\n')
            file.close()
            AddPlayList(link,False)
            AddQueue(link)
            self.remove(link)
            ob=AddPlayList(name=[link],nme=False)
        except Exception as ex:
            self.haserr=True
            self.err=ex
    
    def hasErr(self):
        return self.haserr
    
    def getError(self):
        return self.err
    
    def remove(self,link):
        unliked=GetUnliked().getList()
        out=''
        for like in unliked:
            if like != link:
                out+=like+'\n'
        try:
            file=open('unliked.ghh','w')
            file.write(out)
        except Exception as ex:
            print(ex)
            self.haserr=True
            self.err=ex
            
class UnLike:
    
    def __init__(self, link):
        self.haserr=False
        self.err=None
        self.names=set()
        try:
            file = open('unliked.ghh', 'a')
            file.write(link+'\n')
            file.close()
            self.remove(link)
        except Exception as ex:
            self.haserr=True
            self.err=ex
    
    def hasErr(self):
        return self.haserr
    
    def getError(self):
        return self.err
    
    def remove(self,link):
        liked=GetLiked().getList()
        out=''
        for like in liked:
            if like != link:
                out+=like+'\n'
        try:
            file=open('liked.ghh','w')
            file.write(out)
        except Exception as ex:
            print(ex)
            self.haserr=True
            self.err=ex
        queue=GetQueue().get()
        out=''
        for song in queue:
            if song != link:
                out+=song+'\n'
        try:
            file=open('playlist.ghh','w')
            file.write(out)
        except Exception as ex:
            print(ex)
            self.haserr=True
            self.err=ex
                    
class Filter:
    
    def __init__(self,lst1,lst2):
        self.out=[]
        for item in lst1:
            if item not in lst2:
                self.out.append(item)
    
    def getList(self):
        return self.out
    
class GetLiked:
    
    def __init__(self):
        self.liked=set()
        self.out=[]
        self.haserr=False
        self.err=None
        try:
            file = open('liked.ghh','r')
            for each in file:
                if each.lstrip() != '':
                    if each.endswith('\n'):
                        self.liked.add(each[0:len(each)-1])
                    else:
                        self.liked.add(each)
            file.close()
            self.out=list(self.liked)
        except Exception as ex:
            self.haserr=True
            self.err=ex
    
    def getList(self):
        return self.out

class GetUnliked:
    
    def __init__(self):
        self.unliked=set()
        self.out=[]
        self.haserr=False
        self.err=None
        try:
            file = open('unliked.ghh','r')
            for each in file:
                if each.lstrip() != '':
                    if each.endswith('\n'):
                        self.unliked.add(each[0:len(each)-1])
                    else:
                        self.unliked.add(each)
            file.close()
            self.out=list(self.unliked)
        except Exception as ex:
            self.haserr=True
            self.err=ex
    
    def getList(self):
        return self.out
    
class GetQueue:
    
    def __init__(self):
        self.links=set()
        self.haserr=False
        try:
            file = open('playlist.ghh','r')
            for each in file:
                if each.lstrip() != '':
                    if each.find('&amp;list')==-1:
                        if each.endswith('\n'):
                            self.links.add(each[0:len(each)-1])
                        else:
                            self.links.add(each)
            file.close()
        except Exception as ex:
            self.err=ex
            self.haserr=True
    
    def get(self):
        return list(self.links)

class AddQueue:
    
    def __init__(self,link):
        try:
            file = open('playlist.ghh','a')
            file.write(link+'\n')
            file.close()
        except Exception as ex:
            print(ex)