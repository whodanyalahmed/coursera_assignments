from bs4 import BeautifulSoup
from urllib import request

o = request.urlopen("https://www.daraz.pk/dslr-hybrid-cameras/?spm=a2a0e.home.cate_1.8.35e34937OgPDuu").read()
html = BeautifulSoup(o,'lxml')
# print(html)
tags = html('span')
for tag in tags:
    print(tag.get('class',None)['c13VH6'])