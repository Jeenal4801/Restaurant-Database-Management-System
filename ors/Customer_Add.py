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
        self.maxsize(500,417)
        self.minsize(500,417)
        self.title('Add Customer')
        self.canvas = Canvas(width=500, height=417, bg='gray')
        self.canvas.pack()
        cust_name = StringVar()
        cust_address = StringVar()
        cust_contactno = StringVar()
        c = StringVar()
#verifying input
        def asi():
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                                        database='ors',
                                                        user='ors',
                                                        password='')
                    self.myCursor = self.conn.cursor()
                    custname = cust_name.get()
                    custaddress = cust_address.get()
                    custcontactno = cust_contactno.get()
                    self.myCursor.execute("Insert into customer(name,address,contactno) values (%s,%s,%s)",[custname,custaddress,custcontactno])
                    self.conn.commit()
                    messagebox.showinfo("Done","Customer Inserted Successfully")
                    ask = messagebox.askyesno("Confirm","Do you want to add another Customer?")
                    if ask:
                     self.destroy()
                     os.system('%s %s' % (py, 'Customer_Add.py'))
                    else:
                     self.destroy()
                     self.myCursor.close()
                     self.conn.close()
                except Error:
                    messagebox.showerror("Error","Something goes wrong")

        # label and input box
        Label(self, text='Customer Details',bg='gray', fg='white', font=('Courier new', 25, 'bold')).pack()
        Label(self, text='Customer Name:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=100)
        Entry(self, textvariable=cust_name, width=30).place(x=200, y=104)
        Label(self, text='Address:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=150)
        Entry(self, textvariable=cust_address, width=30).place(x=200, y=152)
        Label(self, text='Contact No:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=200)
        Entry(self, textvariable=cust_contactno, width=30).place(x=200, y=204)
        
        Button(self, text="Save", bg='blue', width=15, command=asi).place(x=200, y=380)

Add().mainloop()
