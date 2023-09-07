import mysql.connector as con
import getpass
import os
loop ='y'
def insertval():
    global loop
    mydb= con.connect(user='root',password=pas,database='Customers')
    curs=mydb.cursor()
    curs.execute("CREATE TABLE IF NOT EXISTS Record(CID VARCHAR(5),phone_no VARCHAR(10),name VARCHAR(20),address VARCHAR(30),PRIMARY KEY(CID));")
    if mydb:
        print("Connection Established")
    else:
        print("connection falied")            
    mydb.commit()
    while loop =='y':
        curs.execute("SELECT CID FROM Record")
        dt =curs.fetchall()
        if dt:
            c=int(dt[-1][0]) +1
            cd= c
        else:
            cd=1
        pn=input("ENTER PHONE NUMBER:")
        if len(pn) !=10:
            print("ENTER A VALID PHONE NO.")
            break
        nm=input("ENTER FULL NAME:")
        add=input("ENTER ADDRESS:")
        sql ="INSERT INTO Record VALUES(%s,%s,%s,%s)"
        dat =(cd,pn,nm,add)
        curs.execute(sql,dat)
        print("")
        print("")
        print("")
        print("YOUR Customer ID NO. IS",cd )
        print("")
        print("")
        print("")
        mydb.commit()
        print("SUCESSFULLY ADDED DATA")
        loop=input("DO YOU WISH TO ADD MORE DATA:(y/n)")
        if loop == 'n'or'y':
            continue
        else:
            loop=input("DO YOU WISH TO ADD MORE DATA:(y/n)")
def booking_record():
    mydb= con.connect(user='root',password=pas,database='Customers')
    curs=mydb.cursor()
    cid=input("ENTER CUSTOMER ID : ")
    sql="SELECT * FROM room_rent WHERE CID= %s"
    curs.execute(sql,(cid,))
    data=curs.fetchall()
    if data:
        print('CID:  ',data[0][0])
        print('Room Choice:  ',data[0][1])
        print('No_of_Days:  ',data[0][2])
        print('Room_No:  ',data[0][3])
        print('Room_rent',data[0][4])
        return True
    else:
        print("Record Not Found Try Again !")
        return False   

def alldetail():
    mydb= con.connect(user='root',password=pas,database='Customers')
    curs=mydb.cursor()
    ql="select cid from record;"
    curs.execute(ql)
    dat = curs.fetchall()
    if dat :
        for i in range(0,len(dat)):
            cid=dat[i][0]
            sql1="SELECT * FROM Record WHERE CID= %s"
            curs.execute(sql1,(cid,))
            data=curs.fetchall()        
            sql2="SELECT * FROM room_rent WHERE CID= %s"
            curs.execute(sql2,(cid,))
            data2=curs.fetchall()
            sql3="SELECT * FROM GAMING WHERE CID= %s"
            curs.execute(sql3,(cid,))
            data3=curs.fetchall()
            if data:
                print('CID:  ',data[0][0])
                print('phone number:  ',data[0][1])
                print('name:  ',data[0][2])
                print('address:  ',data[0][3])
            else:
                continue   

            if data2:
                print('Room Choice:  ',data2[0][1])
                print('No_of_Days:  ',data2[0][2])
                print('Room_No:  ',data2[0][3])
                print('Room_rent',data2[0][4])

            else:
                continue

            if data3:
                print('EVENT:  ',data3[0][1])
                print('No_of_people:  ',data3[0][2])
                print('Events_Cost: ',data3[0][3])
                for k in range(1,5):
                    print("")
            else:
                for k in range(1,5):
                    print("")
                continue


    
