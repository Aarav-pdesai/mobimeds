import mysql.connector as my
import sys
import csv
import subprocess 

mycon= my.connect(host="localhost", user= "root", passwd="admin123", database= "mobimeds")
if mycon.is_connected()==False:
        print("Error Connecting")
else:
        print("Connection Succesful iygyf76f7f \n\n")
cursor=mycon.cursor()
Plist = []
Dlist = []
pricefile=open("Fileprice.txt", "w+")
patientlist=[]
registry=open("Patient.csv","r",newline="\r\n")
customreader=csv.reader(registry)
for rec in customreader:
        patientlist.append(rec)

def items():
        
        mycon= my.connect(host="localhost", user= "root", passwd="admin123", database= "mobimeds")
        if mycon.is_connected()==False:
                print("Error Connecting")
        else:
                print("Connection Succesful iygyf76f7f \n\n")
        cursor=mycon.cursor()
        
        print("\n\n\t\t\t\t\t\t\t...Here is the Product Menu..")
        print("Greetings Customer! Registered Customers will get an special benefits. Kindly choose what you want to do next: \n")
        print("\n\nHere are the following categories of items present in our shop/site: ")
        print("1. Allopathic and General Medicines")
        print("2. Ayurvedic Medicines")
        print("3. Short Term Ailments")
        print("4. Nutrition and Fitness Supplements")
        print("5. Personal care")
        print("6. Exit  This Customer's menu")
        say = int(input("Which Category you want to explore?(1/2/3/4/5/6):  "))
        if say ==1:
                print("\nThe medicines in this 'Allopathic & General Medicines' Category are as follows:\n")
                allo1= "select * from allopathic_medicines"
                cursor.execute(allo1)
                data1=cursor.fetchall()
                for sab1 in range(len(data1)):
                        print("Sr. No.: ", (sab1)+1,"\n")
                        print("PRODUCT ID: ",data1[sab1][0])
                        print("NAME OF THE PRODUCT: ",data1[sab1][1])
                        print("DOSAGE: ",data1[sab1][2])
                        print("PRICE: ",data1[sab1][3])
                        print("DISCOUNTED PRICE: ",data1[sab1][4])
                        print("DISCOUNT % GIVEN: ",data1[sab1][5])
                        print("QUANTITY: ",data1[sab1][6])
                        print("MFG DATE: ",data1[sab1][7])
                        print("EXP DATE: ",data1[sab1][8],"\n")
                ask1= input("\nDo you wish to buy any item? (y/n): ")
                if ask1=="y":
                        purchase("allopathic_medicines")
                else:
                        print("\n\n\t\t\t\t\t\t......$$Going back to the Main ItemList$$.....\n\n")
                        items()
        elif say==2:
                print("\nThe medicines in this 'Ayurvedic Medicines' Category are as follows: \n")
                allo2= "select * from ayurvedic_medicines"
                cursor.execute(allo2)
                data2=cursor.fetchall()
                for sab2 in range(len(data2)):
                        print("Sr. No.:                                                             ", (sab2)+1,"\n")
                        print("PRODUCT ID:                                                 ",data2[sab2][0])
                        print("NAME OF THE PRODUCT:                          ",data2[sab2][1])
                        print("DOSAGE:                                                         ",data2[sab2][2])
                        print("PRICE:                                                              ",data2[sab2][3])
                        print("DISCOUNTED PRICE:                                   ",data2[sab2][4])
                        print("DISCOUNT % GIVEN:                                  ",data2[sab2][5])
                        print("QUANTITY:                                                    ",data2[sab2][6])
                        print("MFG DATE:                                                    ",data2[sab2][7])
                        print("EXP DATE:                                                      ",data2[sab2][8],"\n")
                ask2= input("\nDo you wish to buy any item? (y/n): ")
                if ask2=="y":
                        purchase("ayurvedic_medicines")
                else:
                        print("\n\n\t\t\t\t\t\t......$$Going back to the Main ItemList$$.......\n\n")
                        items()
        elif say==3:
                print("\nThe medicines in this 'Short-term Ailments' Category are as follows: \n")
                allo3= "select * from shortterm_ailments"
                cursor.execute(allo3)
                data3=cursor.fetchall()
                for sab3 in range(len(data3)):
                        print("Sr. No.:                                                             ", (sab3)+1,"\n")
                        print("PRODUCT ID:                                                 ",data3[sab3][0])
                        print("NAME OF THE PRODUCT:                          ",data3[sab3][1])
                        print("DOSAGE:                                                         ",data3[sab3][2])
                        print("PRICE:                                                              ",data3[sab3][3])
                        print("DISCOUNTED PRICE:                                   ",data3[sab3][4])
                        print("DISCOUNT % GIVEN:                                  ",data3[sab3][5])
                        print("QUANTITY:                                                    ",data3[sab3][6])
                        print("MFG DATE:                                                    ",data3[sab3][7])
                        print("EXP DATE:                                                      ",data3[sab3][8],"\n")
                ask3= input("\nDo you wish to buy any item? (y/n): ")
                if ask3=="y":
                        purchase("shortterm_ailments")
                else:
                        print("\n\n\t\t\t\t\t\t......$$Going back to the Main ItemList$$......\n\n")
                        items()
                        
        elif say==4:
                print("\nThe medicines in this 'Nutrition and Fitness Supplements' Category are as follows: \n")
                allo4= "select * from nutrition_fitness_supplements"
                cursor.execute(allo4)
                data4=cursor.fetchall()
                for sab4 in range(len(data4)):
                        print("Sr. No.:                                                             ", (sab4)+1,"\n")
                        print("PRODUCT ID:                                                 ",data4[sab4][0])
                        print("NAME OF THE PRODUCT:                          ",data4[sab4][1])
                        print("DOSAGE:                                                         ",data4[sab4][2])
                        print("PRICE:                                                              ",data4[sab4][3])
                        print("DISCOUNTED PRICE:                                   ",data4[sab4][4])
                        print("DISCOUNT % GIVEN:                                  ",data4[sab4][5])
                        print("QUANTITY:                                                    ",data4[sab4][6])
                        print("MFG DATE:                                                    ",data4[sab4][7])
                        print("EXP DATE:                                                      ",data4[sab4][8],"\n")
                ask4= input("\nDo you wish to buy any item? (y/n): ")
                if ask4=="y":
                        purchase("nutrition_fitness_supplements")
                else:
                        print("\n\n\t\t\t\t\t\t......$$Going back to the Main ItemList$$...\n\n")
                        items()
        elif say==5:
                def PersonalC():
                        print("\n\nThere are the following subcategories in this 'Personal Care' Cateogory: ")
                        print("A.  Skin care")
                        print("B.  Oral Care")
                        print("C.  Hair Care")
                        print("D.  Man care")
                        print("E.  Women Care")
                        print("F.  Weight  Care")
                        sub=input("Enter which subcategory you want to explore(A/B/C/D/E/F): ")
                        if sub=="A":
                                print("The medicines in the 'Skin Care' sub-category are as follows: ")
                                allo_1= "select * from personal_care where Category= 'Skin Care' "
                                cursor.execute(allo_1)
                                data_1=cursor.fetchall()
                                for sab_1 in range(len(data_1)):
                                        print("Sr. No.:                                                             ", (sab_1)+1,"\n")
                                        print("PRODUCT ID:                                                 ",data_1[sab_1][0])
                                        print("NAME OF THE PRODUCT:                          ",data_1[sab_1][1])
                                        print("DOSAGE:                                                         ",data_1[sab_1][2])
                                        print("PRICE:                                                             ",data_1[sab_1][3])
                                        print("DISCOUNTED PRICE:                                   ",data_1[sab_1][4])
                                        print("DISCOUNT % GIVEN:                                  ",data_1[sab_1][5])
                                        print("QUANTITY:                                                    ",data_1[sab_1][6])
                                        print("MFG DATE:                                                    ",data_1[sab_1][7])
                                        print("EXP DATE:                                              ",data_1[sab_1][8],"\n")
                                ask_1= input("\nDo you wish to buy any item? (y/n): ")
                                if ask_1=="y":
                                        purchase("personal_care")
                                else:
                                        print("1. Switch to Main ItemList")
                                        print("2. Switch to Personal Care sub-category List")
                                        say1= int(input("Choose where you want to go back to(1/2): "))
                                        if say1==1:
                                                print("\n\n\t\t\t\t\t\t......$$Going back to the Main ItemList$$...\n\n")
                                                items()
                                        else:
                                                print("\n\n\t\t\t\t\t\t.....$$Going back to the Personal Care sub-category List$$.......\n\n")
                                                PersonalC()
                        if sub=="B":
                                print("The medicines in the 'Oral Care' sub-category are as follows: ")
                                allo_2= "select * from personal_care where Category= 'Oral Care' "
                                cursor.execute(allo_2)
                                data_2=cursor.fetchall()
                                for sab_2 in range(len(data_2)):
                                        print("Sr. No.:                                                             ", (sab_2)+1,"\n")
                                        print("PRODUCT ID:                                                 ",data_2[sab_2][0])
                                        print("NAME OF THE PRODUCT:                          ",data_2[sab_2][1])
                                        print("DOSAGE:                                                         ",data_2[sab_2][2])
                                        print("PRICE:                                                             ",data_2[sab_2][3])
                                        print("DISCOUNTED PRICE:                                   ",data_2[sab_2][4])
                                        print("DISCOUNT % GIVEN:                                  ",data_2[sab_2][5])
                                        print("QUANTITY:                                                    ",data_2[sab_2][6])
                                        print("MFG DATE:                                                    ",data_2[sab_2][7])
                                        print("EXP DATE:                                              ",data_2[sab_2][8],"\n")
                                ask_2= input("\nDo you wish to buy any item? (y/n): ")
                                if ask_2=="y":
                                        purchase("personal_care")
                                else:
                                        print("1. Switch to Main ItemList")
                                        print("2. Switch to Personal Care sub-category List")
                                        say2= int(input("Choose where you want to go back to(1/2): "))
                                        if say2==1:
                                                print("\n\n\t\t\t\t\t\t......$$Going back to the Main ItemList$$...\n\n")
                                                items()
                                        else:
                                                print("\n\n\t\t\t\t\t\t.....$$Going back to the Personal Care sub-category List$$.......\n\n")
                                                PersonalC()
                        if sub=="C": 
                                print("The medicines in the 'Hair Care' sub-category are as follows: ")
                                allo_3= "select * from personal_care where Category= 'Hair Care' "
                                cursor.execute(allo_3)
                                data_3=cursor.fetchall()
                                for sab_3 in range(len(data_3)):
                                        print("Sr. No.:                                                       ", (sab_3)+1,"\n")
                                        print("PRODUCT ID:                                           ",data_3[sab_3][0])
                                        print("NAME OF THE PRODUCT:                      ",data_3[sab_3][1])
                                        print("DOSAGE:                                                  ",data_3[sab_3][2])
                                        print("PRICE:                                                       ",data_3[sab_3][3])
                                        print("DISCOUNTED PRICE:                               ",data_3[sab_3][4])
                                        print("DISCOUNT % GIVEN:                               ",data_3[sab_3][5])
                                        print("QUANTITY:                                               ",data_3[sab_3][6])
                                        print("MFG DATE:                                               ",data_3[sab_3][7])
                                        print("EXP DATE:                                                ",data_3[sab_3][8],"\n")
                                ask_3= input("\nDo you wish to buy any item? (y/n): ")
                                if ask_3=="y":
                                        purchase("personal_care")
                                else:
                                        print("1. Switch to Main ItemList")
                                        print("2. Switch to Personal Care sub-category List")
                                        say3= int(input("Choose where you want to go back to(1/2): "))
                                        if say3==1:
                                                print("\n\n\t\t\t\t\t\t......$$Going back to the Main ItemList$$...\n\n")
                                                items()
                                        else:
                                                print("\n\n\t\t\t\t\t\t.....$$Going back to the Personal Care sub-category List$$.......\n\n")
                                                PersonalC()
                        if sub=="D":
                                print("The medicines in the 'Men Care' sub-category are as follows: ")
                                allo_4= "select * from personal_care where Category= 'Man Care' "
                                cursor.execute(allo_4)
                                data_4=cursor.fetchall()
                                for sab_4 in range(len(data_4)):
                                        print("Sr. No.:                                 ", (sab_4)+1,"\n")
                                        print("PRODUCT ID:                      ",data_4[sab_4][0])
                                        print("NAME OF THE PRODUCT: ",data_4[sab_4][1])
                                        print("DOSAGE:                             ",data_4[sab_4][2])
                                        print("PRICE:                                  ",data_4[sab_4][3])
                                        print("DISCOUNTED PRICE:          ",data_4[sab_4][4])
                                        print("DISCOUNT % GIVEN:          ",data_4[sab_4][5])
                                        print("QUANTITY:                           ",data_4[sab_4][6])
                                        print("MFG DATE:                             ",data_4[sab_4][7])
                                        print("EXP DATE:                           ",data_4[sab_4][8],"\n")
                                ask_4= input("\nDo you wish to buy any item? (y/n): ")
                                if ask_4=="y":
                                        purchase("personal_care")
                                else:
                                        print("1. Switch to Main ItemList")
                                        print("2. Switch to Personal Care sub-category List")
                                        say4= int(input("Choose where you want to go back to(1/2): "))
                                        if say4==1:
                                                print("\n\n\t\t\t\t\t\t......$$Going back to the Main ItemList$$...\n\n")
                                                items()
                                        else:
                                                print("\n\n\t\t\t\t\t\t.....$$Going back to the Personal Care sub-category List$$.......\n\n")
                                                PersonalC()
                        if sub=="E":
                                        print("The medicines in the 'Women Care' sub-category are as follows: ")
                                        allo_5= "select * from personal_care where Category= 'Women Care' "
                                        cursor.execute(allo_5)
                                        data_5=cursor.fetchall()
                                        for sab_5 in range(len(data_5)):
                                                print("Sr. No.:                                    ", (sab_5)+1,"\n")
                                                print("PRODUCT ID:                        ",data_5[sab_5][0])
                                                print("NAME OF THE PRODUCT:    ",data_5[sab_5][1])
                                                print("DOSAGE:                               ",data_5[sab_5][2])
                                                print("PRICE:                                    ",data_5[sab_5][3])
                                                print("DISCOUNTED PRICE:            ",data_5[sab_5][4])
                                                print("DISCOUNT % GIVEN:           ",data_5[sab_5][5])
                                                print("QUANTITY:                            ",data_5[sab_5][6])
                                                print("MFG DATE:                            ",data_5[sab_5][7])
                                                print("EXP DATE:                             ",data_5[sab_5][8],"\n")
                                        ask_5= input("\nDo you wish to buy any item? (y/n): ")
                                        if ask_5=="y":
                                                purchase("personal_care")
                                        else:
                                                print("1. Switch to Main ItemList")
                                                print("2. Switch to Personal Care sub-category List")
                                                say5= int(input("Choose where you want to go back to(1/2): "))
                                                if say5==1:
                                                        print("\n\n\t\t\t\t\t\t......$$Going back to the Main ItemList$$...\n\n")
                                                        items()
                                                else:
                                                        print("\n\n\t\t\t\t\t\t.....$$Going back to the Personal Care sub-category List$$.......\n\n")
                                                        PersonalC()
                        if sub=="F":
                                print("The medicines in the 'Weight Care' sub-category are as follows: ")
                                allo_6= "select * from personal_care where Category= 'Wgt Care' "
                                cursor.execute(allo_6)
                                data_6=cursor.fetchall()
                                for sab_6 in range(len(data_6)):
                                        print("Sr. No.:", (sab_6)+1)
                                        print("PRODUCT ID:",data_6[sab_6][0])
                                        print("NAME OF THE PRODUCT:",data_6[sab_6][1])
                                        print("DOSAGE:",data_6[sab_6][2])
                                        print("PRICE:",data_6[sab_6][3])
                                        print("DISCOUNTED PRICE:",data_6[sab_6][4])
                                        print("DISCOUNT % GIVEN:",data_6[sab_6][5])
                                        print("QUANTITY:                                                    ",data_6[sab_6][6])
                                        print("MFG DATE:                                                    ",data_6[sab_6][7])
                                        print("EXP DATE:                                                    ",data_6[sab_6][8])
                                        print(sab_6)
                                ask_6= input("\nDo you wish to buy any item? (y/n): ")
                                if ask_6=="y":
                                        purchase("personal_care")
                                else:
                                        print("1. Switch to Main ItemList")
                                        print("2. Switch to Personal Care sub-category List")
                                        say6= int(input("Choose where you want to go back to(1/2): "))
                                        if say6==1:
                                                print("\n\n\t\t\t\t\t\t......$$Going back to the Main ItemList$$...\n\n")
                                                items()
                                        else:
                                                print("\n\n\t\t\t\t\t\t.....$$Going back to the Personal Care sub-category List$$.......\n\n")
                                                PersonalC()
                
        elif say==6:
                print("\nThank you for coming! Hope we seen you soon(Please minimize this window now)\n")
                print("STAY SAFE, STAY HEALTHY\n\n")
                print("~~You Only Live Twice, Mobimeds- SAVING LIVES!~~")
                subprocess.Popen(['python', 'TKINTER GUI.py'])
                sys.exit()
        else:
                print("\nINVALID INPUT!")
                items()

