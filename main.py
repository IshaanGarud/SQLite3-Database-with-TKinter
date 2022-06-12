# ------------------------------------------------------------|| श्री ||----------------------------------------

import sqlite3
from tkinter import *

root = Tk()
root.title("Database")
root.geometry("500x500")
conn = sqlite3.connect("C:/Users/WINDOWS/Desktop/PROGRAMMING/Python3_Desktop/DBprojects/DATABASES/User.db")
cursor = conn.cursor()

i_field_color = "#c4c3d0"

# Id, Name, Email, Password
# cursor.execute("CREATE TABLE Users (Id INTEGER, Name TEXT, Email TEXT, Password TEXT)")
# cursor.execute("INSERT INTO Users(Id, Name, Email, Password) VALUES (?, ?, ?, ?)", (1, tt, 'bruh@gmail.com', 'abcd'))

class Entry_Mode:
    def __init__(self):
        self.name = None
        self.email = None
        self.password = None
        self.re_password = None
        self.loc_col = 3
        self.name_field, self.email_field, self.password_field, self.re_password_field = Entry(root, bg=i_field_color), Entry(root, bg=i_field_color), Entry(root, bg=i_field_color), Entry(root, bg=i_field_color)
        self.errors = Label()
        self.errors.grid(row=3, column=self.loc_col+2)

        Label(root, text="Username:-").grid(row=0, column=self.loc_col), self.name_field.grid(row=0, column=self.loc_col + 1)
        Label(root, text="Email:-").grid(row=1, column=self.loc_col), self.email_field.grid(row=1, column=self.loc_col + 1)
        Label(root, text="Password:-").grid(row=2, column=self.loc_col), self.password_field.grid(row=2, column=self.loc_col + 1)
        Label(root, text="Re-Enter Password:-").grid(row=3, column=self.loc_col), self.re_password_field.grid(row=3, column=self.loc_col + 1)

        self.b_enter = Button(root, text="Enter", command=self.get_value and self.enter_data)
        self.b_enter.grid(row=10, column=self.loc_col + 1)

    def get_value(self):
        name = str(self.name_field.get())
        email = str(self.email_field.get())
        password = str(self.password_field.get())
        re_password = str(self.re_password_field.get())
        return name, email, password, re_password

    def id_gen(self):
        cursor.execute("SELECT * FROM Users")
        user_ids = cursor.fetchall()
        new_user_id = len(user_ids)+1
        return new_user_id

    def duplicate_email_detection(self, email):
        cursor.execute("SELECT Email FROM Users")
        email_list = cursor.fetchall()
        for user_email_i in email_list:
            # print(str(email) in user_email_i, [(str(email)), user_email_i])
            if (str(email) in user_email_i) == True:
                return True
                break

    def enter_data(self):
        self.name, self.email, self.password, self.re_password = self.get_value()
        self.id = self.id_gen()
        cursor.execute("SELECT Email FROM Users")
        self.isEmail_in_db = self.duplicate_email_detection(self.email)

        if (self.name != "" and self.email != "" and self.password != "") and (self.password == self.re_password):
            if self.isEmail_in_db == False or self.isEmail_in_db == None:            # i.e. If the Email is not in the Database
                cursor.execute("INSERT INTO Users(Id, Name, Email, Password) VALUES (?, ?, ?, ?)", (self.id, self.name, self.email, self.password))
                self.errors["text"] = ""
            elif self.isEmail_in_db == True:
                self.errors["text"] = "Already there"

        elif self.password != self.re_password:
            self.errors["text"] = "Passwords don't Match"
            self.errors.grid(row=4, column=self.loc_col)

            
# -------------------------------------Other Methods----------------------------------
def p_user():
    cursor.execute("SELECT * FROM Users")
    user_data = cursor.fetchall()
    for user in user_data:
        print(user)

def d():
    cursor.execute("DELETE FROM Users")

e_mode = Entry_Mode()
e_mode.enter_data()

p_b = Button(root, text="Print", command=p_user)
d_b = Button(root, text="Del", command=d)
p_b.grid(row=11, column=5)
d_b.grid(row=11, column=3)

root.mainloop()
conn.commit()
conn.close()

