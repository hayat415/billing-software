from tkinter import*
import math, random, os
from tkinter import messagebox
class Bill_app:

        def __init__(self,root):
                self.root=root
                self.root.geometry("1350x700+0+0")
                self.root.title("Billing Software")
                bg_color="#074463"
                title=Label(self.root, text="Billing Software", bd=12, relief=GROOVE, bg=bg_color, fg="white", font=("times new roman", 30, "bold"), pady=2). pack(fill=X)
        
                # ....................variables..........................#
                self.soap=IntVar()
                self.face_cream=IntVar()
                self.face_wash=IntVar()
                self.spray=IntVar()
        #.................customer...........#
                self.c_name=StringVar()
                self.c_phone=StringVar()
                self.bill_no=StringVar()
                x=random.randint(1000,9999)
                self.bill_no.set(str(x))
                self.search_bill=StringVar()
                #.................Total Product Price & Tax variable......#
                self.cosmetic_price=StringVar()
                self.grocery_price=StringVar()
                self.cold_drink=StringVar()
        #..................customer..............#
        # customer dtail frame
                f1=LabelFrame(self.root, bd=10, relief=GROOVE, text="Customer Details", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
                f1.place(x=0, y=80, relwidth=1)
                cnam_lbl=Label(f1, text="Customer Name", font=("times new roman", 15, "bold")).grid(row=0, column=0, padx=20, pady=5)
                cname_txt=Entry(f1, width=15,textvariable=self.c_name,font="arial 15", bd=7, relief=SUNKEN). grid(row=0, column=1, pady=5, padx=10)

                cphn_lbl=Label(f1, text="Customer Phone No", font=("times new roman", 15, "bold")).grid(row=0, column=2, padx=20, pady=5)
                cphn_txt=Entry(f1, width=15, textvariable=self.c_phone, font="arial 15", bd=7, relief=SUNKEN). grid(row=0, column=3, pady=5, padx=10)

                cbill_lbl=Label(f1, text="Bill Number", font=("times new roman", 15, "bold")).grid(row=0, column=5, padx=20, pady=5)
                cbill_txt=Entry(f1, width=15, textvariable=self.bill_no, font="arial 15", bd=7, relief=SUNKEN). grid(row=0, column=6, pady=5, padx=10)

                bill_bin=Button(f1, text="Search", command=self.find_bill,width=5, bd=7, font="arial 12 bold"). grid (row=0, column=7, padx =10, pady=20)
        #------------dosmetics frame-------------------#
                f1=LabelFrame(self.root, bd=10, relief=GROOVE, text="Cosmetics", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
                f1.place(x=5, y=200, width=325, height=380)

                bath_lbl=Label(f1,text="Bath Soap", font=("times new roman", 16, "bold")).grid(row=0, column=0, padx=10, pady=10)
                bath_text=Entry(f1,width=10, textvariable=self.soap,font=("times new roman",16, "bold"),relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

                face_cream_lbl=Label(f1, text="Face Cream",  font=("times new roman", 16, "bold")).grid(row=1, column=0, padx=10, pady=10)
                face_creat_text=Entry(f1, width=10, textvariable=self.face_cream, font=("times new roman",16, "bold"), relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)  

                face_basan_lbl=Label(f1, text="Spray",  font=("times new roman", 16, "bold")).grid(row=2, column=0, padx=10, pady=10)
                basan_text=Entry(f1, width=10, textvariable=self.spray, font=("times new roman",16, "bold"), relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

                face_wash_lbl=Label(f1, text="Face Wash",  font=("times new roman", 16, "bold")).grid(row=3, column=0, padx=10, pady=10)
                face_wash_text=Entry(f1, width=10, textvariable=self.face_wash, font=("times new roman",16, "bold"), relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

                f1=LabelFrame(self.root, bd=10, relief=GROOVE, text="Cosmetics", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
                f1.place(x=330, y=200, width=325, height=380)

                bath_lbl=Label(f1,text="Bath Soap", font=("times new roman", 16, "bold")).grid(row=0, column=0, padx=10, pady=10)
                bath_text=Entry(f1,width=10, font=("times new roman",16, "bold"),relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

                face_cream_lbl=Label(f1, text="Face Cream", font=("times new roman", 16, "bold")).grid(row=1, column=0, padx=10, pady=10)
                face_creat_text=Entry(f1, width=10, font=("times new roman",16, "bold"), relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)  

                face_basan_lbl=Label(f1, text="Basan", font=("times new roman", 16, "bold")).grid(row=2, column=0, padx=10, pady=10)
                basan_text=Entry(f1, width=10, font=("times new roman",16, "bold"), relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

                face_wash_lbl=Label(f1, text="Face Wash", font=("times new roman", 16, "bold")).grid(row=3, column=0, padx=10, pady=10)
                face_wash_text=Entry(f1, width=10, font=("times new roman",16, "bold"), relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)
                
                f1=LabelFrame(self.root, bd=10, relief=GROOVE, text="Cosmetics", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
                f1.place(x=650, y=200, width=325, height=380)

                bath_lbl=Label(f1,text="Bath Soap", font=("times new roman", 16, "bold")).grid(row=0, column=0, padx=10, pady=10)
                bath_text=Entry(f1,width=10, font=("times new roman",16, "bold"),relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

                face_cream_lbl=Label(f1, text="Face Cream", font=("times new roman", 16, "bold")).grid(row=1, column=0, padx=10, pady=10)
                face_creat_text=Entry(f1, width=10, font=("times new roman",16, "bold"), relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)  

                face_basan_lbl=Label(f1, text="Basan", font=("times new roman", 16, "bold")).grid(row=2, column=0, padx=10, pady=10)
                basan_text=Entry(f1, width=10, font=("times new roman",16, "bold"), relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

                face_wash_lbl=Label(f1, text="Face Wash", font=("times new roman", 16, "bold")).grid(row=3, column=0, padx=10, pady=10)
                face_wash_text=Entry(f1, width=10, font=("times new roman",16, "bold"), relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)  
        #------------receipt-------------------#
                f5=Frame(self.root,bd=20, relief=GROOVE)
                f5.place(x=980, y=200, width=300, height=380)
                bill_title=Label(f5, text="Bill Area", font=("arial", 15, "bold"), bd=7, relief=GROOVE).pack(fill=X)
                scrol_y=Scrollbar(f5, orient=VERTICAL)
                self.textarea=Text(f5, yscrollcommand=scrol_y.set)
                scrol_y.pack(side=RIGHT,fill=Y)
                scrol_y.config(command=self.textarea.yview)
                self.textarea.pack(fill=BOTH, expand=1)

                #>>>>>>>>>>>>>button>>>>>>>>>>#
                f6=LabelFrame(self.root, bd=10, relief=GROOVE, text="Billing Menu", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
                f6.place(x=0, y=560, relwidth=1, height=140)
                m1=Label(f6,text="total cosmetic Price", bg=bg_color, fg="white", font=("time new roman", 15, "bold")).grid(row=0, column=0, padx=20, pady=1,sticky="w")
                m1_txt=Entry(f6, width=18, textvariable=self.cosmetic_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid (row=0, column=1, padx=10, pady=1)

                m2=Label(f6,text="Total Grocery Price", bg=bg_color, fg="white", font=("time new roman", 15, "bold")).grid(row=1, column=0, padx=20, pady=1,sticky="w")
                m2_txt=Entry(f6, width=18, font="arial 10 bold", bd=7, relief=SUNKEN).grid (row=1, column=1, padx=10, pady=1)

                m3=Label(f6,text="Total Cold Drink Price", bg=bg_color, fg="white", font=("time new roman", 15, "bold")).grid(row=3, column=0, padx=10, pady=1,sticky="w")
                m3_txt=Entry(f6, width=18, font="arial 10 bold", bd=7, relief=SUNKEN).grid (row=3, column=1, padx=10, pady=1)

                btn_f=Frame(f6, bd=10, relief=GROOVE)
                btn_f.place(x=750, width=580, height=105)

                total=Button(btn_f, command=self.total, text="Total", bg="cadetblue", fg="white", pady=10, width=10). grid(row=0, column=0, padx=5, pady=5)
                generate=Button(btn_f, text="generate",command=self.bill_area, bg="cadetblue", fg="white", pady=10, width=10). grid(row=0, column=1, padx=5, pady=5)
                clear=Button(btn_f, text="clear", bg="cadetblue", fg="white", pady=10, width=10). grid(row=0, column=2, padx=5, pady=5)
                exit=Button(btn_f, text="exit", bg="cadetblue", fg="white", pady=10, width=10). grid(row=0, column=3, padx=5, pady=5)
                self.wellcome_bill()
        def total(self):
                self.c_s_p=self.soap.get()
                self.c_fc_p=self.face_cream.get()
                self.c_hse_p=self.spray.get()
                self.c_hg_p=self.face_wash.get()

                self.total_cosmetic_price=float(
                                                self.c_s_p+
                                                self.c_fc_p+
                                                self.c_hse_p+
                                                self.c_hg_p                                
                                                )
                self.cosmetic_price.set(str(self.total_cosmetic_price))
        def wellcome_bill(self):
                self.textarea.delete('1.0', END)
                self.textarea.insert(END, "\tWelcome Webcode Retail")
                self.textarea.insert(END, f"\n Bill Number: {self.bill_no.get()}")
                self.textarea.insert(END, f"\nCustomer Name:{self.c_name.get()}")
                self.textarea.insert(END, f"\n Phone Number:{self.c_phone.get()}")
                self.textarea.insert(END, f"\n++++++++++++++++++++++++++++")
                self.textarea.insert(END, f"\n Products \t\t Qty\t\tPrice")
                self.textarea.insert(END, f"\n============================")

        def bill_area(self):
                if self.c_name.get()=="" or self.c_phone.get()=="":
                        messagebox.showerror("Error", "Customer details are Must")
                elif self.cosmetic_price.get()=="0.0":
                        messagebox.showerror("Error", "No Product purchased")
                else:
                        self.wellcome_bill()
                        if self.soap.get()!=0:
                        
                                self.textarea.insert(END,f"\n Bath Soap\t\t {self.soap.get()}\t\t{self.c_s_p}")
                        self.save_bill()
        def save_bill(self):
                op=messagebox.askyesno("Save Bill", "Do you want to save the Bill?")
                if op>0:
                        self.bill_data=self.textarea.get("1.0", END)
                        f1=open("bills/"+str(self.bill_no.get())+".txt","w")
                        f1.write(self.bill_data)
                        f1.close()
                        messagebox.showinfo("Saved", f"Bill no. : {self.bill_no.get()} saved Successfuly")
                else:
                        return
        def find_bill(self):
                present="no"
                for i in os.listdir("bills/"):
                        if i.split('.')[0]==self.search_bill.get():
                                f1=open(f"bills/{i}", "r")
                                self.textarea.delete('1.0', END)
                                for d in f1:
                                        self.textarea.insert(END, d)
                                f1.close()
                                present="yes"
                if present =="no":
                        messagebox.showerror("Error", "Invalid bil No.")



        

root=Tk()
obj=Bill_app(root)
root.mainloop()
