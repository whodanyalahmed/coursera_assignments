fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    f = line.split()
    for i in f:
        if i in lst:
            continue
        lst.append(i)
so = sorted(lst)
print(so)
