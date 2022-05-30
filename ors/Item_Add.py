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
        self.title('Add Item')
        self.canvas = Canvas(width=500, height=417, bg='gray')
        self.canvas.pack()
        item_name = StringVar()
        item_description = StringVar()
        item_price = StringVar()
        item_quantity = StringVar()
        c = StringVar()
#verifying input
        def asi():
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                                        database='ors',
                                                        user='ors',
                                                        password='')
                    self.myCursor = self.conn.cursor()
                    itemname = item_name.get()
                    itemdescription = item_description.get()
                    itemprice = item_price.get()
                    itemquantity = item_quantity.get()
                    self.myCursor.execute("Insert into item(name,description,price,quantity ) values (%s,%s,%s,%s)",[itemname,itemdescription,itemprice,itemquantity])
                    self.conn.commit()
                    messagebox.showinfo("Done","Item Inserted Successfully")
                    ask = messagebox.askyesno("Confirm","Do you want to add another Item?")
                    if ask:
                     self.destroy()
                     os.system('%s %s' % (py, 'Item_Add.py'))
                    else:
                     self.destroy()
                     self.myCursor.close()
                     self.conn.close()
                except Error:
                    messagebox.showerror("Error","Something goes wrong")

        # label and input box
        Label(self, text='Item Details',bg='gray', fg='white', font=('Courier new', 25, 'bold')).pack()
        Label(self, text='Item Name:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=100)
        Entry(self, textvariable=item_name, width=30).place(x=200, y=104)
        Label(self, text='Description:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=150)
        Entry(self, textvariable=item_description, width=30).place(x=200, y=152)
        Label(self, text='Price:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=200)
        Entry(self, textvariable=item_price, width=30).place(x=200, y=204)
        Label(self, text='Quantity:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=250)
        Entry(self, textvariable=item_quantity, width=30).place(x=200, y=254)
        Button(self, text="Save", bg='blue', width=15, command=asi).place(x=200, y=380)

Add().mainloop()
