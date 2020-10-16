from tkinter import*
from tkinter import messagebox
from tkinter import filedialog
from pymysql import*
import os
import pymysql.cursors
from PIL import ImageTk,Image

OPTIONS=[
   "-select security-",
   "What is your nick name?",
   "Name of your childhood friend?",
   "What time of the day were you born?(h:m)",
   "In what town was your first job?"]
#=========================Window_Size=====================================

win=Tk()
win.title("STORE|-|UB")
win.geometry("700x100")
win.maxsize(500,300)
win.minsize(500,300)
menu1=Menu(win)
win.config(menu=menu1,bg="black")
subMenu1=Menu(menu1)
win.maxsize(1350,300)
win.minsize(500,500)


def  fun1():
    print("It's Working")


 #=========================Exit=====================================


def  __quit():
      quit=messagebox.showinfo("Exit","Do You Want To Exit")
      root.destroy()

def  browsefunc():
    filename=filedialog.askopenfilename(filetypes=(("File","*.py"),("All File","*.*")))
    pathLabe1.config(text=filename)


def change():
          un=username.get()
          em=email.get()
          cont=phone.get()
          sec=security.get()
          ans=answer.get()
          try:
               conn=pymysql.connect(host='localhost',user='root',password='',db='reg')
               a=conn.cursor()
               a.execute("select password from registration where username=' "+un+" ' and email=' "+em+" ' and phone=' "+cont+" ' and security=' "+sec+" ' and answer=' "+ans+" ' ")
               results=a.fetchall()
               count=a.rowcount
               print(results)

               if(count>0):
                    messagebox.showinfo('your password is',results[0])
                    import biling
                    win.destroy()
               else:
                     messagebox.showinfo("message","passcode not found")

                     
          except:
                conn.rollback()

           
      
#=========================Menu Items=====================================

    
menu1.add_cascade(label="File",menu=subMenu1)
subMenu1.add_command(label="New File",command=browsefunc) 
subMenu1.add_command(label="Open",command=browsefunc)
subMenu1.add_command(label="Open Module",command=browsefunc)
subMenu1.add_command(label="Recent File",command=browsefunc) 
subMenu1.add_command(label="Module Brower",command=browsefunc)
subMenu1.add_command(label="Path Browser",command=browsefunc)
subMenu1.add_command(label="Save",command=browsefunc) 
subMenu1.add_command(label="Save As",command=browsefunc)
subMenu1.add_command(label="Save Copy As",command=browsefunc)
subMenu1.add_command(label="Print Window",command=browsefunc) 
subMenu1.add_command(label="Close",command=browsefunc)
subMenu1.add_command(label="Exit",command=__quit)

EditMenu=Menu(menu1)
menu1.add_cascade(label="Edit",menu=EditMenu)
EditMenu.add_cascade(label="Undo",command=fun1)
EditMenu.add_cascade(label="Redo",command=fun1)
EditMenu.add_cascade(label="Cut",command=fun1)
EditMenu.add_cascade(label="Copy",command=fun1)
EditMenu.add_cascade(label="Paste",command=fun1)
EditMenu.add_cascade(label="Select All",command=fun1)
EditMenu.add_cascade(label="Find",command=fun1)
EditMenu.add_cascade(label="Find Again",command=fun1)
EditMenu.add_cascade(label="Find Selection",command=fun1)
EditMenu.add_cascade(label="Find In File",command=fun1)
EditMenu.add_cascade(label="Replace",command=fun1)
EditMenu.add_cascade(label="Go To Line",command=fun1)

formatMenu=Menu(menu1)
menu1.add_cascade(label="Format",menu=formatMenu)
formatMenu.add_cascade(label="Undo",command=fun1)
formatMenu.add_cascade(label="Redo",command=fun1)
formatMenu.add_cascade(label="Cut",command=fun1)
formatMenu.add_cascade(label="Copy",command=fun1)
formatMenu.add_cascade(label="Paste",command=fun1)
formatMenu.add_cascade(label="Select All",command=fun1)
formatMenu.add_cascade(label="Find",command=fun1)
formatMenu.add_cascade(label="Find Again",command=fun1)
formatMenu.add_cascade(label="Find Selection",command=fun1)
formatMenu.add_cascade(label="Find In File",command=fun1)
formatMenu.add_cascade(label="Replace",command=fun1)
formatMenu.add_cascade(label="Go To Line",command=fun1)

