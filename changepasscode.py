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
win.title("STORE|-|UB\ChangePasscode")
win.geometry("800x500")
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

#================Function for browsefunc=============

    
def  browsefunc():
    filename=filedialog.askopenfilename(filetypes=(("File","*.py"),("All File","*.*")))
    pathLabe1.config(text=filename)


def changepasscode():
      em=email.get()
      old=oldpassword.get()
      new=newpassword.get()
      confirm=confirmpassword.get()
      try:
           if(new==confirm):
              conn=pymysql.connect(host='localhost',user='root',password='',db='reg')
              a=conn.cursor()
              a.execute("update registration set password=' "+new+" ' where email=' "+em+" ' and  password=' "+old+" ' ")
              conn.commit()
              messagebox.showinfo("Saved","Your passcode change")
              win.destroy()
              import biling
           else:
                messagebox.showinfo("Error","Passcode doesn't match")
      except:
              conn.rollback()
              messagebox.showinfo("Error","Passcode not change")
              conn.close()

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
helpMenu.add_cascade(label="Change Passcode",command=fun1)
helpMenu.add_cascade(label="Forget Passcode",command=forgetpasscode)
helpMenu.add_cascade(label="IDLE Help",command=fun1)
helpMenu.add_cascade(label="Python Docs",command=fun1)
helpMenu.add_cascade(label="Turtle Demo",command=fun1)

mframe=Frame(win,width=1000,height=800,bg="orange",bd=10,relief="raise")
mframe.pack(padx=50,pady=70)

lb=Label(mframe,text="Change Passcode",font=('Comic Sans MS',15,'bold'),width=30,bd=2,fg="black",relief="raise")
lb.grid(row=0,column=0,columnspan=2,padx=10,pady=10)

lb2=Label(mframe,text="Email-Id",width=15,font=('Comic Sans MS',9,'bold'))
lb2.grid(row=1,column=0,padx=10,pady=10)

lb2=Label(mframe,text="Old Passcode",width=15,font=('Comic Sans MS',9,'bold'))
lb2.grid(row=2,column=0,padx=10,pady=10)

lb2=Label(mframe,text="New Passcode",width=15,font=('Comic Sans MS',9,'bold'))
lb2.grid(row=3,column=0,padx=10,pady=10)

lb2=Label(mframe,text="Confirm Passcode",width=15,font=('Comic Sans MS',9,'bold'))
lb2.grid(row=4,column=0,padx=10,pady=10)


email=StringVar()
tb1=Entry(mframe,textvariable=email)
tb1.grid(row=1,column=1)

oldpassword=StringVar()
tb2=Entry(mframe,textvariable=oldpassword,show="*")
tb2.grid(row=2,column=1)

newpassword=StringVar()
tb3=Entry(mframe,textvariable=newpassword,show="*")
tb3.grid(row=3,column=1)

confirmpassword=StringVar()
tb4=Entry(mframe,textvariable=confirmpassword,show="*")
tb4.grid(row=4,column=1)

btn=Button(mframe,text="Change Passcode",command=changepasscode,font=('Comic Sans MS',10,'bold'),bd=5,width=15,fg='black',cursor="hand2",relief='raise')
btn.grid(row=5,column=0,columnspan=2,padx=10,pady=20)


