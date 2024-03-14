import mysql.connector as my
import sys
import pickle
import subprocess
mycon= my.connect(host="localhost", user= "root", passwd="admin123",database= "mobimeds")
cursor=mycon.cursor(buffered=True)   

#SUBFUNCTIONS FOR EMPLOYEE FUNCTION
#1 - To go Back
def Back():
        print("\nWhich window would you like to go back to?\n")
        print("1. Employee Screen")
        print("2. Main Owner Screen")
        b1=int(input("Your Choice?(1/2): "))
        if b1==1:
                print("\n\n\t\t\t\t\t\t\t...Going Back to Main Employee Screen...\n")
                Employee()
        elif b1==2:
                print("\n\n\t\t\t\t\t\t...Going Back to Main Owner's Menu...\n")
                Owner()
        else:
                print("ERROR!!!INVALID INPUT\n")
                Back()

#2 - To View Employee List
def empView():
        mycon= my.connect(host="localhost", user= "root", passwd="admin123",database= "mobimeds")
        cursor=mycon.cursor(buffered=True)
        cursor.execute("select * from employees")
        data=cursor.fetchall()
        for v in range(len(data)):
                print("\nSr No.:                                           ", v+1)
                print("Name of Employee:                      ",data[v][0])
                print("Date of Birth:                                  ",data[v][1])
                print("Gender:                                             ",data[v][2])
                print("Salary:                                                ",data[v][3])
                print("Shift Timing:                                    ",data[v][4])
                print("Date of Joining :                             ",data[v][5])
                print("City:                                                    ",data[v][6])
        Back()

#3 - To insert/Add Employee Record
def empInsert():
        mycon= my.connect(host="localhost", user= "root", passwd="admin123",database= "mobimeds")
        cursor=mycon.cursor(buffered=True)
        times_1=int(input("How many records you want to enter today?: "))
        for i in range(times_1):
                nme= input("Enter the Name of the Employee(PLEASE ENTER THE FULL NAME): ")
                date=input("Enter the Date Of Bith of the Employee(YYYY-MM-DD Format): ")
                gen= input("Enter the Gender of the Employee(M/F/T): ")
                sal= int(input("Enter the Salary of the Employee: "))
                stime=input("Enter the Shift Time(HH:MM:SS Format) of the Employee: ")
                datejoin=input("Enter the Date of Joining of the Employee(YYYY-MM-DD Format): ")
                cty= input("Enter the City where the Employee works: ")
                em="insert into employees values('{}','{}','{}',{},'{}','{}','{}')".format(nme,date,gen,sal,stime,datejoin,cty)
                cursor.execute(em)
                mycon.commit()
                print("\n Following Record was added: \n")
                cursor.execute("select * from employees where Name= '{}' ".format(nme)) 
                rec=cursor.fetchone()
                print(rec,"\n")
        Back()

#4 - To Delete Employee record(s)        
def empDelete():
        mycon= my.connect(host="localhost", user= "root", passwd="admin123",database= "mobimeds")
        cursor=mycon.cursor(buffered=True)
        which_1= input("Enter the Full name of the Employee whose record you want to delete: ")
        delete_1="delete from employees where Name= '{}' ".format(which_1)
        cursor.execute(delete_1)
        mycon.commit()
        print("\n Record Deleted Successfully!\n")
        yes=input("Want to delete more records? (y/n): ")
        if yes=="y":
                empDelete()
        else:
                print("\n\t\t\t\t\t\t...Going Back...\n")
                Back()

#5 - Ask whether owner wants to update more
def UpdateMore():
        want=input("Want to update more?(y/n): ")
        if want=="y":
                empModify()
        else:
                Back()

