from tkinter import *
from customtkinter import *
calculation = '' 

button_grid = [ 
    ('C',1,0),('D',1,2),('%',1,3),
    (1,2,0),(2,2,1),(3,2,2),('x',2,3),
    (4,3,0),(5,3,1),(6,3,2), ('-',3,3), 
    (7,4,0),(8,4,1),(9,4,2),('+',4,3),
    (0,5,0),('.',5,2),('=',5,3)
]

def add_expression(expression,result_screen):
    global calculation
    calculation = calculation + str(expression) 
    print(calculation)
    result_screen.config(text=calculation)


def calculate(result_screen):
    global calculation    
    try:
        result = str(eval(calculation))  
        result_screen.config(text=result)
        calculation = result
    except: 
        result_screen.config(text='ERROR')  
        print('Error') 
    
   

def delete(result_screen):
    global calculation
    new_calculation = calculation[:-1] 
    calculation = new_calculation 
    result_screen.config(text=calculation)
    print(calculation)

def clear(result_screen):
    global calculation 
    calculation = '' 
    result_screen.config(text=calculation)

def main():
    window = Tk()    
    button_frame = Frame(window)
    button_frame.grid(row=1)
    #SCREEN
    result_screen = Label(window,text='0',background='white',width=19,height=1,font=6)
    result_screen.grid(row=0)
    
    for i in button_grid: 
        if i[0] == 'C' :
            Button(button_frame,text=i[0],width=10,height=2,background='lightgrey',command=lambda value=f'{i[0]}':clear(result_screen)).grid(row=i[1],column=i[2],columnspan=2,padx=5,pady=5)
        elif i[0]=='D':
            Button(button_frame,text=i[0],width=4,height=2,background='red',command=lambda value=f'{i[0]}':delete(result_screen)).grid(row=i[1],column=i[2],padx=5,pady=5)
        elif i[0]==0 :
            Button(button_frame,text=i[0],width=10,height=2,command=lambda value=f'{i[0]}':add_expression(value,result_screen)).grid(row=i[1],column=i[2],columnspan=2,padx=5,pady=5)
        elif i[0]=='=':
            Button(button_frame,text=i[0],width=4,height=2,background='orange',command=lambda :calculate(result_screen)).grid(row=i[1],column=i[2],padx=5,pady=5)
        elif i[0] == 'x' :
            Button(button_frame,text=i[0],width=4,height=2,background='orange',command=lambda value='*':add_expression(value,result_screen)).grid(row=i[1],column=i[2],padx=5,pady=5)
        elif  i[0]=='+' or i[0]=='-' or i[0]=='%': 
            Button(button_frame,text=i[0],width=4,height=2,background='orange',command=lambda value=f'{i[0]}':add_expression(value,result_screen)).grid(row=i[1],column=i[2],padx=5,pady=5)
        else : 
            Button(button_frame,text=i[0],width=4,height=2,command=lambda value=f'{i[0]}':add_expression(value,result_screen)).grid(row=i[1],column=i[2],padx=5,pady=5)

    window.mainloop()

if __name__ == '__main__':
    main()