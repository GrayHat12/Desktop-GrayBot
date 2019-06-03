import GrayAPI
import colorama as clr

inp = input('Input the Topic to get News On : ')
ob = GrayAPI.GrayNews(inp)

print('MAKE REQUEST ', ob.makeRequest())
print('REQ ERR ', ob.getRequestError())
print('SOURCE ', ob.getSource(),end='\n\n')
art = ob.getArticles()
#print('GET ARTICLES ',art)
print('LENGTH : ', len(art),end='\n\n')

clr.init(autoreset=True)
for ar in art:
    print(clr.Fore.RED+'TITLE : ', clr.Fore.GREEN+str(ar.getTitle()))
    print(clr.Fore.RED+'AUTHOR : ', clr.Fore.GREEN+str(ar.getAuthor()))
    print(clr.Fore.RED+'URL : ', clr.Fore.GREEN+str(ar.getUrl()))
    print(clr.Fore.RED+'DESCRIPTION : ', clr.Fore.GREEN+str(ar.getShortDesc()))
    print(clr.Fore.RED+'IMAGE : ', clr.Fore.GREEN+str(ar.getImage()))
    print(clr.Fore.RED+'PUBLISHED : ', clr.Fore.GREEN+str(ar.getPublishedAt()))
    print('\n\n')
