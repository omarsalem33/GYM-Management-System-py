from tkinter import*
from tkinter import messagebox
import sqlite3


db =sqlite3.connect("GYM.DB")
cr=db.cursor()
cr.execute("CREATE TABLE if not exists  Client (id INTEGER PRIMARY KEY,age INTEGER ,name TEXT,RenewalDate TEXT,startDate TEXT,gender)")
cr.execute("CREATE TABLE if not exists payment (id INTEGER,payment TEXT)")

root = Tk()
root.geometry("500x500")
root.resizable(False,False)
root.config(background="#333333")
root.title('Admin')

pagenum = 1

def page1():
    page=Frame(root)
    photo=PhotoImage("f")
    fnt="none 14 bold"
    username_text=Label(text="Username",bg="#333333",fg="#CC6666",font=fnt)
    password_text=Label(text="Password",bg="#333333",fg="#CC6666",font=fnt)
    
    username=StringVar()
    password=StringVar()
    username_text.place(x=200,y=100)
    password_text.place(x=200,y=190)
    username_entry=Entry(textvariable=username,width=20,font="none 20 ")
    passwor_entry = Entry(textvariable=password, width=20,font="none 20")
    username_entry.place(x=100,y=130)
    passwor_entry.place(x=100,y=220)
    b1=Button(text="Login",bg="#CC6666",fg="black",font=fnt,width="10",height="1")
    b1.place(x=185,y=300)
    def login():
        if username.get() !="admin":
            messagebox.showinfo("wrong","wrong username or password")
        elif password.get() !="admin":
            messagebox.showinfo("wrong","wrong username or password")
        else:
            b1.config(command=changepage1)
    b1.config(command=login)

def page2():
    page=Frame(root)
    fnt="none 12 "
    fnnt="none 12 bold"
    b1 = Button(text="delete",bg="#CC6666",fg="black",font=fnt,width="10",command=changepage2)
    b1.place(x=5,y=25)
    b2 = Button(text="Add",bg="#CC6666",fg="black",font=fnt,width="10",command=changepage3)
    b2.place(x=5,y=80)
    b3 = Button(text="Update", bg="#CC6666", fg="black", font=fnt, width="10",command=changepage4)
    b3.place(x=5,y=135)
    b4 = Button(text="Search", bg="#CC6666", fg="black", font=fnt, width="10",command=changepage5)
    b4.place(x=5,y=190)
    canvas1=Canvas(root,width=360,height="100")
    canvas1.place(x=150,y=25)
    canvas2= Canvas(root, width=360, height="80")
    canvas2.place(x=150, y=150)
    b4 = Button(text="Logout", bg="#CC6666", fg="black", font=fnnt, width="20",height="2",command=changepage1)
    b4.place(x=150,y=300)

def page3():
    page=Frame(root)
    root.title("Delete")
    fnt = "none 18 bold"
    fnnt="none 13 bold"
    title=Label(text="Client id",font=fnt,bg="#333333",fg="#CC6666")
    title.place(x=200,y=120)
    Client_id=IntVar()
    delete_entry=Entry(textvariable=Client_id,width=12,font=fnt)
    delete_entry.place(x=50,y=210)
    confirm_button=Button(text="confirm",width="15",height="1",bg="#CC6666",fg="black",font=fnnt)
    confirm_button.place(x=270,y=210)
    Back_Button=Button(text="Back",bg="#CC6666",fg="black",width="15",height="2",font="none 10 bold",command=changepage2)
    Back_Button.place(x=30,y=320)
    delete_all=Button(text="Delete all",bg="#CC6666",fg="black",width="15",height="2",font="none 10 bold")
    delete_all.place(x=330,y=320)
    def cudeletedata():
      if messagebox.askyesno("delete", "DO you want delete all data ?")==YES:
            cr.execute("delete from Client")
            cr.execute('delete from payment')
            db.commit()
      else:
          messagebox.showinfo('Admin','please return to your program')

    def Budeletedatafrom():
        cr.execute('delete from Client where id=?',(Client_id.get(),))
        cr.execute('delete from payment where id=?',(Client_id.get(),))
        messagebox.showinfo('Done', 'client removed')
        db.commit()
        delete_entry.delete(0,END)
    delete_all.config(command=cudeletedata)
    confirm_button.config(command=Budeletedatafrom)




