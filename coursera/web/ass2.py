from urllib import request
from bs4 import BeautifulSoup 

req = request.urlopen("http://py4e-data.dr-chuck.net/comments_323661.html")
html = BeautifulSoup(req,'lxml')

span = html.find_all('span')
co = 0
sums = 0
for i in span:
    print(i.text)
    sums += int(i.text)
    co +=1
print("Total counts : ",co)

print("Sum is : ",sums)