def customerdetail():
    mydb= con.connect(user='root',password=pas,database='Customers')
    curs=mydb.cursor()
    cid=input("ENTER CUSTOMER ID : ")
    sql1="SELECT * FROM Record WHERE CID= %s"
    curs.execute(sql1,(cid,))
    data=curs.fetchall()        
    sql2="SELECT * FROM room_rent WHERE CID= %s"
    curs.execute(sql2,(cid,))
    data2=curs.fetchall()
    sql3="SELECT * FROM GAMING WHERE CID= %s"
    curs.execute(sql3,(cid,))
    data3=curs.fetchall()
    if data:
        print('CID:  ',data[0][0])
        print('phone number:  ',data[0][1])
        print('name:  ',data[0][2])
        print('address:  ',data[0][3])
    else:
        print("Record Not Found in Customer Details !")    

    if data2:
        print('Room Choice:  ',data2[0][1])
        print('No_of_Days:  ',data2[0][2])
        print('Room_No:  ',data2[0][3])
        print('Room_rent',data2[0][4])

    else:
        print("Record Not Found in Room Rent !")

    if data3:
        print('EVENT:  ',data3[0][1])
        print('No_of_people:  ',data3[0][2])
        print('Events_Cost: ',data3[0][3])

    else:
        print("Record Not Found in GAMING !")
        return False
    
def customsearch():
    mydb= con.connect(user='root',password=pas,database='Customers')
    curs=mydb.cursor()
    curs.execute("CREATE TABLE IF NOT EXISTS Record(CID VARCHAR(5),phone_no VARCHAR(10),name VARCHAR(20),address VARCHAR(30),PRIMARY KEY(CID));")
    global cid
    cid=input("ENTER CUSTOMER ID : ")
    sql="SELECT * FROM Record WHERE CID= %s"
    curs.execute(sql,(cid,))
    dat=curs.fetchall()
    return dat
def reset():
    mydb= con.connect(user='root',password=pas)
    curs=mydb.cursor()
    curs.execute("DROP DATABASE Customers;")
    mydb.commit()
    mydb.close()
    print("RESET SUCESSFULL..........")
    login()

def roomrent():
    global cid
    customer =customsearch()
    if customer:
        mydb= con.connect(user='root',password=pas,database='Customers')
        global roomrent
        if mydb:
            
            curs=mydb.cursor()
            createTable ="CREATE TABLE IF NOT EXISTS ROOM_RENT(CID VARCHAR(20),ROOM_CHOICE VARCHAR(15),NO_OF_DAYS INT,ROOMNO INT ,ROOMRENT INT, PRIMARY KEY(CID))"
            curs.execute(createTable)
            print ("\n ##### WE HAVE THE FOLLOWING ROOMS FOR YOU #####")
            print (" 1. DELUXE ----> Rs 2000 per day\-")
            print (" 2. SUPER DELUXE ----> Rs 5000 per day\-")
            print (" 3. ROYAL ----> Rs 7000 per day\-")
            print (" 4. ULTRA ROYAL ----> Rs 10000 per day\- ")
            print (" 5. ELITE ----> Rs 20000 per day\-")
            roomchoice =int(input("Enter Your Option : "))
            roomno=int(input("Enter Customer Room No : "))
            noofdays=int(input("Enter No. Of Days : "))
            if roomchoice==1:
                roomrent = noofdays * 2000
                print("\nDELUXE ROOM HAS BEEN SELECTED")
            elif roomchoice==2:
                roomrent = noofdays * 5000
                print("\nSUPER DELUXE ROOM HAS BEEN SELECTED")
            elif roomchoice==3:
                roomrent = noofdays * 7000
                print("\nROYAL ROOM HAS BEEN SELECTED")
            elif roomchoice==4:
                roomrent = noofdays * 10000
                print("\nULTRA ROYAL ROOM HAS BEEN SELECTED")
            elif roomchoice==5:
                roomrent = noofdays * 20000
                print("\nELITE ROOM HAS BEEN SELECTED")
            else:
                print("Sorry ,May Be You Are Giving Me Wrong Input, Please Try Again !!! ")
                return
            sql= "INSERT INTO ROOM_RENT VALUES(%s,%s,%s,%s,%s)"
            roomdict={1:"DELUXE",2:"SUPER DELUXE",3:"ROYAL",4:"ULTRA ROYAL",5:"ELITE"}
            room=roomdict.get(roomchoice)
            values= (cid,room,noofdays,roomno,roomrent)
            curs.execute(sql,values)
            curs.execute("COMMIT")
            print("Thank You , Your Room Has Been Booked For :",noofdays , "Days" )
            print("Your Total Room Rent is : Rs",roomrent)
            curs.close()
    else:
        print("NO RECORD FOUND")
