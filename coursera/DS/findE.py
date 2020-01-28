# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
total = 0
count = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    pos = line.find(":")
    f = float(line[pos+1:])
    total = total + f
    pos = line.find(':')
average = total/count
print("Average spam confidence:",average)

