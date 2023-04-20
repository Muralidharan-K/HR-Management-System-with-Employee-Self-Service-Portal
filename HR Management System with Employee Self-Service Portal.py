from tkinter import *
from tkinter import messagebox, ttk
from time import *
import calendar
import math
import mysql.connector as mc
from datetime import datetime as dt
from fpdf import FPDF

# Main window creation
M_win=Tk()
M_win.title('Welcom to login page')
M_win.configure(bg='#7586cc')
M_win.geometry('350x450')
M_win.state('zoomed')

# Title label
class AppTitle:
    def __init__(self):
        global banner
        banner=Label(M_win, text='Payroll System', bg='#FF3399',font=('Polya',50, 'bold', 'italic')).pack(side='top', fill='x')

# Login page creation
class Login:
    def __init__(self):        
        self.frame=Frame(M_win, relief='raised',bg='#65A8E1', borderwidth=2)        
        self.login=Label(self.frame, text='Login', bg='#FF3399', fg='#FFFFFF', font=('Arial',16)).grid(row=3, column=0, columnspan=2, sticky='news', pady=0)
        self.username=Label(self.frame, text='Username', bg='#65A8E1', fg='#FFFFFF', font=('Arial',10)).grid(row=4, column=0)
        self.username_entry=Entry(self.frame)
        self.username_entry.grid(row=4, column=1, padx=10, pady=20)
        self.password=Label(self.frame, text='Password', bg='#65A8E1', fg='#FFFFFF', font=('Arial',10)).grid(row=5, column=0)
        self.password_entry=Entry(self.frame, show='*')
        self.password_entry.grid(row=5, column=1, pady=5)
        self.login_buttom=Button(self.frame, text='Login', bg='#FF3399', fg='#FFFFFF', font=('Arial',9), command=self.EnterLogin).grid(row=6,column=0, columnspan=2, pady=20)
        self.frame.pack(pady=120, anchor='center') 
   
    def EnterLogin(self):
        global e_empy_id
        e_empy_id=self.username_entry.get()
        e_username=self.username_entry.get()
        e_password=self.password_entry.get()
        employee_id=""
        global designation
        designation=""
        conn=mc.connect(host='localhost', user='root', password='KMDdharan@25', database="employee_db")
        cur=conn.cursor()
        cur.execute("SELECT Employee_ID, Employee_Name, Mob_number, Designation FROM employee_info WHERE Employee_ID = '{}'".format(e_username))
        record=cur.fetchall()
        cur.close()
        conn.close()
        for row in record:
            employee_id=row[0]
            global emp_username
            emp_username=row[1]
            mob_number=row[2]
            designation=row[3]  
        if e_username == employee_id and e_password == mob_number and designation == 'Admin':                    
            self.frame.destroy()
            Logout()
            Employer()         
        elif e_username == employee_id and e_password == mob_number:
            self.frame.destroy()
            Logout()
            Employee()                   
        else:
            self.username_entry.delete(0, 'end')
            self.password_entry.delete(0, 'end')
            messagebox.showerror(title='Error', message='Invalid username or password')
         
# Employer portal creation           
class Employer:
    def __init__(self):        
        global EMP_frame
        EMP_frame=Frame(M_win, relief='raised',bg='#65A8E1')
        for i in range(0,3):
             EMP_frame.columnconfigure(i, weight=1)
             EMP_frame.rowconfigure(i, weight=1)       
        enroll_btn=Button(EMP_frame, text='Employee Enroll', font=('Gadugi',20), bg='magenta', fg='white', command=self.enroll).grid(row=0,column=0, padx=10, pady=5, sticky=W+E)
        self.leave_btn=Button(EMP_frame, text='Off Day Update', font=('Gadugi',20), bg='magenta', fg='white', command=self.offday).grid(row=0,column=1, padx=10, pady=5, sticky=E+W)
        self.atten_btn=Button(EMP_frame, text='Payslip Generate', font=('Gadugi',20), bg='magenta', fg='white', command=self.pay).grid(row=0,column=2, padx=10, pady=5, sticky=W+E)
        self.org_btn=Button(EMP_frame, text='Organization', font=('Gadugi',20), bg='magenta', fg='white').grid(row=1,column=1, padx=10, pady=5, sticky=E+W)
        EMP_frame.pack(fill='both', expand='yes')
        
    def enroll(self):
        EMP_frame.destroy()
        Enrollment()   
    def offday(self):
        EMP_frame.destroy()
        OffDay()   
    def pay(self):
        EMP_frame.destroy()
        Payslip()
        
# Variable assignment
i_Employee_ID=StringVar()
i_Employee_Name=StringVar()
i_Email_ID=StringVar ()
i_Mob_number=StringVar ()
i_Date_of_birth=StringVar ()
i_Marriage_status=StringVar ()
i_Father_name=StringVar ()
i_Mother_name=StringVar ()
i_Spouse_name=StringVar ()
i_Employee_type=StringVar ()
i_Designation=StringVar ()
i_Department_name=StringVar ()
i_Date_of_joining=StringVar ()
i_PF_Number=StringVar ()
i_UAN_number=StringVar ()
i_PAN_number=StringVar ()
i_Aadhar_number=StringVar ()
i_Basic_pay=StringVar ()
i_HRA=StringVar ()
i_Special_allowance=StringVar ()
i_Gross=StringVar ()
i_PF_Emp_cont=StringVar ()
i_PF_Org_cont=StringVar ()
i_Cost_to_the_company=StringVar ()
i_AC_number=StringVar ()
i_Bank_name=StringVar ()
i_Branch=StringVar ()
i_IFSC=StringVar ()
i_Flat_Door_no=StringVar ()
i_Street=StringVar ()
i_Area_locality=StringVar ()
i_City=StringVar ()
i_State=StringVar ()
i_Country=StringVar ()
i_PIN=StringVar ()

