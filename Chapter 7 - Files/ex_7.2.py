# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
tot_values = 0
number_average = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    # update the count tally
    count = count + 1
    
    # extract the value as float
    spam_value = float(line.rstrip().split(": ",-1)[1])
    
    # add the values together
    tot_values = tot_values + spam_value
    
    # calculate the average (standard maths)
    number_average = tot_values / count
    
print("Average spam confidence:", number_average)