def purchase(tableau):
        mycon= my.connect(host="localhost", user= "root", passwd="admin123", database= "mobimeds")
        if mycon.is_connected()==False:
                print("Error Connecting")
        else:
                print("Connection Succesful for purchase \n\n")
        cursor=mycon.cursor()
        prodid=int(input("\nPlease enter the correct product id no. of the respective medicine, referring above: "))
        cursor.execute("select * from {}".format(tableau))
        details=cursor.fetchall()
        for i in details:
                if i[0]==prodid:
                        print("\nThe details of the medicine selected by you are: \n")
                        print("NAME:                                                                                  ",i[1])
                        print("DOSAGE:                                                                              ",i[2])
                        print("PRICE:                                                                                   ",i[3])
                        print("NEW PRICE AFTER DISCOUNT:                                     ",i[4])
                        print("DISCOUNT %:                                                                     ",i[5])
                        print("QUANTITY OF MEDICINE(IN ONE TAB/BOTTLE):   ",i[6])
                        print("MFG. DATE:                                                                        ",i[7])
                        print("EXP. DATE:                                                                          ",i[8])
                        Plist.append([prodid,tableau])
                        Dlist.append(i[4])                        
                        ask2= input("\nWant to buy more items?(y/n): ")                        
                        if ask2=="y":
                                items()
                        elif ask2=="n":
                                bill()
                        break