# Enrollment
class Enrollment:
    def __init__(self):        
        global En_Mframe
        En_Mframe=Frame(M_win, relief='raised',bg='#dadada', width=900)
        for i in range(0,7):
             En_Mframe.columnconfigure(i, weight=1)
        self.En_lab=Label(En_Mframe, text='Enrollment', font=('Arial',15,'bold'), bg='#dadada', fg='#ed0c61').grid(row=1, column=1, sticky=W)  
        self.em_id=Label(En_Mframe, text='Employee ID', font=('Arial',12), bg='#dadada').grid(row=2, column=1, sticky=W)
        self.em_id_e=Entry(En_Mframe, width=20, font=('Times',12), textvariable=i_Employee_ID)
        self.em_id_e.grid(row=2,column=2, padx=2, pady=5, sticky=W)
        self.em_name=Label(En_Mframe, text='Employee name', font=('Arial',12), bg='#dadada').grid(row=3, column=1, sticky=W)
        self.em_name_e=Entry(En_Mframe, width=20, font=('Times',12), textvariable=i_Employee_Name)
        self.em_name_e.grid(row=3,column=2, padx=2, pady=5, sticky=W)
        self.mail=Label(En_Mframe, text='E-mail ID', font=('Arial',12), bg='#dadada').grid(row=4, column=1, sticky=W)
        self.mail_e=Entry(En_Mframe, width=20, font=('Times',12), textvariable=i_Email_ID)
        self.mail_e.grid(row=4,column=2, padx=2, pady=5, sticky=W)   
        self.mob_num=Label(En_Mframe, text='Mob number', font=('Arial',12), bg='#dadada').grid(row=5, column=1, sticky=W)
        self.mob_num_e=Entry(En_Mframe, width=20, font=('Times',12), textvariable=i_Mob_number)
        self.mob_num_e.grid(row=5,column=2, padx=2, pady=5, sticky=W)                
        self.dob=Label(En_Mframe, text='Date of birth', font=('Arial',12), bg='#dadada').grid(row=6, column=1, sticky=W)
        self.dob_e=Entry(En_Mframe, width=20, font=('Times',12), textvariable=i_Date_of_birth)
        self.dob_e.grid(row=6,column=2, padx=2, pady=5, sticky=W)
        self.mrg_sta=Label(En_Mframe, text='Marriage status', font=('Arial',12), bg='#dadada').grid(row=7, column=1, sticky=W)
        self.mrg_sta_e=Entry(En_Mframe, width=20, font=('Times',12), textvariable=i_Marriage_status)
        self.mrg_sta_e.grid(row=7,column=2, padx=2, pady=5, sticky=W)
        self.father=Label(En_Mframe, text='Father name', font=('Arial',12), bg='#dadada').grid(row=8, column=1, sticky=W)
        self.father_e=Entry(En_Mframe, width=20, font=('Times',12), textvariable=i_Father_name)
        self.father_e.grid(row=8,column=2, padx=2, pady=5, sticky=W)
        self.mother=Label(En_Mframe, text='Mother name', font=('Arial',12), bg='#dadada').grid(row=9, column=1, sticky=W)
        self.mother_e=Entry(En_Mframe, width=20, font=('Times',12), textvariable=i_Mother_name)
        self.mother_e.grid(row=9,column=2, padx=2, pady=5, sticky=W)
        self.spouse=Label(En_Mframe, text='Spouse name', font=('Arial',12), bg='#dadada').grid(row=10, column=1, sticky=W)
        self.spouse_e=Entry(En_Mframe, width=20, font=('Times',12), textvariable=i_Spouse_name)
        self.spouse_e.grid(row=10,column=2, padx=2, pady=5, sticky=W)
        self.em_type=Label(En_Mframe, text='Employee type', font=('Arial',12), bg='#dadada').grid(row=11, column=1, sticky=W)
        self.em_type_e=Entry(En_Mframe, width=20, font=('Times',12), textvariable=i_Employee_type)
        self.em_type_e.grid(row=11,column=2, padx=2, pady=5, sticky=W)
        self.des=Label(En_Mframe, text='Designation', font=('Arial',12), bg='#dadada').grid(row=12, column=1, sticky=W)
        self.des_e=Entry(En_Mframe, width=20, font=('Times',12), textvariable=i_Designation)
        self.des_e.grid(row=12,column=2, padx=2, pady=5, sticky=W)
        self.dep=Label(En_Mframe, text='Department name', font=('Arial',12), bg='#dadada').grid(row=13, column=1, sticky=W)
        self.dep_e=Entry(En_Mframe, width=20, font=('Times',12), textvariable=i_Department_name)
        self.dep_e.grid(row=13,column=2, padx=2, pady=5, sticky=W)
        self.doj=Label(En_Mframe, text='Date of joining', font=('Arial',12), bg='#dadada').grid(row=2, column=3, sticky=W)
        self.doj_e=Entry(En_Mframe, width=20, font=('Times',12), textvariable=i_Date_of_joining)
        self.doj_e.grid(row=2,column=4, padx=2, pady=5,sticky=W)
        self.pf_num=Label(En_Mframe, text='PF Number', font=('Arial',12), bg='#dadada').grid(row=3, column=3, sticky=W)
        self.pf_num_e=Entry(En_Mframe, width=20, font=('Times',12), textvariable=i_PF_Number)
        self.pf_num_e.grid(row=3,column=4, padx=2, pady=5, sticky=W)        
        self.uan=Label(En_Mframe, text='UAN number', font=('Arial',12), bg='#dadada').grid(row=4, column=3, sticky=W)
        self.uan_e=Entry(En_Mframe, width=20, font=('Times',12), textvariable=i_UAN_number)
        self.uan_e.grid(row=4,column=4, padx=2, pady=5, sticky=W)        
        self.pan=Label(En_Mframe, text='PAN number', font=('Arial',12), bg='#dadada').grid(row=5, column=3, sticky=W)
        self.pan_e=Entry(En_Mframe, width=20, font=('Times',12), textvariable=i_PAN_number)
        self.pan_e.grid(row=5,column=4, padx=2, pady=5, sticky=W)
        self.aadhar=Label(En_Mframe, text='Aadhar number', font=('Arial',12), bg='#dadada').grid(row=6, column=3, sticky=W)
        self.aadhar_e=Entry(En_Mframe, width=20, font=('Times',12), textvariable=i_Aadhar_number)
        self.aadhar_e.grid(row=6,column=4, padx=2, pady=5, sticky=W)
        self.basic=Label(En_Mframe, text='Basic pay', font=('Arial',12), bg='#dadada').grid(row=7, column=3, sticky=W)
        self.basic_e=Entry(En_Mframe, width=20, font=('Times',12), textvariable=i_Basic_pay)
        self.basic_e.grid(row=7,column=4, padx=2, pady=5, sticky=W)
        self.hra=Label(En_Mframe, text='HRA', font=('Arial',12), bg='#dadada').grid(row=8, column=3, sticky=W)
        self.hra_e=Entry(En_Mframe, width=20, font=('Times',12), textvariable=i_HRA)
        self.hra_e.grid(row=8,column=4, padx=2, pady=5, sticky=W)
        self.spl=Label(En_Mframe, text='Special allowance', font=('Arial',12), bg='#dadada').grid(row=9, column=3, sticky=W)
        self.spl_e=Entry(En_Mframe, width=20, font=('Times',12), textvariable=i_Special_allowance)
        self.spl_e.grid(row=9,column=4, padx=2, pady=5, sticky=W)
        self.gross=Label(En_Mframe, text='Gross', font=('Arial',12), bg='#dadada').grid(row=10, column=3, sticky=W)
        self.gross_e=Entry(En_Mframe, width=20, font=('Times',12), textvariable=i_Gross)
        self.gross_e.grid(row=10,column=4, padx=2, pady=5, sticky=W)
        self.pf_em_con=Label(En_Mframe, text='PF Emp_cont', font=('Arial',12), bg='#dadada').grid(row=11, column=3, sticky=W)
        self.pf_em_con_e=Entry(En_Mframe, width=20, font=('Times',12), textvariable=i_PF_Emp_cont)
        self.pf_em_con_e.grid(row=11,column=4, padx=2, pady=5, sticky=W)
        self.pf_org_con=Label(En_Mframe, text='PF Org_cont', font=('Arial',12), bg='#dadada').grid(row=12, column=3, sticky=W)
        self.pf_org_con_e=Entry(En_Mframe, width=20, font=('Times',12), textvariable=i_PF_Org_cont)
        self.pf_org_con_e.grid(row=12,column=4, padx=2, pady=5, sticky=W)
        self.ctc=Label(En_Mframe, text='Cost to the company', font=('Arial',12), bg='#dadada').grid(row=13, column=3, sticky=W)
        self.ctc_e=Entry(En_Mframe, width=20, font=('Times',12), textvariable=i_Cost_to_the_company)
        self.ctc_e.grid(row=13,column=4, padx=2, pady=5, sticky=W)
        self.Ac_num=Label(En_Mframe, text='Account detail', font=('Arial',15,'bold'), bg='#dadada', fg='#ed0c61').grid(row=1, column=5, sticky=W) #label        
        self.ac_num=Label(En_Mframe, text='A/C number', font=('Arial',12), bg='#dadada').grid(row=2, column=5, sticky=W)
        self.ac_num_e=Entry(En_Mframe, width=20, font=('Times',12), textvariable=i_AC_number)
        self.ac_num_e.grid(row=2,column=6, padx=2, pady=5, sticky=W)
        self.bank=Label(En_Mframe, text='Bank name', font=('Arial',12), bg='#dadada').grid(row=3, column=5, sticky=W)
        self.bank_e=Entry(En_Mframe, width=20, font=('Times',12), textvariable=i_Bank_name)
        self.bank_e.grid(row=3,column=6, padx=2, pady=5, sticky=W)        
        self.branch=Label(En_Mframe, text='Branch', font=('Arial',12), bg='#dadada').grid(row=4, column=5, sticky=W)
        self.branch_e=Entry(En_Mframe, width=20, font=('Times',12), textvariable=i_Branch)
        self.branch_e.grid(row=4,column=6, padx=2, pady=5, sticky=W)
        self.ifsc=Label(En_Mframe, text='IFSC', font=('Arial',12), bg='#dadada').grid(row=5, column=5, sticky=W)
        self.ifsc_e=Entry(En_Mframe, width=20, font=('Times',12), textvariable=i_IFSC)
        self.ifsc_e.grid(row=5,column=6, padx=2, pady=5, sticky=W)
        self.Add=Label(En_Mframe, text='Address', font=('Arial',15,'bold'), bg='#dadada', fg='#ed0c61').grid(row=6, column=5, sticky=W) #label
        self.flat_num=Label(En_Mframe, text='Flat/Door no.', font=('Arial',12), bg='#dadada').grid(row=7, column=5, sticky=W)
        self.flat_num_e=Entry(En_Mframe, width=20, font=('Times',12), textvariable=i_Flat_Door_no)
        self.flat_num_e.grid(row=7,column=6, padx=2, pady=5, sticky=W)
        self.street=Label(En_Mframe, text='Street', font=('Arial',12), bg='#dadada').grid(row=8, column=5, sticky=W)
        self.street_e=Entry(En_Mframe, width=20, font=('Times',12), textvariable=i_Street)
        self.street_e.grid(row=8,column=6, padx=2, pady=5, sticky=W)
        self.area=Label(En_Mframe, text='Area/locality', font=('Arial',12), bg='#dadada').grid(row=9, column=5, sticky=W)
        self.area_e=Entry(En_Mframe, width=20, font=('Times',12), textvariable=i_Area_locality)
        self.area_e.grid(row=9,column=6, padx=2, pady=5, sticky=W)
        self.city=Label(En_Mframe, text='City', font=('Arial',12), bg='#dadada').grid(row=10, column=5, sticky=W)
        self.city_e=Entry(En_Mframe, width=20, font=('Times',12), textvariable=i_City)
        self.city_e.grid(row=10,column=6, padx=2, pady=5, sticky=W)
        self.state=Label(En_Mframe, text='State', font=('Arial',12), bg='#dadada').grid(row=11, column=5, sticky=W)
        self.state_e=Entry(En_Mframe, width=20, font=('Times',12), textvariable=i_State)
        self.state_e.grid(row=11,column=6, padx=2, pady=5, sticky=W)
        self.country=Label(En_Mframe, text='Country', font=('Arial',12), bg='#dadada').grid(row=12, column=5, sticky=W)
        self.country_e=Entry(En_Mframe, width=20, font=('Times',12), textvariable=i_Country)
        self.country_e.grid(row=12,column=6, padx=2, pady=5, sticky=W)
        self.pin=Label(En_Mframe, text='PIN', font=('Arial',12), bg='#dadada').grid(row=13, column=5, sticky=W)
        self.pin_e=Entry(En_Mframe, width=20, font=('Times',12), textvariable=i_PIN)
        self.pin_e.grid(row=13,column=6, padx=2, pady=5, sticky=W)
        self.sub_btn=Button(En_Mframe, text='SUBMIT', font=('Times',15, 'bold'), bg='#dadada', fg='#217cd8', command=self.submit).grid(row=15, column=6, padx=5, pady=10, sticky=W)
        self.sub_btn=Button(En_Mframe, text='HOME', font=('Times',15, 'bold'), bg='#dadada', fg='#217cd8', command=self.home).grid(row=15, column=7, padx=5, pady=10, sticky=W)        
        En_Mframe.pack(fill='both', expand='yes')
        
    def submit(self,*args):
        e_Employee_ID = i_Employee_ID.get()
        e_Employee_Name = i_Employee_Name.get()        
        e_Email_ID = i_Email_ID.get()
        e_Mob_number = i_Mob_number.get()
        e_Date_of_birth = i_Date_of_birth.get()
        e_Marriage_status = i_Marriage_status.get()
        e_Father_name = i_Father_name.get()
        e_Mother_name = i_Mother_name.get()
        e_Spouse_name = i_Spouse_name.get()
        e_Employee_type = i_Employee_type.get()
        e_Designation = i_Designation.get()
        e_Department_name = i_Department_name.get()
        e_Date_of_joining = i_Date_of_joining.get()
        e_PF_Number = i_PF_Number.get()
        e_UAN_number = i_UAN_number.get()
        e_PAN_number = i_PAN_number.get()
        e_Aadhar_number = i_Aadhar_number.get()
        e_Basic_pay = i_Basic_pay.get()
        e_HRA = i_HRA.get()
        e_Special_allowance = i_Special_allowance.get()
        e_Gross = i_Gross.get()
        e_PF_Emp_cont = i_PF_Emp_cont.get()
        e_PF_Org_cont = i_PF_Org_cont.get()
        e_Cost_to_the_company = i_Cost_to_the_company.get()
        e_AC_number = i_AC_number.get()
        e_Bank_name = i_Bank_name.get()
        e_Branch = i_Branch.get()
        e_IFSC = i_IFSC.get()
        e_Address = i_Flat_Door_no.get()+'\n'+ i_Street.get()+'\n' + i_Area_locality.get()+'\n' + i_City.get()+'\n' + i_State.get()+'\n' + i_Country.get()+'\n' + i_PIN.get()
        
        # database connection
        conn = mc.connect(host="localhost", user="root", password="KMDdharan@25" ,database="employee_db")
        cur=conn.cursor()
        cur.execute("INSERT INTO employee_info(Employee_ID,  Employee_Name,  Email_ID,  Mob_number,  Date_of_birth,  Marriage_status,  Father_name,  Mother_name,  Spouse_name,  Employee_type,  Designation,  Department_name,  Date_of_joining,  PF_Number,  UAN_number,  PAN_number,  Aadhar_number,  Basic_pay,  HRA,  Special_allowance,  Gross,  PF_Emp_cont,  PF_Org_cont,  Cost_to_the_company,  AC_number,  Bank_name,  Branch,  IFSC,  Address) values ('"+e_Employee_ID+"',  '"+e_Employee_Name+"',  '"+e_Email_ID+"',  '"+e_Mob_number+"',  '"+e_Date_of_birth+"',  '"+e_Marriage_status+"',  '"+e_Father_name+"',  '"+e_Mother_name+"',  '"+e_Spouse_name+"',  '"+e_Employee_type+"',  '"+e_Designation+"',  '"+e_Department_name+"',  '"+e_Date_of_joining+"',  '"+e_PF_Number+"',  '"+e_UAN_number+"',  '"+e_PAN_number+"',  '"+e_Aadhar_number+"',  '"+e_Basic_pay+"',  '"+e_HRA+"',  '"+e_Special_allowance+"',  '"+e_Gross+"',  '"+e_PF_Emp_cont+"',  '"+e_PF_Org_cont+"',  '"+e_Cost_to_the_company+"',  '"+e_AC_number+"',  '"+e_Bank_name+"',  '"+e_Branch+"',  '"+e_IFSC+"',  '"+e_Address+"')")
        cur.close()
        conn.close()
        entries=[self.em_id_e,  self.em_name_e,  self.mail_e,  self.mob_num_e,  self.dob_e,  self.mrg_sta_e,  self.father_e,  self.mother_e,  self.spouse_e,  self.em_type_e,  self.des_e,  self.dep_e,  self.doj_e,  self.pf_num_e,  self.uan_e,  self.pan_e,  self.aadhar_e,  self.basic_e,  self.hra_e,  self.spl_e,  self.gross_e,  self.pf_em_con_e,  self.pf_org_con_e,  self.ctc_e,  self.ac_num_e,  self.bank_e,  self.branch_e,  self.ifsc_e,  self.flat_num_e,  self.street_e,  self.area_e,  self.city_e,  self.state_e,  self.country_e,  self.pin_e]
        for entry in entries:
            entry.delete(0,'end')
        messagebox.showinfo(title='message', message='Data entered successfully')
        
    def home(self):
        En_Mframe.destroy()
        Employer()
        