def page4():
    page=Frame(root)
    fnt="none 12 bold"
    root.title('Add client')
    client_id=Label(text="Client ID",bg="#333333",fg="#CC6666",font=fnt)
    client_id.place(x=10,y=30)
    client_ID = StringVar()
    clientID_entry=Entry(textvariable=client_ID,width=15)
    clientID_entry.place(x=100,y=30)
    start_text=Label(text="Start ",bg="#333333",fg="#CC6666",font=fnt)
    start_text.place(x=10,y=90)
    start = StringVar()

    start_entry=Entry(textvariable=start,width=15)
    start_entry.place(x=100,y=90)


    Fullname_text=Label(text="Fullname",bg="#333333",fg="#CC6666",font=fnt)
    Fullname_text.place(x=10,y=150)
    name = StringVar()
    Fullname_entry=Entry(textvariable=name,width=15)
    Fullname_entry.place(x=100,y=150)

    gender=Label(text="Gender",bg="#333333",fg="#CC6666",font=fnt)
    gender.place(x=10,y=210)
    i=IntVar()
    gender1 = Radiobutton(root, text="Male", bg="#333333",fg="#CC6666",font="none 10 bold", value=1, variable=i).place(x=100, y=210)
    gender2 = Radiobutton(root, text="Female", bg="#333333",fg="#CC6666",font="none 10 bold", value=2, variable=i).place(x=185, y=210)
    variable = StringVar(root)
    j=IntVar()
    payment=Label(text="Payment",bg="#333333",fg="#CC6666",font=fnt)
    payment.place(x=10,y=250)
    payment1 = Radiobutton(root, text="Done", bg="#333333", fg="#CC6666", font="none 10 bold", value=1,variable=j).place(x=100, y=250)
    payment2 = Radiobutton(root, text="Not", bg="#333333", fg="#CC6666", font="none 10 bold", value=2,variable=j).place(x=185, y=250)
    variable = StringVar(root)


    age=Label(text="Age",bg="#333333",fg="#CC6666",font=fnt)
    age.place(x=300,y=30)
    Age = IntVar()
    age_entry=Entry(textvariable=Age,width=15)
    age_entry.place(x=370,y=30)

    Renewaldate_text=Label(text="RenewalDate",bg="#333333",fg="#CC6666",font=fnt)
    Renewaldate_text.place(x=250,y=90)
    RenewalDate = StringVar()
    Renewaldate_entry=Entry(textvariable=RenewalDate,width=15)
    Renewaldate_entry.place(x=390,y=90)
    Add=Button(text='Add',bg="#CC6666",fg="black",width="20",height="2",font="none 10 bold")
    Add.place(x=300,y=320)
    Back= Button(text='Back', bg="#CC6666", fg="black", width="20", height="2", font="none 10 bold",command=changepage3)
    Back.place(x=30, y=320)

    def BuSaveData():

        if i.get() == 1:
            cr.execute(
                f"insert into Client(id,age,name,RenewalDate,startDate,gender) values({client_ID.get()},'{Age.get()}','{name.get()}','{RenewalDate.get()}','{start.get()}','Male')")
            db.commit()
        elif i.get() == 2:
            cr.execute(
                f"insert into Client(id,age,name,RenewalDate,Birthdate,gender) values({client_ID.get()},'{Age.get()}','{name.get()}','{RenewalDate.get()}','{start.get()}','Female')")
            db.commit()
        if j.get() == 1:
            cr.execute(
                f"insert into payment(id,payment) values({client_ID.get()},'Done')")
            db.commit()

        elif j.get() == 2:
            cr.execute(
                f"insert into payment(id,payment) values({client_ID.get()},'Not Done')")
            db.commit()
        messagebox.showinfo('Done','Done')
        clientID_entry.delete(0,END)
        start_entry.delete(0,END)
        Fullname_entry.delete(0,END)
        age_entry.delete(0,END)
        Renewaldate_entry.delete(0,END)




    Add.config(command=BuSaveData)