def bill():
        print("\n\n\t\t\t\t\t\t\t.....Preparing the bill.....\n")
        reg_status = registered()
        if reg_status==False:
                print("Since you aren't registered, hence you won't be eligible for the Special Membership Offer. However, the billing will continue nevertheless.\n")
                t1=billing()
                print("GRAND TOTAL = ", t1)
                ending()
        else:
                print("\nCongratulations! Since you are a registered member, you are eligible for our special discount service.\n")
                t2=billing()
                ids=((t2)*0.2)
                Final=t2-ids
                print("GRAND TOTAL(After 20% deduction)= ", Final,"\n\n")
                ending()

def billing():
        mycon= my.connect(host="localhost", user= "root", passwd="admin123", database= "mobimeds")
        if mycon.is_connected()==False:
                print("Error Connecting")
        else:
                print("Connection Succesful iygyf76f7f \n\n")
        cursor=mycon.cursor()
        discount_total= sum(Dlist)
        print("\n\n\t\t\t\t\t\t\t ##Your Summary:##\n\n")
        for i in Plist:
                so="select * from {} where Prdt_id={}".format(i[1],i[0])
                cursor.execute(so)
                DETA=cursor.fetchall()
                for i in DETA:
                        print("\nNAME: ",i[1])
                        print("DOSAGE: ",i[2])
                        print("PRICE: ",i[3])
                        print("NEW PRICE AFTER DISCOUNT: ",i[4])
                        print("DISCOUNT % given: ",i[5])
                        print("QUANTITY OF MEDICINE(INONE TAB/BOTTLE): ",i[6])
                        print("MFG. DATE: ",i[7])
                        print("EXP. DATE: ",i[8])
        print("\nNet Total(Net Discounted Price): ", discount_total)
        return discount_total

