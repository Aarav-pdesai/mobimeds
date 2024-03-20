import threading
from Customer import *
from owner import *
from tkinter import *
from PIL import ImageTk,Image
import PIL
import pygame

pygame.init()
window = Tk()
window.title('mobimeds')
photo = PhotoImage(file = "C:\\Users\parim\\Desktop\\snake logo.ico")
window.iconphoto(False, photo)
#buttons,labels and functions

pygame.mixer.music.load("moment-14023.mp3")
pygame.mixer.music.play(-1)
def on_close():
    pygame.mixer.music.stop()  # Stop the music when the window is closed
    window.destroy()
window.protocol("WM_DELETE_WINDOW", on_close)


passw_var=StringVar()
def submit():
    password=passw_var.get()
    if password=="enigma":
        openowner()
        
        
    elif password!="enigma":
        passw_var.set("")


#customer
def purchase():
    threading.Thread(target=items).start()
    #items() function is from customer module
def register1():
    threading.Thread(target=register).start()
def opencustomer():
    newWindow1 = Toplevel(window)
    newWindow1.title("CUSTOMER")
    canvas1= Canvas(newWindow1, width= 1526, height=1000,bg='lightblue')
    canvas1.pack()
    l1 = Label(newWindow1, height = 5, width = 53,bg="lightblue",text="what would you like to do?",fg="green")
    l1.config(font=("Times new roman",24))
    l1.place(x=290,y=20)
    btn3=Button(newWindow1,height=3,width=28, borderwidth=5,command = lambda:[newWindow1.destroy(), register1(), window.destroy()]) 
    btn3.config(font=("Impact",30), fg="navy",bg="red",text="REGISTER\n(special discount for members)")
    btn3.place(x=460,y=400)
    btn4=Button(newWindow1,height=3,width=28, borderwidth=5,command = lambda:[newWindow1.destroy(), purchase(), window.destroy()])
    btn4.config(font=("Impact",30),fg="navy",bg="red",text="PURCHASE")
    btn4.place(x=460,y=200)
    ex4 = Button(newWindow1,text = "Exit",height=1,width=6, command = newWindow1.destroy)
    ex4.place(x=720,y=700)

        
    
#owner
def openpassword():
    newWindow3 = Toplevel(window)
    newWindow3.title("Please enter the password")
    canvas1= Canvas(newWindow3, width= 1550, height=1500,bg='lightblue')
    canvas1.pack()
    #textbox
    t=Entry(newWindow3,width=30,show="*",textvariable=passw_var)
    t.place(x=700,y=200)
    #submit button
    sub_btn=Button(newWindow3,text = 'Submit', command = lambda:[submit(),newWindow3.destroy()])
    sub_btn.place(x=755,y=250)
    #label
    l = Label(newWindow3, height = 1, width = 53,bg="lightblue",text="AUTHORIZATION CODE REQUIRED",fg="red",font="Verdana 15 underline")
    #l.config(font=(15)
    l.place(x=470,y=140)
def empmang():
    threading.Thread(target=Employee).start()
    #employee_management() from owner module
    #threading prevents the freezing/crashing issue
    #by shifting the high time-complexity tasks to a different thread
    
def prodmang():
    threading.Thread(target=Product).start()
    #product_management() from owner module
    

def openowner():
    newWindow2 = Toplevel(window)
    newWindow2.title("OWNER")
    canvas2= Canvas(newWindow2, width= 1550, height= 1500,bg='lightblue')
    canvas2.pack()
    l1 = Label(newWindow2, height = 5, width = 53,bg="lightblue",text="what would you like to do?",fg="green")
    l1.config(font=("Times new roman",24))
    l1.place(x=290,y=20)
    btn5=Button(newWindow2,height=3,width=28, borderwidth=5, command= lambda: [empmang(),newWindow2.destroy(),window.destroy()])
    btn5.config(font=("Impact",30),fg="green",bg="yellow",text="EMPLOYEE MANAGEMENT")
    btn5.place(x=460,y=200)
    
    b6=Button(newWindow2,height=3,width=28, borderwidth=5,command=lambda: [prodmang(), newWindow2.destroy(), window.destroy()])
    b6.config(font=("Impact",30),fg="green",bg="yellow",text="PRODUCT MANAGEMENT")
    b6.place(x=460,y=500)
    
    ex3 = Button(newWindow2,text = "Exit",height=1,width=6, command = newWindow2.destroy)
    ex3.place(x=720,y=700)

#rgb function
def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb  

    
#Create a canvas
canvas= Canvas(window, width= 1526, height= 1000,bg='lightblue')
canvas.pack()

f = Frame(window)
f.place(x=480, y=690)

scrollbar = Scrollbar(f)
t = Text(f, height=3, width=70, yscrollcommand=scrollbar.set)
t.insert(index=1.0,chars='''Courtesy of advancements in medical science, today's healthcare systemhas become highly complex and segmented. As a result pharmacy store owners have to keep an up-to-date account of a myriad of medications at their disposal.''')
scrollbar.config(command=t.yview)
scrollbar.pack(side=RIGHT, fill=Y)
t.pack(side="left")
t.config(state="disabled")

#Load an image in the script
img2=(Image.open("C:\\Users\\parim\\Pictures\\medical background.jpg"))
img= (Image.open("C:\\Users\\parim\\Pictures\\final2background.png"))

#Resize the Image using resize method
resized_image2=img2.resize((1526,1000), PIL.Image.LANCZOS)
new_image2=ImageTk.PhotoImage(resized_image2)
resized_image= img.resize((600,300), PIL.Image.LANCZOS)
new_image= ImageTk.PhotoImage(resized_image)

#Add image to the Canvas Items
canvas.create_image(0,0, anchor=NW, image=new_image2)
canvas.create_image(470,100,anchor=NW, image=new_image)    

click_btn= PhotoImage(file='C:\\Users\\parim\\Pictures\\customer.png')
btn=Button(window,height=50,width=460,image=click_btn, borderwidth=5, command=opencustomer)
btn.place(x=520,y=470)
#button 2 image
click_btn2=PhotoImage(file="C:\\Users\\parim\\Pictures\\owner.png")
btn2=Button(window,height=50,width=460,image=click_btn2, borderwidth=5,command=openpassword)
btn2.place(x=520,y=560)


l = Label(window, height = 1, width = 53,text="~Welcome to Mobimeds! The person using this app is:...~",fg="green")
l.config(font=(15),bg=_from_rgb((205,235,233)))
l.place(x=490,y=420)

ex=Button(window,text = "Exit",height=1,width=6, command = window.destroy)
ex.place(x=750,y=650)

window.mainloop()                                                                                                              
