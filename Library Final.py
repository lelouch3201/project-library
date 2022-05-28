from tkinter import *
import pymysql as p
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter.ttk import Treeview
import datetime

b1,b2,b3,b4,b5,b6,b7,b8,sID,cur,con,e1,e2,e3,e4,e5,i,ps=None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
window,win=None,None
com1d,com1m,com1y,com2d,com2m,com2y=None,None,None,None,None,None


month=['January','February','March','April','May','June','July','August','September','October','November','December']
y = list(range(2020, 2040))
d = list(range(1,32))

def loginlibr():
    global window,sID
    connectdb()
    for i in range(cur.rowcount):
        data=cur.fetchone()
        if e1.get().strip()==str(data[1]) and e2.get().strip()==(data[2]):
            sID=e1.get()
            print(sID)
            closedb()
            libr()
            break
    else:
        window.withdraw()
        closedb()
        home()

def libr():
    global window
    window.withdraw()
    global win,b1,b2,b3,b4
    win=Tk()
    win.title('Library')
    win.geometry("400x400+480+180")
    win.resizable(False,False)
    b1=Button(win, height=2,width=25,text=' Issue Book ',command=issuebook)
    b2=Button(win, height=2,width=25,text=' Return Book ',command=returnbook)
    b3=Button(win, height=2,width=25,text=' View Book ',command=viewbook)
    b4=Button(win, height=2,width=25,text=' Issued Book ',command=issuedbook)
    b5=Button(win, height=2,width=25,text=' LogOut ',command=logout)
    b1.place(x=110,y=40)
    b2.place(x=110,y=90)
    b3.place(x=110,y=140)
    b4.place(x=110,y=190)
    b5.place(x=110,y=240)
    
    win.mainloop()

def addbook():
    global win
    win.destroy()
    win=Tk()
    win.title('Add Book')
    win.geometry("400x400+480+180")
    win.resizable(False,False)
    sub=Label(win,text='TITLE')
    tit=Label(win,text='AUTHOR')
    auth=Label(win,text='GENRE')
    ser=Label(win,text='BOOK ID')
    global e1,b,b1
    e1=Entry(win,width=25)
    global e2
    e2=Entry(win,width=25)
    global e3
    e3=Entry(win,width=25)
    global e4
    e4=Entry(win,width=25)
    b=Button(win, height=2,width=21,text=' ADD BOOK TO DB ',command=addbooks)
    b1=Button(win, height=2,width=21,text=' CLOSE ',command=closebooks)
    sub.place(x=70,y=50)
    tit.place(x=70,y=90)
    auth.place(x=70,y=130)
    ser.place(x=70,y=170)
    e1.place(x=180,y=50)
    e2.place(x=180,y=90)
    e3.place(x=180,y=130)
    e4.place(x=180,y=170)
    b.place(x=180,y=210)
    b1.place(x=180,y=252)
    win.mainloop()

def addbooks():
    connectdb()
    q='INSERT INTO Book VALUE("%s","%s","%s","%i")'
    global cur,con
    cur.execute(q%(e1.get(),e2.get(),e3.get(),int(e4.get())))
    con.commit()
    win.destroy()
    messagebox.showinfo("Book", "Book Added")
    closedb()
    libr()

def closebooks():
    global win
    win.destroy()
    libr()

def issuebook():
    global win,sID
    win.destroy()
    win=Tk()
    win.title('Issue Book')
    win.geometry("400x400+480+180")
    win.resizable(False,False)
    name=Label(win,text='ISSUE ',font='Helvetica 30 bold')
    

    sid=Label(win,text='Student ID')
    no=Label(win,text='BOOK NO')
    issue=Label(win,text='ISSUE DATE')
    exp=Label(win,text='EXPIRY DATE')
    global e1,b,b1
    e1=Entry(win,width=25)
    e1.insert(0, sID)
    e1.configure(state = 'disabled')
    global e4
    e4=Entry(win,width=25)
    global com1y,com1m,com1d,com2y,com2m,com2d
    com1y=Combobox(win,value=y,width=5)
    com1m=Combobox(win,value=month,width=5)
    com1d=Combobox(win,value=d,width=5)
    com2y=Combobox(win,value=y,width=5)
    com2m=Combobox(win,value=month,width=5)
    com2d=Combobox(win,value=d,width=5)
    now=datetime.datetime.now()
    com1y.set(now.year)
    com1m.set(month[now.month-1])
    com1d.set(now.day)
    
    com2y.set(now.year)
    com2m.set(month[now.month-1])
    com2d.set(now.day)
    
    b=Button(win, height=2,width=21,text=' ISSUE BOOK ',command=issuebooks)
    b1=Button(win, height=2,width=21,text=' CLOSE ',command=closebooks)
    name.place(x=55,y=30)
    sid.place(x=70,y=130)
    no.place(x=70,y=170)
    issue.place(x=70,y=210)
    exp.place(x=70,y=240)
    e1.place(x=180,y=130)
    e4.place(x=180,y=170)
    com1y.place(x=180,y=210)
    com1m.place(x=230,y=210)
    com1d.place(x=280,y=210)
    com2y.place(x=180,y=240)
    com2m.place(x=230,y=240)
    com2d.place(x=280,y=240)
    b.place(x=178,y=270)
    b1.place(x=178,y=312)
    win.mainloop()

