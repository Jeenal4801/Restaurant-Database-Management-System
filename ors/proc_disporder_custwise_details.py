import mysql.connector
from tabulate import tabulate


#Establishing connection
conn = mysql.connector.connect(user='ors',
							host='localhost',
							password ='',
							database='ors')

# Creating a cursor object using
# the cursor() method
mycursor = conn.cursor();

print ("Customerwise Order Details")
print ("=========================================")

print ("Enter Customer ID : ")
inputstring = input()
# print ("input string : " , inputstring)


# SQL Query

#sql = "select price,count(*) from item group by price;"

#sql = """select * from item where name like     '%s'""" %inputstring
#sql = "call proc_dispitem('%s') " %inputstring
#sql = "call proc_dispitem('%s') " %inputstring
#print ("sql: " , sql)


args=mycursor.callproc('proc_disporder_custwise',(inputstring,))
# print ("args : ", args)


#for result in mycursor.stored_results():
#    print(result.fetchall())


for result in mycursor.stored_results():
#    print(tabulate(result, tablefmt='psql'))
    print(tabulate(result, headers=['Cust. Name','Order Date','Item Name','Qty','Price'], tablefmt='psql'))


# Executing query
#mycursor.execute(sql,inputstring)
#mycursor.execute(sql,adr)

#mycursor.execute(sql)
#myresult = mycursor.fetchall()
#for x in myresult:
#	print(x)

# Closing the connection
conn.close()
