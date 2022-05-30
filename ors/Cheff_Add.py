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
        self.title('Add Cheff')
        self.canvas = Canvas(width=500, height=417, bg='gray')
        self.canvas.pack()
        cheff_name = StringVar()
        cheff_contactno = StringVar()
        c = StringVar()
#verifying input
        def asi():
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                                        database='ors',
                                                        user='ors',
                                                        password='')
                    self.myCursor = self.conn.cursor()
                    cheffname = cheff_name.get()
                    
                    self.myCursor.execute("Insert into cheff(name) values (%s)",[cheffname])
                    self.conn.commit()
                    messagebox.showinfo("Done","Cheff Inserted Successfully")
                    ask = messagebox.askyesno("Confirm","Do you want to add another Cheff?")
                    if ask:
                     self.destroy()
                     os.system('%s %s' % (py, 'Cheff_Add.py'))
                    else:
                     self.destroy()
                     self.myCursor.close()
                     self.conn.close()
                except Error:
                    messagebox.showerror("Error","Something goes wrong")

        # label and input box
        Label(self, text='Cheff Details',bg='gray', fg='white', font=('Courier new', 25, 'bold')).pack()
        Label(self, text='Cheff Name:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=100)
        Entry(self, textvariable=cheff_name, width=30).place(x=200, y=104)
        
        Button(self, text="Save", bg='blue', width=15, command=asi).place(x=200, y=380)

Add().mainloop()
