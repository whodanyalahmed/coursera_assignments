import re

f = open("dan.txt","r")
x = f.read()
f.close()

y = re.findall('[0-9]+',x)
d = []
for i in y:
    i = int(i)
    d.append(i)

print(sum(d))