def issuebooks():
    connectdb()
    q='INSERT INTO BookIssue VALUE("%s","%s","%s","%s")'
    i=datetime.datetime(int(com1y.get()),month.index(com1m.get())+1,int(com1d.get()))
    e=datetime.datetime(int(com2y.get()),month.index(com2m.get())+1,int(com2d.get()))
    i=i.isoformat()
    e=e.isoformat()
    cur.execute(q%(e1.get(),e4.get(),i,e))
    con.commit()
    win.destroy()
    messagebox.showinfo("Book", "Book Issued")
    closedb()
    libr()
def returnbook():
    global win
    #win.destroy()
    win=Tk()
    win.title('Return Book')
    win.geometry("400x400+480+180")
    win.resizable(False,False)
    ret=Label(win,text='RETURN ',font='Helvetica 30 bold')
    book=Label(win,text='BOOK',font='Helvetica 30 bold')
    no=Label(win,text='BOOK NO')
    date=Label(win,text='RETURN DATE')
    exp=Label(win,text='')
    global b,b1
    global e4
    e4=Entry(win,width=25)
    global com1y,com1m,com1d,com2y,com2m,com2d
    com1y=Combobox(win,value=y,width=5)
    com1m=Combobox(win,value=month,width=5)
    com1d=Combobox(win,value=d,width=5)
    '''com2y=Combobox(win,width=5)
    com2m=Combobox(win,width=5)
    com2d=Combobox(win,width=5)'''
    now=datetime.datetime.now()
    com1y.set(now.year)
    com1m.set(month[now.month-1])
    com1d.set(now.day)

    b=Button(win, height=2,width=21,text=' RETURN BOOK ',command=returnbooks)
    b1=Button(win, height=2,width=21,text=' CLOSE ',command=closebooks)
    ret.place(x=55,y=30)
    book.place(x=225,y=30)
    no.place(x=70,y=120)
    date.place(x=70,y=160)
    exp.place(x=70,y=200)
    e4.place(x=180,y=120)
    com1y.place(x=180,y=160)
    com1m.place(x=230,y=160)
    com1d.place(x=280,y=160)
    '''com2y.place(x=180,y=200)
    com2m.place(x=230,y=200)
    com2d.place(x=280,y=200)'''
    b.place(x=178,y=200)
    b1.place(x=178,y=242)
    win.mainloop()

def returnbooks():
    connectdb()
    q='SELECT exp FROM BookIssue WHERE bookids="%s"'
    cur.execute(q%(e4.get()))
    e=cur.fetchone()
    e=str(e[0])
    i=datetime.date.today()
    e=datetime.date(int(e[:4]),int(e[5:7]),int(e[8:10]))
    if i<=e:
        a='DELETE FROM BookIssue WHERE bookids="%s"'
        cur.execute(a%e4.get())
        con.commit()
    else:
        t=str((i-e)*10)
        messagebox.showinfo("Fine",t[:4]+' Fine ')
    win.destroy()
    closedb()
    libr()

def viewbook():
    win=Tk()
    win.title('View Books')
    win.geometry("800x300+270+180")
    win.resizable(False,False)

    treeview=Treeview(win,columns=("Title","Author","Genre","Book ID"),show='headings')
    treeview.heading("Title", text="Title")
    treeview.heading("Author", text="Author")
    treeview.heading("Genre", text="Genre")
    treeview.heading("Book ID", text="Book ID")
    treeview.column("Title", anchor='center')
    treeview.column("Author", anchor='center')
    treeview.column("Genre", anchor='center')
    treeview.column("Book ID", anchor='center')
    index=0
    iid=0
    connectdb()
    q='SELECT * FROM Book'
    cur.execute(q)
    details=cur.fetchall()
    for row in details:
        treeview.insert("",index,iid,value=row)
        index=iid=index+1
    treeview.pack()
    win.mainloop()
    closedb()

