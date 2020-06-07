from tkinter import *
import pywhatkit as kit
import os


root = Tk()
root.title('The wisher')
root.geometry("400x420")                

def number():
    try:
        A=int(my_box1.get())
        if len(str(A))>10:
            answer1.config(text="Enter valid Number")
    except ValueError:
        answer3.config(text="Values are not correct !!!")


a = StringVar()
b = StringVar()
c = StringVar()

##################################################################################################################

my_lable1 = Label(root, text="Enter mobile number:")
my_lable1.pack(pady=5)

my_box1 = Entry(root,textvariable=a)
my_box1.pack(pady=5)

answer1 = Label(root, text="")
answer1.pack(pady=5)

###################################################################################################################

my_lable2 = Label(root, text="Enter message:")
my_lable2.pack(pady=5)

my_box2 = Entry(root,textvariable=b)
my_box2.pack(pady=5)

answer2 = Label(root, text="")
answer2.pack(pady=5)

###################################################################################################################

my_lable3 = Label(root, text="Enter Time:- Example(12:05)")
my_lable3.pack(pady=5)

my_box3 = Entry(root,textvariable=c)
my_box3.pack(pady=5)

answer3 = Label(root, text="")
answer3.pack(pady=5)

#####################################################################################################################

my_button1 = Button(root,text="Wish and Sleep",command=number)
my_button1.pack(pady=5)

root.mainloop()

######################################################################################################################

number=a.get()
message=b.get()
time=c.get()

add="+91"

if number[0]!='+':
    number=add+number 

h,m=time.split(':')
h=int(h)
m=int(m)

kit.sendwhatmsg(number ,message, h,m)
os.system("shutdown /s /t 1");

 

