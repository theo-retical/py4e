name = input("Enter file:")

# open mbox file by default
if len(name) < 1:
    name = "mbox-short.txt"

# define lists, dictionaries and variables
handle = open(name)
hour_fetch = dict()
hour_list = list()
h_list = list()


# iterate over the lines in the file
for line in handle:
    # find lines starting with From
    if "From " in line:
        # split the words in the line
        words = line.split()
        # extract the times
        time = words[5]
        #extract the hours
        hour = time[:2]
        
        # add hour to dictionary as a key   
        hour_fetch[hour] = hour_fetch.get(hour, 0) + 1

# sort and print results

for hour, count in sorted(hour_fetch.items()):
    print (hour, count)
