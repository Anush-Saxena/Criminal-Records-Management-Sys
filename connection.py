import mysql.connector as msc
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import re
def mw():
     def c20():
          global b
          if b==0:
               b+=1; c2()
          else:
               messagebox.showerror(""," Another Window In Use ")
     def c2():# new record  COMPLETED
          def co21():
               v250=op250.get().strip()
               v251=op251.get().strip()
               v252=op252.get().strip()
               a=t22.get().strip()
               if len(a)!=0 and len(t23.get())!=0 and len(t24.get())!=0 and len(v250)!=0 and len(v251)!=0 and len(v252)!=0 and len(t26.get())!=0 :
                    if a.isdigit()==True:
                         if v250 in l250 and v251 in l251 and v252 in l252:
                              con=msc.connect(user='root',host='localhost',passwd="#im@No.1",database='CRS')
                              if con.is_connected()==True:
                                   date=v250+'-'+v251+'-'+v252
                                   global j2
                                   q21="select crno from rec"
                                   cur=con.cursor()
                                   cur.execute(q21)
                                   l=cur.fetchall()
                                   crno=int(a)
                                   for i in l:
                                        if i[0]==crno:
                                             j2=1
                                             messagebox.showerror(""," Criminal Number Occupied ")
                                             break
                                   if j2!=1:
                                        q22="insert into rec values({},'{}','{}','{}','{}')".format(crno,t23.get(),t24.get(),date,t26.get())
                                        cur.execute(q22)
                                        con.commit()
                                        con.close()
                                        t22.delete(0,'end')
                                        t23.delete(0,'end')
                                        t24.delete(0,'end')
                                        op250.set("DD")
                                        op251.set("MM")
                                        op252.set("YYYY")
                                        t26.delete(0,'end')
                                        messagebox.showinfo("","Data Has Been Uploaded")
                              else:
                                   messagebox.showerror("","  ERROR! Please Check Connection  ")
                         else:
                              messagebox.showerror("","Enter Valid Arrest Date")
                              op250.set("DD")
                              op251.set("MM")
                              op252.set("YYYY")
                    else:
                         messagebox.showerror("","Enter Valid Criminal Number")
                         t22.delete(0,'end')
               else:
                    messagebox.showerror(""," Enter All Details ")
          def co22():
               global b
               b=0
               cont.destroy()
          cont=Tk()
          cont.geometry("800x785+100+4")
          cont.configure(bg="red")
          cont.overrideredirect(True)
          c31=Label(cont,width=20,text="",bg="black",font="algerian 120")
          c31.place(x=0,y=0)
          #
          l21=Label(cont,width=25,text=" ENTERING  NEW  RECORDS ",bg="black",fg="cyan",font="cambria 35 bold underline")
          #
          l22=Label(cont,width=15,text="ENTER CR.NO. ->",bg="red",fg="white",font="courier 20 bold")
          l23=Label(cont,width=15,text="ENTER NAME   ->",bg="red",fg="white",font="courier 20 bold")
          l24=Label(cont,width=15,text="ENTER CRIME  ->",bg="red",fg="white",font="courier 20 bold")
          l25=Label(cont,width=15,text="ENTER D.O.A. ->",bg="red",fg="white",font="courier 20 bold")
          l26=Label(cont,width=15,text="ENTER TENURE ->",bg="red",fg="white",font="courier 20 bold")
          #
          t22=Entry(cont,width=11,bg="red",fg="white",font="courier 25 bold",bd=4,highlightcolor="yellow",command=None)
          t23=Entry(cont,width=11,bg="red",fg="white",font="courier 25 bold",bd=4)
          t24=Entry(cont,width=11,bg="red",fg="white",font="courier 25 bold",bd=4)
          ####
          l250=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
          s250=StringVar()
          op250=Combobox(cont,width="3",textvariable=s250,values=l250,foreground="red",font="comic 15 bold")
          op250.set("DD")
          l251=["JAN","FEB","MAR","APR","MAY","JUNE","JUL","AUG","SEP","OCT","NOV","DEC"]
          s251=StringVar()
          op251=Combobox(cont,width="5",textvariable=s251,values=l251,foreground="red",font="comic 15 bold")
          op251.set("MM")
          l252=["1990","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021"]
          s252=StringVar()
          op252=Combobox(cont,width="5",textvariable=s252,values=l252,foreground="red",font="comic 15 bold")
          op252.set("YYYY")
          ####
          t26=Entry(cont,width=11,bg="red",fg="white",font="courier 25 bold",bd=4)
          #
          b21=Button(cont,width=7,text=' ♦  ADD ',command=co21,bg="green",activebackground="red",activeforeground="white",font="comic 15 bold",bd=5)
          b22=Button(cont,width=5,text='  EXIT  ',command=co22,font="comic 15 bold",bg="white",bd=5)
          b21.place(x=513,y=720)
          b22.place(x=640,y=720)
          #
          l21.place(x=55,y=60)
          #
          l22.place(x=50,y=235)
          t22.place(x=500,y=235)
          #
          l23.place(x=50,y=335)
          t23.place(x=500,y=335)
          #
          l24.place(x=50,y=435)
          t24.place(x=500,y=435)
          #
          l25.place(x=50,y=535)
          op250.place(x=500,y=540)
          op251.place(x=565,y=540)
          op252.place(x=653,y=540)
          #
          l26.place(x=50,y=635)
          t26.place(x=500,y=635)
          cont.mainloop()
     ########################################
     def c30():
          global c
          if c==0:
               c+=1; c3()
          else:
               messagebox.showerror(""," Another Window In Use ")
     def c3(): #update COMPLETED NOT SQL
          def co31():
               v350=op350.get().strip()
               v351=op351.get().strip()
               v352=op352.get().strip()
               a=t32.get().strip()
               if len(a)!=0 and len(t33.get())!=0 and len(t34.get())!=0 and len(v350)!=0 and len(v351)!=0 and len(v352)!=0 and len(t36.get())!=0:
                    if a.isdigit()==True:
                         if v350 in l350 and v351 in l351 and v352 in l352:
                              con=msc.connect(user='root',host='localhost',passwd="#im@No.1",database='CRS')
                              if con.is_connected()==True:
                                   date=v350+'-'+v351+'-'+v352
                                   global j3
                                   q31="select crno from rec"
                                   cur=con.cursor()
                                   cur.execute(q31)
                                   l=cur.fetchall()
                                   crno=int(t32.get())
                                   for i in l:
                                        if i[0]==crno:
                                             j3=1
                                             break
                                   if j3==1:
                                        q32="update rec set name='{}',crime='{}',doa='{}',tenure='{}' where crno={}".format(t33.get(),t34.get(),date,t36.get(),int(t32.get()))
                                        cur.execute(q32)
                                        con.commit()
                                        con.close()
                                        t32.delete(0,'end')
                                        t33.delete(0,'end')
                                        t34.delete(0,'end')
                                        op350.set("DD")
                                        op351.set("MM")
                                        op352.set("YYYY")
                                        t36.delete(0,'end')
                                        messagebox.showinfo("","Data Has Been Updated")
                                   else:
                                        messagebox.showerror(""," Criminal Number Does Not Exists ")
                              else:
                                   messagebox.showerror("","  ERROR! Please Check Connection  ")
                         else:
                              messagebox.showerror("","Enter Valid Arrest Date")
                              op350.set("DD")
                              op351.set("MM")
                              op352.set("YYYY")
                    else:
                         messagebox.showerror("","Enter Valid Criminal Number")
                         t32.delete(0,'end')
               else:
                    messagebox.showerror(""," Enter All Details ")
          def co32():
               global c
               c=0
               cont.destroy()
          def co33():
               sm=0
               a=t32.get()
               a=a.strip()
               if a.isdigit()==True:
                    con=msc.connect(user='root',host='localhost',passwd="#im@No.1",database='CRS')
                    q33="select crno from rec"
                    cur=con.cursor()
                    cur.execute(q33)
                    l=cur.fetchall()
                    crno=int(t32.get())
                    for cr in l:
                         if cr[0]==crno:
                              sm=1
                              messagebox.showinfo(""," Record Present ")
                              break
                    if sm!=1:
                         messagebox.showerror(""," Record Does Not Exists ")
               else:
                    messagebox.showerror(""," Enter Valid Criminal Number ")
          cont=Tk()
          cont.geometry("815x770+80+50")
          cont.configure(bg="red")
          cont.overrideredirect(True)
          c31=Label(cont,width=50,text="",bg="black",font="algerian 160")
          c31.place(x=0,y=0)
          #
          l31=Label(cont,width=22,text=" UPDATING RECORDS ",bg="black",fg="cyan",font="cambria 35 bold underline")
          #
          l32=Label(cont,width=25,text="ENTER CR.NO. TO UPDATE ->",bg="white",fg="black",font="courier 23 bold")
          #
          l33=Label(cont,width=15,text="ENTER NAME   ->",bg="red",fg="white",font="courier 20 bold")
          l34=Label(cont,width=15,text="ENTER CRIME  ->",bg="red",fg="white",font="courier 20 bold")
          l35=Label(cont,width=15,text="ENTER D.O.A. ->",bg="red",fg="white",font="courier 20 bold")
          l36=Label(cont,width=15,text="ENTER TENURE ->",bg="red",fg="white",font="courier 20 bold")
          #
          t32=Entry(cont,width=11,bg="white",fg="black",font="courier 24",bd='4')
          #
          t33=Entry(cont,width=11,bg="red",fg="white",font="courier 25 bold",bd=4)
          t34=Entry(cont,width=11,bg="red",fg="white",font="courier 25 bold",bd=4)
          ####
          l350=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
          s350=StringVar()
          op350=Combobox(cont,width="3",textvariable=s350,values=l350,foreground="red",font="comic 15 bold")
          op350.set("DD")
          l351=["JAN","FEB","MAR","APR","MAY","JUNE","JUL","AUG","SEP","OCT","NOV","DEC"]
          s351=StringVar()
          op351=Combobox(cont,width="5",textvariable=s351,values=l351,foreground="red",font="comic 15 bold")
          op351.set("MM")
          l352=["1990","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021"]
          s352=StringVar()
          op352=Combobox(cont,width="5",textvariable=s352,values=l352,foreground="red",font="comic 15 bold")
          op352.set("YYYY")
          ####
          t36=Entry(cont,width=11,bg="red",fg="white",font="courier 25 bold",bd=4)
          #
          b31=Button(cont,width=10,text='♦   UPDATE',command=co31,bg="green",fg="white",activebackground="red",activeforeground="white",font="comic 15 bold",bd=5)
          b32=Button(cont,width=5,text='  EXIT  ',command=co32,font="comic 15 bold",bg="white",bd=5)
          b33=Button(cont,width=8,text=" SEARCH ",command=co33,bg="green",fg="white",activebackground="red",activeforeground="white",font="comic 15 bold",bd=5)
          b31.place(x=590,y=690)
          b32.place(x=479,y=690)
          b33.place(x=687,y=177)
          #
          l31.place(x=105,y=65)
          #
          l32.place(x=20,y=180)
          t32.place(x=450,y=177)
          #
          l33.place(x=60,y=300)
          t33.place(x=485,y=299)
          #
          l34.place(x=60,y=400)
          t34.place(x=485,y=399)
          #
          l35.place(x=60,y=500)
          op350.place(x=485,y=505)
          op351.place(x=551,y=505)
          op352.place(x=639,y=505)
          #
          l36.place(x=60,y=600)
          t36.place(x=485,y=599)
          cont.mainloop()
     ############################################
     def c40():
          global d
          if d==0:
               d+=1; c4()
          else:
               messagebox.showerror(""," Another Window In Use ")
     def c4(): # search a record
          def co41():
               if len(t42.get())!=0:
                    a=t42.get().strip()
                    if a.isdigit()==True:
                         con=msc.connect(user="root",host="localhost",passwd="#im@No.1",database="CRS")
                         a=int(a)
                         if con.is_connected()==True:
                              q41="select crno from rec"
                              cur=con.cursor()
                              cur.execute(q41)
                              l=cur.fetchall()
                              for x in l:
                                   if x[0]==a:
                                        global j4
                                        j4=1
                                        q42="select * from rec where crno={}".format(a)
                                        cur.execute(q42)
                                        l=cur.fetchall()
                                        root=Tk()
                                        root.geometry("774x200+722+100")
                                        root.configure(bg="black")
                                        ch1=Label(root,width=50,pady=-2,text="- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -",bg="black",fg='white',font="'' 20")
                                        ch1.place(x=0,y=25)
                                        #
                                        l10=Label(root,width=7,text="CR.NO.",bg="black",fg="white",font="courier 17 bold") 
                                        l11=Label(root,width=14,text="NAME",bg="black",fg="white",font="courier 17 bold")
                                        l12=Label(root,width=9,text="CRIME",bg="black",fg="white",font="courier 17 bold")
                                        l13=Label(root,width=12,text="D.O.A",bg="black",fg="white",font="courier 17 bold")
                                        l14=Label(root,width=15,text="TENURE ",bg="black",fg="white",font="courier 17 bold")
                                        l10.place(x=0,y=0)
                                        l11.place(x=93,y=0)
                                        l12.place(x=282,y=0)
                                        l13.place(x=411,y=0)
                                        l14.place(x=576,y=0)
                                        #
                                        i=l[0]
                                        l20=i[0]
                                        p=i[1].split(" ")
                                        l21=''
                                        for tn in p:
                                             l21+=tn+'\n'
                                        q=i[2].split(' ')
                                        l22='\n'
                                        for tn in q:
                                             l22+=tn+'\n'
                                        l23=i[3]
                                        l24=''
                                        s=i[4].split(' ')
                                        for tn in range(len(s)):
                                             if len(s)>=4 and tn%2==0:
                                                  l24+=s[tn]+" "+s[tn+1]+"\n"
                                             else:
                                                  l24+=s[tn]+"\n"
                                        b=l24.split('\n')
                                        rl20=Label(root,width=7,text=l20,bg="black",fg="white",font="courier 16 bold")
                                        rl21=Label(root,width=15,height=3,text=l21,bg="black",fg="white",font="courier 16 bold")
                                        rl22=Label(root,width=10,height=3,text=l22,bg="black",fg="white",font="courier 16 bold")
                                        rl23=Label(root,width=13,text=l23,bg="black",fg="white",font="courier 16 bold")
                                        rl20.place(x=0,y=74)
                                        rl21.place(x=93,y=66)
                                        rl22.place(x=282,y=66)
                                        rl23.place(x=411,y=74)
                                        if len(b)==2:
                                             l24=b[0]
                                             rl24=Label(root,width=16,text=l24,bg="black",fg="white",font="courier 16 bold")
                                             rl24.place(x=576,y=74)
                                        elif len(b)==3:
                                             l24=b[0]+'\n'+b[1]
                                             rl24=Label(root,width=16,height=2,text=l24,bg="black",fg="white",font="courier 16 bold")
                                             rl24.place(x=576,y=60)
                                        else:
                                             l24=b[0]+'\n'+b[1]+'\n'+b[2]
                                             rl24=Label(root,width=16,height=4,text=l24,bg="black",fg="white",font="courier 16 bold")
                                             rl24.place(x=576,y=50)
                                        #
                                        cv1=Label(root,width=0,text="",bg="white",font="'' 150 ")
                                        cv1.place(x=93,y=0)
                                        cv2=Label(root,width=0,text="",bg="white",font="'' 150 ")
                                        cv2.place(x=282,y=0)
                                        cv3=Label(root,width=0,text="",bg="white",font="'' 150 ")
                                        cv3.place(x=411,y=0)
                                        cv4=Label(root,width=0,text="",bg="white",font="'' 150 ")
                                        cv4.place(x=576,y=0)
                                        root.mainloop()
                                        break
                              if j4==0:
                                   messagebox.showinfo(""," Criminal Record Does Not Exists ")
                              j4=0
                         else:
                              messagebox.showerror("","  ERROR! Please Check Connection  ")
          def co42():
               global d
               d=0
               cont.destroy()
          cont=Tk()
          cont.geometry("620x350+110+100")
          cont.configure(bg="white")
          cont.overrideredirect(True)
          c41=Label(cont,width=10,text="",bg="black",font="'' 100")
          c41.place(x=0,y=0)
          #
          l41=Label(cont,width=20,text=" SEARCHING RECORDS ",bg="black",fg="cyan",font="cambria 35 bold underline")
          l42=Label(cont,width=31,text="ENTER CRIMINAL NUMBER TO SEARCH",bg="white",fg="green",font="courier 23 bold")
          l41.place(x=35,y=45)
          l42.place(x=10,y=180)
          #
          t42=Entry(cont,width=6,bg="black",fg="white",font="courier 23 bold",bd=5)
          t42.config(insertbackground="blue")
          t42.place(x=15,y=270)
          #
          b41=Button(cont,width=10,text='♦   SEARCH',command=co41,bg="green",activebackground="red",activeforeground="white",font="comic 15 bold",bd=5)
          b42=Button(cont,width=8,text='  CANCEL  ',command=co42,font="comic 15 bold",bg="white",bd=5)
          b41.place(x=163,y=270)
          b42.place(x=488,y=270)
          cont.mainloop()
     #########################################
     def c50():
          global e
          if e==0:
               e+=1; c5()
          else:
               messagebox.showerror(""," Another Window In Use ")
     def c5(): # delete   '''COMPLETED''' NOT SQL 
          def co51():
               global j5
               a=t51.get()
               if len(a)!=0 and a.strip().isdigit()==True:
                    a=a.strip()
                    a=int(a)
                    con=msc.connect(user='root',host="localhost",passwd="#im@No.1",database="CRS")
                    if con.is_connected()==True:
                         q50="select crno from rec"
                         cur=con.cursor()
                         cur.execute(q50)
                         l=cur.fetchall()
                         for y in l:
                              if y[0]==a:
                                   j5=1
                                   q51="delete from rec where crno={}".format(a)
                                   cur.execute(q51)
                                   con.commit()
                                   con.close()
                                   messagebox.showinfo(""," RECORD HAS BEEN DELETED ")
                                   break
                         if j5==0:
                              messagebox.showerror(""," Criminal Number Does Not Exists ")
                         j5=0
                    else:
                         messagebox.showerror("","  ERROR! Please Check Connection  ")
               else:
                    messagebox.showerror(""," Enter Correct Criminal Number ")
          def co52():
               global e
               e=0
               cont.destroy()
          cont=Tk()
          cont.geometry("650x230+100+100")
          cont.configure(bg="black")
          cont.overrideredirect(True)
          #
          l51=Label(cont,text="ENTER CR.NO. TO BE DELETED",bg="black",fg="White",font="courier 27 italic bold")
          l51.place(x=33,y=50)
          #
          t51=Entry(cont,width=6,bg="red",fg="white",font="courier 27 bold",bd=5)
          t51.place(x=38,y=140)
          #
          b51=Button(cont,width=6,text="DELETE",command=co51,font="courier 20 bold",fg="black",bg="white",bd=5)
          b52=Button(cont,width=6,text="CANCEL",command=co52,font="courier 20 bold",fg="black",bg="grey",bd=5)
          b51.place(x=225,y=137)
          b52.place(x=460,y=137)
          cont.mainloop()
     ###########################
     def c60():
          global f
          if f==0:
               f+=1
               c6()
          else:
               messagebox.showerror(""," Another Window In Use ")
     def c6(): #show all records
          def co61():
               global x,cnt1,cnt2,j6,f
               x,cnt1,cnt2,j6,f=1,0,6,0,0
               root.destroy()
          global cnt1,cnt2,x,j6,mainl
          con=msc.connect(user="root",host="localhost",passwd="#im@No.1",database="CRS")
          if con.is_connected()==True:
               q61="select * from rec"
               cur=con.cursor()
               cur.execute(q61)
               mainl=cur.fetchall()
               con.close()
               cnt,rest=len(mainl)//6,len(mainl)%6
               def disp():
                    r=0; l=[]
                    global cnt1,cnt2,x,j6,mainl
                    if cnt1>=0 and cnt2<=len(mainl):
                         for ml in range(cnt1,cnt2):
                              l.append(mainl[ml])
                         ch1=Label(root,width=50,pady=-2,text="- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -",bg="black",fg='white',font="'' 20")
                         ch1.place(x=0,y=25)
                         #
                         l10=Label(root,width=7,text="CR.NO.",bg="black",fg="white",font="courier 17 bold") 
                         l11=Label(root,width=14,text="NAME",bg="black",fg="white",font="courier 17 bold")
                         l12=Label(root,width=9,text="CRIME",bg="black",fg="white",font="courier 17 bold")
                         l13=Label(root,width=12,text="D.O.A",bg="black",fg="white",font="courier 17 bold")
                         l14=Label(root,width=15,text="TENURE ",bg="black",fg="white",font="courier 17 bold")
                         l10.place(x=52,y=0)
                         l11.place(x=133,y=0)
                         l12.place(x=322,y=0)
                         l13.place(x=451,y=0)
                         l14.place(x=616,y=0)
                         l00=cnt1
                         ltn=0
                         for i in l:
                              l00+=1
                              l20=i[0]            #no.
                              p=i[1].strip().split(" ")             #name
                              l21=''
                              for tn in p:
                                   l21+=tn+'\n'
                              q=i[2].strip()                      #crime
                              q=re.split(",| ",q)
                              l22=''
                              for tn in q:                                   
                                   l22+=tn+'\n'
                              l23=i[3]                 #doa
                              l24=''
                              s=i[4].strip()#tenure
                              s=re.split(",| ",s)
                              for tn in range(len(s)):
                                   if len(s)>=2:
                                        if tn%2==0:
                                             l24+=s[tn]+" "+s[tn+1]+"\n"
                              a=l24.split('\n')
                              rl00=Label(root,width=4,text=l00,bg="black",fg="white",font="courier 16 bold")
                              rl20=Label(root,width=7,text=l20,bg="black",fg="white",font="courier 16 bold")
                              rl21=Label(root,width=15,text=l21,bg="black",fg="white",font="courier 16 bold",height=3)
                              rl22=Label(root,width=10,text=l22,bg="black",fg="white",font="courier 16 bold")
                              rl23=Label(root,width=13,text=l23,bg="black",fg="white",font="courier 16 bold")
                              rl00.place(x=-8,y=85+r)
                              rl20.place(x=50,y=85+r)
                              rl21.place(x=133,y=74+r)
                              rl22.place(x=322,y=70+r)
                              rl23.place(x=451,y=84+r)
                              if len(a)==2:
                                   l24=a[0]
                                   rl24=Label(root,width=16,text=l24,bg="black",fg="white",font="courier 16 bold")
                                   rl24.place(x=616,y=84+r)
                              elif len(a)==3:
                                   l24=a[0]+'\n'+a[1]
                                   rl24=Label(root,width=16,height=2,text=l24,bg="black",fg="white",font="courier 16 bold")
                                   rl24.place(x=616,y=67+r)
                              else:
                                   l24=a[0]+'\n'+a[1]+'\n'+a[2]
                                   rl24=Label(root,width=16,height=4,text=l24,bg="black",fg="white",font="courier 16 bold")
                                   rl24.place(x=616,y=50+r)
                              #
                              ch2=Label(root,width=50,pady=-2,text="- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -",bg="black",fg='white',font="'' 20")
                              ch2.place(x=0,y=135+r)
                              cv0=Label(root,width=0,text="",bg="white",font="'' 150 ")
                              cv0.place(x=40,y=0+r)
                              cv1=Label(root,width=0,text="",bg="white",font="'' 150 ")
                              cv1.place(x=143,y=0+r)
                              cv2=Label(root,width=0,text="",bg="white",font="'' 150 ")
                              cv2.place(x=322,y=0+r)
                              cv3=Label(root,width=0,text="",bg="white",font="'' 150 ")
                              cv3.place(x=452,y=0+r)
                              cv4=Label(root,width=0,text="",bg="white",font="'' 150 ")
                              cv4.place(x=616,y=0+r)
                              r+=112
                              ldest=Label(root,width=15,bg='black',font="'' 60",relief='flat')
                              ldest.place(x=-19,y=728)
                              bdest=Button(root,width=5,text=' EXIT ',command=co61,height=0,font="comic 20 bold",bg="white",bd=5)
                              bdest.place(x=336,y=738)
                    if cnt1<0:
                         messagebox.showinfo(""," Already At First Page ")
                         cnt1+=6; cnt2+=6; x+=1
               def g_up():
                    global cnt1,cnt2,x,j6
                    if j6==0:
                         x-=1; cnt1-=6; cnt2-=6; disp()
                    if j6==1:
                         x-=1; cnt1-=6; cnt2-=rest; disp();  j6=0
               def g_dn():
                    global cnt1,cnt2,x,j6
                    if  x<cnt:
                         x+=1; cnt1+=6; cnt2+=6; disp()
                    elif rest!=0 and x==cnt:
                         x+=1; cnt1+=6; cnt2+=rest; disp(); j6=1
                    elif rest!=0 and x>cnt:
                         messagebox.showinfo(""," Already At Last Page ")
                    elif rest==0 and x==cnt:
                         messagebox.showinfo(""," Already At Last Page ")
               root=Tk()
               root.geometry("960x800+0+0")
               root.configure(bg="black")
               root.overrideredirect(True)
               #
               disp()
               lud=Label(root,height=100,bg="white",text="     ",font="'' 100")
               bup=Button(root,command=g_up,width=2,text="▲",font="'' 80 bold",fg='black',bg="white",activeforeground="white",activebackground="black",relief="flat")
               bdown=Button(root,command=g_dn,width=2,text="▼",font="'' 80 bold",fg='black',bg="white",activeforeground="white",activebackground="black",relief="flat")
               bup.place(x=831,y=165)
               bdown.place(x=831,y=460)
               lud.place(x=831,y=0)
               root.mainloop()
     def c70():
          global g
          if g==0:
               g+=1; c7()
          else:
               messagebox.showerror(""," Another Window In Use ")
     def c7():
          def co71():
               global j7
               if j7!=2:
                    con=msc.connect(user='root',host="localhost",passwd="#im@No.1",database="CRS")
                    q7="select pass from passwd"
                    cur=con.cursor()
                    cur.execute(q7)
                    l=cur.fetchone()
                    a,b=t72.get(),t73.get()
                    if len(a)!=0 and len(b)>=8 and len(b)<14:
                         if a==l[0]:
                              q71="update passwd set pass='{}' where sn=1;".format(b)
                              cur.execute(q71)
                              con.commit()
                              con.close()
                              messagebox.showinfo(""," Password Changed ")
                         else:
                              j7+=1
                              if j7==1:
                                   messagebox.showwarning(""," Wrong Password! You have only 1 attempt left.")
                              else:
                                   messagebox.showerror(""," Max attempts have been made ")
                    else:
                         messagebox.showerror(""," Fill Both Boxes, Password should be atleast 8 characters ")
               else:
                    messagebox.showerror(""," Max attempts have been made ")
          def co72():
               global g
               g=0
               cont.destroy()
          cont=Tk()
          cont.geometry("670x400+110+100")
          cont.configure(bg="white")
          cont.overrideredirect(True)
          c71=Label(cont,width=10,text="",bg="black",font="'' 100")
          c71.place(x=0,y=0)
          #
          l71=Label(cont,width=20,text=" UPDATING PASSWORD ",bg="black",fg="cyan",font="cambria 35 bold underline",bd=6)
          #
          l72=Label(cont,width=21,text="ENTER OLD PASSWORD ->",bg="white",fg="green",font="courier 23 bold")
          l73=Label(cont,width=21,text="ENTER NEW PASSWORD ->",bg="white",fg="green",font="courier 23 bold")
          l71.place(x=58,y=40)
          l72.place(x=8,y=180)
          l73.place(x=8,y=270)
          #
          t72=Entry(cont,width=12,bg="black",fg="white",font="courier 20 bold",bd=5,show='٭')
          t73=Entry(cont,width=12,bg="black",fg="white",font="courier 20 bold",bd=5,show='٭')
          t72.config(insertbackground='white')
          t73.config(insertbackground='white')
          t72.place(x=442,y=177)
          t73.place(x=442,y=267)
          #
          b71=Button(cont,width=10,text='♦   UPDATE',command=co71,bg="green",activebackground="red",activeforeground="white",font="comic 15 bold",bd=5)
          b72=Button(cont,width=8,text='  CANCEL  ',command=co72,font="comic 15 bold",bg="white",bd=5)
          b71.place(x=483,y=340)
          b72.place(x=10,y=340)
          cont.mainloop()
     global img
     mf=Tk()
     mf.geometry('1100x720+430+30')
     mf.title("PROJECT  ON  CRIMINAL  RECORDS")
     canvas = Canvas(mf, width =1100, height =740)      
     canvas.pack()      
     img = PhotoImage(file="Prison.gif")      
     canvas.create_image(0,0, anchor=NW, image=img)
     #
     l1=Label(mf,width=30,text="CRIMINAL  RECORDS OF INDIA",bg="grey",fg="black",font="times 35 underline bold")
     #
     b2=Button(mf,width=25,text='♦  ENTER  NEW  RECORDS ',command=c20,bg="white",activebackground="red",activeforeground="white",font="cambria 20 bold",bd=5)
     b3=Button(mf,width=25,text='♦  UPDATE  EXISTING  RECORDS',command=c30,bg="white",activebackground="red",activeforeground="white",font="cambria 20 bold",bd=5)
     b4=Button(mf,width=25,text='♦  SEARCH  EXISTING  RECORDS',command=c40,bg="white",activebackground="red",activeforeground="white",font="cambria 20 bold",bd=5)
     b5=Button(mf,width=25,text='♦  DELETE  EXISTING  RECORDS',command=c50,bg="white",activebackground="red",activeforeground="white",font="cambria 20 bold",bd=5)
     b6=Button(mf,width=25,text='♦  SHOW  ALL  RECORDS ',command=c60,bg="white",activebackground="red",activeforeground="white",font="cambria 20 bold",bd=5)
     b7=Button(mf,width=25,text='♦  CHANGE  THE  PASSWORD ',command=c70,bg="white",activebackground="red",activeforeground="white",font="cambria 20 bold",bd=5)
     #
     b8=Button(mf,width=7,text=' QUIT ',command=mf.destroy,bg="white",font="comic 20 bold",bd=5)
     #
     l1.place(x=120,y=35)
     #
     b2.place(x=55,y=190)
     b3.place(x=630,y=190)
     b4.place(x=85,y=330)
     b5.place(x=600,y=330)
     b6.place(x=123,y=470)
     b7.place(x=570,y=470)
     #
     b8.place(x=493,y=610)
     mf.mainloop()
def passw():
     con=msc.connect(user='root',host="localhost",passwd="#im@No.1",database="CRS")
     qmwc="select pass from passwd"
     cur=con.cursor()
     cur.execute(qmwc)
     l=cur.fetchone()
     con.close()
     if l[0]==t0.get():
          root.destroy()
          mw()
     else:
          messagebox.showerror(""," Wrong Password ")
          root.destroy()
b,c,d,e,f,g,j2,j3,j4,j5,j6,j7=0,0,0,0,0,0,0,0,0,0,0,0
mainl,cnt1,cnt2,x=[],0,6,1
root=Tk()
root.geometry("320x150+300+300")
root.config(bg="black")
l0=Label(root,width=16,text=" Enter Password ",bg="black",fg="white",font="courier 20 bold")
b0=Button(root,width=3,text=" OK ",pady=-1,command=passw,bg='white',fg="black",font="courier 17 bold",bd=4)
t0=Entry(root,width=12,bg='white',fg="black",font="courier 20 bold",bd=4,show='٭')
l0.place(x=2,y=10)
t0.place(x=20,y=70)
b0.place(x=240,y=67)
root.mainloop()