# Off Day Update
class OffDay:
    def __init__ (self):
        global Off_frame
        Off_frame=Frame(M_win, relief='raised',bg='#65A8E1')
        mon=[]
        for i in range(1,13):
            mon.append(i)
        for i in range(1,20):
            Off_frame.columnconfigure(i, weight=1)
        for j in range(1,25):
            Off_frame.rowconfigure(j, weight=1)
        home_btn=Button(Off_frame, text='Home', bg='#FF3399', fg='#FFFFFF', font=('Arial',14), command=self.home).grid(row=1, column=1)
        lab=Label(Off_frame, text='Off day update', bg='#FF3399', fg='#FFFFFF', font=('Arial',14)).grid(row=2, column=2, columnspan=2)
        m_lab=Label(Off_frame, text='Month', bg='#65A8E1', fg='#FFFFFF', font=('Arial',10)).grid(row=3, column=2)
        y_lab=Label(Off_frame, text='Year', bg='#65A8E1', fg='#FFFFFF', font=('Arial',10)).grid(row=3, column=3)
        global clicked
        clicked=StringVar()        
        drop_down=OptionMenu(Off_frame, clicked, *mon).grid(row=4, column=2)
        global i_yr_ent
        i_yr_ent=StringVar()
        yr_ent=Entry(Off_frame, font=('Arial',9), textvariable=i_yr_ent).grid(row=4, column=3)
        update_btn=Button(Off_frame, text='Update', bg='#FF3399', fg='#FFFFFF', font=('Arial',9), command=self.update).grid(row=4, column=4)
        Off_frame.pack(fill='both', expand='yes')
        
    def update(self):
        wk_d={0:[6,7],1:[5,6],2:[4,5],3:[3,4],4:[2,3],5:[1,2],6:[7,1]}
        m=int(clicked.get())
        mo=calendar.month_abbr[m]
        if m<10:
            m_s='0'+str(m)
        else:
            m_s=str(m)
        y=int(i_yr_ent.get())
        yr=i_yr_ent.get()
        mo_yr=mo+" "+yr
        w_s_dt=calendar.monthrange(y,m)[0]
        mo_end_day=calendar.monthrange(y,m)[1]+1
        first_sat=wk_d[w_s_dt][0]
        first_sun=wk_d[w_s_dt][1]
        conn=mc.connect(host="localhost", user="root", password="KMDdharan@25", database="employee_db")
        cur=conn.cursor()
        cur.execute("SELECT Employee_id, Employee_name FROM employee_info")
        record=cur.fetchall()
        conn.close()
        for row in record:
            emp_id=row[0]
            emp_name=row[1]  
            for i in range (first_sat, mo_end_day,7):
                if i<10:
                    dt='0'+str(i)
                    off_date=dt+"-"+m_s+"-"+yr
                else:
                    dt=str(i)
                    off_date=dt+"-"+m_s+"-"+yr                 
                conn=mc.connect(host="localhost", user="root", password="KMDdharan@25", database="employee_db")
                cur=conn.cursor()
                cur.execute("INSERT INTO attendance(Employee_ID, Employee_Name, clk_date, mo_yr, status) values('"+emp_id+"','"+emp_name+"', '"+off_date+"', '"+mo_yr+"', 'Off day')")
                cur.close()
                conn.close()    
            for i in range (first_sun, mo_end_day,7):
                if i<10:
                    dt='0'+str(i)
                    off_date=dt+"-"+m_s+"-"+yr                    
                else:
                    dt=str(i)
                    off_date=dt+"-"+m_s+"-"+yr  
                conn=mc.connect(host="localhost", user="root", password="KMDdharan@25", database="employee_db")
                cur=conn.cursor()
                cur.execute("INSERT INTO attendance(Employee_ID, Employee_Name, clk_date, mo_yr, status) values('"+emp_id+"','"+emp_name+"', '"+off_date+"', '"+mo_yr+"', 'Off day')")
                cur.close()
                conn.close()             
    def home(self):
        Off_frame.destroy()
        Employer()        

