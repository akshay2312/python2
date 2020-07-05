from tkinter import *
import mysql.connector
import tkinter.messagebox as MessageBox
def insert():
    n = name.get()
    e = email.get()
    id = username.get()
    pas = password.get()

    if (n== "" or e == "" or id == "" or pas == ""):
        MessageBox.showinfo("Registration status", "All fields are mandatory")
    else:

            connection = mysql.connector.connect(host="localhost", user="root", password="8843", database="game")
            cursor = connection.cursor()
            cursor.execute(
                "insert into userinfo values('" + n + "','" + e + "','" + id + "','" + pas + "')")
            cursor.execute("commit")

            name.delete(0, 'end')
            email.delete(0, 'end')
            username.delete(0, 'end')
            password.delete(0, 'end')
            MessageBox.showinfo("registration status", "Registration complete")
            cursor.close()
def new_screen():
       screen=Toplevel()
       screen.geometry("400x300")
       screen.title("Register")
       #label
       label = Label(screen, text="Register here", bg="grey", width="30", height="3", font=("Calibri", 13))
       label.grid(row=0,column=1)
       name_label = Label(screen,text="Name:",font=("Calibri",13))
       name_label.grid(row=1,column=0)
       email_label = Label(screen, text="E-mail:",font=("Calibri",13))
       email_label.grid(row=2, column=0)
       username_label = Label(screen, text="Username:",font=("Calibri",13))
       username_label.grid(row=3, column=0)
       password_label = Label(screen, text="Password:",font=("Calibri",13))
       password_label.grid(row=4, column=0)
       # text box
       name=Entry(screen,width=25)
       name.grid(row=1,column=1)
       email = Entry(screen, width=25)
       email.grid(row=2, column=1)
       username = Entry(screen, width=25)
       username.grid(row=3, column=1)
       password = Entry(screen, width=25)
       password.grid(row=4, column=1)
       #button
       register = Button(screen, text="REGISTER", width="30", height="1",command=insert)
       register.grid(row=5, column=0 , columnspan=2,pady=10,padx=10)







root = Tk()
root.title("login Page")
root.geometry("400x300")

# creating label widget
myLabel1 = Label(root,text="Welcome Back!!",bg="grey",width="30",height="3",font=("Calibri",13))
myLabel2 = Label(root,text="Username:",font=("Calibri",13))
myLabel3 = Label(root,text="Password:",font=("Calibri",13))
myLabel4 = Label(root,text="new user,register",font=("Calibri",9),fg="blue")
# shoving it onto the screen
myLabel1.grid(row=0,column=1)
myLabel2.grid(row=1,column=0)
myLabel3.grid(row=2,column=0)
myLabel4.grid(row=5,column=1)
# Creating input box
username=Entry(root,width=25)
username.grid(row=1,column=1,padx=10,pady=10)
password=Entry(root,width=25)
password.grid(row=2,column=1)
#creating buttons
login = Button(root,text="LOGIN",width="20", height="1")
login.grid(row=3, column=1,pady=10)
register = Button(root,text="REGISTER",width="20",height="1",command=new_screen)
register.grid(row=4,column=1)





root.mainloop()