def issuedbook():
    connectdb()
    q='SELECT * FROM BookIssue where stdid = %s'
    val = (sID,)
    cur.execute(q,val)
    details=cur.fetchall()
    if len(details)!=0:
        win=Tk()
        win.title('View Books')
        win.geometry("800x300+270+180")
        win.resizable(False,False)    
        treeview=Treeview(win,columns=("Student ID","Book ID","Issue Date","Expiry Date"),show='headings')
        treeview.heading("Student ID", text="Student ID")
        treeview.heading("Book ID", text="Book ID")
        treeview.heading("Issue Date", text="Issue Date")
        treeview.heading("Expiry Date", text="Expiry Date")
        treeview.column("Student ID", anchor='center')
        treeview.column("Book ID", anchor='center')
        treeview.column("Issue Date", anchor='center')
        treeview.column("Expiry Date", anchor='center')
        index=0
        iid=0
        for row in details:
            treeview.insert("",index,iid,value=row)
            index=iid=index+1
        treeview.pack()
        win.mainloop()
    else:
        messagebox.showinfo("Books","No Book Issued")
    closedb()

def loginadmin():
    if e1.get()=='admin' and e2.get()=='admin':
        admin()

def admin():
    window.withdraw()
    global win,b1,b2,b3,b4,cur,con
    win=Tk()
    win.title('Admin')
    win.geometry("400x500+480+180")
    win.resizable(False,False)
    b1=Button(win, height=2,width=25,text=' Add User ',command=adduser)
    b2=Button(win, height=2,width=25,text=' Add Book ',command=addbook)
    b3=Button(win, height=2,width=25,text=' View User ',command=viewuser)
    b4=Button(win, height=2,width=25,text=' View Book ',command=viewbook)
    b5=Button(win, height=2,width=25,text=' Issued Book ',command=issuedbook)
    b6=Button(win, height=2,width=25,text=' Delete Book ',command=deletebook)
    b7=Button(win, height=2,width=25,text=' Delete User ',command=deleteuser)
    b8=Button(win, height=2,width=25,text=' LogOut ',command=logout)
    b1.place(x=110,y=60)
    b2.place(x=110,y=110)
    b3.place(x=110,y=160)
    b4.place(x=110,y=210)
    b5.place(x=110,y=260)
    b6.place(x=110,y=310)
    b7.place(x=110,y=360)
    b8.place(x=110,y=410)
    
    
    
    win.mainloop()

def logout():    
    win.destroy()
    try:
        closedb()
    except:
        print("Logged Out")
    home()

def closedb():
    global con,cur
    cur.close()
    con.close()

def addbook():
    global win
    win.destroy()
    win=Tk()
    win.title('Add Book')
    win.geometry("400x400+480+180")
    win.resizable(False,False)
    sub=Label(win,text='TITLE')
    tit=Label(win,text='AUTHOR')
    auth=Label(win,text='GENRE')
    ser=Label(win,text='BOOK ID')
    global e1,b,b1,b5,b4
    e1=Entry(win,width=25)
    global e2
    e2=Entry(win,width=25)
    global e3
    e3=Entry(win,width=25)
    global e4
    e4=Entry(win,width=25)
    b=Button(win, height=2,width=21,text=' ADD BOOK TO DB ',command=addbooks)
    b1=Button(win, height=2,width=21,text=' CLOSE ',command=admin)
    sub.place(x=70,y=50)
    tit.place(x=70,y=90)
    auth.place(x=70,y=130)
    ser.place(x=70,y=170)
    e1.place(x=180,y=50)
    e2.place(x=180,y=90)
    e3.place(x=180,y=130)
    e4.place(x=180,y=170)
    b.place(x=180,y=210)
    b1.place(x=180,y=252)
    win.mainloop()

def closebooks1():
    global win
    win.destroy()
    admin()

def addbooks():
    connectdb()
    q='INSERT INTO Book VALUE("%s","%s","%s","%i")'
    global cur,con
    cur.execute(q%(e1.get(),e2.get(),e3.get(),int(e4.get())))
    con.commit()
    win.destroy()
    messagebox.showinfo("Book", "Book Added")
    closedb()
    admin()


