name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
cur = dict()
for i in handle:
    if i.startswith("From "):
    	words = i.split()
    	time = words[5].split(":")
        h = time[0]
    else:
        continue
print(time)