#6 - To Modify/Update Employee Records
def empModify():
        mycon= my.connect(host="localhost", user= "root", passwd="admin123",database= "mobimeds")
        cursor=mycon.cursor(buffered=True)
        print("\n\t\t\t\t\t\t\tMODIFICATION MENU\n")
        ask2=input("Which Employee's record you want to update?(PLEASE ENTER THE FULL NAME): ")
        print("\nNOTE: Once you Modify the name of an employee, you won't be able to make further changes in its record\n")
        print("\nPlease select which record you want to update: ")
        print("\n1. Name")
        print("2. DOB")
        print("3.  Gender")
        print("4. Salary")
        print("5. Shift_time")
        print("6. Date_join")
        print("7. City\n")
        ask3= int(input("Enter your choice(1/2/3/4/5/6/7): "))
        if ask3==1:
                newName=input("Enter the New Name: ")
                nn1="update employees set Name= '{}' where Name='{}'".format(newName,ask2)
                cursor.execute(nn1)
                mycon.commit
                print("\nUpdated Record: \n")
                cursor.execute("select * from employees where Name='{}'".format(newName))
                data=cursor.fetchone()
                print(data)
                UpdateMore() 
        elif ask3==2:
                DB=input("Enter the New DOB: ")
                nn2="update employees set DOB= '{}' where Name= '{}'".format(DB,ask2)
                cursor.execute(nn2)
                mycon.commit
                print("\nUpdated Record: \n")
                cursor.execute("select * from employees where Name= '{}'".format(ask2))
                data=cursor.fetchone()
                print(data)
                UpdateMore()
        elif ask3==3:
                GEN_DER=input("Enter the New Gender: ")
                nn3="update employees set Gender= '{}' where Name= '{}'".format(GEN_DER,ask2)
                cursor.execute(nn3)
                mycon.commit
                print("\nUpdated Record: \n")
                cursor.execute("select * from employees where Name='{}'".format(ask2))
                data=cursor.fetchone()
                print(data)
                UpdateMore()
        elif ask3==4:
                Sal=int(input("Enter new Salary(Should not exceed 5 figure mark): "))
                nn4="update employees set Salary= '{}' where Name= '{}'".format(Sal,ask2)
                cursor.execute(nn4)
                mycon.commit
                print("\nUpdated Record: \n")
                cursor.execute("select * from employees where Name='{}' ".format(ask2))
                data=cursor.fetchone()
                print(data)
                UpdateMore()
        elif ask3==5:
                ST=input("Enter new ShiftTiming: ")
                nn5="update employees set Shift_time= '{}' where Name='{}'".format(ST,ask2)
                cursor.execute(nn5)
                mycon.commit
                print("\nUpdated Record: \n")
                cursor.execute("select * from employees where Name='{}' ".format(ask2))
                data=cursor.fetchone()
                print(data)
                UpdateMore()
        elif ask3==6:
                DT=input("Enter new Joining Date: ")
                nn6="update employees set Date_join= '{}' where Name= '{}'".format(DT,ask2)
                cursor.execute(nn6)
                mycon.commit
                print("\nUpdated Record: \n")
                cursor.execute("select * from employees where Name='{}' ".format(ask2))
                data=cursor.fetchone()
                print(data)
                UpdateMore()
        elif ask3==7:
                City=input("Enter new City: ")
                nn7="update employees set City= '{}' where Name='{}'".format(City,ask2)
                cursor.execute(nn7)
                mycon.commit
                print("\nUpdated Record: \n")
                cursor.execute("select * from employees where Name='{}' ".format(ask2))
                data=cursor.fetchone()
                print(data)
                UpdateMore()
        

#SUB-FUNCTIONS FOR PRODUCTS FUNCTION
#1 - To go Back
def ProdBack():
        print("\nWhich window would you like to go back to?\n")
        print("1. Product Screen")
        print("2. Main Owner Screen")
        b2=input("Your Choice?(1/2): ")
        if b2=='1':
                print("\n\t\t\t\t\t\t\t\t....Going back to Main Products Menu....\n")
                Product()
        elif b2=='2':
                print("\n\t\t\t\t\t\t\t\t....Going back to Main Owners Menu....\n")
                Owner()
        else:
                print("\nERROR!! iNVALID INPUT\n")
                ProdBack()

#2 - To View Products of a Category
def prdView(table1):
        mycon= my.connect(host="localhost", user= "root", passwd="admin123",database= "mobimeds")
        cursor=mycon.cursor(buffered=True)
        cursor.execute("select * from {} ".format(table1))
        data=cursor.fetchall()
        for product in range(len(data)):
                print("Sr. No.:                                                             ", product+1,"\n")
                print("PRODUCT ID:                                                 ",data[product][0])
                print("NAME OF THE PRODUCT:                          ",data[product][1])
                print("DOSAGE:                                                         ",data[product][2])
                print("PRICE:                                                              ",data[product][3])
                print("DISCOUNTED PRICE:                                   ",data[product][4])
                print("DISCOUNT % GIVEN:                                  ",data[product][5])
                print("QUANTITY:                                                    ",data[product][6])
                print("MFG DATE:                                                    ",data[product][7])
                print("EXP DATE:                                                      ",data[product][8],"\n")
        ProdBack()

