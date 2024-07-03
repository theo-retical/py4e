# prompt for file name
name = input("Enter file:")

# open mbox file by default
if len(name) < 1:
    name = "mbox-short.txt"

# define lists, dictionaries and variables
handle = open(name)
addresses = dict()
most_sent = None
most_freq_sender = None

# iterate over the lines in the file
for line in handle:
    # find lines starting with From
    if "From " in line:
        # split the words in the line
        words = line.split()
        
        # extract sender (email address, this is the second value in the words array)
        sender = words[1]
        
        # add email address to the addresses dictionary - this is the key, the value is the counter
        addresses[sender] = addresses.get(sender, 0) + 1

# create a max loop, check sender in the dictionary and the send count              
for sender,sent in addresses.items():
    # most_freq_sender starts at zero, so set as the sender found in the dictionary at the same time set the most_sent to the corresponding count until the highest sent value is found
    if most_freq_sender is None or sent > most_sent:
        most_freq_sender = sender
        most_sent = sent
                
print(most_freq_sender, most_sent)   
