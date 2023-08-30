import tkinter as tk
field_text=""
def add_to_field(sth):
    global field_text
    field_text=field_text+str(sth)
    field.delete("1.0","end")
    field.insert("1.0",field_text)
def calculate():
    global field_text
    result=str(eval(field_text))
    field.delete("1.0","end")
    field.insert("1.0",result)
def clear():
    global field_text
    field_text=""
    field.delete("1.0","end")
    
    
window=tk.Tk()
window.geometry("340x350")
field=tk.Text(window,height=2,width=21,font=("Times New Roman",20))
field.grid(row=1,column=1,columnspan=4)

button1=tk.Button(window,text='1',command=lambda:add_to_field(1),width=5,font=("Times New Roman",20))
button1.grid(row=4,column=1)

button2=tk.Button(window,text='2',command=lambda:add_to_field(2),width=5,font=("Times New Roman",20))
button2.grid(row=4,column=2)

button3=tk.Button(window,text='3',command=lambda:add_to_field(3),width=5,font=("Times New Roman",20))
button3.grid(row=4,column=3)

button4=tk.Button(window,text='4',command=lambda:add_to_field(4),width=5,font=("Times New Roman",20))
button4.grid(row=3,column=1)

button5=tk.Button(window,text='5',command=lambda:add_to_field(5),width=5,font=("Times New Roman",20))
button5.grid(row=3,column=2)

button6=tk.Button(window,text='6',command=lambda:add_to_field(6),width=5,font=("Times New Roman",20))
button6.grid(row=3,column=3)

button7=tk.Button(window,text='7',command=lambda:add_to_field(7),width=5,font=("Times New Roman",20))
button7.grid(row=2,column=1)

button8=tk.Button(window,text='8',command=lambda:add_to_field(8),width=5,font=("Times New Roman",20))
button8.grid(row=2,column=2)

button9=tk.Button(window,text='9',command=lambda:add_to_field(9),width=5,font=("Times New Roman",20))
button9.grid(row=2,column=3)

button0=tk.Button(window,text='0',command=lambda:add_to_field(0),width=5,font=("Times New Roman",20))
button0.grid(row=5,column=1)

button_div=tk.Button(window,text='/',command=lambda:add_to_field("/"),width=5,font=("Times New Roman",20))
button_div.grid(row=2,column=4)

button_times=tk.Button(window,text='*',command=lambda:add_to_field("*"),width=5,font=("Times New Roman",20))
button_times.grid(row=3,column=4)

button_add=tk.Button(window,text='+',command=lambda:add_to_field("+"),width=5,font=("Times New Roman",20))
button_add.grid(row=4,column=4)

button_clear=tk.Button(window,text='clear',command=lambda:clear(),width=5,font=("Times New Roman",20))
button_clear.grid(row=5,column=3)

button_sub=tk.Button(window,text='-',command=lambda:add_to_field("-"),width=5,font=("Times New Roman",20))
button_sub.grid(row=5,column=4)


button_dic=tk.Button(window,text='.',command=lambda:add_to_field("."),width=5,font=("Times New Roman",20))
button_dic.grid(row=5,column=2)

button_cal=tk.Button(window,text='=',command=lambda:calculate(),width=5,font=("Times New Roman",20))
button_cal.grid(row=6,column=1,columnspan=4)

window.mainloop()