#3 - To Add/Insert Products of a Category
def prdAdd(table2):
        mycon= my.connect(host="localhost", user= "root", passwd="admin123",database= "mobimeds")
        cursor=mycon.cursor(buffered=True)
        times_2=int(input("How many records you want to enter today?: "))
        for i in range(times_2):
                prdid=int(input("Enter the Productid, mentioned in the Pamphlet: "))
                nme= input("Enter the Name of the Product:  ")
                Dosage= input("Enter the Dosage of the Medicine(eg- 40ml,40g,500mg,etc): ")
                price= float(input("Enter the Price of the Medicine: "))
                Dprice= float(input("Enter the  Discounted Price of the Product(Enter Original Price of the item, if no discount):  "))
                price_pcnt= int(input("Enter the Discount Percentage on the Medicine(Enter 0, if no discount): "))
                Qty= input("Enter the Quantity of the Medicine,in 1 pack/bottle/strip: ")
                datemfg=input("Enter the Mfg Date of the Medicine(YYYY-MM-DD Format): ")
                dateexp=input("Enter the Expiry Date of the Medicine(YYYY-MM-DD Format): ")
                if table2=="personal_care":
                        Cat=input("Enter the Category of the item: ")
                        prod=PROD="insert into {} values({},'{}','{}',{},{},{},'{}','{}','{}','{}')".format(table2,prdid,nme,Dosage,price,Dprice,price_pcnt,Qty,datemfg,dateexp,Cat)
                        cursor.execute(PROD)
                        mycon.commit()
                        print("\n Following Record was added: \n")
                        cursor.execute("select * from {} where Name= '{}' ".format(table2,nme))
                        rec=cursor.fetchone()
                        print(rec,"\n")
                else:
                        PROD="insert into {} values({},'{}','{}',{},{},{},'{}','{}','{}')".format(table2,prdid,nme,Dosage,price,Dprice,price_pcnt,Qty,datemfg,dateexp)
                        cursor.execute(PROD)
                        mycon.commit()
                        print("\n Following Record was added: \n")
                        cursor.execute("select * from {} where Name= '{}' ".format(table2,nme))
                        rec=cursor.fetchone()
                        print(rec,"\n")
        ProdBack()

#4 - To Delete Products of a Category
def prdDel(table3):
        mycon= my.connect(host="localhost", user= "root", passwd="admin123",database= "mobimeds")
        cursor=mycon.cursor(buffered=True)
        print("\nFollowing Medicines are present in this ", table3," category/table:\n")
        cursor.execute("select * from {}".format(table3))
        PRODVALUES=cursor.fetchall()
        print(PRODVALUES)
        which_2= int(input("\nEnter the Product Id of the Medicine whose record you want to delete: "))
        delete_2="delete from {} where Prdt_id= {} ".format(table3,which_2)
        cursor.execute(delete_2)
        mycon.commit()
        print("\n Record Deleted Successfully!\n")
        yes=input("Want to delete more records? (y/n): ")
        if yes=="y":
                print("\nPlease select from which Category/Table you want to delete\n")
                print("1. Allopathic and General Medicines")
                print("2. Ayurvedic Medicines")
                print("3. Short Term Ailments")
                print("4. Nutrition and Fitness Supplements")
                print("5. Personal Care")
                whichT=int(input("\n Your Choice(1/2/3/4/5): "))
                if whichT==1:
                        prdDel("allopathic_medicines")
                elif whichT==2:
                        prdDel("ayurvedic_medicines")
                elif whichT==3:
                        prdDel("shortterm_ailments")
                elif whichT==4:
                        prdDel("nutrition_fitness_supplements")
                elif whichT==5:
                        prdDel("personal_care")
        else:
                ProdBack()

