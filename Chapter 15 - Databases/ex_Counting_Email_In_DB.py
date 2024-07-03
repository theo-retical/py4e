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

    # extract the domain name from the email address
    org = email.split('@')[1]
    #print(domain)
    
    # count the number of times the domain appears in the file, this is done by
    # selecting the domain from domain and adding 1 to the count when it appears
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    
    # if the domain is not in the database, add it to the database, count of 1
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
               VALUES (?, 1)''', (org,))
    else:
       cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
