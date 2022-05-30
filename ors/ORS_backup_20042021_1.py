from tkinter import *
from tkinter import messagebox
import os
import sys
from tkinter import ttk

import mysql.connector
from mysql.connector import Error

py=sys.executable

#creating window
class MainWin(Tk):
    def __init__(self):
        super().__init__()
        self.configure(bg='gray')
        self.canvas = Canvas(width=1366, height=768, bg='gray')
        self.canvas.pack()
        self.maxsize(1320, 768)
        self.minsize(1320,768)
        self.state('zoomed')
        self.title('Online Restaurant Management System')
        self.a = StringVar()
        self.b = StringVar()
        self.mymenu = Menu(self)
#calling scripts

 
       
        # call Restaurant foam
        def restaurant_add():
            os.system('%s %s' % (py,'Restaurant_Add.py'))
        #def restaurant_update():
        #    os.system('%s %s' % (py, 'Restaurant_Update.py'))
        def restaurant_delete():
            os.system('%s %s' % (py, 'Restaurant_Delete.py'))
            
        # call Manager foam
        def manager_add():
            os.system('%s %s' % (py,'Manager_Add.py'))
        #def manager_update():
        #    os.system('%s %s' % (py, 'Manager_Update.py'))
        def manager_delete():
            os.system('%s %s' % (py, 'Manager_Delete.py'))
            
        # call Waiter foam
        def waiter_add():
            os.system('%s %s' % (py,'Waiter_Add.py'))
        #def waiter_update():
        #    os.system('%s %s' % (py, 'Waiter_Update.py'))
        def waiter_delete():
            os.system('%s %s' % (py, 'Waiter_Delete.py'))
            
         # call Cheff foam
        def cheff_add():
            os.system('%s %s' % (py,'Cheff_Add.py'))
        #def cheff_update():
        #    os.system('%s %s' % (py, 'Cheff_Update.py'))
        def cheff_delete():
            os.system('%s %s' % (py, 'Cheff_Delete.py'))

        # call Cashier foam
        def cashier_add():
            os.system('%s %s' % (py,'Cashier_Add.py'))
        #def cashier_update():
        #    os.system('%s %s' % (py, 'Cashier_Update.py'))
        def cashier_delete():
            os.system('%s %s' % (py, 'Cashier_Delete.py'))

       # call Item foam
        def item_add():
            os.system('%s %s' % (py,'Item_Add.py'))
        def item_update():
            os.system('%s %s' % (py, 'Item_Update.py'))
        def item_delete():
            os.system('%s %s' % (py, 'Item_Delete.py'))


      # call Customer foam
        def customer_add():
            os.system('%s %s' % (py,'Customer_Add.py'))
        #def customer_update():
        #    os.system('%s %s' % (py, 'Customer_Update.py'))
        def customer_delete():
            os.system('%s %s' % (py, 'Customer_Delete.py'))

      # call Order foam
        def order_add():
            os.system('%s %s' % (py,'Order_Add.py'))
        #def order_update():
        #    os.system('%s %s' % (py, 'Order_Update.py'))
        def order_delete():
            os.system('%s %s' % (py, 'Order_Delete.py'))


