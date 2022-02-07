from tkinter import *
#creating window base
root=Tk()
root.title("CALCULATOR")
root.geometry("660x670")  #size of window
root.resizable(0,0)  #prevents resizing of window

def button_click(item):
    global expression
    expression=expression+str(item)
    input_text.set(expression)

def button_clear():  #clears the input field
    global expression
    expression=""
    input_text.set("")

def button_equal():
    global expression
    result=str(eval(expression))    #evaluates the string expression directly
    input_text.set(result)
    expression=""

expression=""
#StringVar() is used to get the instance of input field
input_text=StringVar()
#creating a frame for the input field
input_frame=Frame(root, width=600, height=100, bd=0, highlightcolor="black", highlightthickness=1)
input_frame.pack(side=TOP)
#creating a inut field inside the frame
input_field=Entry(input_frame,font=('arial',57,'bold'),textvariable=input_text,width=50,justify=RIGHT)
input_field.grid(row=0,column=0)
input_field.pack(ipady=60) #internal padding to increase the height of input field

#creating another 'Frame' for the button below the 'input_frame'
buttons_frame=Frame(root,width=600,height=600, bg="grey")
buttons_frame.pack()

#first row
clear=Button(buttons_frame, text="C", fg="black", width=70, height=7, bd=0, bg="#eee", cursor="hand2",command=lambda: button_clear()).grid(row=0, column=0,columnspan=3, padx=3, pady=1)
divide = Button(buttons_frame, text="/", fg="black", width=20, height=7, bd=0, bg="#eee", cursor="hand2",
                command=lambda: button_click("/")).grid(row=0, column=3, padx=3, pady=1)

# second row

seven = Button(buttons_frame, text="7", fg="black", width=22, height=5, bd=0, bg="#fff", cursor="hand2",
               command=lambda: button_click(7)).grid(row=1, column=0, padx=1, pady=1)

eight = Button(buttons_frame, text="8", fg="black", width=22, height=5, bd=0, bg="#fff", cursor="hand2",
               command=lambda: button_click(8)).grid(row=1, column=1, padx=1, pady=1)

nine = Button(buttons_frame, text="9", fg="black", width=22, height=5, bd=0, bg="#fff", cursor="hand2",
              command=lambda: button_click(9)).grid(row=1, column=2, padx=1, pady=1)

multiply = Button(buttons_frame, text="*", fg="black", width=20, height=5, bd=0, bg="#eee", cursor="hand2",
                  command=lambda: button_click("*")).grid(row=1, column=3, padx=1, pady=1)

# third row

four = Button(buttons_frame, text="4", fg="black", width=22, height=5, bd=0, bg="#fff", cursor="hand2",
              command=lambda: button_click(4)).grid(row=2, column=0, padx=1, pady=1)

five = Button(buttons_frame, text="5", fg="black", width=22, height=5, bd=0, bg="#fff", cursor="hand2",
              command=lambda: button_click(5)).grid(row=2, column=1, padx=1, pady=1)

six = Button(buttons_frame, text="6", fg="black", width=22, height=5, bd=0, bg="#fff", cursor="hand2",
             command=lambda: button_click(6)).grid(row=2, column=2, padx=1, pady=1)

minus = Button(buttons_frame, text="-", fg="black", width=20, height=5, bd=0, bg="#eee", cursor="hand2",
               command=lambda: button_click("-")).grid(row=2, column=3, padx=1, pady=1)

# fourth row

one = Button(buttons_frame, text="1", fg="black", width=22, height=5, bd=0, bg="#fff", cursor="hand2",
             command=lambda: button_click(1)).grid(row=3, column=0, padx=1, pady=1)

two = Button(buttons_frame, text="2", fg="black", width=22, height=5, bd=0, bg="#fff", cursor="hand2",
             command=lambda: button_click(2)).grid(row=3, column=1, padx=1, pady=1)

three = Button(buttons_frame, text="3", fg="black", width=22, height=5, bd=0, bg="#fff", cursor="hand2",
               command=lambda: button_click(3)).grid(row=3, column=2, padx=1, pady=1)

plus = Button(buttons_frame, text="+", fg="black", width=20, height=5, bd=0, bg="#eee", cursor="hand2",
              command=lambda: button_click("+")).grid(row=3, column=3, padx=1, pady=1)

# fourth row

zero = Button(buttons_frame, text="0", fg="black", width=46, height=5, bd=0, bg="#fff", cursor="hand2",
              command=lambda: button_click(0)).grid(row=4, column=0, columnspan=2, padx=4, pady=1)

point = Button(buttons_frame, text=".", fg="black", width=22, height=5, bd=0, bg="#eee", cursor="hand2",
               command=lambda: button_click(".")).grid(row=4, column=2, padx=5, pady=1)

equals = Button(buttons_frame, text="=", fg="black", width=20, height=5, bd=0, bg="#eee", cursor="hand2",
                command=lambda: button_equal()).grid(row=4, column=3, padx=2, pady=1)


root.mainloop()