#5 - To Modify Products of a Category
continuing = "y"
def  prdModify(table4):
        mycon= my.connect(host="localhost", user= "root", passwd="admin123",database= "mobimeds")
        cursor=mycon.cursor(buffered=True)
        global continuing
        while continuing=="y":
                print("\nPlease Select which column you want to update. \nNOTE: Product Id can be changed only by the CEO, or from the Database directly")
                print("\n1. Name")
                print("2.  Dosage")
                print("3. Price")
                print("4. Discounted_price")
                print("5. Discount_percent")
                print("6. Quantity")
                print("7. Manufacturing Date")
                print("8. Expiry Date")
                print("9. Category (ONLY FOR THE 'PERSONAL CARE' Category/Table")
                ask5= int(input("Enter your choice(1/2/3/4/5/6/7/8/9): "))
                print("\nThe items in ", table4, " category/table are: ",'\n')
                cursor.execute("select * from {}".format(table4))
                daata=cursor.fetchall()
                for modi in daata:
                        print(modi)
                ask4=int(input("\nEnter the Product Id of the medicine whose record you want to update?: "))                

                if ask5==1:
                        newPname=input("Enter the New Product name:  ")
                        nn_1="update {} set Name= '{}' where Prdt_id= {} ".format(table4,newPname,ask4)
                        cursor.execute(nn_1)
                        mycon.commit
                        print("\nUpdated Record: \n")
                        cursor.execute("select * from {} where Prdt_id= {} ".format(table4,ask4))
                        data=cursor.fetchone()
                        print(data)
                        continuing="n"
                        continuing=input("Want to continue updating? (y/n): ")
                elif ask5==2:
                        Dosa_ge=input("Enter the New Product Dosage(eg: 40ml,40g,500mg,etc):  ")
                        nn_2="update {} set Dosage= '{}' where Prdt_id= {} ".format(table4,Dosa_ge,ask4)
                        cursor.execute(nn_2)
                        mycon.commit
                        print("\nUpdated Record: \n")
                        cursor.execute("select * from {} where Prdt_id= {} ".format(table4,ask4))
                        data=cursor.fetchone()
                        print(data)
                        continuing="n"
                        continuing=input("Want to continue updating? (y/n): ")
                elif ask5==3:
                        Pri_ce=float(input("Enter the New Price of the Product:  "))
                        nn_3="update {} set Price={} where Prdt_id= {} ".format(table4,Pri_ce,ask4)
                        cursor.execute(nn_3)
                        mycon.commit
                        print("\nUpdated Record: \n")
                        cursor.execute("select * from {} where Prdt_id= {} ".format(table4,ask4))
                        data=cursor.fetchone()
                        print(data)
                        continuing="n"
                        continuing=input("Want to continue updating? (y/n): ")
                elif ask5==4:
                        DisPri_ce=float(input("Enter the New Discounted Price of the Product(Enter Original Price of the item, if no discount):  "))
                        nn_4="update {} set Discounted_price={} where Prdt_id= {} ".format(table4,DisPri_ce,ask4)
                        cursor.execute(nn_4)
                        mycon.commit
                        print("\nUpdated Record: \n")
                        cursor.execute("select * from {} where Prdt_id= {} ".format(table4,ask4))
                        data=cursor.fetchone()
                        print(data)
                        continuing="n"
                        continuing=input("Want to continue updating? (y/n): ")
                elif ask5==5:
                        Dispercent=int(input("Enter the New Discount Percentage on the Product(Enter 0 if no discount):  "))
                        nn_5="update {} set Discount_percent={} where Prdt_id= {} ".format(table4,Dispercent,ask4)
                        cursor.execute(nn_5)
                        mycon.commit
                        print("\nUpdated Record: \n")
                        cursor.execute("select * from {} where Prdt_id= {} ".format(table4,ask4))
                        data=cursor.fetchone()
                        print(data)
                        continuing="n"
                        continuing=input("Want to continue updating? (y/n): ")
                elif ask5==6:
                        newQty=input("Enter the New Quantity of the Product in 1 strip/bottle/pack:  ")
                        nn_6="update {} set Qty= '{}' where Prdt_id= {} ".format(table4,newQty,ask4)
                        cursor.execute(nn_6)
                        mycon.commit
                        print("\nUpdated Record: \n")
                        cursor.execute("select * from {} where Prdt_id= {} ".format(table4,ask4))
                        data=cursor.fetchone()
                        print(data)
                        continuing="n"
                        continuing=input("Want to continue updating? (y/n): ")
                elif ask5==7:
                        newMFG=input("Enter the New Mfg date of the Product:  ")
                        nn_7="update {} set Mfg_date= '{}' where Prdt_id= {}         ".format(table4,newMFG,ask4)
                        cursor.execute(nn_7)
                        mycon.commit
                        print("\nUpdated Record: \n")
                        cursor.execute("select * from {} where Prdt_id= {} ".format(table4,ask4))
                        data=cursor.fetchone()
                        print(data)
                        continuing="n"
                        continuing=input("Want to continue updating? (y/n): ")
                elif ask5==8:
                        newEFG=input("Enter the New Exp. date of the Product:  ")
                        nn_8="update {} set Exp_date= '{}' where Prdt_id= {} ".format(table4,newEFG,ask4)
                        cursor.execute(nn_8)
                        mycon.commit
                        print("\nUpdated Record: \n")
                        cursor.execute("select * from {} where Prdt_id= {} ".format(table4,ask4))
                        data=cursor.fetchone()
                        print(data)
                        continuing="n"
                        continuing=input("Want to continue updating? (y/n): ")
                elif ask5==9:
                        if go==True:
                                newCAT_gy=input("Enter the New Category of the Product:  ")
                                nn_9="update {} set Category= '{}' where Prdt_id= {} ".format("personal_care",newCAT_gy,ask4)
                                cursor.execute(nn_9)
                                mycon.commit
                                print("\nUpdated Record: \n")
                                cursor.execute("select * from {} where Prdt_id= {} ".format("personal_care",ask4))
                                data=cursor.fetchone()
                                print(data)
                                continuing="n"
                                continuing=input("Want to continue updating? (y/n): ")
                        else:
                                print("Sorry! Can only make 'Category' column's Changes, if you are updating the 'Personal Care' Category Table")
                                ProdBack()                        
                        
        else:
                ProdBack() #This executes only when he modifies some record, satisfied, and says "n"(i.e. doesn't want to update more. There he has choice to go back to whichever window he wants to

