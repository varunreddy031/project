import sys
import csv
import os

import sqlite3
con = sqlite3.connect('business1')

cur = con.cursor()
cur.execute('SELECT * FROM finan;')
names = [description[0] for description in cur.description]
rows = cur.fetchall()
fp = open('finan1.csv', 'w')
myFile = csv.writer(fp)
myFile.writerows([names])
myFile.writerows(rows)
fp.close()
print('finan1.csv file successfully created')
cur.execute('SELECT * FROM trans;')
names = [description[0] for description in cur.description]
rows = cur.fetchall()
fp = open('trans1.csv', 'w')
myFile = csv.writer(fp)
myFile.writerows([names])
myFile.writerows(rows)
fp.close()
print('trans1.csv file successfully created')
con.commit()

