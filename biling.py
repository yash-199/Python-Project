from tkinter import*
from tkinter import messagebox
from tkinter import filedialog
import math,random
import os
import requests

class Bill_App:
      def __init__(self,root):
           self.root=root
           self.root.geometry("1310x950+0+0")
           self.root.title("Billing Software")
           self.root.config(bg="white")
           

           title=Label(self.root,text="Customer Billing",font=("Comic Sans MS",20,"bold"),padx=10,width=62,height=2,bd=8,relief="raise",bg="black",fg="white").pack()

           #===========variable================

           self.bathsoap=IntVar()
           self.wash=IntVar()
           self.cream=IntVar()
           self.sampoo=IntVar()
           self.oil=IntVar()
           self.gel=IntVar()
           self.perfume=IntVar()
           self.cond=IntVar()
           self.toothbrush=IntVar()
           self.blade=IntVar()

           self.rice=IntVar()
           self.wheat=IntVar()
           self.foodoil=IntVar()
           self.pulse=IntVar()
           self.sugar=IntVar()
           self.tea=IntVar()
           self.ghee=IntVar()
           self.nut=IntVar()
           self.salt=IntVar()
           self.turmeric=IntVar()
           
           self.thumbup=IntVar()
           self.cocakola=IntVar()
           self.maza=IntVar()
           self.limca=IntVar()
           self.sprite=IntVar()
           self.appy=IntVar()
           self.pepsi=IntVar()
           self.mirinda=IntVar()
           self.mountaindew=IntVar()

           self.tshirt=IntVar()
           self.shirt=IntVar()
           self.jean=IntVar()
           self.shoe=IntVar()
           self.gymcloth=IntVar()
           self.top=IntVar()
           self.palzo=IntVar()
           self.sandel=IntVar()
           self.gymcloths=IntVar()


           self.knife=IntVar()
           self.spoons=IntVar()
           self.cups=IntVar()
           self.mixingbowl=IntVar()
           self.fryingpan=IntVar()
           self.ovengloves=IntVar()
           self.pastafork=IntVar()
           self.kitchenfoil=IntVar()
           self.zipperbags=IntVar()
           self.plasticclingfilm=IntVar()

           self.cosmeticprice=StringVar()
           self.groceryprice=StringVar()
           self.drinkprice=StringVar()
           self.clothprice=StringVar()
           self.utenslisprice=StringVar()
           self.c=StringVar()
           
           self.cosmetictax=StringVar()
           self.grocerytax=StringVar()
           self.drinktax=StringVar()
           self.clothtax=StringVar()
           self.utenslistax=StringVar()


           self.cname=StringVar()
           self.c_no=StringVar()
           self.billno=StringVar()
           x=random.randint(1000,9999)
           self.billno.set(str(x))
           self.searchbill=StringVar()
           

                                             #======================================Customer Details================

           
           f1=LabelFrame(self.root,text="Customer Detail",font=("Comic Sans MS",10,"bold"),bd=8,relief="raise",bg="black",fg="white")
           f1.place(x=0,y=112,relwidth=1)
           
           cn=Label(f1,text="Customer Name",font=("Comic Sans MS",10,"bold"),bg="black",fg="white").grid(row=0,column=0)
           cn=Entry(f1,width=20,bd=6,relief="raise",textvariable=self.cname,font=("Comic Sans MS",10,"bold")).grid(row=0,column=1,pady=5,padx=10)
           
           cno=Label(f1,text="Customer No:",font=("Comic Sans MS",10,"bold"),bg="black",fg="white").grid(row=0,column=2)
           cno=Entry(f1,width=20,bd=6,textvariable=self.c_no,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=0,column=3,pady=5,padx=10)
           
           bn=Label(f1,text="Bill No:",font=("Comic Sans MS",10,"bold"),bg="black",fg="white").grid(row=0,column=5)
           bn=Entry(f1,width=20,bd=6,textvariable=self.searchbill,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=0,column=6,pady=5,padx=10)
           
           bill_btn=Button(f1,text="Search",command=self.find_bill,font=("Comic Sans MS",10,"bold"),bd=6,relief="raise",bg="black",fg="white")
           bill_btn.grid(row=0,column=7,pady=5,padx=10)


