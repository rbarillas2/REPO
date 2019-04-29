from tkinter import *

MyCalc = Tk()

calc = 0.0
math_op = ''

#window

MyCalc.title("CALCULATOR")
MyCalc.geometry("300x350")
MyCalc.configure(background="grey")
MyCalc.resizable(width=False,height=False)

#calculator

def num_btn_click(value):
    global calc
    if value != 'C':
        var = inp.get() + value
        inp.delete(0,"end")
        inp.insert(0,var)
    else:
        inp.delete(0,"end")
        calc = 0.0

def math_btn_click(value):
    global calc
    global math_op
    try:
        if value != '=':
            calc = float(inp.get())
            print("cals is",calc)
            inp.delete(0,"end")
            
        if value == '+':
            math_op = '+'
        elif value == '-':
            math_op = '-'
        elif value == '*':
            math_op = '*'
        elif value == '/':
            math_op = '/'
        elif value == '=':
            print("value1:",calc,"value2:",inp.get())
            if math_op == '+':
                ans = calc + float(inp.get())
            elif math_op == '-':
                ans = calc - float(inp.get())
            elif math_op == '*':
                ans = calc * float(inp.get())
            elif math_op == '/':
                ans = calc / float(inp.get())    
            inp.delete(0,"end")
            if math_op !='':
                inp.insert(0,str(ans))
            
    except ValueError:
        print("wrong value","calc=",calc,"mathop=",math_op)
        inp.delete(0,"end")
    
inp = Entry(width="32")
inp.grid(row=0,columnspan=4,padx=2,pady=2)

#buttons
    
Btn7 = Button(MyCalc,height=3,width=7,text="7", highlightbackground='blue' ,command=lambda: num_btn_click('7'))
Btn7.grid(row=2,column=0,padx=2,pady=5)

Btn8 = Button(MyCalc,height=3,width=7,text="8", highlightbackground='blue' ,command=lambda: num_btn_click('8'))
Btn8.grid(row=2,column=1,padx=2,pady=5)

Btn9 = Button(MyCalc,height=3,width=7,text="9", highlightbackground='blue' ,command=lambda: num_btn_click('9'))
Btn9.grid(row=2,column=2,padx=2,pady=5)

BtnDivide = Button(MyCalc,height=3,width=7,text="/",command=lambda: math_btn_click('/'))
BtnDivide.grid(row=2,column=3,padx=2,pady=5)

Btn4 = Button(MyCalc,height=3,width=7,text="4", highlightbackground='blue' ,command=lambda: num_btn_click('4'))
Btn4.grid(row=3,column=0,padx=2,pady=5)

Btn5 = Button(MyCalc,height=3,width=7,text="5", highlightbackground='blue' ,command=lambda: num_btn_click('5'))
Btn5.grid(row=3,column=1,padx=2,pady=5)

Btn6 = Button(MyCalc,height=3,width=7,text="6", highlightbackground='blue' ,command=lambda: num_btn_click('6'))
Btn6.grid(row=3,column=2,padx=2,pady=5)

BtnMultiply = Button(MyCalc,height=3,width=7,text="*",command=lambda: math_btn_click('*'))
BtnMultiply.grid(row=3,column=3,padx=2,pady=5)

Btn1 = Button(MyCalc,height=3,width=7,text="1", highlightbackground='blue' ,command=lambda: num_btn_click('1'))
Btn1.grid(row=4,column=0,padx=2,pady=5)

Btn2 = Button(MyCalc,height=3,width=7,text="2", highlightbackground='blue' ,command=lambda: num_btn_click('2'))
Btn2.grid(row=4,column=1,padx=2,pady=5)

Btn3 = Button(MyCalc,height=3,width=7,text="3", highlightbackground='blue' ,command=lambda: num_btn_click('3'))
Btn3.grid(row=4,column=2,padx=2,pady=5)

BtnSubtract = Button(MyCalc,height=3,width=7,text="-",command=lambda: math_btn_click('-'))
BtnSubtract.grid(row=4,column=3,padx=2,pady=5)

Btn0 = Button(MyCalc,height=3,width=7,text="0", highlightbackground='blue',command=lambda: num_btn_click('0'))
Btn0.grid(row=5,column=0,padx=2,pady=5)

Btn0 = Button(MyCalc,height=3,width=32,text="AC",command=lambda: num_btn_click('C'))
Btn0.grid(row=6,rowspan=5,columnspan=7,column=0,padx=2,pady=5)

BtnEqual = Button(MyCalc,height=3,width=7,text="=",command=lambda: math_btn_click('='))
BtnEqual.grid(row=5,column=2,padx=2,pady=5)

BtnPlus = Button(MyCalc,height=3,width=7,text="+",command=lambda: math_btn_click('+'))
BtnPlus.grid(row=5,column=3,padx=2,pady=5)

BtnPer = Button(MyCalc,height=3,width=7,text=".",command=lambda: num_btn_click('.'))
BtnPer.grid(row=5,column=1,padx=2,pady=5)



MyCalc.mainloop()

