import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sanjadit',
    database='pratik'
    )


print("_"*52)
while(True):
    print("\t\t..............................................")
    print("\t\t*****WELCOME TO COURIER MANAGEMENT SYSTEM*****")
    print("\t\t..............................................")
    print("\n\t\t********PURV INTERNATIONAL SCHOOL********")
    print("Enter 1. INFO")
    print("Enter 2. ADMIN")
    print("Enter 3. STAFF")
    print("Enter 4. CUSTOMER")
    print("Enter 5. EXIT")
    print("----------------------------")
    try:
        a=int(input("Enter Your Choice: "))
        print()
        if(a==1):
            info=open("info.txt",'r')
            lines=info.read()
            print(lines)
        elif(a==2):
            print("Sample ID =admin")
            print("Sample PASSWORD = pass")
            b1=str(input("Enter the ID"))
            p1=str(input("Enter the Password"))
            if b1=="admin" and p1=="pass":
                print("Enter 1. VEHICLES TABLE")
                print("Enter 2. STAFF TABLE")
                print("Enter 3. ORDERS TABLE")
                a2=int(input("Enter Your Choice: "))
                print()
                if(a2==1):
                    print("Enter 1. SHOW TABLE")
                    print("Enter 2. EDIT TABLE")
                    a21=int(input("Enter Your Choice: "))
                    print()
                    if (a21==1):
                        mycursor=mydb.cursor()
                        mycursor.execute("SELECT * FROM vehicle")
                        myresult=mycursor.fetchall()
                        for x in myresult:
                            print(x)
                        print("_"*52)    
                    elif(a21==2):
                        mycursor=mydb.cursor()
                        mycursor.execute("SELECT * FROM vehicle")
                        myresult=mycursor.fetchall()
                        for x in myresult:
                            print(x)
                        print("_"*52)
                        print("SAMPLE EDIT QUERY =UPDATE vehicle set status='on the way' where Vehicle_no = 32102;")
                        qu=str(input("ENTER THER QUERY : "))
                        mycursor=mydb.cursor()
                        mycursor.execute(qu)
                        myresult=mycursor.fetchall()
                        for x in myresult:
                            print(x)
                        print("_"*52)    
                    else:
                        print("Enter a valid choice")
                elif(a2==2):
                    print("Enter 1. SHOW TABLE")
                    print("Enter 2. EDIT TABLE")
                    a22=int(input("Enter Your Choice: "))
                    print()
                    if (a22==1):
                        mycursor=mydb.cursor()
                        mycursor.execute("SELECT * FROM STAFF")
                        myresult=mycursor.fetchall()
                        for x in myresult:
                            print(x)
                        print("_"*52)    
                    elif(a22==2):
                        mycursor=mydb.cursor()
                        mycursor.execute("SELECT * FROM STAFF")
                        myresult=mycursor.fetchall()
                        for x in myresult:
                            print(x)
                        print("_"*52)
                        print("SAMPLE EDIT QUERY =UPDATE STAFF set salary = 42100 where EMP_NAME = 'JOHN';")
                        qu=str(input("ENTER THER QUERY : "))
                        mycursor=mydb.cursor()
                        mycursor.execute(qu)
                        myresult=mycursor.fetchall()
                        for x in myresult:
                            print(x)
                        print("_"*52)    
                    else:
                         print("Please enter a valid choice")
                elif(a2==3):
                    print("Enter 1. SHOW TABLE")
                    print("Enter 2. EDIT TABLE")
                    a23=int(input("Enter Your Choice: "))
                    print()
                    if (a23==1):
                        mycursor=mydb.cursor()
                        mycursor.execute("SELECT * FROM order")
                        myresult=mycursor.fetchall()
                        for x in myresult:
                            print(x)
                    elif(a23==2):
                        mycursor=mydb.cursor()
                        mycursor.execute("SELECT * FROM order")
                        myresult=mycursor.fetchall()
                        for x in myresult:
                            print(x)
                        print("_"*52)    
                        print("SAMPLE EDIT QUERY =UPDATE order set status='on the way' where ORDER_ID = 12307;")
                        qu=str(input("ENTER THER QUERY : "))
                        mycursor=mydb.cursor()
                        mycursor.execute(qu)
                        myresult=mycursor.fetchall()
                        for x in myresult:
                            print(x)
                    else:
                         print("Please enter a valid choice")
                else:
                     print("Please enter a valid choice")
            else:
                print("Please enter correct id password")
        elif(a==3):
            print("Sample ID =staff")
            print("Sample PASSWORD = pass")
            b2=str(input("Enter the ID"))
            p2=str(input("Enter the Password"))
            if b2=="staff" and p2=="pass":
                print("Enter 1. VEHICLES TABLE")
                print("Enter 2. STAFF TABLE")
                print("Enter 3. ORDERS TABLE")
                a3=int(input("Enter Your Choice: "))
                print()
                if(a3==1):
                    print("Enter 1. SHOW TABLE")
                    print("Enter 2. EDIT TABLE")
                    a31=int(input("Enter Your Choice: "))
                    print()
                    if (a31==1):
                        mycursor=mydb.cursor()
                        mycursor.execute("SELECT * FROM vehicle")
                        myresult=mycursor.fetchall()
                        for x in myresult:
                            print(x)
                        print("_"*52)    
                    elif(a31==2):
                        mycursor=mydb.cursor()
                        mycursor.execute("SELECT * FROM vehicle")
                        myresult=mycursor.fetchall()
                        for x in myresult:
                            print(x)
                        print("_"*52)
                        print("SAMPLE EDIT QUERY =UPDATE vehicle set status='on the way' where Vehicle_no = 32102;")
                        qu=str(input("ENTER THER QUERY : "))
                        mycursor=mydb.cursor()
                        mycursor.execute(qu)
                        myresult=mycursor.fetchall()
                        for x in myresult:
                            print(x)
                        print("_"*52)
                    else:
                         print("Enter a valid choice")
                elif(a3==2):
                    print("Enter 1. SHOW TABLE")
                    a32=int(input("Enter Your Choice: "))
                    print()
                    if (a32==1):
                        mycursor=mydb.cursor()
                        mycursor.execute("SELECT * FROM STAFF")
                        myresult=mycursor.fetchall()
                        for x in myresult:
                            print(x)
                        print("_"*52)    
                    else:
                         print("Please enter a valid choice")
                elif(a3==3):
                    print("Enter 1. SHOW TABLE")
                    print("Enter 2. EDIT TABLE")
                    a33=int(input("Enter Your Choice: "))
                    print()
                    if (a33==1):
                        mycursor=mydb.cursor()
                        mycursor.execute("SELECT * FROM order")
                        myresult=mycursor.fetchall()
                        for x in myresult:
                            print(x)
                    elif(a33==2):
                        mycursor=mydb.cursor()
                        mycursor.execute("SELECT * FROM order")
                        myresult=mycursor.fetchall()
                        for x in myresult:
                            print(x)
                        print("_"*52)    
                        print("SAMPLE EDIT QUERY =UPDATE order set status='on the way' where ORDER_ID = 12307;")
                        qu=str(input("ENTER THER QUERY : "))
                        mycursor=mydb.cursor()
                        mycursor.execute(qu)
                        myresult=mycursor.fetchall()
                        for x in myresult:
                            print(x)    
                    else:
                        print("Please enter a valid choice")
                else:
                    print("Please enter a valid choice")
            else:
                print("Please enter correct id pass")
    except Exception as e:
        print("Please input as suggested.",e)        

        elif(a==4):
            print("Enter customer details")
            n1=str(input("Enter your name = "))
            e1=str(input("Enter your mail = "))
            print("Enter 1. Place order")
            print("Enter 2. Track Order")
            print("Enter 3. Contact Details")
            a4=int(input("Enter Your Choice: "))
            print()
            print("Welcome  " ,n1)
            if(a4==1):
                print("enter order details :")
                print("SAMPLE ORDER DETAILS")
                print("pickp : durgapur")
                print("drop : asansol")
                print("weight(in kgs) : 3")
                pick=str(input("Enter package pickup loaction : "))
                drop=str(input("Enter package drop loaction : "))
                weig=str(input("Enter package weight : "))
                dis=str(input("Package distance in kms : "))
                pay=int(int(weig)*5*int(dis))
            
                print("_"*55)
            
                print("Your order is confirmed")
            
                print("SELECT PAYMENT OPTION")
                print("ENTER 1: ONLINE PAYMENT")
                print("ENTER 2: COD")
                bi=int(input("Enter the command : "))
                if (bi==1):
                    print("ACCOUNT NUMBER-1203848719273")
                    print("  IFSC CODE-827389 ")
                    print("  PH-7319482358")
                    print("AMOUNT IN INR=",pay)
                    print("Confirm payment and enter the transaction id ")
                    print("SAMPLE ID=1234567890")
                    tran=int(input("Enter transaction ID : "))
                
                elif(bi==2):
                    print("AMOUNT IN INR=",pay)
                    print("Pay on delivery to delivery boy")
                else:
                     print("Please enter a valid choice")
            
            elif(a4==2):
                 print("Enter order Id")
                 
            elif(a4==3):
                print("CONTACT US AT")
                print("PH- 7319482358")
                print("couriermanagementsoftware@gmail.com")
            else:
        elif(a==5):
            print("Thank you for using Courier management system")
            break
        else:
            print("Please enter a valid choice from 1-4")
    except Exception as e:
        print("Please input as suggested.",e)