#==============================================Cosmetics Details=============================================

           
           f2=LabelFrame(self.root,bd=8,relief="raise",text="Cosmetics",font=("Comic Sans MS",10,"bold"),bg="black",fg="white")
           f2.place(x=1,y=214,width=180,height=450)
           label=Label(f2,text="Bath Soap:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=0,column=0)
           label=Entry(f2,width=3,bd=1,textvariable=self.bathsoap,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=0,column=1,pady=6)

           label=Label(f2,text="Face Wash:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=1,column=0)
           label=Entry(f2,width=3,bd=1,textvariable=self.wash,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=1,column=1,pady=6,padx=20)

           label=Label(f2,text="Face Cream:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=2,column=0)
           label=Entry(f2,width=3,bd=1,textvariable=self.cream,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=2,column=1,pady=6,padx=20)

           label=Label(f2,text="Hair Sampoo:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=3,column=0)
           label=Entry(f2,width=3,bd=1,textvariable=self.sampoo,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=3,column=1,pady=6,padx=20)

           label=Label(f2,text="Hair Oil:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=4,column=0)
           label=Entry(f2,width=3,bd=1,textvariable=self.oil,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=4,column=1,pady=6,padx=20)

           label=Label(f2,text="Hair Gel:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=5,column=0)
           label=Entry(f2,width=3,bd=1,textvariable=self.gel,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=5,column=1,pady=6,padx=20)

           label=Label(f2,text="Perfume:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=6,column=0)
           label=Entry(f2,width=3,bd=1,textvariable=self.perfume,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=6,column=1,pady=6,padx=20)

           label=Label(f2,text="Hair Cond:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=7,column=0)
           label=Entry(f2,width=3,bd=1,textvariable=self.cond,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=7,column=1,pady=6,padx=20)

           label=Label(f2,text="Tooth Brush:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=8,column=0)
           label=Entry(f2,width=3,bd=1,textvariable=self.toothbrush,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=8,column=1,pady=6,padx=20)

           label=Label(f2,text="Shav Blade:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=9,column=0)
           label=Entry(f2,width=3,bd=1,textvariable=self.blade,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=9,column=1,pady=6,padx=20)

          
#==============================================Grocery Details=============================================


           f3=LabelFrame(self.root,bd=8,relief="raise",text="Grocery",font=("Comic Sans MS",10,"bold"),bg="black",fg="white")
           f3.place(x=183,y=214,width=160,height=450)
           
           label=Label(f3,text="Rice:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=0,column=0)
           label=Entry(f3,width=3,bd=1,textvariable=self.rice,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=0,column=1,pady=6,padx=20)
           
           label=Label(f3,text="Wheat:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=1,column=0)
           label=Entry(f3,width=3,bd=1,textvariable=self.wheat,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=1,column=1,pady=6,padx=20)

           label=Label(f3,text="Food Oil:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=2,column=0)
           label=Entry(f3,width=3,bd=1,textvariable=self.foodoil,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=2,column=1,pady=6,padx=20)

           label=Label(f3,text="Pulse:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=3,column=0)
           label=Entry(f3,width=3,bd=1,textvariable=self.pulse,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=3,column=1,pady=6,padx=20)

           label=Label(f3,text="Sugar:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=4,column=0)
           label=Entry(f3,width=3,bd=1,textvariable=self.sugar,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=4,column=1,pady=6,padx=20)

           label=Label(f3,text="Tea:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=5,column=0)
           label=Entry(f3,width=3,bd=1,textvariable=self.tea,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=5,column=1,pady=6,padx=20)

           label=Label(f3,text="Ghee:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=6,column=0)
           label=Entry(f3,width=3,bd=1,textvariable=self.ghee,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=6,column=1,pady=6,padx=20)

           label=Label(f3,text="Nuts:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=7,column=0)
           label=Entry(f3,width=3,bd=1,textvariable=self.nut,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=7,column=1,pady=6,padx=20)

           label=Label(f3,text=" Salt:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=8,column=0)
           label=Entry(f3,width=3,bd=1,textvariable=self.salt,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=8,column=1,pady=6,padx=20)

           label=Label(f3,text="Turmeric:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=9,column=0)
           label=Entry(f3,width=3,bd=1,textvariable=self.turmeric,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=9,column=1,pady=6,padx=20)

           

#==============================================Cold Drinks Details=============================================


           f4=LabelFrame(self.root,bd=8,relief="raise",text="Cold Drinks",font=("Comic Sans MS",10,"bold"),bg="black",fg="white")
           f4.place(x=345,y=216,width=178,height=450)
           
           label=Label(f4,text="Thumb Up:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=0,column=0)
           label=Entry(f4,width=3,bd=1,textvariable=self.thumbup,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=0,column=1,pady=6,padx=20)
           
           label=Label(f4,text="Coca Cola:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=1,column=0)
           label=Entry(f4,width=3,bd=1,textvariable=self.cocakola,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=1,column=1,pady=6,padx=20)
           
           label=Label(f4,text="Maza:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=2,column=0)
           label=Entry(f4,width=3,bd=1,textvariable=self.maza,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=2,column=1,pady=6,padx=20)
           
           label=Label(f4,text="Limca:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=3,column=0)
           label=Entry(f4,width=3,bd=1,textvariable=self.limca,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=3,column=1,pady=6,padx=20)
           
           label=Label(f4,text="Sprite:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=4,column=0)
           label=Entry(f4,width=3,bd=1,textvariable=self.sprite,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=4,column=1,pady=6,padx=20)
           
           label=Label(f4,text="Appy",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=5,column=0)
           label=Entry(f4,width=3,bd=1,textvariable=self.appy,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=5,column=1,pady=6,padx=20)
           
           label=Label(f4,text="Pepsi:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=7,column=0)
           label=Entry(f4,width=3,bd=1,textvariable=self.pepsi,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=7,column=1,pady=6,padx=20)

           label=Label(f4,text="Mirinda:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=8,column=0)
           label=Entry(f4,width=3,bd=1,textvariable=self.mirinda,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=8,column=1,pady=6,padx=20)

           label=Label(f4,text="MountainDew:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=9,column=0)
           label=Entry(f4,width=3,bd=1,textvariable=self.mountaindew,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=9,column=1,pady=6,padx=20)



#==============================================Clothes Details=============================================


           f6=LabelFrame(self.root,bd=8,relief="raise",text="Clothes",font=("Comic Sans MS",10,"bold"),bg="black",fg="white")
           f6.place(x=525,y=216,width=190,height=450)
           label=Label(f6,text="Men's Clothes",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=0,column=0)
           
           label=Label(f6,text="T-Shirt:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=1,column=0)
           label=Entry(f6,width=3,bd=1,textvariable=self.tshirt,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=1,column=1,pady=6)
           
           label=Label(f6,text="Shirt:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=2,column=0)
           label=Entry(f6,width=3,bd=1,textvariable=self.shirt,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=2,column=1,pady=6,padx=20)
           
           label=Label(f6,text="Jean:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=3,column=0)
           label=Entry(f6,width=3,bd=1,textvariable=self.jean,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=3,column=1,pady=6,padx=20)
           
           label=Label(f6,text="Shoe:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=4,column=0)
           label=Entry(f6,width=3,bd=1,textvariable=self.limca,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=4,column=1,pady=6,padx=20)

           label=Label(f6,text="GYM Cloth:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=5,column=0)
           label=Entry(f6,width=3,bd=1,textvariable=self.gymcloth,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=5,column=1,pady=6,padx=20)

           label=Label(f6,text="Women's ",font=("Comic Sans MS",10,"bold"),bg="black",fg="white").grid(row=6,column=0)
           
           label=Label(f6,text="Top:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=7,column=0)
           label=Entry(f6,width=3,bd=1,textvariable=self.top,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=7,column=1,pady=6,padx=20)
           
           label=Label(f6,text="Palzo",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=8,column=0)
           label=Entry(f6,width=3,bd=1,textvariable=self.palzo,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=8,column=1,pady=6,padx=20)
           
           label=Label(f6,text="Sandel:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=9,column=0)
           label=Entry(f6,width=3,bd=1,textvariable=self.sandel,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=9,column=1,pady=6,padx=20)

           label=Label(f6,text="GYM Cloth:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=10,column=0)
           label=Entry(f6,width=3,bd=1,textvariable=self.gymcloths,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=10,column=1,pady=6,padx=20)



#==============================================Utensils Details=============================================


           f6=LabelFrame(self.root,bd=8,relief="raise",text="Utensils",font=("Comic Sans MS",10,"bold"),bg="black",fg="white")
           f6.place(x=715,y=216,width=198,height=450)
           
           label=Label(f6,text="knife:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=0,column=0)
           label=Entry(f6,width=3,bd=1,textvariable=self.knife,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=0,column=1,pady=6)
           
           label=Label(f6,text="Spoons:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=1,column=0)
           label=Entry(f6,width=3,bd=1,textvariable=self.spoons,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=1,column=1,pady=6,padx=20)
           
           label=Label(f6,text="Cups:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=2,column=0)
           label=Entry(f6,width=3,bd=1,textvariable=self.cups,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=2,column=1,pady=6,padx=20)
           
           label=Label(f6,text="Mixing bowl:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=3,column=0)
           label=Entry(f6,width=3,bd=1,textvariable=self.mixingbowl,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=3,column=1,pady=6,padx=20)
           
           label=Label(f6,text="Frying pan:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=4,column=0)
           label=Entry(f6,width=3,bd=1,textvariable=self.fryingpan,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=4,column=1,pady=6,padx=20)
           
           label=Label(f6,text="Oven gloves",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=5,column=0)
           label=Entry(f6,width=3,bd=1,textvariable=self.ovengloves,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=5,column=1,pady=6,padx=20)
           
           label=Label(f6,text="Pasta fork:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=6,column=0)
           label=Entry(f6,width=3,bd=1,textvariable=self.pastafork,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=6,column=1,pady=6,padx=20)

           label=Label(f6,text="Zipper bags:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=7,column=0)
           label=Entry(f6,width=3,bd=1,textvariable=self.zipperbags,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=7,column=1,pady=6,padx=20)

           label=Label(f6,text="Kitchen foil:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=8,column=0)
           label=Entry(f6,width=3,bd=1,textvariable=self.kitchenfoil,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=8,column=1,pady=6,padx=20)

           label=Label(f6,text="Plastic clingfilm:",font=("Comic Sans MS",9,"bold"),bg="black",fg="white").grid(row=9,column=0)
           label=Entry(f6,width=3,bd=1,textvariable=self.plasticclingfilm,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=9,column=1,pady=6,padx=20)


#==============================================Bill TextArea=============================================


           f5=Frame(self.root,bd=8,relief="raise")
           f5.place(x=920,y=217,width=360,height=450)
           bill_title=Label(f5,text="Bill Area",font=("Comic Sans MS",15,"bold"),relief="raise").pack(fill=X)
           scrol_y=Scrollbar(f5,orient=VERTICAL)
           self.txtarea=Text(f5,yscrollcommand=scrol_y.set)
           scrol_y.pack(side=RIGHT,fill=Y)
           scrol_y.config(command=self.txtarea.yview)
           self.txtarea.pack(fill=BOTH,expand=1)


#==============================================Billing PRICES=============================================


           f6=LabelFrame(self.root,bd=8,relief="raise",text="Billing Menu",font=("Comic Sans MS",10,"bold"),bg="black",fg="white")
           f6.place(x=0,y=670,relwidth=1)
           
           label=Label(f6,text="Total Cosmetic Price:",font=("Comic Sans MS",10,"bold"),bg="black",fg="white").grid(row=0,column=0)
           label=Entry(f6,width=10,bd=1,textvariable=self.cosmeticprice,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=0,column=1,pady=7,padx=20)

           label=Label(f6,text="Total Grocery Price:",font=("Comic Sans MS",10,"bold"),bg="black",fg="white").grid(row=1,column=0)
           label=Entry(f6,width=10,bd=1,textvariable=self.groceryprice,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=1,column=1,pady=7,padx=20)

           label=Label(f6,text="Total Drink  Price:",font=("Comic Sans MS",10,"bold"),bg="black",fg="white").grid(row=2,column=0)
           label=Entry(f6,width=10,bd=1,textvariable=self.drinkprice,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=2,column=1,pady=7,padx=17)

           label=Label(f6,text="Total Clothes  Price:",font=("Comic Sans MS",10,"bold"),bg="black",fg="white").grid(row=3,column=0)
           label=Entry(f6,width=10,bd=1,textvariable=self.clothprice,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=3,column=1,pady=7,padx=17)

           label=Label(f6,text="Total Utenslis  Price:",font=("Comic Sans MS",10,"bold"),bg="black",fg="white").grid(row=4,column=0)
           label=Entry(f6,width=10,bd=1,textvariable=self.utenslisprice,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=4,column=1,pady=7,padx=17)


#==============================================BILLING TAXES=============================================


           label=Label(f6,text="Cosmetic Tax:",font=("Comic Sans MS",10,"bold"),bg="black",fg="white").grid(row=0,column=5)
           label=Entry(f6,width=10,bd=1,textvariable=self.cosmetictax,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=0,column=6,pady=8,padx=20)

           label=Label(f6,text="Grocery Taxes:",font=("Comic Sans MS",10,"bold"),bg="black",fg="white").grid(row=1,column=5)
           label=Entry(f6,width=10,bd=1,textvariable=self.grocerytax,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=1,column=6,pady=8,padx=20)

           label=Label(f6,text="Drink Taxes:",font=("Comic Sans MS",10,"bold"),bg="black",fg="white").grid(row=2,column=5)
           label=Entry(f6,width=10,bd=1,textvariable=self.drinktax,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=2,column=6,pady=8,padx=20)

           label=Label(f6,text="Clothes Taxes:",font=("Comic Sans MS",10,"bold"),bg="black",fg="white").grid(row=3,column=5)
           label=Entry(f6,width=10,bd=1,textvariable=self.clothtax,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=3,column=6,pady=8,padx=20)

           label=Label(f6,text="Clothes Taxes:",font=("Comic Sans MS",10,"bold"),bg="black",fg="white").grid(row=4,column=5)
           label=Entry(f6,width=10,bd=1,textvariable=self.utenslistax,font=("Comic Sans MS",10,"bold"),relief="raise").grid(row=4,column=6,pady=8,padx=20)


#==============================================BUTTONS=============================================

           f7=LabelFrame(self.root,bd=2,relief="raise",font=("Comic Sans MS",10,"bold"),bg="black",fg="white")
           f7.place(x=630,y=740,width=610,height=120)
           
           Total_btn=Button(f7,text="Total",width=8,font=("Comic Sans MS",10,"bold"),bd=6,relief="raise",bg="black",fg="white",command=self.total)
           Total_btn.grid(row=0,column=6,pady=25,padx=12)
           
           gn_btn=Button(f7,text="Genrate Bill",command=self.bill_area,font=("Comic Sans MS",10,"bold"),bd=6,relief="raise",bg="black",fg="white")
           gn_btn.grid(row=0,column=7,pady=35,padx=30)
           
           clear_btn=Button(f7,text="Clear",width=5,command=self.clear_data,font=("Comic Sans MS",10,"bold"),bd=6,relief="raise",bg="black",fg="white")
           clear_btn.grid(row=0,column=8,pady=35,padx=16)

           send_btn=Button(f7,text="Send",width=5,command=self.send_sms,font=("Comic Sans MS",10,"bold"),bd=6,relief="raise",bg="black",fg="white")
           send_btn.grid(row=0,column=9,pady=35,padx=16)
                      
           Exit_btn=Button(f7,text="LogOut",width=6,command=self.Exit_App,font=("Comic Sans MS",10,"bold"),bd=6,relief="raise",bg="black",fg="white")
           Exit_btn.grid(row=0,column=10,pady=45,padx=12)
           self.welcome_bill()

#==============================================FUNCTIONS=============================================


      def total(self):
          self.cbsp=(self.bathsoap.get()*40)
          self.cwp=(self.wash.get()*120)
          self.c_cp=(self.cream.get()*150)
          self.csp=(self.sampoo.get()*180)
          self.cop=(self.oil.get()*100)
          self.cpp=(self.perfume.get()*280)
          self.cgp=(self.gel.get()*100)
          self.chcp=(self.cond.get()*100)
          self.ctbp=(self.toothbrush.get()*50)
          self.csbp=(self.blade.get()*100)
          self.total_cosmetic_price=float(self.cbsp+
                                                        self.cwp+
                                                        self.c_cp+
                                                        self.csp+
                                                        self.cop+
                                                        self.cpp+
                                                        self.cgp+
                                                        self.chcp+
                                                        self.ctbp+
                                                        self.csbp
                                                        )
          self.cosmeticprice.set("Rs."+str(self.total_cosmetic_price))
          self.c_tax=round((self.total_cosmetic_price*0.02),2)
          self.cosmetictax.set("Rs."+str(self.c_tax))
          

          self.grp=(self.rice.get()*270)
          self.gwp=(self.wheat.get()*250)
          self.gfp=(self.foodoil.get()*130)
          self.gpp=(self.pulse.get()*100)
          self.gsp=(self.sugar.get()*100)
          self.gtp=(self.tea.get()*280)
          self.ggp=(self.ghee.get()*250)
          self.gnp=(self.nut.get()*250)
          self.gsap=(self.salt.get()*120)
          self.gtup=(self.turmeric.get()*150)
          self.total_grocery_price=float(self.grp+
                                                      self.gwp+
                                                      self.gfp+
                                                      self.gpp+
                                                      self.gsp+
                                                      self.gtp+
                                                      self.ggp+
                                                      self.gnp+
                                                      self.gsap+
                                                      self.gtup
                                                      )
          self.groceryprice.set("Rs."+str(self.total_grocery_price))
          self.g_tax=round((self.total_grocery_price*0.01),2)
          self.grocerytax.set("Rs."+str(self.g_tax))
          

          self.dtp=(self.thumbup.get()*70)
          self.dckp=(self.cocakola.get()*50)
          self.dmp=(self.maza.get()*60)
          self.dlp=(self.limca.get()*40)
          self.dsp=(self.sprite.get()*90)
          self.dap=(self.appy.get()*50)
          self.drbp=(self.pepsi.get()*80)
          self.dmip=(self.mirinda.get()*60)
          self.dmdp=(self.mountaindew.get()*40)
          self.total_drink_price=float(self.dtp+
                                                  self.dckp+
                                                  self.dmp+
                                                  self.dlp+
                                                  self.dsp+
                                                  self.dap+
                                                  self.drbp+
                                                  self.dmip+
                                                  self.dmdp
                                                  )
          self.drinkprice.set("Rs."+str(self.total_drink_price))
          self.d_tax=round((self.total_drink_price*0.03),2)
          self.drinktax.set("Rs."+str(self.d_tax))

          self.c_tsp=(self.tshirt.get()*99)
          self.c_shp=(self.shirt.get()*290)
          self.c_jp=(self.jean.get()*600)
          self.c_sop=(self.shoe.get()*299)
          self.c_gyp=(self.gymcloth.get()*300)
          self.c_wtp=(self.top.get()*99)
          self.c_wpp=(self.palzo.get()*100)
          self.c_sanp=(self.sandel.get()*299)
          self.c_gymp=(self.gymcloths.get()*399)
          self.total_cloth_price=float(self.c_tsp+
                                                  self.c_shp+
                                                  self.c_jp+
                                                  self.c_sop+
                                                  self.c_gyp+
                                                  self.c_wtp+
                                                  self.c_wpp+
                                                  self.c_sanp+
                                                  self.c_gymp
                                                  )
          self.clothprice.set("Rs."+str(self.total_cloth_price))
          self.clot_tax=round((self.total_cloth_price*0.02),2)
          self.clothtax.set("Rs."+str(self.clot_tax))

          self.ukp=(self.knife.get()*99)
          self.usp=(self.spoons.get()*290)
          self.ucp=(self.cups.get()*100)
          self.umbp=(self.mixingbowl.get()*299)
          self.ufpp=(self.fryingpan.get()*300)
          self.uogp=(self.ovengloves.get()*99)
          self.upfp=(self.pastafork.get()*100)
          self.uzb=(self.zipperbags.get()*50)
          self.ukfp=(self.kitchenfoil.get()*299)
          self.upcp=(self.plasticclingfilm.get()*399)
          
          self.total_utenslis_price=float(self.ukp+
                                                  self.usp+
                                                  self.ucp+
                                                  self.umbp+
                                                  self.ufpp+
                                                  self.uogp+
                                                  self.upfp+
                                                  self.uzb+
                                                  self.ukfp+
                                                  self.upcp
                                                  )
          self.utenslisprice.set("Rs."+str(self.total_utenslis_price))
          self.u_tax=round((self.total_utenslis_price*0.02),2)
          self.utenslistax.set("Rs."+str(self.u_tax))




          self.Total_bill=float(self.total_cosmetic_price+
                                      self.total_cloth_price+
                                      self.total_grocery_price+
                                      self.total_drink_price+
                                      self.total_utenslis_price+
                                      self.c_tax+
                                      self.g_tax+
                                      self.d_tax+
                                      self.u_tax+
                                      self.clot_tax
                                      )


          
      def welcome_bill(self):
            self.txtarea.delete('1.0',END)
            self.txtarea.insert(END,"\tWelcome to STORE|-|UB\n")
            self.txtarea.insert(END,f"\n Bill No:{self.billno.get()}")
            self.txtarea.insert(END,f"\n Customer Name:{self.cname.get()}")
            self.txtarea.insert(END,f"\n Contact No:{self.c_no.get()}")
            self.txtarea.insert(END,f"\n============================")
            self.txtarea.insert(END,f"\n  Products\t\tQTY\tPrice")
            self.txtarea.insert(END,f"\n============================")

            
      def bill_area(self):
            if self.cname.get()=="" or self.c_no.get()=="":
                  messagebox.showerror ("Error","Customer Details Must")
            elif self.cosmeticprice.get()=="Rs. 0.0" and self.groceryprice.get()=="Rs. 0.0" and  self.drinkprice.get()=="Rs. 0.0" and self.clothprice.get()=="Rs.0.0" and self.untenslis.get()=="Rs. 0.0":
                 messagebox.showerror ("Error","No Product Added !")
            else:
                  self.welcome_bill()
            #=================cosmeticproduct===========================
            
            if self.bathsoap.get()!=0:
                 self.txtarea.insert(END,f"\n Bath Soap \t\t{self.bathsoap.get()}\t{self.cbsp}")
                 
            if self.wash.get()!=0:
                 self.txtarea.insert(END,f"\n Face Wash \t\t{self.wash.get()}\t{self.cwp}")
                 
            if self.cream.get()!=0:
                 self.txtarea.insert(END,f"\n Face Cream \t\t{self.cream.get()}\t{self.c_cp}")
                 
            if self.sampoo.get()!=0:
                 self.txtarea.insert(END,f"\n Sampoo \t\t{self.sampoo.get()}\t{self.csp}")
                 
            if self.oil.get()!=0:
                 self.txtarea.insert(END,f"\n Hair Oil \t\t{self.oil.get()}\t{self.cop}")
                 
            if self.perfume.get()!=0:
                 self.txtarea.insert(END,f"\n Perfume \t\t{self.perfume.get()}\t{self.cpp}")
                 
            if self.gel.get()!=0:
                 self.txtarea.insert(END,f"\n Hair Gel \t\t{self.gel.get()}\t{self.cgp}")

            if self.cond.get()!=0:
                 self.txtarea.insert(END,f"\n Hair Cond \t\t{self.cond.get()}\t{self.chcp}")

            if self.toothbrush.get()!=0:
                 self.txtarea.insert(END,f"\n Tooth Brush \t\t{self.toothbrush.get()}\t{self.ctbp}")

            if self.blade.get()!=0:
                 self.txtarea.insert(END,f"\n Shav Blade \t\t{self.blade.get()}\t{self.csbp}")
                 
                 
                 
            #=========================Grocery Product====================
                 
            if self.rice.get()!=0:
                 self.txtarea.insert(END,f"\n Rice \t\t{self.rice.get()}\t{self.grp}")

            if self.wheat.get()!=0:
                 self.txtarea.insert(END,f"\n Wheat \t\t{self.wheat.get()}\t{self.gwp}")

            if self.foodoil.get()!=0:
                 self.txtarea.insert(END,f"\n Food Oil \t\t{self.foodoil.get()}\t{self.gfp}")

            if self.pulse.get()!=0:
                 self.txtarea.insert(END,f"\n Pulse \t\t{self.pulse.get()}\t{self.gpp}")

            if self.sugar.get()!=0:
                 self.txtarea.insert(END,f"\nDbl Filter Sugar \t{self.sugar.get()}\t\t{self.gsp}")

            if self.tea.get()!=0:
                 self.txtarea.insert(END,f"\n TATA Tea \t\t{self.tea.get()}\t{self.gtp}")

            if self.ghee.get()!=0:
                 self.txtarea.insert(END,f"\n Ghee \t\t{self.ghee.get()}\t{self.ggp}")

            if self.nut.get()!=0:
                 self.txtarea.insert(END,f"\n Nuts \t\t{self.nut.get()}\t{self.gnp}")

            if self.salt.get()!=0:
                 self.txtarea.insert(END,f"\n TATA salt \t\t{self.salt.get()}\t{self.gsap}")

            if self.turmeric.get()!=0:
                 self.txtarea.insert(END,f"\n Turmeric \t\t{self.turmeric.get()}\t{self.gtup}")
                 
                 
                 

            #=========================Drink Product====================
                 
            if self.thumbup.get()!=0:
                 self.txtarea.insert(END,f"\n ThumbUp \t\t{self.thumbup.get()}\t{self.dtp}")

            if self.cocakola.get()!=0:
                 self.txtarea.insert(END,f"\n CocaKola \t\t{self.cocakola.get()}\t{self.dckp}")

            if self.maza.get()!=0:
                 self.txtarea.insert(END,f"\n Maza \t\t{self.maza.get()}\t{self.dmp}")

            if self.limca.get()!=0:
                 self.txtarea.insert(END,f"\n Limca \t\t{self.limca.get()}\t{self.dlp}")

            if self.sprite.get()!=0:
                 self.txtarea.insert(END,f"\n Sprite \t\t{self.sprite.get()}\t{self.dsp}")

            if self.appy.get()!=0:
                 self.txtarea.insert(END,f"\n Appy \t\t{self.appy.get()}\t{self.dap}")

            if self.pepsi.get()!=0:
                 self.txtarea.insert(END,f"\n Pepsi \t\t{self.pepsi.get()}\t{self.drbp}")

            if self.mirinda.get()!=0:
                 self.txtarea.insert(END,f"\n Mirinda \t\t{self.mirinda.get()}\t{self.dmip}")

            if self.mountaindew.get()!=0:
                 self.txtarea.insert(END,f"\n MountainDew \t\t{self.mountaindew.get()}\t{self.dmdp}")

                  #=========================clothes Product====================

            if self.tshirt.get()!=0:
                 self.txtarea.insert(END,f"\n M t-Shirt \t\t{self.tshirt.get()}\t{self.c_tsp}")

            if self.shirt.get()!=0:
                 self.txtarea.insert(END,f"\n M Shirt \t\t{self.shirt.get()}\t{self.c_shp}")

            if self.jean.get()!=0:
                 self.txtarea.insert(END,f"\n M-Jean \t\t{self.jean.get()}\t{self.c_jp}")

            if self.shoe.get()!=0:
                 self.txtarea.insert(END,f"\n M-Shoe \t\t{self.shoe.get()}\t{self.c_sop}")

            if self.gymcloth.get()!=0:
                 self.txtarea.insert(END,f"\n M-GymCloth \t\t{self.gymcloth.get()}\t{self.c_gyp}")

            if self.top.get()!=0:
                 self.txtarea.insert(END,f"\n F-Top \t\t{self.top.get()}\t{self.c_wtp}")

            if self.palzo.get()!=0:
                 self.txtarea.insert(END,f"\n F-Palzo \t\t{self.palzo.get()}\t{self.c_wpp}")

            if self.sandel.get()!=0:
                 self.txtarea.insert(END,f"\n F-Sandel \t\t{self.sandel.get()}\t{self.c_sanp}")

            if self.gymcloths.get()!=0:
                 self.txtarea.insert(END,f"\n F-Gym Colth \t\t{self.gymcloths.get()}\t{self.c_gymp}")


             #=========================utenslis Product====================

            if self.knife.get()!=0:
                 self.txtarea.insert(END,f"\n Knife \t\t{self.knife.get()}\t{self.ukp}")

            if self.spoons.get()!=0:
                 self.txtarea.insert(END,f"\n Spoons \t\t{self.spoons.get()}\t{self.usp}")

            if self.cups.get()!=0:
                 self.txtarea.insert(END,f"\n Cups \t\t{self.cups.get()}\t{self.ucp}")

            if self.mixingbowl.get()!=0:
                 self.txtarea.insert(END,f"\n Mixing Bowl \t\t{self.mixingbowl.get()}\t{self.umbp}")

            if self.fryingpan.get()!=0:
                 self.txtarea.insert(END,f"\n Frying-Pan \t\t{self.fryingpan.get()}\t{self.ufpp}")

            if self.ovengloves.get()!=0:
                 self.txtarea.insert(END,f"\n Oven-gloves \t\t{self.ovengloves.get()}\t{self.uogp}")

            if self.pastafork.get()!=0:
                 self.txtarea.insert(END,f"\n Pasta-Fork \t\t{self.pastafork.get()}\t{self.upfp}")

            if self.zipperbags.get()!=0:
                 self.txtarea.insert(END,f"\n zipperBags \t\t{self.zipperbags.get()}\t{self.uzb}")

            if self.kitchenfoil.get()!=0:
                 self.txtarea.insert(END,f"\n Kitchen-Foil \t\t{self.kitchenfoil.get()}\t{self.ukfp}")

            if self.plasticclingfilm.get()!=0:
                 self.txtarea.insert(END,f"\n Plastic-Clingfilm \t\t{self.plasticclingfilm.get()}\t{self.upcp}")
                 
                 
#===============================================


            self.txtarea.insert(END,f"\n-----------------------------")
            if self.cosmetictax.get()!="Rs.0.0":
                 self.txtarea.insert(END,f"\n Comestic Tax\t\t\t{self.cosmetictax.get()}")

            if self.grocerytax.get()!="Rs.0.0":
                 self.txtarea.insert(END,f"\n Grocery Tax\t\t\t{self.grocerytax.get()}")

            if self.drinktax.get()!="Rs.0.0":
                 self.txtarea.insert(END,f"\n Drink Tax\t\t\t{self.drinktax.get()}")
                 
            self.txtarea.insert(END,f"\n Total Bill:\t\t\tRs.{str(self.Total_bill)}")     
            self.txtarea.insert(END,f"\n-----------------------------")
            self.txtarea.insert(END,f"\n ------Thank You For Visit-----")
            self.save_bill()
            
      def save_bill(self):
            op=messagebox.askyesno("Save Bill","Do you want to save a bill?")
            if op>0:
                   self.bill_data=self.txtarea.get('1.0',END)
                   f1=open("bills/"+str(self.billno.get())+".txt","w")
                   f1.write(self.bill_data)
                   f1.close()
                   messagebox.showinfo("Saved",f"Bill no:{self.billno.get()} saved Sucessfully")
            else:
                  return
      def find_bill(self):
            present="no"
            for i in os.listdir("bills/"):
                 if i.split('.')[0]==self.searchbill.get():
                     f1=open(f"bills/{i}","r")
                     self.txtarea.delete('1.0',END)
                     for d in f1:
                           self.txtarea.insert(END,d)
                     f1.close()
                     present="yes"
            if present=="no":
                 messagebox.showerror("error","Invaild Bill No!")

      def clear_data(self):
            op=messagebox.askyesno("Clear","Do you want to Clear Data?")
            if op>0:
                  self.bathsoap.set(0)
                  self.wash.set(0)
                  self.cream.set(0)
                  self.sampoo.set(0)
                  self.oil.set(0)
                  self.gel.set(0)
                  self.perfume.set(0)
                  self.cond.set(0)
                  self.toothbrush.set(0)
                  self.blade.set(0)
 
                  
                  self.rice.set(0)
                  self.wheat.set(0)
                  self.foodoil.set(0)
                  self.pulse.set(0)
                  self.sugar.set(0)
                  self.tea.set(0)
                  self.ghee.set(0)
                  self.nut.set(0)
                  self.salt.set(0)
                  self.turmeric.set(0)
                  
                  self.thumbup.set(0)
                  self.cocakola.set(0)
                  self.maza.set(0)
                  self.limca.set(0)
                  self.sprite.set(0)
                  self.appy.set(0)
                  self.pepsi.set(0)
                  self.mirinda.set(0)
                  self.mountaindew.set(0)


                  self.tshirt.set(0)
                  self.shirt.set(0)
                  self.jean.set(0)
                  self.shoe.set(0)
                  self.gymcloth.set(0)
                  self.top.set(0)
                  self.palzo.set(0)
                  self.sandel.set(0)
                  self.gymcloths.set(0)


                  self.knife.set(0)
                  self.spoons.set(0)
                  self.cups.set(0)
                  self.mixingbowl.set(0)
                  self.fryingpan.set(0)
                  self.ovengloves.set(0)
                  self.pastafork.set(0)
                  self.kitchenfoil.set(0)
                  self.zipperbags.set(0)
                  self.plasticclingfilm.set(0)

                  
                  self.cosmeticprice.set("")
                  self.groceryprice.set("")
                  self.drinkprice.set("")
                  self.clothprice.set("")
                  self.utenslisprice.set("")

                  self.cosmetictax.set("")
                  self.grocerytax.set("")
                  self.drinktax.set("")
                  self.clothtax.set("")
                  self.utenslistax.set("")

                  
                  self.cname.set("")
                  self.c_no.set("")
                  self.billno.set("")
                  x=random.randint(1000,9999)
                  self.billno.set(str(x))
                  self.searchbill.set("")
                  self.welcome_bill()
            
           
      def Exit_App(self):
            op=messagebox.askyesno("LogOut","Do you want to LogOut?")
            if op>0:
                   import loginforhotel
                   self.root.destroy()

      def send_sms(self):
            import sndno

root=Tk()
obj=Bill_App(root)
root.mainloop()
