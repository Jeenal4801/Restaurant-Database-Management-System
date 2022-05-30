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
        self.title('Add Restaurant')
        self.canvas = Canvas(width=500, height=417, bg='gray')
        self.canvas.pack()
        rest_name = StringVar()
        rest_address = StringVar()
        rest_contactno = StringVar()
        c = StringVar()
#verifying input
        def asi():
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                                        database='ors',
                                                        user='ors',
                                                        password='')
                    self.myCursor = self.conn.cursor()
                    restname = rest_name.get()
                    restaddress = rest_address.get()
                    restcontactno = rest_contactno.get()
                    self.myCursor.execute("Insert into restaurant(name,address,contactno) values (%s,%s,%s)",[restname,restaddress,restcontactno])
                    self.conn.commit()
                    messagebox.showinfo("Done","Restaurant Inserted Successfully")
                    ask = messagebox.askyesno("Confirm","Do you want to add another Restaurant?")
                    if ask:
                     self.destroy()
                     os.system('%s %s' % (py, 'Restaurant_Add.py'))
                    else:
                     self.destroy()
                     self.myCursor.close()
                     self.conn.close()
                except Error:
                    messagebox.showerror("Error","Something goes wrong")

        # label and input box
        Label(self, text='Restaurant Details',bg='gray', fg='white', font=('Courier new', 25, 'bold')).pack()
        Label(self, text='Restaurant Name:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=100)
        Entry(self, textvariable=rest_name, width=30).place(x=200, y=104)
        Label(self, text='Address:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=150)
        Entry(self, textvariable=rest_address, width=30).place(x=200, y=152)
        Label(self, text='Contact No:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=200)
        Entry(self, textvariable=rest_contactno, width=30).place(x=200, y=204)
        
        Button(self, text="Save", bg='blue', width=15, command=asi).place(x=200, y=380)

Add().mainloop()
