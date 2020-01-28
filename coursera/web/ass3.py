from urllib import request
from bs4 import BeautifulSoup 



def getnames(url,count,position):
    if(count == 0):
        exit()
    req = request.urlopen(url)
    html = BeautifulSoup(req,'lxml')
    span = html.find_all('a')


    url = span[position-1].get('href',None)
    # print(url)
    print(span[position-1].text)
    getnames(url,count-1,position)


url = input("Enter URL: ")
req = request.urlopen(url)
count = 1
count = int(input("Enter count: "))

position = 1
position = int(input("Enter Position: "))



getnames(url,count,position)





