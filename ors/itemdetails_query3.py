# Note : for installing tabulate package , please use this command : pip install tabulate
import mysql.connector
from tabulate import tabulate

mydb = mysql.connector.connect(
                host="localhost",
                user="ors",
                passwd="",
                database="ors"
              )

mycursor = mydb.cursor()
#mycursor.execute("SELECT itemno, name  FROM item")
mycursor.execute("SELECT itemno,name,quantity,price  FROM item")
myresult = mycursor.fetchall()


#print(tabulate(myresult, headers=['ItemNo', 'ItemName'], tablefmt='psql'))
print(tabulate(myresult, tablefmt='psql'))
