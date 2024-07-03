# import libraries
import sqlite3

# connect to sqllite database
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# delete table to start fresh
cur.execute('DROP TABLE IF EXISTS Counts')

# create table called counts with domain and count columns
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

# file name input
fname = input('Enter file name: ')

# redundacny if blank
if (len(fname) < 1): 
    fname = 'mbox.txt'

# open file
fh = open(fname)

# loop through file
for line in fh:
    # find lines that start with 'From '
    if not line.startswith('From: '):
        continue
        
    # split line into words
    pieces = line.split()

    # email address is the second word in the line so can be selected by [1]
    email = pieces[1]
    #print(email)
