count = dict()
line = input("Enter line you want to count: ")
words = line.split()

print("Words: ",words)
print("Counting...")

for i in words:
    count[i] = count.get(i,0) + 1
print(count)
print(list(count))