def viewbook():
    win=Tk()
    win.title('View Books')
    win.geometry("800x300+270+180")
    win.resizable(False,False)

    treeview=Treeview(win,columns=("Title","Author","Genre","Book ID"),show='headings')
    treeview.heading("Title", text="Title")
    treeview.heading("Author", text="Author")
    treeview.heading("Genre", text="Genre")
    treeview.heading("Book ID", text="Book ID")
    treeview.column("Title", anchor='center')
    treeview.column("Author", anchor='center')
    treeview.column("Genre", anchor='center')
    treeview.column("Book ID", anchor='center')
    index=0
    iid=0
    connectdb()
    q='SELECT * FROM Book'
    cur.execute(q)
    details=cur.fetchall()
    for row in details:
        treeview.insert("",index,iid,value=row)
        index=iid=index+1
    treeview.pack()
    win.mainloop()
    closedb()

def deletebook():
    global win
    win.destroy()
    win=Tk()
    win.title('Delete Book')
    win.geometry("400x400+480+180")
    win.resizable(False,False)
    usid=Label(win,text='BOOK ID')
    paswrd=Label(win,text='PASSWORD')
    global e1
    e1=Entry(win)
    global e2,b2
    e2=Entry(win)
    b1=Button(win, height=2,width=17,text=' DELETE ',command=deletebooks)
    b2=Button(win, height=2,width=17,text=' CLOSE ',command=closebooks1)
    usid.place(x=80,y=100)
    paswrd.place(x=70,y=140)
    e1.place(x=180,y=100)
    e2.place(x=180,y=142)
    b1.place(x=180,y=180)
    b2.place(x=180,y=230)
    win.mainloop()

def deletebooks():
    connectdb()
    if e2.get()=='admin':
        q='DELETE FROM Book WHERE bookid="%i"'
        cur.execute(q%(int(e1.get())))
        con.commit()
        win.destroy()
        messagebox.showinfo("Delete", "Book Deleted")
        closedb()
        admin()
    else:
        messagebox.showinfo("Error", "Incorrect Password")
        closedb()

def adduser():
    global win
    win.destroy()
    win=Tk()
    win.title('Add User')
    win.geometry("400x440+480+180")
    win.resizable(False,False)
    name=Label(win,text='NAME')
    Ssid=Label(win,text='STUDENT ID')
    spass=Label(win,text='PASSWORD')
    level=Label(win,text='YEAR LEVEL')
    course=Label(win,text='COURSE')
   
    global e1,b
    e1=Entry(win,width=25)
    global e2
    e2=Entry(win,width=25)
    global e3
    e3=Entry(win,width=25)
    global e4
    e4=Entry(win,width=25)
    global e5
    e5=Entry(win,width=25)
    b=Button(win, height=2,width=21,text=' ADD USER ',command=addusers)
    b1=Button(win, height=2,width=21,text=' CLOSE ',command=closeusers)
    name.place(x=70,y=100)
    Ssid.place(x=70,y=140)
    spass.place(x=70,y=180)
    level.place(x=70,y=220)
    course.place(x=70,y=260)
    e1.place(x=180,y=100)
    e2.place(x=180,y=140)
    e3.place(x=180,y=180)
    e4.place(x=180,y=220)
    e5.place(x=180,y=260)
    b.place(x=178,y=293)
    b1.place(x=178,y=340)
    win.mainloop()

def addusers():
    connectdb()
    q='INSERT INTO Login VALUE("%s","%i","%s","%s","%s")'
    global con,cur
    cur.execute(q%(e1.get(),int(e2.get()),e3.get(),e4.get(),e5.get()))
    con.commit()
    win.destroy()
    messagebox.showinfo("User", "User Added")
    closedb()
    admin()

def closeusers():
    global win
    win.destroy()
    admin()

def viewuser():
    win=Tk()
    win.title('View User')
    win.geometry("1000x300+270+180")
    win.resizable(False,False)
    treeview=Treeview(win,columns=("Name","User ID","Password","YearLevel","Course"),show='headings')
    treeview.heading("Name", text="Name")
    treeview.heading("User ID", text="User ID")
    treeview.heading("Password", text="Password")
    treeview.heading("YearLevel", text="YearLevel")
    treeview.heading("Course", text="Course")
    treeview.column("Name", anchor='center')
    treeview.column("User ID", anchor='center')
    treeview.column("Password", anchor='center')
    treeview.column("YearLevel", anchor='center')
    treeview.column("Course", anchor='center')
    index=0
    iid=0
    connectdb()
    details=cur.fetchall()
    for row in details:
        treeview.insert("",index,iid,value=row)
        index=iid=index+1
    treeview.pack()
    win.mainloop()
    closedb()