def events():
    global cid
    customer=customsearch()
    if customer:
        mydb= con.connect(user='root',password=pas,database='Customers')
        global eventbill
        if mydb:
            curs=mydb.cursor()
            createTable ="""CREATE TABLE IF NOT EXISTS GAMING(CID VARCHAR(20),EVENTS
          VARCHAR(30),PEOPLE VARCHAR(30),EVENT_BILL VARCHAR(30),PRIMARY KEY(CID))"""
            curs.execute(createTable)
            print ("\n##### WE HAVE THE FOLLOWING EVENTS FOR YOU TO ENJOY #####")
            print("""
            1. MUSICAL NIGHT-----> Rs 900 per person/-
            2. POOL PARTY-----> Rs 600 per person/-
            3. FUN GAMES-----> Rs 200 per person/-
            4. MOVIES-----> Rs 300 per person/-
            """)
            event=int(input("Enter which event you want to enjoy:"))
            people=int(input("Enter no of people participating in the event:"))
            if event==1:
                eventbill = people * 900
                print("YOU HAVE SELECTED TO BE IN A MUSICAL NIGHT")
            elif event==2:
                eventbill = people * 600
                print("YOU HAVE SELECTED TO BE IN A POOL PARTY")
            elif event==3:
                eventbill = people * 200
                print("YOU HAVE SELECTED TO PLAY SOME FUN GAMES")
            elif event==4:
                eventbill = people * 300
                print("YOU HAVE SELECTED TO WATCH A MOVIE")
            else:
                print("Sorry ,May Be You Are Giving Me Wrong Input, Please Try Again !!! ")
                return
            sql= "INSERT INTO GAMING VALUES(%s,%s,%s,%s)"
            allevents ={1:"Musical Night",2:"Pool Party",3:"Fun Games",4:"Movie"}
            eventname=allevents.get(event)
            values= (cid,eventname,people,eventbill)
            curs.execute(sql,values)
            curs.execute("COMMIT")
            print("Your Total Event Bill Is : Rs",eventbill)
            print("\nWE HOPE YOU WILL ENJOY THE EVENT")
            curs.close() 
        else:
            print("""Error Connecting To Mysql server ....
            Please try again.....""")
            login()
    else:
        print("""ERROR..........
        INCORRECT Customer ID or Customer Dosen't Exist""")
        login()

