counts = dict()
names = ["Ali","Dan","Soul","Dan","Soul"]

for name in names:
    counts[name] = counts.get(name,0) + 1
print(counts)