def page5():
    page=Frame(root)
    fnt="none 14 bold"
    canvas=Canvas(root,width=480,height=200)
    canvas.place(x=7,y=30)

    Client_id=Label(text="Client id",bg="#333333",fg="#CC6666",font=fnt)
    Clientid=StringVar()
    Client_id.place(x=30,y=300)
    Client_entry=Entry(textvariable=Clientid,width=25)
    Client_entry.place(x=160,y=300)
    Update_text = Label(text="Update", bg="#333333", fg="#CC6666", font=fnt)
    Update= StringVar()
    Update_text.place(x=30, y=360)
    Update_entry = Entry(textvariable=Update, width=25)
    Update_entry.place(x=160, y=360)
    confirm=Button(text="confirm",bg="#CC6666", fg="black", width="10",font="none 10 bold")
    confirm.place(x=390,y=358)
    show=Button(text="Show",bg="#CC6666", fg="black", width="10",font="none 10 bold")
    show.place(x=390,y=296)
    Back=Button(text="Back",bg="#CC6666", fg="black", width="10",height="2",font="none 10 bold",command=changepage4)
    Back.place(x=200,y=430)
    def TheUpdate():
        if Update.get()=='':
            messagebox.showinfo("error","please fill update entry")
        elif Update.get()!='':
             cr.execute('update Client set Renewaldate=? where id=?',(Update.get(),Clientid.get()))
             db.commit()
             messagebox.showinfo("Done","Update is done")
             canvas.delete('all')
             Client_entry.delete(0, END)
             Update_entry.delete(0,END)

    def showdata():
        if Clientid.get()=='':
            messagebox.showinfo("error","please enter client id")
        elif Clientid.get()!='':
            cr.execute("select name,Renewaldate from Client where id=?",(Clientid.get(),))
            canvas.create_text(110,10,text=cr.fetchone(),font="none 14 bold")

    show.config(command=showdata)
    confirm.config(command=TheUpdate)





def page6():
    page=Frame(root)
    canvas = Canvas(root, width=480, height=200)
    canvas.place(x=7, y=30)
    Search=StringVar()
    search_entry=Entry(textvariable=Search,width=25)
    search_entry.place(x=50,y=320)

    word=Button(text="Search",bg="#CC6666", fg="black", width="10",height="1",font="none 10 bold")
    word.place(x=280,y=315)
    Back =Button(text="Back",bg="#CC6666", fg="black", width="10",height="2",font="none 10 bold",command=changepage5)
    Back.place(x=70,y=400)

    def delete_canvas():
        canvas.delete('all')
    clear=Button(text="Clear canvas",bg="#CC6666", fg="black", width="10",height="2",font="none 10 bold",command=delete_canvas)
    clear.place(x=350,y=400)


    def search():
        cr.execute("select name,Renewaldate from Client where id=?",(Search.get(),))
        canvas.create_text(220,10,text=cr.fetchone(),font="none 14 bold")
        db.commit()
        if Search.get()!='':
            search_entry.delete(0,END)

    word.config(command=search)





def changepage1():
    global pagenum,root
    for widget in root.winfo_children():
        widget.destroy()
    if pagenum==1:
        page2()
        pagenum=2
    elif pagenum == 2:
        page1()
        pagenum=1
def changepage2():
    global pagenum, root
    for widget in root.winfo_children():
        widget.destroy()
    if pagenum==2:
        page3()
        pagenum=3
    elif pagenum==3:
        page2()
        pagenum=2
def changepage3():
    global pagenum, root
    for widget in root.winfo_children():
        widget.destroy()
    if pagenum == 2:
        page4()
        pagenum = 4
    elif pagenum==4:
        page2()
        pagenum=2
def changepage4():
    global pagenum, root
    for widget in root.winfo_children():
        widget.destroy()
    if pagenum == 2:
        page5()
        pagenum = 5
    elif pagenum == 5:
        page2()
        pagenum = 2
def changepage5():
    global pagenum, root
    for widget in root.winfo_children():
        widget.destroy()
    if pagenum == 2:
        page6()
        pagenum = 6
    elif pagenum == 6:
        page2()
        pagenum = 2

page1()
root.mainloop()