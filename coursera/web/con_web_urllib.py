# import urllib.request,urllib.error,urllib.parse
# html = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

# for d in html:
#     print(d.decode().strip())



import urllib.request,urllib.error,urllib.parse
html = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

counts = dict()

for d in html:
    words = d.decode().split()
    for word in words:
        counts[word] = counts.get(word,0)+1

print(counts)