def issuedbook():
    connectdb()
    q='SELECT * FROM BookIssue '
    cur.execute(q)
    details=cur.fetchall()
    if len(details)!=0:
        win=Tk()
        win.title('View Books')
        win.geometry("800x300+270+180")
        win.resizable(False,False)    
        treeview=Treeview(win,columns=("Student ID","Book ID","Issue Date","Expiry Date"),show='headings')
        treeview.heading("Student ID", text="Student ID")
        treeview.heading("Book ID", text="Book ID")
        treeview.heading("Issue Date", text="Issue Date")
        treeview.heading("Expiry Date", text="Expiry Date")
        treeview.column("Student ID", anchor='center')
        treeview.column("Book ID", anchor='center')
        treeview.column("Issue Date", anchor='center')
        treeview.column("Expiry Date", anchor='center')
        index=0
        iid=0
        for row in details:
            treeview.insert("",index,iid,value=row)
            index=iid=index+1
        treeview.pack()
        win.mainloop()
    else:
        messagebox.showinfo("Books","No Book Issued")
    closedb()

def deleteuser():
    global win
    win.destroy()
    win=Tk()
    win.title('Delete user')
    win.geometry("400x400+480+180")
    win.resizable(False,False)
    usid=Label(win,text='USER ID')
    paswrd=Label(win,text='ADMIN \n PASSWORD')
    global e1
    e1=Entry(win)
    global e2,b2
    e2=Entry(win)
    b1=Button(win, height=2,width=17,text=' DELETE ',command=deleteusers)
    b2=Button(win, height=2,width=17,text=' CLOSE ',command=closeusers)
    usid.place(x=80,y=100)
    paswrd.place(x=70,y=140)
    e1.place(x=180,y=100)
    e2.place(x=180,y=142)
    b1.place(x=180,y=180)
    b2.place(x=180,y=230)
    win.mainloop()

def deleteusers():
    connectdb()
    if e2.get()=='admin':
        q='DELETE FROM Login WHERE userid="%i"'
        cur.execute(q%(int(e1.get())))
        con.commit()
        win.destroy()
        messagebox.showinfo("Delete", "User Deleted")
        closedb()
        admin()
    else:
        messagebox.showinfo("Error", "Incorrect Password")
        closedb()

def connectdb():
    global con,cur
    #Enter your username and password of MySQL
    con=p.connect(host="localhost",user="root",passwd="")
    cur=con.cursor()
    cur.execute('CREATE DATABASE IF NOT EXISTS LIBRARY')
    cur.execute('USE LIBRARY')
    global enter
    if enter==1:
        l='CREATE TABLE IF NOT EXISTS Login(name varchar(50),userid varchar(10),password varchar(30),yearlevel varchar(20),course varchar(20))'
        b='CREATE TABLE IF NOT EXISTS Book(title varchar(50),author varchar(50),genre varchar(50),bookid int(15))'
        i='CREATE TABLE IF NOT EXISTS BookIssue(stdid varchar(50),bookids varchar(50),issue date,exp date)'
        cur.execute(l)
        cur.execute(b)
        cur.execute(i)
        enter=enter+1
    query='SELECT * FROM Login'
    cur.execute(query)

def home():
    try:
        global window,b1,b2,e1,e2,con,cur,win
        window=Tk()
        window.title('Welcome')
        window.resizable(False,False)
        window.geometry("400x400+480+180")
        #wel=Label(window,text='LIBRARY',font='Helvetica 28 bold')
        #lib=Label(window,text='MANAGEMENT',font='Helvetica 28 bold')
        usid=Label(window,text='USER ID')
        paswrd=Label(window,text='PASSWORD')
        e1=Entry(window,width=22)
        e2=Entry(window,width=22)
        b1=Button(window,text=' LOGIN AS STUDENT' ,height=2,width=20,command=loginlibr)
        b2=Button(window,text=' LOGIN AS ADMIN ', height=2,width=20,command=loginadmin)
        #wel.place(x=160,y=20)
        #lib.place(x=110,y=70)
        usid.place(x=70,y=100)
        paswrd.place(x=70,y=140)
        e1.place(x=180,y=100)
        e2.place(x=180,y=140)
        b1.place(x=175,y=180)
        b2.place(x=175,y=225)
        window.mainloop()
    except Exception:
        window.destroy()
enter=1
home()
