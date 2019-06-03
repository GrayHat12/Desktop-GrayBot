import requests as req
import urllib as urlib
import Article

class GrayNews:

    HOME = "https://news.google.com/"
    WORLD = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pKVGlnQVAB"
    TECHNOLOGY = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pKVGlnQVAB"
    SCIENCE = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp0Y1RjU0FtVnVHZ0pKVGlnQVAB"

    def __init__(self, search='Google'):
        self.search = search
        self.madeReq = False
        self.reqerr = None
        self.lnk = "https://news.google.com/search?q="
        #if search == GrayNews.HOME:
            #self.lnk = GrayNews.HOME
        #elif search == GrayNews.WORLD:
            #self.lnk = GrayNews.WORLD
        #elif search == GrayNews.TECHNOLOGY:
            #self.lnk = GrayNews.TECHNOLOGY
        #elif search == GrayNews.SCIENCE:
            #self.lnk = GrayNews.SCIENCE
        #else:
        #print(search)
        self.lnk = "https://news.google.com/search?q="+urlib.parse.quote(str(self.search).encode('utf-8'))

    def getSource(self):
        if self.madeReq:
            return self.lnk
        else:
            return -1

    def getRequestError(self):
        if self.reqerr == None:
            return None
        else:
            return self.reqerr

    def makeRequest(self):
        try:
            r = req.get(self.lnk)
            self.code = r.text
            self.madeReq = True
        except Exception as err:
            self.reqerr = err
            self.madeReq = False
            return False

    def getArticles(self):
        indent = '<div class=\"NiLAwe y6IFtc R7GTQ keNKEd j7vNaf nID9nc\">'
        endent = '</article>'
        self.out = []
        while self.code.find(indent) != -1:
            self.code = self.code[self.code.find(indent):]
            self.out.append(Article.Article(self.code[:self.code.find(endent)]))
            self.code = self.code[self.code.find(endent):]
        return self.out