def settings():
    mydb= con.connect(user='root',password=pas,database='Customers')
    curs=mydb.cursor()
    print(("SETTINGS").center(50,'*'))
    print(("""
    1--->EDIT CUSTOMER RECORD DETAILS
    2--->EDIT ROOM RENT DETAILS
    3--->RESET""").center(50,))
    choice = input("ENTER CHOICE:  ")
    if choice=="1":
        print(('''
            1--->Name
            2--->Phone no.
            3--->Address
            4--->Customer
            '''))
        choice=int(input("ENTER CHOICE:"))
        cid=input("ENTER CUSTOMER ID : ")
        if choice == 1:
            val=input("ENTER NEW VALUE:")
            sql='''update record set name = %s where CID = %s'''
            dat = (val,cid)
            curs.execute(sql,dat)
        elif choice == 2:
            val=input("ENTER NEW VALUE:")
            sql='''update record set phone_no = %s where CID = %s'''
            dat = (val,cid)
            curs.execute(sql,dat)
        elif choice ==3:
            val=input("ENTER NEW VALUE:")
            sql='''update record set address = %s where CID = %s'''
            dat = (val,cid)
            curs.execute(sql,dat)

        elif choice==4:
            valu_1="DELETE FROM Record WHERE cid = {} ".format(cid)
            vat="DELETE FROM room_rent WHERE cid = {} ".format(cid)
            print("SUCESSFULLY DELETED ALL CUSTOMER DETAILS")
            curs.execute(valu_1)
            curs.execute(vat)
        else:
            print("INVALID ENTRY!!!")
        mydb.commit()
    if choice == "2":
        print(('''
            1--->Room Choice
            2--->No. of days
            3--->Room no.
            '''))
        choice=int(input("ENTER CHOICE:"))
        cid=input("ENTER CUSTOMER ID : ")
        if choice == 1:    
            val=input("ENTER NEW VALUE:")
            sql='''update record set name = %s where CID = %s'''
            dat = (val,cid)
            curs.execute(sql,dat)
        elif choice == 2:
            val=input("ENTER NEW VALUE:")
            sql='''update record set phone_no = %s where CID = %s'''
            dat = (val,cid)
            curs.execute(sql,dat)
        elif choice ==3:
            val=input("ENTER NEW VALUE:")
            sql='''update record set address = %s where CID = %s'''
            dat = (val,cid)
            curs.execute(sql,dat)
        else:
            print("INVALID ENTRY!!!")
    mydb.commit()
    if choice=="3":
        print("ARE YOU SURE YOU WANT TO RESET..... \nALL DATA FROM DATABASE WILL BE DELETED")
        sure=input("PRESS ENTER KEY TO CONTINUE..... \nOR PRESS 'c' TO CANCEL:           ")
        if sure.lower() != "c":
            reset()           
        else:
            print("CANCELLING RESET.......")
            startup()
        
def totalbill():
    mydb= con.connect(user='root',password=pas,database='Customers')
    curs=mydb.cursor()  
    customer = customsearch()
    if customer :     
        sql2="SELECT * FROM room_rent WHERE CID= %s"
        curs.execute(sql2,(cid,))
        data2=curs.fetchall()
        sql3="SELECT * FROM GAMING WHERE CID= %s"
        curs.execute(sql3,(cid,))
        data3=curs.fetchall()   

        if data2:
            rent=int(data2[0][4])

        if data3:
            eventcost=int(data3[0][3])
        bil=('''
        YOUR TOTAL BILL
        Rent : %s Rs
        Event Cost : %s Rs
        ------------------------------
        TOTAL AMOUNT(Rs): %s ''')
        bill = (rent,eventcost,rent+eventcost)
        print(bil % bill)
        print("""
        
        
        
        """)
def startup():
    while True:
            print(("WELCOME TO HOTEL MANAGEMENT SYSTEM").center(50,'*'))
            print(('''
            1--->Enter Customer Details
            2--->Calculate Room Rent
            3--->Display Customer Details
            4--->Display Extra Events
            5--->Settings
            6--->BiLL
            7--->EXIT''').center(50,))
            choice=input("ENTER CHOICE:")
            if choice == '1':
                insertval()
            elif choice == '2':
                roomrent()
            elif choice =='3':
                print('''
                1--->Display a customer details
                2--->Display details of all customers''')
                choic = int(input("Enter choice: "))
                if choic == 1:
                    customerdetail()
                elif choic ==2:
                    alldetail()
                else:
                    print("INVAILD CHOICE!!")
            elif choice=='4':
                events()
            elif choice == '5':
                settings()
            elif choice =='6':
                totalbill()
            elif choice =='7':
                print("""
                
                
                
                """)
                print("EXITING........")
                for abc in range(0,5):
                    print("")
                login()
            else:
                print("INCORRECT CHOICE:")
def connection():
    mydb= con.connect(user='root',password=pas)
    curs=mydb.cursor()
    curs.execute("CREATE DATABASE IF NOT EXISTS Customers;")
    mydb.close() 
    return curs

def login():
    print("LOGIN INTO MYSQL SERVER TO CONTINUE............")
    while True:
        try:
            global pas
            pas=getpass.getpass("ENTER PASSWORD: ")
            connection()
            break
        except:
            print("INCORRECT PASSWORD")
            
    
cid=''
pas=""
login()
startup()


    
