import mysql.connector

#Establishing connection
conn = mysql.connector.connect(user='ors',
							host='localhost',
							password ='',
							database='ors')

# Creating a cursor object using
# the cursor() method
mycursor = conn.cursor();

print ("Display the Order Details of Customer ")
print ("Enter Customer ID : ")
inputstring = input()
print ("input string : " , inputstring)


# SQL Query

#sql = "select price,count(*) from item group by price;"

#sql = """select * from order where customerid =     '%s'""" %inputstring
sql = "select * from ors.order where customerid = %s" %inputstring



# Executing query
#mycursor.execute(sql,inputstring)
#mycursor.execute(sql,adr)

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
	print(x)

# Closing the connection
conn.close()
