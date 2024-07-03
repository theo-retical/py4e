fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

count = 0
fh = open(fname)
linebacker = list()

# iterate over the lines
for line in fh:
    words = line.split()
    
    if "From" in words:
        print(words[1])
        count = count + 1

print("There were", count, "lines in the file with From as the first word")
