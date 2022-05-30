
import mysql.connector

#Establishing connection
conn = mysql.connector.connect(user='ors',
							host='localhost',
							password ='',
							database='ors')

# Creating a cursor object using
# the cursor() method
mycursor = conn.cursor();


sql = "SELECT * FROM ors.order;"
mycursor.execute(sql)
conn.commit()
results = mycursor.fetchall()

widths = []
columns = []
tavnit = '|'
separator = '+' 

for cd in mycursor.description:
    widths.append(max(cd[2], len(cd[0])))
    columns.append(cd[0])

for w in widths:
    tavnit += " %-"+"%ss |" % (w,)
    separator += '-'*w + '--+'

print(separator)
print(tavnit % tuple(columns))
print(separator)

for row in results:
    print(tavnit % row)
print(separator)