#6 - Allopathic Medicines
def AlloGen():
        print("\n\nHello!  What would you like to do next?: \n")
        print("1. View Records of all the medicines")
        print("2. Add Records")
        print("3. Delete Records")
        print("4. Modify a record\n")
        say = input("Your choice?(1/2/3/4)(Press 5 to go back to Products Screen):  ")
        if say=='1':
                prdView("allopathic_medicines")
        elif say=='2':
                prdAdd("allopathic_medicines")
        elif say=='3':
                prdDel("allopathic_medicines")
        elif say=='4':
                prdModify("allopathic_medicines")
        elif say=='5':
                Product()
        else:
                print("\nERROR! Please recheck your input\n")
                AlloGen()

#7 - Ayurvedic Medicines                
def AyuMed():
        print("\n\nHello!  What would you like to do next?: \n")
        print("1. View Records of all the medicines")
        print("2. Add Records")
        print("3. Delete Records")
        print("4. Modify a record\n")
        say = input("Your choice?(1/2/3/4)(Press 5 to go back to Products Screen):  ")
        if say=='1':
                prdView("ayurvedic_medicines")
        elif say=='2':
                prdAdd("ayurvedic_medicines")
        elif say=='3':
                prdDel("ayurvedic_medicines")
        elif say=='4':
                prdModify("ayurvedic_medicines")
        elif say=='5':
                Product()
        else:
                print("\nVALUE ERROR! Please recheck your input\n")
                AyuMed()

#8 - Short term Ailments
def STA():
        print("\n\nHello!  What would you like to do next?: \n")
        print("1. View Records of all the medicines")
        print("2. Add Records")
        print("3. Delete Records")
        print("4. Modify a record\n")
        say = input("Your choice?(1/2/3/4)(Press 5 to go back to Products Screen):  ")
        if say=='1':
                prdView("shortterm_ailments")
        elif say=='2':
                prdAdd("shortterm_ailments")
        elif say=='3':
                prdDel("shortterm_ailments")
        elif say=='4':
                prdModify("shortterm_ailments")
        elif say=='5':
                Product()
        else:
                print("\nVALUE ERROR! Please recheck your input")
                STA()
                
