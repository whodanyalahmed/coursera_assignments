name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for i in handle:
    if i.startswith("From "):
        sp = i.split()
        counts[sp[1]] = counts.get(sp[1],0)+1
    else:
        continue
mx = 0
high = dict()

for j,k in counts.items():
    if k > mx:
        mx = k
        high[j] = k
        lg = j
    else:
        continue


print(lg,mx)