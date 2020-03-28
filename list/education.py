fname = input("Enter file name: ")
if len(fname) < 1: fname = "mbox-short.txt"

fh = open(fname)
count = 0

for i in fh:
    if i.startswith('From '):
        count += 1
        print(i.split()[1])

print("There were", count, "lines in the file with From as the first word")
