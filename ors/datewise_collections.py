import mysql.connector
from tabulate import tabulate
from datetime import date

#Establishing connection
conn = mysql.connector.connect(user='ors',
							host='localhost',
							password ='',
							database='ors')

# Creating a cursor object using
# the cursor() method
mycursor = conn.cursor();

today = str(date.today())
#print(today)

print ("Datewise Total Amt. Collection Details : ")
print ("=====================================================");

print ("Enter Orde/Bill Date in YYYY-MM-DD Format : [Press Enter for All Date Records] ")
inputstring = input()
#print ("input string : " , inputstring)
#inputstring = today ;

if inputstring == '' : 
   sql=  "select o.orderdate , count(*) , sum(o.quantity) , sum(o.price)   \
            from  ors.order o  \
        group by o.orderdate \
        order by o.orderdate " 
else: 
    sql=  "select o.orderdate , count(*) , sum(o.quantity) , sum(o.price)   \
            from  ors.order o  \
            where o.orderdate = '%s'  \
        group by o.orderdate \
        order by o.orderdate " %inputstring


# SQL Query

#sql = "select price,count(*) from item group by price;"

#sql = """select * from order where customerid =     '%s'""" %inputstring
#sql = "select * from ors.order where customerid = %s" %inputstring



# Executing query
#mycursor.execute(sql,inputstring)
#mycursor.execute(sql,adr)

mycursor.execute(sql)

myresult = mycursor.fetchall()

#print(tabulate(myresult, tablefmt='psql'))
print(tabulate(myresult, headers=['Order Date','Ttoal Orders','Total Item Quantity','Total Price'], tablefmt='psql'))


#for x in myresult:
#	print(x)

# Closing the connection
conn.close()
