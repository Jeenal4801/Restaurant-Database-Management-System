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

print ("Display the Order/Bill Details of Customer  : ")
print ("Enter Customer ID : ")
inputstring = input()
print ("input string : " , inputstring)


# SQL Query

#sql = "select price,count(*) from item group by price;"

#sql = """select * from order where customerid =     '%s'""" %inputstring
#sql = "select * from ors.order where customerid = %s" %inputstring

sql = "select order.orderdate, customer.name ,item.name , order.quantity, order.price \
        from ors.order, ors.customer,ors.item \
        where order.customerid= customer.customer_id \
        and order.itemid = item.itemno \
        and order.customerid = '%s'   \
        order by order.orderdate, order.customerid " %inputstring

#        and order.customerid = %s" %inputstring \

# Executing query
#mycursor.execute(sql,inputstring)
#mycursor.execute(sql,adr)

mycursor.execute(sql)

myresult = mycursor.fetchall()

#print(tabulate(myresult, tablefmt='psql'))
print(tabulate(myresult, headers=['OrderDate','CustName', 'ItemName','Quantity','Price'], tablefmt='psql'))

# conn.close()



mycursor = conn.cursor();
sql1 = "select bill.billdate, customer.name , bill.totqty, bill.totprice, bill.tax, bill.totvalue \
        from ors.bill , ors.customer  \
        where bill.customerid = customer.customer_id \
        and bill.customerid = '%s'   \
        order by bill.billdate, bill.customerid " %inputstring


mycursor.execute(sql1)
myresult = mycursor.fetchall()

#print(tabulate(myresult, tablefmt='psql'))
print(tabulate(myresult, headers=['Billdate', 'CustomerName','Tot.Qty','Tot.Price',"Total Tax","Tot.Value"], tablefmt='psql'))


#for x in myresult:
#	print(x)

# Closing the connection
conn.close()
