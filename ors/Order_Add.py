from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
import sys
import mysql.connector
from mysql.connector import Error
py = sys.executable

#creating window
class Add(Tk):
    def __init__(self):
        super().__init__()
        #self.maxsize(500,417)
        #self.minsize(500,417)
        #self.canvas = Canvas(width=500, height=417, bg='gray')
        self.maxsize(600,500)
        self.minsize(600,500)
        self.title('Add Order')
        self.canvas = Canvas(width=600, height=500, bg='gray')
        self.canvas.pack()
        order_customerid = StringVar()
        order_managerid = StringVar()
        order_waiterid = StringVar()
        order_itemid = StringVar()
        order_quantity = StringVar()
        order_price = StringVar()
        c = StringVar()
        
        def customer_view():
           os.system('%s %s' % (py, 'Customer_View.py'))
        def manager_view():
           os.system('%s %s' % (py, 'Manager_View.py'))
        def waiter_view():
           os.system('%s %s' % (py, 'Waiter_View.py'))
        def item_view():
           os.system('%s %s' % (py, 'Item_View.py'))
  
 
        #verifying input
        def asi():
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                                        database='ors',
                                                        user='ors',
                                                        password='')
                    self.myCursor = self.conn.cursor()
                    ordercustomerid = order_customerid.get()
                    ordermanagerid = order_managerid.get()
                    orderwaiterid  =   order_waiterid.get()
                    orderitemid  =   order_itemid.get()
                    orderquantity = order_quantity.get()
                    #orderprice = order_price.get()
                    
                    #self.myCursor.execute("Insert into ors.order(customerid,managerid,waiterid,itemid,quantity,price ) values (%s,%s,%s,%s,%s,%s)",[ordercustomerid,ordermanagerid,orderwaiterid,orderitemid,orderquantity,orderprice])
                    self.myCursor.execute("Insert into ors.order(customerid,managerid,waiterid,itemid,quantity) values (%s,%s,%s,%s,%s)",[ordercustomerid,ordermanagerid,orderwaiterid,orderitemid,orderquantity])
                    self.conn.commit()
                    messagebox.showinfo("Done","Order Inserted Successfully")
                    ask = messagebox.askyesno("Confirm","Do you want to add another Order in Same Customer or New Order ?")
                    if ask:
                     self.destroy()
                     os.system('%s %s' % (py, 'Order_Add.py'))
                    else:
                     self.destroy()
                     self.myCursor.close()
                     self.conn.close()
                except Error:
                    messagebox.showerror("Error","Something goes wrong")

        # label and input box
        #Label(self, text='Order Details',bg='gray', fg='white', font=('Courier new', 25, 'bold')).pack()
        Label(self, text='Order Details',bg='gray', fg='white', font=('Courier new', 25, 'bold')).place(x=200, y=25)
        
        Label(self, text='Customer ID:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=100)
        Entry(self, textvariable=order_customerid, width=30).place(x=200, y=104)
        Label(self, text='Manager ID :', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=150)
        Entry(self, textvariable=order_managerid, width=30).place(x=200, y=152)
        
        Label(self, text='Waiter ID:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=200)
        Entry(self, textvariable=order_waiterid, width=30).place(x=200, y=204)
        Label(self, text='Item ID:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=250)
        Entry(self, textvariable=order_itemid, width=30).place(x=200, y=254)
        
        Label(self, text='Quantity:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=300)
        Entry(self, textvariable=order_quantity, width=30).place(x=200, y=304)
        #Label(self, text='Price:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=350)
        #Entry(self, textvariable=order_price, width=30).place(x=200, y=354)
       
           
        Button(self, text="Save", bg='blue', width=15, command=asi).place(x=200, y=380)
        
        # Customer - Button
        self.button = Button(self, text='View Customer(s)', width=20,bg='pink', font=('Courier new', 10), command=customer_view).place(x=400,y=100)
        self.button = Button(self, text='View Manager(s)', width=20,bg='pink', font=('Courier new', 10), command=manager_view).place(x=400,y=150)
        self.button = Button(self, text='View Waiter(s)', width=20,bg='pink', font=('Courier new', 10), command=waiter_view).place(x=400,y=200)
        self.button = Button(self, text='View Item(s)', width=20,bg='pink', font=('Courier new', 10), command=item_view).place(x=400,y=250)

Add().mainloop()
