#dispaly image on label

 #=========================Tkinter_Import=====================================
 
from tkinter import*
from tkinter import messagebox
from tkinter import filedialog
from pymysql import*
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
win.geometry("850x620+200+200")
menu1=Menu(win)
win.config(menu=menu1,bg="white")
subMenu1=Menu(menu1)

 #=========================Icon Image=====================================


'''titleimage=PhotoImage(file='logo.png')
win.iconphoto(False,titleimage)'''

  #=========================Function=====================================


def  fun1():
    print("It's Working")


 #=========================Exit=====================================


def  __quit():
      op=messagebox.askyesno("Exit","Do you want to Exit?")
      if op>0:
          win.destroy()

              

                                           #================Function for browsefunc=============

    
def  browsefunc():
    filename=filedialog.askopenfilename(filetypes=(("File","*.py"),("All File","*.*")))
    pathLabe1.config(text=filename)


                                               #================Function for clear=============

    
def __clear():
    username.set(" ")
    lastname.set(" ")
    email.set(" ")
    phone.set(" ")
    address.set(" ")
    password.set("")
    variable.set("")
    answer.set("")

                                                  #================Function for insert=============

def __register():
    un=username.get()
    ln=lastname.get()
    pas=password.get()
    em=email.get()
    cn=phone.get()
    add=address.get()
    sec=variable.get()
    ans=answer.get()
    if ('@gmail.com' not in em or em ==" " or pas==" " or sec==" "):
                messagebox.showerror('Register error',"Please write the valid Email")
    else:
        try:
            conn= pymysql.connect(host='localhost',user='root',password='',db='reg')
            a=conn.cursor()
            a.execute("insert into registration(username,lastname,password,email,phone,address,security,answer)values(' "+un+" ' ,' "+ln+" ', ' "+pas+" ',' "+em+" ',' "+cn+" ',' "+add+" ',' "+sec+" ',' "+ans+" ')")
            conn.commit()
            messagebox.showinfo("message",f"Welcome:{username.get()}")
            win.destroy()
            import biling
        except:
           conn.rollback()
           messagebox.showinfo("Error","Error")
        conn.close()


  #================POPUP New Window of Login=============
def login():
    import loginforhotel
    win.destroy()

def changepasscode():
      import changepasscode
      win.destroy()


def forgetpasscode():
      import ForgetPasscode
      win.destroy()

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
helpMenu.add_cascade(label="Python Docs",command=fun1)
helpMenu.add_cascade(label="Turtle Demo",command=fun1)

  #=========================Main Title=====================================

title=Label(win,text="Registration",font=("Comic Sans MS",30),bd=0,width=11,fg='black',bg="white",relief='raise')
title.place(x=440,y=0)

  #=========================Left Image=====================================

logo=PhotoImage(file="logo-2.png")
w1=Label(win,image=logo,width=400,height=600,bg="black")
w1.pack(side="left")

#=========================Frame and User Field==============================


frame=Frame(win,width=450,height=510,bg="pink",bd=5,relief="ridge")
frame.place(x=380,y=80)

lb1=Label(win,padx=5,text="click on Clear btn*",font=("Comic Sans MS",10),bg="pink")
lb2=Label(win,padx=5,text="FirstName",font=("Comic Sans MS",10),bg="pink")
lb3=Label(win,padx=5,text="LastName",font=("Comic Sans MS",10),bg="pink")
lb4=Label(win,padx=10,text="Email-Id",font=("Comic Sans MS",10),bg="pink")
lb5=Label(win,padx=5,text="Phone No.",font=("Comic Sans MS",10),bg="pink")
lb6=Label(win,padx=12,text="Address",font=("Comic Sans MS",10),bg="pink")
lb7=Label(win,padx=12,text="Passcode",font=("Comic Sans MS",10),bg="pink")
lb9=Label(win,padx=12,text="Security Q",font=("Comic Sans MS",10),bg="pink")
lb10=Label(win,padx=12,text="Answer",font=("Comic Sans MS",10),bg="pink")
lb8=Button(win,padx=5,text="Do You Have Account ? Login",font=("Comic Sans MS",10),command=login,bd=0,cursor="hand2",bg="pink")

  #=========================Field Place=====================================
lb2.place(x=450,y=130)
lb1.place(x=550,y=90)
lb3.place(x=450,y=180)
lb4.place(x=450,y=230)
lb5.place(x=450,y=280)
lb6.place(x=450,y=330)
lb7.place(x=450,y=380)
lb8.place(x=500,y=520)
lb9.place(x=450,y=430)
lb10.place(x=450,y=480)

#=========================Table_Input=====================================
username=StringVar()
tb2=Entry(win,textvariable=username)
tb2.place(x=560,y=130)

lastname=StringVar()
tb3=Entry(win,textvariable=lastname)
tb3.place(x=560,y=180)

email=StringVar()
tb4=Entry(win,textvariable=email)
tb4.place(x=560,y=230)

phone=StringVar()
tb5=Entry(win,textvariable=phone)
tb5.place(x=560,y=280)

address=StringVar()
tb6=Entry(win,textvariable=address)
tb6.place(x=560,y=330)

variable=StringVar()
variable.set(OPTIONS[0])
tb6=OptionMenu(win,variable,*OPTIONS)
tb6.place(x=560,y=430)

answer=StringVar()
tb6=Entry(win,textvariable=answer)
tb6.place(x=560,y=480)


password=StringVar()
tb6=Entry(win,show="*",textvariable=password)
tb6.place(x=560,y=380)

#==============================Button=============================


btn=Button(win,text="Register ",fg="white",bg="red",cursor="hand2",width=8,font=("Comic Sans MS",10),command=__register)
btn.place(x=520,y=570)

btn=Button(win,text="Clear",fg="white",bg="red",cursor="hand2",width=8,font=("Comic Sans MS",10),command=__clear)
btn.place(x=618,y=570)

win.mainloop()