def register():
        print("Greetings Customer! Registered Customers will get an exclusive  membership. Perks of being a member is that you will get exclusive discounts and offers.\n")
        name= input("Enter your name:            ")
        age=int(input("Enter your age:              "))
        gen= input("Enter you Gender(M/F/T):  ")
        add= input("Enter your address(only enter Flat/residence no., Flat/residence name,city & Pincode):        ")
        phn= int(input("Enter your 10 digit mobile number:   "))
        regis= open("Patient.csv","a")
        customwriter=csv.writer(regis)
        plist=[name,age,gen,add,phn]
        customwriter.writerow(plist)
        print("\nRegistered Successfully! Your details are: \n",plist)
        regis.close()
        items()

def registered():
        phone= int(input("Enter your Mobile Number: "))
        for customers in patientlist:
                if customers[4]==str(phone):
                    print(customers)
                    print("\n\nYes, You are registered! Hence we will offer you 20% off on your Grand Total.\n\n")
                    registry.close()
                    return True
        return False

def ending():
        print("The items will be delivered within 48 hours by one of our employees. Thank you for shopping. Please Visit again. Click on the cross on the top right hand corner.\n\n")
        print("YOU ONLY LIVE TWICE, MOBIMEDS-SAVING LIVES! y ")
        

mycon.close()
