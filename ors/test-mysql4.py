#import all the modules
from tkinter import *
import mysql.connector
from mysql.connector import Error
import tkinter.messagebox
import mysql.connector

#Establishing connection
conn = mysql.connector.connect(user='ors',
							host='localhost',
							password ='',
							database='ors')

# Creating a cursor object using
# the cursor() method
mycursor = conn.cursor();

print ("Enter Item name : ")
inputstring = input()
print ("input string : " , inputstring)


    #sql = "SELECT * FROM item WHERE itemno >= 5;"
    
    sql = """select * from item where itemno >= '%s'""" %inputstring
   
   # Execute the SQL command
   mycursor.execute(sql)
   
   # Fetch all the rows in a list of lists.
   
   results = mycursor.fetchall()
   for row in results:
     # print (row)
      
      itemno = row[0]
      print("itemno="%s,itemno)
     # itemname = row[1]
     # itemdescription = row[2]
     # itemprice = row[3]
     # itemquanitity = row[4] 
     # # Now print fetched result
     # print ("itemno = %s,itemname = %s,itemdescription = %d,itemprice = %s,itemquanitity = %d" % \
     #    (itemno, itemname, itemdescription, itemprice, itemquanitity ))
except:
   print ("Error: unable to fetch data")

# disconnect from server
conn.close()