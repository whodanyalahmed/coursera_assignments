name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
cur = dict()
for i in handle:
    if i.startswith("From "):
        sp = i.split()
        #for d in sp: 
        #	h = d.split(":")
        cur[sp[5].split(":")[0]] = cur.get(sp[5].split(":")[0],0)+1
    else:
        continue

m = 0
for k,v in sorted(cur.items()):
    print(k,v)