RunMenu=Menu(menu1)
menu1.add_cascade(label="Run",menu=RunMenu)
RunMenu.add_cascade(label="Run Module",command=fun1)
RunMenu.add_cascade(label="Run..c\Customized",command=fun1)
RunMenu.add_cascade(label="Check Module",command=fun1)
RunMenu.add_cascade(label="Python Shell",command=fun1)

optionsMenu=Menu(menu1)
menu1.add_cascade(label="Options",menu=optionsMenu)
optionsMenu.add_cascade(label="Configure IDLE",command=fun1)
optionsMenu.add_cascade(label="Show Code Content",command=fun1)
optionsMenu.add_cascade(label="Show Line No",command=fun1)
optionsMenu.add_cascade(label="Zoom Height",command=fun1)


windowMenu=Menu(menu1)
menu1.add_cascade(label="Window",menu=windowMenu)

helpMenu=Menu(menu1)
menu1.add_cascade(label="Help",menu=helpMenu)
helpMenu.add_cascade(label="About IDLE",command=fun1)
helpMenu.add_cascade(label="IDLE Help",command=fun1)
helpMenu.add_cascade(label="Python Docs",command=fun1)
helpMenu.add_cascade(label="Turtle Demo",command=fun1)


mframe=Frame(win,width=1000,height=700,bg="orange",bd=10,relief="raise")
mframe.pack(padx=50,pady=60)


lb=Label(mframe,text="Forget Passcode",font=('Comic Sans MS',15,'bold'),bd=2,width=30,fg='black',relief='raise')
lb.grid(row=0,column=0,columnspan=2,padx=10,pady=10)

lb2=Label(mframe,text="Username",width=8,fg='black',font=('Comic Sans MS',10,'bold'))
lb2.grid(row=1,column=0,padx=10,pady=10)
lb2=Label(mframe,text="Email",width=8,fg='black',font=('Comic Sans MS',10,'bold'))
lb2.grid(row=2,column=0,padx=10,pady=10)
lb2=Label(mframe,text="Contact",width=8,fg='black',font=('Comic Sans MS',10,'bold'))
lb2.grid(row=3,column=0,padx=10,pady=10)
lb2=Label(mframe,text="Security Q",width=8,fg='black',font=('Comic Sans MS',10,'bold'))
lb2.grid(row=4,column=0,padx=10,pady=10)
lb2=Label(mframe,text="Answer",width=8,fg='black',font=('Comic Sans MS',10,'bold'))
lb2.grid(row=5,column=0,padx=10,pady=10)


username=StringVar()
tb1=Entry(mframe,textvariable=username,font=('Comic Sans MS',8,'bold'))
tb1.grid(row=1,column=1)

email=StringVar()
tb2=Entry(mframe,textvariable=email,font=('Comic Sans MS',8,'bold'))
tb2.grid(row=2,column=1)

phone=StringVar()
tb1=Entry(mframe,textvariable=phone,font=('Comic Sans MS',8,'bold'))
tb1.grid(row=3,column=1)

security=StringVar()
security.set(OPTIONS[0])
tb6=OptionMenu(win,security,*OPTIONS)
tb6.place(x=374,y=295)

answer=StringVar()
tb1=Entry(mframe,textvariable=answer,font=('Comic Sans MS',8,'bold'))
tb1.grid(row=5,column=1)

btn=Button(mframe,text="Your Passcode",font=('Comic Sans MS',10),bd=5,command=change,width=15,fg='black',relief='raise')
btn.grid(row=6,column=0,columnspan=2,padx=10,pady=10)
