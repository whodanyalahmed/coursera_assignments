name = input("Enter file name: ")
fhand = open(name + ".txt")
words = dict()
for i in fhand:
    wo = i.split()
    for word in wo:
        words[word] = words.get(word,0) + 1

lst = list()

for k,v in words.items():
    newtup = (v,k)
    lst.append(newtup)

lst = sorted(lst,reverse=True)

for v,k in lst[:10]:
    print(k,v)