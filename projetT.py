from tkinter import *
from tkinter import ttk
import pymysql

class student:
    #-----------3mltil fenetre------
    def __init__(self,root):#constructeur
        self.root= root
        self.root.geometry('1350x690+1+1')
        self.root.title('Programme Gestion des TP')
        self.root.configure(background="silver")
        self.root.resizable(False,False)#bch mtet7kmch bl 3orth o ertife3
        title=Label(self.root,
                text="[Gestion Des Notes Des TP]",background="#1AAECB",
                font=("monosapce",14,"bold"),fg="white"
                )
        title.pack(fill=X)#yani yt3aba fl  3orth lkol
        #---------variable---
        self.id_var=StringVar()
        self.nomP_var=StringVar()
        self.class_var=StringVar()
        self.group_var=StringVar()
        self.del_var=StringVar()
        self.se_var=StringVar()
        self.tp1_var=StringVar()
        self.tp2_var=StringVar()
        self.tp3_var=StringVar()
        self.tp4_var=StringVar()
        self.tp5_var=StringVar()
        self.tp6_var=StringVar()
        self.rtp_var=StringVar()
        
        
    #--------------adwet il t7kom----------
    
        Manage_Frame = Frame(self.root,bg="white")
        Manage_Frame.place(x=1137,y=30,width=210,height=400)
        lbl_id= Label(Manage_Frame,text="Num Serie",bg="white")
        lbl_id.pack()
        id_entry=Entry(Manage_Frame,textvariable=self.id_var,bd="2")
        id_entry.pack()
        lbl_namep= Label(Manage_Frame,text="Nom et Prenom D'etudiant",bg="white")
        lbl_namep.pack()
        namep_entry=Entry(Manage_Frame,textvariable=self.nomP_var,bd="2")
        namep_entry.pack()
        lbl_class= Label(Manage_Frame,text="Classe D'etudiant",bg="white")
        lbl_class.pack()
        class_entry=Entry(Manage_Frame,textvariable=self.class_var,bd="2")
        class_entry.pack()
        lbl_gp= Label(Manage_Frame,text="Groupe D'etudiant",bg="white")
        lbl_gp.pack()
        lbl_tp= Label(Manage_Frame,text="Les TP",bg="white")
        lbl_tp.pack()
        nametp1_entry=Entry(Manage_Frame,textvariable=self.tp1_var,bd="2")
        nametp1_entry.pack()
        nametp2_entry=Entry(Manage_Frame,textvariable=self.tp2_var,bd="2")
        nametp2_entry.pack()
        nametp3_entry=Entry(Manage_Frame,textvariable=self.tp3_var,bd="2")
        nametp3_entry.pack()
        nametp4_entry=Entry(Manage_Frame,textvariable=self.tp4_var,bd="2")
        nametp4_entry.pack()
        nametp5_entry=Entry(Manage_Frame,textvariable=self.tp5_var,bd="2")
        nametp5_entry.pack()
        nametp6_entry=Entry(Manage_Frame,textvariable=self.tp6_var,bd="2")
        nametp6_entry.pack()
        lbl_rtp= Label(Manage_Frame,text="Moyenne general TP",bg="white")
        lbl_rtp.pack()
        namertp_entry=Entry(Manage_Frame,textvariable=self.rtp_var,bd="2")
        namertp_entry.pack()
        combo_gp=ttk.Combobox(Manage_Frame,textvariable=self.group_var)
        combo_gp['value']=('Group1','Group2')
        combo_gp.pack()
        lbl_delete= Label(Manage_Frame,text="Supprimer un etudiant avec le nom",fg="red",bg="white")
        lbl_delete.pack()
        delete_entry=Entry(Manage_Frame,textvariable=self.del_var,bd="2")
        delete_entry.pack()
        #-----------il buttonet----
        btn_frm=Frame(self.root,bg="white")
        btn_frm.place(x=1137,y=435,width=210,height=253)
        title1=Label(btn_frm,text="Panneau de contrôle",font=('Deco',14),fg="white",bg="#2980B9")
        title1.pack(fill=X)
        
        add_btn=Button(btn_frm ,text="ajouter un etudiant",bg="#85929E",fg='white',command=self.add_Student)#lel ajout mte3 DB
        add_btn.place(x=33,y=39,width='150',height='30')
        
        del_btn=Button(btn_frm ,text="supprimer un etudiant",bg="#85929E",fg='white',command=self.delete)
        del_btn.place(x=33,y=80,width='150',height='30')
        
        update_btn=Button(btn_frm ,text="modifier un etudiant",bg="#85929E",fg='white',command=self.update)
        update_btn.place(x=33,y=115,width='150',height='30')
        
        clear_btn=Button(btn_frm ,text="vider les champs",bg="#85929E",fg='white',command=self.clear)
        clear_btn.place(x=33,y=150,width='150',height='30')
        
        exit_btn=Button(btn_frm ,text="Fermer le programme ",bg="#85929E",fg='white',command=root.quit)
        exit_btn.place(x=33,y=185,width='150',height='30')
        calc_btn=Button(btn_frm ,text="calcul Moyenne ",bg="#85929E",fg='white',command=self.calc)
        calc_btn.place(x=33,y=220,width='150',height='30')
        
        #-------il recherche--------
        search_frm=Frame(self.root,bg='white')
        search_frm.place(x=1,y=31,width=1134,height=50)
        
        lbl_search=Label(search_frm,text='Recherche :',bg='white')
        lbl_search.place(x=34,y=12)
        
        combo_search=ttk.Combobox(search_frm,)
        combo_search['value']=('Nom et Prenom','id','Class')
        combo_search.place(x=100,y=12)
        
        search_Entry=Entry(search_frm,textvariable=self.se_var,bd=3)
        search_Entry.place(x=250,y=12)
        
        se_btn=Button(search_frm,text='Recherche',bg='#3498DB',fg='white',command=self.search)
        se_btn.place(x=1034,y=12)
        #------détails-------
        dietals_frm=Frame(self.root,bg='#F2F4F4')
        dietals_frm.place(x=1,y=82,width=1134,height=605)
        #---scrool---
        scroll_x=Scrollbar(dietals_frm,orient=HORIZONTAL)
        scroll_y=Scrollbar(dietals_frm,orient=VERTICAL)
        #----------treeview----
        self.student_tab=ttk.Treeview(dietals_frm,
        columns=('id','Nom et Prenom','Classe','Groupe','tp1','tp2','tp3','tp4','tp5','tp6','rtp'),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set)
        self.student_tab.place(x=18,y=1,width=1130,height=580)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=LEFT,fill=Y)
        #-----tzid 3anwin il tab----- 
        self.student_tab['show']='headings'
        self.student_tab.heading('id',text='id')
        self.student_tab.heading('Nom et Prenom',text='Nom et Prenom')
        self.student_tab.heading('Classe',text='Classe')
        self.student_tab.heading('Groupe',text='Groupe')
        self.student_tab.heading('tp1',text='TP1')
        self.student_tab.heading('tp2',text='TP2')
        self.student_tab.heading('tp3',text='TP3')
        self.student_tab.heading('tp4',text='TP4')
        self.student_tab.heading('tp5',text='TP5')
        self.student_tab.heading('tp6',text='TP6')
        self.student_tab.heading('rtp',text='Moyenne TP')
        self.student_tab.column('id',width=102)
        self.student_tab.column('Nom et Prenom',width=102)
        self.student_tab.column('Classe',width=102)
        self.student_tab.column('Groupe',width=102)
        self.student_tab.column('tp1',width=102)
        self.student_tab.column('tp2',width=102)
        self.student_tab.column('tp3',width=102)
        self.student_tab.column('tp4',width=102)
        self.student_tab.column('tp5',width=102)
        self.student_tab.column('tp6',width=102)
        self.student_tab.column('rtp',width=102)
        self.student_tab.bind("<ButtonRelease-1>",self.get_cursor)#bind hya evenment al na9er 
        #----------connecet+add-----
        self.fetch_all()
    def add_Student(self):
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='stud'
            )
        cur = con.cursor()
        query = "INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data = (
            self.id_var.get(),
            self.nomP_var.get(),
            self.class_var.get(),
            self.group_var.get(),
            self.tp1_var.get(),
            self.tp2_var.get(),
            self.tp3_var.get(),
            self.tp4_var.get(),
            self.tp5_var.get(),
            self.tp6_var.get(),
            self.rtp_var.get(),
            )
        cur.execute(query, data)
        con.commit()
        self.fetch_all()# bch mnokdh nsker o nhel bch ytzed etudiant
        self.clear()
        con.close()
        
        
    def fetch_all(self):
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='stud'
            )
        cur = con.cursor()
        cur.execute('select * from student')
        rows =cur.fetchall()# jbna formation lkol fi rows
        if len (rows) !=0:
            self.student_tab.delete(*self.student_tab.get_children())#5thina mo3tyet lkol
            for row in rows :
                self.student_tab.insert("",END,value=row)
            con.commit()
        con.close()
    def delete(self):
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='stud'
            )
        cur = con.cursor()
        cur.execute('delete from student where name=%s',self.del_var.get())
        con.commit()
        self.fetch_all()
        con.close()
        
    def clear(self):
        self.id_var.set('')
        self.nomP_var.set('')
        self.class_var.set('')
        self.group_var.set('')
        self.tp1_var.set('')
        self.tp2_var.set('')
        self.tp3_var.set('')
        self.tp4_var.set('')
        self.tp5_var.set('')
        self.tp6_var.set('')
        self.rtp_var.set('')
        
        
    def get_cursor(self,ev):
        cursor_row=self.student_tab.focus()#il tab focus wktli tenzl alih
        contents  =self.student_tab.item(cursor_row)#il information ili nzlt alihom fi var contents
        row=contents['values']#5outh il values mte3 il contents
        self.id_var.set(row[0])
        self.nomP_var.set(row[1])
        self.class_var.set(row[2])
        self.group_var.set(row[3])
        self.tp1_var.set(row[4])
        self.tp2_var.set(row[5])
        self.tp3_var.set(row[6])
        self.tp4_var.set(row[7])
        self.tp5_var.set(row[8])
        self.tp6_var.set(row[9])
        self.rtp_var.set(row[10])
        
        
    def update(self):
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='stud'
            )
        cur = con.cursor()
        query = "UPDATE student SET name=%s, class=%s, groupe=%s, tp1=%s, tp2=%s, tp3=%s, tp4=%s, tp5=%s, tp6=%s, moytp=%s WHERE id=%s"
        data = (
            self.nomP_var.get(),
            self.class_var.get(),
            self.group_var.get(),
            self.tp1_var.get(),
            self.tp2_var.get(),
            self.tp3_var.get(),
            self.tp4_var.get(),
            self.tp5_var.get(),
            self.tp6_var.get(),
            self.rtp_var.get(),
            self.id_var.get()
        )
        cur.execute(query, data)
        con.commit()
        self.fetch_all()  # Refresh the student records
        self.clear()  # Clear the input fields
        con.close()

    def search(self):
        con = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='stud'
    )
        cur = con.cursor()
        search_column = str(self.se_var.get())
        search_value = str(self.se_var.get())
        query = f"SELECT * FROM student WHERE {search_column} LIKE '%{search_value}%'"
        cur.execute(query)
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_tab.delete(*self.student_tab.get_children())
            for row in rows:
                self.student_tab.insert("", END, value=row)
        con.close()
        
    def calc(self):
        tp1 = float(self.tp1_var.get())
        tp2 = float(self.tp2_var.get())
        tp3 = float(self.tp3_var.get())
        tp4 = float(self.tp4_var.get())
        tp5 = float(self.tp5_var.get())
        tp6 = float(self.tp6_var.get())

        average = (tp1 + tp2 + tp3 + tp4 + tp5 + tp6) / 6
        self.rtp_var.set(str(average))


        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
root=Tk()
ob=student(root)#bch yothher il class fi west il root
root.mainloop()