# Payslip generate
class Payslip:
    def __init__ (self):
        global Pay_frame
        Pay_frame=Frame(M_win, relief='raised',bg='#65A8E1')
        for i in range(1,20):
            Pay_frame.columnconfigure(i, weight=1)
        for j in range(1,25):
            Pay_frame.rowconfigure(j, weight=1)    
        home_btn=Button(Pay_frame, text='Home', bg='#FF3399', fg='#FFFFFF', font=('Arial',12), command=self.home).grid(row=2, column=2) 
        lab=Label(Pay_frame, text='Pay slip generate', bg='#FF3399', fg='#FFFFFF', font=('Arial',14)).grid(row=3, column=3, columnspan=3)
        m_lab=Label(Pay_frame, text='Month', bg='#65A8E1', fg='#FFFFFF', font=('Arial',10)).grid(row=4, column=3)
        y_lab=Label(Pay_frame, text='Year', bg='#65A8E1', fg='#FFFFFF', font=('Arial',10)).grid(row=4, column=4)
        mon=[]
        for i in range(1,13):
            mon.append(i)
        global clicked
        clicked=IntVar()        
        drop_down=OptionMenu(Pay_frame, clicked, *mon).grid(row=5, column=3)
        global i_yr_ent
        i_yr_ent=StringVar()
        yr_ent=Entry(Pay_frame, font=('Arial',9), textvariable=i_yr_ent).grid(row=5, column=4)
        update_btn=Button(Pay_frame, text='Generate', bg='#FF3399', fg='#FFFFFF', font=('Arial',9), command=self.generate).grid(row=5, column=5)
        Pay_frame.pack(fill='both', expand='yes')
        
    def home(self):
        Pay_frame.destroy()
        Employer()        
    def generate(self):
        month=clicked.get()
        mo=calendar.month_abbr[month]
        year=int(i_yr_ent.get())
        yr=i_yr_ent.get()
        mo_yr=mo+" "+yr
        no_of_day_in_mo=calendar.monthrange(year, month)[1]
        conn=mc.connect(host="localhost", user="root", password="KMDdharan@25", database="employee_db")
        cur=conn.cursor()
        cur.execute("SELECT Employee_id, Employee_name, Employee_type, Designation, Department_name, Date_of_joining, PF_Number, UAN_number, Basic_pay, HRA, Special_allowance, Gross, PF_Emp_cont FROM employee_info")
        record=cur.fetchall()
        conn.close()
        for row in record:
            emp_id=row[0]
            emp_name=row[1]
            emp_type=row[2]
            desig=row[3]
            depart=row[4]
            DOJ=row[5]
            PF=row[6]
            UAN=row[7]
            basic=int(row[8])
            hra=int(row[9])
            spl_allow=int(row[10])
            gross=int(row[11])
            pf_cont=int(row[12])
            conn=mc.connect(host="localhost", user="root", password="KMDdharan@25", db="employee_db")
            cur=conn.cursor()
            cur.execute("SELECT COUNT(employee_id) FROM attendance WHERE employee_id='"+emp_id+"' AND mo_yr='"+mo_yr+"' AND status='Present'")
            pre_c=cur.fetchone()
            present=pre_c[0]
            cur.execute("SELECT COUNT(employee_id) FROM attendance WHERE employee_id='"+emp_id+"' AND mo_yr='"+mo_yr+"' AND status='Off day'")
            off_c=cur.fetchone()
            off_day=off_c[0]
            work_days=present+off_day
            LOP_days=no_of_day_in_mo-work_days
            conn.close()
            LOP=math.ceil(LOP_days*(basic/no_of_day_in_mo))
            deduction=pf_cont+LOP
            net_pay=gross-deduction
            title='Pay Slip Management System'
            pdf=FPDF('P','mm')
            pdf.add_page()
            pdf.set_font('arial','B',size=18)
            pdf.set_line_width(2)
            pdf.cell(175,10,title,ln=1,align='C')
            pdf.ln(5)
            pdf.set_font('arial','I',size=16)
            pdf.cell(175,10,'Salary Slip for '+mo_yr,ln=1,align='C')
            pdf.ln(10)
            pdf.set_font('helvetica',size=10)
            pdf.cell(100,10,'Employee Name : '+emp_name,ln=0,align='L')
            pdf.cell(80,10,'Employee ID : '+emp_id,ln=0,align='L')
            pdf.ln(5)
            pdf.cell(100,10,'Employee Type : '+emp_type,ln=0,align='L')
            pdf.cell(80,10,'Designation : '+desig,ln=0,align='L')
            pdf.ln(5)
            pdf.cell(100,10,'Department : '+depart,ln=0,align='L')
            pdf.cell(80,10,'Date of Joining : '+DOJ,ln=0,align='L')
            pdf.ln(5)
            pdf.cell(100,10,'PF number : '+PF,ln=0,align='L')
            pdf.cell(80,10,'UAN number : '+UAN,ln=0,align='L')
            pdf.ln(20)
            pdf.set_font('arial','I',size=14)
            pdf.cell(100,10,'Earnings',ln=0,align='L')
            pdf.cell(85,10,'Deduction',ln=0,align='L')
            pdf.ln(10)
            pdf.set_font('helvetica',size=10)
            pdf.cell(100,10,'Basic : '+str(basic),ln=0,align='L')
            pdf.cell(80,10,'PF Deduction : '+str(pf_cont),ln=0,align='L')
            pdf.ln(5)
            pdf.cell(100,10,'HRA : '+str(hra),ln=0,align='L')
            pdf.cell(80,10,'LOP : '+str(LOP),ln=0,align='L')
            pdf.ln(5)
            pdf.cell(100,10,'Allowance : '+str(spl_allow),ln=0,align='L')
            pdf.ln(7)
            pdf.set_font('helvetica','B',size=10)
            pdf.cell(100,10,'Gross (A) : '+str(gross),ln=0,align='L')
            pdf.cell(80,10,'Total deduction (B) : '+str(deduction),ln=0,align='L')
            pdf.ln(7)
            pdf.cell(100,10,'Net Pay (A-B): '+str(net_pay),ln=0,align='L')
            pdf.ln(5)
            pdf.output(emp_id+".pdf")
        
