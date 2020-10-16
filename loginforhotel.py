#dispaly image on label

 #=========================Tkinter_Import=====================================
 
from tkinter import*
from tkinter import messagebox
from tkinter import filedialog
from pymysql import*
import os
import pymysql.cursors
from PIL import ImageTk,Image

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
#=========================Icon Image=====================================

#ttitleimage=PhotoImage(file='logo.png')
#win.iconphoto(False,titleimage)

'''canvas=Canvas(win,width=800,height=800)
canvas.pack()
my_image=PhotoImage(file="LOGO-2.png")
canvas.create_image(60,60,anchor=NW,image=my_image)'''




  #=========================Function=====================================


def  fun1():
    print("It's Working")


 #=========================Exit=====================================


def  __quit():
      quit=messagebox.showinfo("Exit","Do You Want To Exit")
      root.destroy()

 #================Function for browsefunc=============
      
def sign():
    import registerforhotel
    win.destroy()

def forgetpasscode():
      import ForgetPasscode
      win.destroy()

def changepasscode():
      import changepasscode
      win.destroy()

#================Function for browsefunc=============

    
def  browsefunc():
    filename=filedialog.askopenfilename(filetypes=(("File","*.py"),("All File","*.*")))
    pathLabe1.config(text=filename)


 #=========================mysql connect=====================================
def login():
      em=email.get()
      pwd=password.get()
      if ('@gmail.com' not in em or em ==" "):
                messagebox.showerror('Login error',"Please write the valid Email")
      else:
             conn=pymysql.connect(host='localhost',user='root',password='',db='reg')
             a=conn.cursor()
             a.execute("select * from registration where email=' "+em+" ' and password=' "+pwd+" '")
             results=a.fetchall()
             count=a.rowcount
             print(results)
             print(count)
             if(count>0):
                  import biling
                  win.destroy()
             else:
                 messagebox.showinfo("Error","Record Not Found")
                       


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
menu1.add_cascade(label="Setting",menu=helpMenu)
helpMenu.add_cascade(label="Change Passcode",command=changepasscode)
helpMenu.add_cascade(label="Forget Passcode",command=forgetpasscode)
helpMenu.add_cascade(label="IDLE Help",command=fun1)
helpMenu.add_cascade(label="Python Docs",command=fun1)
helpMenu.add_cascade(label="Turtle Demo",command=fun1)


 #=========================Login frame=====================================
header=Label(win,text="Login",font=("Comic Sans MS",30),bd=2,width=12,fg="white",bg="orange",relief='raise')
header.place(x=168,y=5)

#=========================Input AreA=====================================
frame=Frame(win,width=380,height=300,bg="orange",bd=5,relief="ridge")
frame.place(x=160,y=130)



lb2=Label(win,padx=5,text="Email Address",font=("Comic Sans MS",10),bg="orange")
lb3=Label(win,padx=25,text="Passcode",font=("Comic Sans MS",10),bg="orange")
lb8=Button(win,padx=5,text="You have not a account? sign",font=("Comic Sans MS",10),command=sign,bd=0,cursor="hand2",bg="orange")

lb8.place(x=240,y=300)

lb2.place(x=180,y=200)

lb3.place(x=172,y=260)

email=StringVar()
tb2=Entry(win,textvariable=email)
tb2.place(x=340,y=200)

password=StringVar()
tb3=Entry(win,textvariable=password,show="*")
tb3.place(x=340,y=260)


btn=Button(win,text="Login ",fg="white",bg="red",cursor="hand2",width=8,font=("Comic Sans MS",10),command=login)
btn.place(x=310,y=380)