#9 - Nutrition and Fitness Supplements
def NFS():
        print("\n\nHello!  What would you like to do next?: \n")
        print("1. View Records of all the medicines")
        print("2. Add Records")
        print("3. Delete Records")
        print("4. Modify a record\n")
        say = input("Your choice?(1/2/3/4)(Press 5 to go back to Products Screen):  ")
        if say=='1':
                prdView("nutrition_fitness_supplements")
        elif say=='2':
                prdAdd("nutrition_fitness_supplements")
        elif say=='3':
                prdDel("nutrition_fitness_supplements")
        elif say=='4':
                prdModify("nutrition_fitness_supplements")
        elif say=='5':
                Product()
        else:
                print("\nVALUE ERROR! Please recheck your input")
                NFS()
go=True
#10 - Personal Care Products
def PersonaC():
        print("\n\nHello! What would you like to do next?: \n")
        print("1. View Records of all the medicines")
        print("2. Add records")
        print("3. Delete Records")
        print("4. Modify Records\n")
        say=input("Your Choice?(1/2/3/4)(Press 5 to go back to Products Screen): ")
        if say=='1':
                prdView("personal_care")
        elif say=='2':
                prdAdd("personal_care")
        elif say=='3':
                prdDel("personal_care")
        elif say=='4':
                go=True
                prdModify("personal_care")
        elif say=='5':
                Product()
        else:
                print("\nVALUE ERROR! PLEASE RECHECK YOUR INPUT")
                PersonaC()

#OWNER
                
def OwnerMenu():
    print("\n\n\t\t\t\t\t\t\t|||MAIN OWNER MENU|||\n\n\n")
    print("Hi! Where would you like to go next sir/ma'am?\n")
    print("1. Product Management")
    print("2. Employee Management")
    print("3. Exit")
    ask = input("Your input(1/2/3): ")
    return ask

def Owner():
    while True:
        choice = OwnerMenu()
        if choice == '1':
            Product()
        elif choice == '2':
            Employee()
        elif choice == '3':
            print("\nThank you for coming! Hope we see you soon (Please minimize this window now)\n")
            print("STAY SAFE, STAY HEALTHY\n\n")
            print("~~You Only Live Twice, Mobimeds- SAVING LIVES!~~")
            # Run the GUI application in a new process
            subprocess.Popen(['python', 'TKINTER GUI.py'])
            # Terminate the current shell
            sys.exit()
        else:
            print("\nERROR!! Invalid Input!\n")
#EMPLOYEE

def Employee():
        print("\n\t\t\t\t\t\t\t###MAIN EMPLOYEES MENU###")
        print("\n\nHello!  What would you like to do next?: \n")
        print("1. View Records of all the employees")
        print("2. Add Records")
        print("3. Delete Records")
        print("4. Modify a record\n")
        ask1=input("Your choice?(1/2/3/4)(Press 5 to go back to Owner's screen): ")
        if ask1=='1':
                empView()
        elif ask1=='2':
                empInsert()
        elif ask1=='3':
                empDelete()
        elif ask1=='4':
                empModify()
        elif ask1=='5':
                print("\n\n\t\t\t\t\t\t\t......Going back to Owner's Screen......\n\n")
                Owner()
        else:
                print("\nVALUE ERROR! Please Try Again")
                Employee()

#PRODUCT

def Product():
        print("\n\t\t\t\t\t\t\t$$$MAIN PRODUCTS MENU$$$")
        print("\n\nHello!  Which Category of Product would you like to see? : \n")
        print("1. Allopathic and General Medicines")
        print("2. Ayurvedic Medicines")
        print("3. Short Term Ailments")
        print("4. Nutrition and Fitness Supplements")
        print("5. Personal care\n")
        P1=input("Your choice?(1/2/3/4/5)(Press 6 to go back to Owner's screen): ")
        if P1=='1':
                AlloGen()
        elif P1=='2':
                AyuMed()
        elif P1=='3':
                STA()
        elif P1=='4':
                NFS()
        elif P1=='5':
                PersonaC()
        elif P1=='6':
                Owner()
        else:
                print("\nERROR!!Invalid Input!\n")
                Product()
mycon.close()
