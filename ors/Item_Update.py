#import all the modules
from tkinter import *
import mysql.connector
from mysql.connector import Error
import tkinter.messagebox

conn=mysql.connector.connect(host='localhost',
                             database='ors',
                             user='ors',
                             password='')
mycursor = conn.cursor()

class Database:
    def __init__(self,master,*args,**kwargs):
         self.master=master
         self.heading=Label(master,text="Update Item Information",font=('Courier new', 40),fg='black')
         self.heading.place(x=100,y=0)

         #label and entry for id
         self.id_le=Label(master,text="Enter Item No : ",font=('Courier new', 10))
         self.id_le.place(x=0,y=70)

         self.id_leb=Entry(master,font=('Courier new', 10),width=10)
         self.id_leb.place(x=380,y=70)

         self.btn_search=Button(master,text="search",width=8,height=0,bg='orange',command=self.search)
         self.btn_search.place(x=500,y=70)

         #lables  for the window
         self.itemname=Label(master,text="Enter Item Name : ",font=('Courier new', 10,'bold'))
         self.itemname.place(x=0,y=120)

         self.itemdescription=Label(master,text="Enter Item Description :",font=('Courier new', 10,'bold'))
         self.itemdescription.place(x=0,y=170)

         self.itemprice = Label(master, text="Enter Price : ", font=('Courier new', 10,'bold'))
         self.itemprice.place(x=0, y=220)

         self.itemquantity = Label(master, text="Enter Quantity : ", font=('Courier new', 10,'bold'))
         self.itemquantity.place(x=0, y=270)

  
        #enteries for window

         self.itemname=Entry(master,width=25,font=('Courier new', 10,'bold'))
         self.itemname.place(x=380,y=120)

         self.itemdescription = Entry(master, width=25, font=('Courier new', 10,'bold'))
         self.itemdescription.place(x=380, y=170)

         self.itemprice = Entry(master, width=25, font=('Courier new', 10,'bold'))
         self.itemprice.place(x=380, y=220)

         self.itemquantity = Entry(master, width=25, font=('Courier new', 10,'bold'))
         self.itemquantity.place(x=380, y=270)

       
         #button to add to the database
         self.btn_add=Button(master,text='Update Item ',width=27,height=1,bg='green',fg='white',command=self.update)
         self.btn_add.place(x=380,y=420)


    def search(self, *args, **kwargs):
         mycursor.execute("SELECT * FROM Item WHERE itemno=%s",[self.id_leb.get()])
         result = mycursor.fetchall()
         for r in result:
              self.n1 = r[1]
              self.n2 = r[2]
              self.n3 = r[3]
              self.n4 = r[4]
  
         conn.commit()

          #inster into the enteries to update
         self.itemname.delete(0,END)
         self.itemname.insert(0, str(self.n1))

         self.itemdescription.delete(0, END)
         self.itemdescription.insert(0, str(self.n2))

         self.itemprice.delete(0, END)
         self.itemprice.insert(0, str(self.n3))

         self.itemquantity.delete(0, END)
         self.itemquantity.insert(0, str(self.n4))

    

    def update(self,*args,**kwargs):
          self.u1 = self.itemname.get()
          self.u2 = self.itemdescription.get()
          self.u3 = self.itemprice.get()
          self.u4 = self.itemquantity.get()
    

          mycursor.execute("UPDATE item SET name=%s,description=%s,price=%s,quantity=%s WHERE itemno=%s",[self.u1,self.u2,self.u3,self.u4,self.id_leb.get()])
          conn.commit()
          tkinter.messagebox.showinfo("Success","Update Item successfully")


root=Tk()
b=Database(root)
root.geometry("1000x760+0+0")
root.title("Update Item Information")
root.mainloop()