#creating table

        self.listTree = ttk.Treeview(self,height=14,columns=('Name','Description','Price','Quantity'))
        self.vsb = ttk.Scrollbar(self,orient="vertical",command=self.listTree.yview)
        self.hsb = ttk.Scrollbar(self,orient="horizontal",command=self.listTree.xview)
        self.listTree.configure(yscrollcommand=self.vsb.set,xscrollcommand=self.hsb.set)
        self.listTree.heading("#0", text='Itemno')
        self.listTree.column("#0", width=50,minwidth=50,anchor='center')
        self.listTree.heading("Name", text='Name')
        self.listTree.column("Name", width=200, minwidth=200,anchor='center')
        self.listTree.heading("Description", text='Description')
        self.listTree.column("Description", width=200, minwidth=200,anchor='center')
        self.listTree.heading("Price", text='Price')
        self.listTree.column("Price", width=125, minwidth=125,anchor='center')
        self.listTree.heading("Quantity", text='Quantity')
        self.listTree.column("Quantity", width=125, minwidth=125, anchor='center')
        self.listTree.place(x=200,y=325)
        self.vsb.place(x=975,y=325,height=310)
        self.hsb.place(x=200,y=650,width=800)
        ttk.Style().configure("Treeview",font=('Times new Roman',15))        
        



        def ser():
             try:
                conn = mysql.connector.connect(host='localhost',
                                         database='ors',
                                         user='ors',
                                         password='')
                cursor = conn.cursor()

                cursor.execute("Select * from item order by itemno")
                pc = cursor.fetchall()
                if pc:
                    self.listTree.delete(*self.listTree.get_children())
                    for row in pc:
                        self.listTree.insert("",'end',text=row[0] ,values = (row[1],row[2],row[3],row[4]))
                else:
                    messagebox.showinfo("Error", "No Item...!")
             except Error:
                #print(Error)
              messagebox.showerror("Error","Something Goes Wrong")

        def check():

                    #label and input box
                    self.label3 = Label(self, text='Online Restaurant Management System',fg='black',bg="gray" ,font=('Courier new', 30, 'bold'))
                    self.label3.place(x=100, y=22)
                    #self.label6 = Label(self, text="ITEM INFORMATION DETAILS",bg="gray",  font=('Courier new', 15, 'underline', 'bold'))
                    #self.label6.place(x=150, y=200)
                    

                    # Restaurant - Button
                    #self.button = Button(self, text='View Restaurant(s)', width=20,bg='blue', font=('Courier new', 10), command=ser).place(x=200,y=100)
                    self.button = Button(self, text='Add Restaurant', width=20,bg='green', font=('Courier new', 10), command=restaurant_add).place(x=400,y=100)
                    #self.brt = Button(self, text="Update Restaurant", width=20,bg='orange', font=('Courier new', 10), command=item_update).place(x=600, y=100)
                    self.brt = Button(self, text="Delete Restaurant", width=20,bg='red', font=('Courier new', 10), command=restaurant_delete).place(x=800, y=100)

                    # Manager - Button
                    #self.button = Button(self, text='View Manager(s)', width=20,bg='blue', font=('Courier new', 10), command=ser).place(x=200,y=125)
                    self.button = Button(self, text='Add Manager', width=20,bg='green', font=('Courier new', 10), command=manager_add).place(x=400,y=125)
                    #self.brt = Button(self, text="Update Manager", width=20,bg='orange', font=('Courier new', 10), command=manager_update).place(x=600, y=125)
                    self.brt = Button(self, text="Delete Manager", width=20,bg='red', font=('Courier new', 10), command=manager_delete).place(x=800, y=125)

                    # Waiter - Button
                    #self.button = Button(self, text='View Waiter(s)', width=20,bg='blue', font=('Courier new', 10), command=ser).place(x=200,y=150)
                    self.button = Button(self, text='Add Waiter', width=20,bg='green', font=('Courier new', 10), command=waiter_add).place(x=400,y=150)
                    #self.brt = Button(self, text="Update Waiter", width=20,bg='orange', font=('Courier new', 10), command=waiter_update).place(x=600, y=150)
                    self.brt = Button(self, text="Delete Waiter", width=20,bg='red', font=('Courier new', 10), command=waiter_delete).place(x=800, y=150)

                    # Cheff - Button
                    #self.button = Button(self, text='View Cheff(s)', width=20,bg='blue', font=('Courier new', 10), command=ser).place(x=200,y=175)
                    self.button = Button(self, text='Add Cheff', width=20,bg='green', font=('Courier new', 10), command=cheff_add).place(x=400,y=175)
                    #self.brt = Button(self, text="Update Cheff", width=20,bg='orange', font=('Courier new', 10), command=cheff_update).place(x=600, y=175)
                    self.brt = Button(self, text="Delete Cheff", width=20,bg='red', font=('Courier new', 10), command=cheff_delete).place(x=800, y=175)

                    # Cashier - Button
                    #self.button = Button(self, text='View Cashier(s)', width=20,bg='blue', font=('Courier new', 10), command=ser).place(x=200,y=200)
                    self.button = Button(self, text='Add Cashier', width=20,bg='green', font=('Courier new', 10), command=cashier_add).place(x=400,y=200)
                    #self.brt = Button(self, text="Update Cashier", width=20,bg='orange', font=('Courier new', 10), command=cashier_update).place(x=600, y=200)
                    self.brt = Button(self, text="Delete Cashier", width=20,bg='red', font=('Courier new', 10), command=cashier_delete).place(x=800, y=200)

                    # Item - Button
                    self.button = Button(self, text='View Item(s)', width=20,bg='blue', font=('Courier new', 10), command=ser).place(x=200,y=225)
                    self.button = Button(self, text='Add Item', width=20,bg='green', font=('Courier new', 10), command=item_add).place(x=400,y=225)
                    self.brt = Button(self, text="Update Item", width=20,bg='orange', font=('Courier new', 10), command=item_update).place(x=600, y=225)
                    self.brt = Button(self, text="Delete Item", width=20,bg='red', font=('Courier new', 10), command=item_delete).place(x=800, y=225)

                    # Customer - Button
                    #self.button = Button(self, text='View Customer(s)', width=20,bg='blue', font=('Courier new', 10), command=ser).place(x=200,y=250)
                    self.button = Button(self, text='Add Customer', width=20,bg='green', font=('Courier new', 10), command=customer_add).place(x=400,y=250)
                    #self.brt = Button(self, text="Update Customer", width=20,bg='orange', font=('Courier new', 10), command=customer_update).place(x=600, y=250)
                    self.brt = Button(self, text="Delete Customer", width=20,bg='red', font=('Courier new', 10), command=customer_delete).place(x=800, y=250)


                    # Order - Button
                    #self.button = Button(self, text='View Order(s)', width=20,bg='blue', font=('Courier new', 10), command=ser).place(x=200,y=275)
                    self.button = Button(self, text='Add Order', width=20,bg='green', font=('Courier new', 10), command=order_add).place(x=400,y=275)
                    #self.brt = Button(self, text="Update Order", width=20,bg='orange', font=('Courier new', 10), command=order_update).place(x=600, y=275)
                    self.brt = Button(self, text="Delete Order", width=20,bg='red', font=('Courier new', 10), command=order_delete).place(x=800, y=275)


        check()

MainWin().mainloop()
