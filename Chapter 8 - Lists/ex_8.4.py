fname = input("Enter file name: ")
fh = open(fname)
lst = list()
# for each line, split the words and add them to a list called words
for line in fh:
    words = line.split()
    # for each word in the list words check if it is present in list lst, if not add it
    for word in words:
        if word not in lst:
            lst.append(word)
    # sort the list
    lst.sort()
# print the lst
print(lst)
