from html.parser import HTMLParser
class Article:

    def __init__(self, article):
        self.article = article

    def getTitle(self):
        ident = 'class=\"DY5T1d\" >'
        endit = '</a>'
        si = self.article.find(ident)
        if si == -1:
            return 'NOT FOUND'
        si += len(ident)
        ei = (self.article[si:]).find(endit)
        if ei == -1:
            return self.article[si:]+'END NOT FOUND'
        ei += si
        return self.article[si:ei]

    def getAuthor(self):
        identifier = "wEwyrc"
        start = False
        start2 = False
        si = -1
        ei = -1
        i = 0
        while i < len(self.article)-len(identifier):
            if self.article[i:i+len(identifier)] == identifier:
                start = True
            if start and self.article[i] == '>' and self.article[i+1] != '<':
                si = i+1
                start2 = True
            if start2 and self.article[i] == '<':
                ei = i-1
                break
            i += 1
        return self.article[si:ei+1]
    
    def getClass1(self):
        idnt='class=\"DY5T1d\" >'
        si=self.article.index(idnt)+len(idnt)
        tmp1=self.article[si:]
        ei = self.article[si:].index('</a>')
        return tmp1[:ei]
    
    def getClass2(self):
        idnt = 'class=\"xBbh9\">'
        si = self.article.index(idnt)+len(idnt)
        tmp1=self.article[si:]
        ei = self.article[si:].index('</span')
        return tmp1[:ei]

    def getShortDesc(self):
        out = self.getClass1()+' . '+self.getClass2()
        out = HTMLParser().unescape(out)
        return out

    def getImage(self):
        ident = 'src=\"'
        endnt = '\"'
        art = self.article[self.article.find(ident)+len(ident):]
        return art[:art.find(endnt)]

    def getUrl(self):
        url = "\"https://news.google.com"
        identifier = "./articles/"
        si = -1
        ei = -1
        i = 0
        while i < len(self.article)-len(identifier):
            if self.article[i:i+len(identifier)] == identifier:
                si = i-1
            elif i > si and si > -1 and self.article[i] == '\"':
                ei = i
                break
            i += 1
        return url+self.article[si+2:ei]+"\""

    def getPublishedAt(self):
        snip=self.article[self.article.find('datetime=\"'):]
        snip=snip[snip.find('>'):]
        return snip[:snip.find('<')]