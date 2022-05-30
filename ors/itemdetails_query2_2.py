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

print ("Display the Order Details of Customer ")
print ("Enter Customer ID : ")
inputstring = input()
print ("input string : " , inputstring)


# SQL Query

#sql = "select price,count(*) from item group by price;"

#sql = """select * from order where customerid =     '%s'""" %inputstring
#sql = "select * from ors.order where customerid = %s" %inputstring

sql = "select customer.name ,item.name , order.quantity, order.price \
        from ors.order, ors.customer,ors.item \
        where order.customerid= customer.customer_id \
        and order.itemid = item.itemno \
        and order.customerid = %s" %inputstring



# Executing query
#mycursor.execute(sql,inputstring)
#mycursor.execute(sql,adr)

mycursor.execute(sql)

myresult = mycursor.fetchall()

#print(tabulate(myresult, tablefmt='psql'))
print(tabulate(myresult, headers=['CustName', 'ItemName','Quantity','Price'], tablefmt='psql'))


#for x in myresult:
#	print(x)

# Closing the connection
conn.close()
