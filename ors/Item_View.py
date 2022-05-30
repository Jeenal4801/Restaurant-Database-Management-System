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
       
        #def order_update():
        #    os.system('%s %s' % (py, 'Order_Update.py'))
        #def order_delete():
        #    os.system('%s %s' % (py, 'Order_Delete.py'))


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
                    #self.label6 = Label(self, text="ITEM INFORMATION DETAILS",bg="pink",  font=('Courier new', 15, 'underline', 'bold'))
                    #self.label6.place(x=150, y=200)
                    

                    # Customer - Button
                    self.button = Button(self, text='View Item(s)', width=20,bg='pink', font=('Courier new', 10), command=ser).place(x=200,y=250)






        check()

MainWin().mainloop()