# Employee page creation
class Employee:
    def __init__(self):        
        global EE_frame
        EE_frame=Frame(M_win, relief='raised',bg='#65A8E1')
        for i in range(0,3):
             EE_frame.columnconfigure(i, weight=1)
             EE_frame.rowconfigure(i, weight=1)       
        self.enroll_btn=Button(EE_frame, text='Attendance View', font=('Gadugi',20), bg='magenta', fg='white', command=self.atten).grid(row=0,column=0, padx=10, pady=5, sticky=W+E)
        self.leave_btn=Button(EE_frame, text='Apply Leave', font=('Gadugi',20), bg='magenta', fg='white').grid(row=0,column=1, padx=10, pady=5, sticky=E+W)
        self.atten_btn=Button(EE_frame, text='Profile', font=('Gadugi',20), bg='magenta', fg='white').grid(row=0,column=2, padx=10, pady=5, sticky=W+E)
        EE_frame.pack(fill='both', expand='yes')
        
    def atten(self):
        EE_frame.destroy()
        Attendance()
    def leave(self):
        EE_frame.destroy()
        #Leave()
        
# Employee attendance clock-in and clock-out page
class Attendance:
    def __init__(self):        
        global Att_frame        
        Att_frame=Frame(M_win, bg='#dadada')
        global mo_yr
        mo_yr=strftime("%b %Y", localtime()) # month and year
        #mo_yr='Apr 2023' # replece for month and year
        home_btn=Button(Att_frame, text='Home', font=('Century Schoolbook',12,'bold'), bg='#dadada', justify=LEFT, command=self.emp_home).grid(row=1, column=2, sticky=W+E)
        mo_yr_bal=Label(Att_frame, text=mo_yr, font=('Century Schoolbook',12,'bold'), bg='#dadada', justify=LEFT).grid(row=1, column=3, sticky=W+E)
    #----Attendance view-----   
        year=int(strftime("%Y", localtime())) # used for attd label
        month=int(strftime("%m", localtime())) # used for attd label
        dt=int(strftime("%d", localtime())) # used to check and update absent upto current date
        if month<10:
            month_str='0'+str(month)
        else:
            month_str=str(month)
        first_weekday_of_mo=calendar.monthrange(year,month)[0]+2
        no_of_weeks_in_mo=math.ceil((calendar.monthrange(year,month)[1]+calendar.monthrange(year,month)[0])/7)
        no_of_days_in_mo=calendar.monthrange(year,month)[1]        
        days=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']       
        day_one=1
        shift='Second shift:\n14:00:00 to 23:00:00'
        self.clk_in=""
        global status_dict
        status_dict={}
        conn=mc.connect(host="localhost", user="root", password="KMDdharan@25", database="employee_db")
        cur=conn.cursor()
        cur.execute("SELECT clk_date, status FROM attendance WHERE Employee_ID ='"+e_empy_id+"' AND mo_yr='"+mo_yr+"'")
        rec=cur.fetchall()
        cur.close()
        conn.close()
        for y in range(1,32):
            for row in rec:
                date=row[0]
                key=int(date[0:2])
                value=str(row[1])
                if y==key and value=='Present':
                    status_dict[y]=[value+'\n','#7ae767']
                    break
                elif y==key and value=='Absent':
                    status_dict[y]=[value+'\n','#f03757']
                    break
                elif y==key and value=='Off day':
                    status_dict[y]=[value+'\n','#ffbfff']
                    break
            else: 
                status_dict[y]=['NA\n','white']
        #____check and update absent___
        for x in range(1,dt):
            state=status_dict[x][0]
            if state=='NA\n' and x<dt:
                status='Absent'
                status_dict[x]=['Absent\n','#f03757']
                if x<10:
                    d='0'+str(x)
                    clk_dt=d+"-"+month_str+"-"+str(year)
                else:
                    d=str(x)
                    clk_dt=d+"-"+month_str+"-"+str(year) 
                try:
                    conn=mc.connect(host="localhost", user="root", password="KMDdharan@25", database="employee_db")
                    cur=conn.cursor()
                    cur.execute("INSERT INTO attendance(employee_id, employee_name, clk_date, mo_yr, status) value('"+e_empy_id+"', '"+emp_username+"' , '"+clk_dt+"', '"+mo_yr+"', 'Absent')")
                    cur.close()
                    conn.close()
                except:
                    pass                    
        #______row configuration_____
        for rc in range(0,12): 
            Att_frame.rowconfigure(rc,weight=1)
        #______column configuration_____
        for cc in range(0,11):
            Att_frame.columnconfigure(cc, weight=1)    
        #_____Day label___
        i=0
        for d in range(2,9):
            lab=Label(Att_frame, text=days[i], font=('Times',14,'bold'), bg='#ceceff', borderwidth=1, relief="solid")
            lab.grid(row=3, column=d, sticky=W+E)
            i+=1    
        #_____Label creation 1st week null date_____
        for r in range(4,5):
            for c in range(2,first_weekday_of_mo):
                label=Label(Att_frame, text="\n\n\n", font=('Times',14,), bg='white', borderwidth=1, relief="solid", justify=LEFT)
                label.grid(row=r, column=c, sticky=W+E)       
        #_____Label creation 1st week start date to last week end date_____
        for r in range(4,no_of_weeks_in_mo+3):
            for c in range(first_weekday_of_mo,9):
                status=status_dict[day_one][0]
                BG=status_dict[day_one][1]
                label=Label(Att_frame, text="Date: "+str(day_one)+"\n"+status+shift, font=('Times',12), bg=BG, borderwidth=1, relief="solid", justify=LEFT)
                label.grid(row=r, column=c, sticky=W+E)
                first_weekday_of_mo=2
                day_one+=1                
        #__Label for last weekday___    
        for r in range(no_of_weeks_in_mo+3,no_of_weeks_in_mo+4):            
            for c in range(2,no_of_days_in_mo-day_one+3):
                status=status_dict[day_one][0]
                BG=status_dict[day_one][1]
                label=Label(Att_frame, text="Date: "+str(day_one)+"\n"+status+shift, font=('Times',12), bg=BG, borderwidth=1, relief="solid", justify=LEFT)
                label.grid(row=r, column=c, sticky=W+E)
                first_weekday_of_mo=2
                day_one+=1
        self.clk_in_btn=Button(Att_frame, text='Clock-in', font=('Century Schoolbook',10,'bold'), fg='black', bg='#59ffff', command=self.clkin)
        self.clk_in_btn.grid(row=1, column=7, sticky=W+E)  
        self.clk_out_btn=Button(Att_frame, text='Clock-out',font=('Century Schoolbook',10,'bold'), fg='black', bg='#59ffff', command=self.clkout)
        self.clk_out_btn.grid(row=1, column=8, sticky=W+E)        
        Att_frame.pack(fill='both', expand='yes')
        
    def clkin(self,*args):
        self.clk_in=dt.strptime(strftime("%H:%M:%S", localtime()),"%H:%M:%S").time()
        clk_in_str=str(self.clk_in)
        self.clk_in_btn['text']=clk_in_str
        self.clk_in_btn['state']='disabled'
        att_date=strftime("%d-%m-%Y",localtime())
        conn=mc.connect(host="localhost", user="root", password="KMDdharan@25", database="employee_db")
        cur=conn.cursor()
        cur.execute("INSERT INTO attendance(Employee_ID, Employee_Name, clk_date, mo_yr, clock_in) values('"+e_empy_id+"','"+emp_username+"', '"+att_date+"', '"+mo_yr+"', '"+clk_in_str+"')")
        cur.close()
        conn.close()        
        
    def clkout(self):
        clk_out=dt.strptime(strftime("%H:%M:%S", localtime()),"%H:%M:%S").time()
        clk_out_str=str(clk_out)
        self.clk_out_btn['text']=clk_out
        att_date=strftime("%d-%m-%Y",localtime())
        if self.clk_in=="":
            status='Absent'
        elif self.clk_in<=dt.strptime("09:00:00","%H:%M:%S").time() and clk_out>=dt.strptime("18:00:00", "%H:%M:%S").time():            
            status='Present'
        else:
            status="Absent"
        conn=mc.connect(host="localhost", user="root", password="KMDdharan@25", database="employee_db")
        cur=conn.cursor()
        cur.execute("UPDATE attendance SET clock_out='"+clk_out_str+"', status='"+status+"' WHERE employee_id='"+e_empy_id+"' and clk_date='"+att_date+"'")
        cur.close()
        conn.close()
        
    def emp_home(self):
        Att_frame.destroy()
        Employee()      
        
# Leave apply: #WIP

# Logout page creation
class Logout:
    def __init__(self):        
        self.Log_frame=Frame(M_win, bg='white', bd=2, height='5')
        self.label=Label(self.Log_frame, text=emp_username, font=('Times',14,'bold'), bg='white' ).grid(row=0, column=0, sticky=W)
        self.logout_btn=Button(self.Log_frame, text='Logout',bg='white', fg='#ff1717', font=('Arial',8,'bold'), command=self.logout).place(relx = 1, rely=0, x =-2, y = 2, anchor = NE)
        self.Log_frame.pack(fill='x', side='top')     
    def logout(self):
        for frm in M_win.winfo_children():
            frm.destroy()
        AppTitle()
        Login()

AppTitle()      
Login()
M_win.mainloop()

