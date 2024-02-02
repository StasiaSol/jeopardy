from tkinter import *
from PIL import Image, ImageTk
import os

def create_root(i):
    root1 = Tk()
    root1.title('Своя игра')
    root1.geometry(f'{width}x950')
    root1['bg']= 'steelblue1'
    if line[i][0] == '/':
        label_root = Label(root1)
        file = line[i][1:-1]
        img_file = Image.open(file).resize((400,400))
        img = ImageTk.PhotoImage(image=img_file)
        label_root.image=img
        label_root.pack(expand = True, fill=BOTH) 
    else:
        label_root = Label(root1, text=line[i], bg='steelblue1',font = ('Consolas', 45,'bold'),borderwidth=5,relief="raised",wraplength=1500) 
        label_root.pack(expand = True, fill=BOTH)
    root1.mainloop()
#Label1
def command_button11():
    if but11['bg'] == 'blue':
        but11['bg'] = 'red'
        create_root(0)
def command_button21():
    if but21['bg'] == 'blue':
        but21['bg'] = 'red'
        create_root(1)
def command_button31():
    if but31['bg'] == 'blue':
        but31['bg'] = 'red'
        create_root(2)
def command_button41():
    if but41['bg'] == 'blue':
        but41['bg'] = 'red'
        create_root(3)
#label2
def command_button12():
    if but12['bg'] == 'blue':
        but12['bg'] = 'red'
        create_root(4)
def command_button22():
    if but22['bg'] == 'blue':
        but22['bg'] = 'red'
        create_root(5)       
def command_button32():
    if but32['bg'] == 'blue':
        but32['bg'] = 'red'
        create_root(6)
def command_button42():
    if but42['bg'] == 'blue':
        but42['bg'] = 'red'
        create_root(7)
#label3
def command_button13():
    if but13['bg'] == 'blue':
        but13['bg'] = 'red'
        create_root(8)
def command_button23():
    if but23['bg'] == 'blue':
        but23['bg'] = 'red'
        create_root(9)
        
def command_button33():
    if but33['bg'] == 'blue':
        but33['bg'] = 'red'
        create_root(10)
def command_button43():
    if but43['bg'] == 'blue':
        but43['bg'] = 'red'
        create_root(11)
#label4
def command_button1():
    if but14['bg'] == 'blue':
        but14['bg'] = 'red'
        create_root(12)
def command_button2():
    if but24['bg'] == 'blue':
        but24['bg'] = 'red'
        create_root(13)
def command_button3():
    if but34['bg'] == 'blue':
        but34['bg'] = 'red'
        create_root(14)
def command_button4():
    if but44['bg'] == 'blue':
        but44['bg'] = 'red'
        create_root(15)

if __name__=='__main__':
    root = Tk()
    root.title('Своя игра')
    width = 1500
    root.geometry(f'{width}x950')
    root['bg']= 'steelblue1'
    line = []
    theme = []
    try:
        
        with open('text.txt','r',encoding='utf-8') as file:
            for fline in file:
                line.append(fline)
        
        with open('theme.txt','r',encoding='utf-8') as file:
            for fline in file:
                theme.append(fline)
        
        label1 = Label(text=theme[0],bg='blue',font = ('Consolas', 30,'bold'),fg='white',borderwidth=5,relief="raised",wraplength=500)
        label2 = Label(text=theme[1],bg='blue',font = ('Consolas', 30,'bold'),fg='white',borderwidth=5,relief="raised",wraplength=500)
        label3 = Label(text=theme[2],bg='blue',font = ('Consolas', 30,'bold'),fg='white',borderwidth=5,relief="raised",wraplength=500)
        label4 = Label(text=theme[3],bg='blue',font = ('Consolas', 30,'bold'),fg='white',borderwidth=5,relief="raised",wraplength=500)
        label = [label1,label2,label3,label4]
        a = 0
        for x in label:
            x.place(relx=0.01,rely=a*0.24+0.02,relwidth=0.4,relheight=0.22)
            a +=1
        # label5 = Label(text='',bg='light blue',font = ('Consolas', 35,'bold'), fg = 'black',wraplength=1500)
        # label5.place(relx=0.01,rely=0.73,relwidth=0.98,relheight=0.25)
        but11 = Button(text = '100',bg='blue',font = ('Consolas', 30,'bold'),bd = '5',fg='white',command=command_button11)
        but21 = Button(text = '200',bg='blue',font = ('Consolas', 30,'bold'),bd = '5',command=command_button21,fg='white')
        but31 = Button(text = '300',bg='blue',font = ('Consolas', 30,'bold'),bd = '5',command=command_button31,fg='white')
        but41 = Button(text = '400',bg='blue',font = ('Consolas', 30,'bold'),bd = '5',command=command_button41,fg='white')
        button1 = [but11,but21,but31,but41]
        but12 = Button(text = '100',bg='blue',font = ('Consolas', 30,'bold'),bd = '5',command=command_button12,fg='white')
        but22 = Button(text = '200',bg='blue',font = ('Consolas', 30,'bold'),bd = '5',command=command_button22,fg='white')
        but32 = Button(text = '300',bg='blue',font = ('Consolas', 30,'bold'),bd = '5',command=command_button32,fg='white')
        but42 = Button(text = '400',bg='blue',font = ('Consolas', 30,'bold'),bd = '5',command=command_button42,fg='white')
        button2 = [but12,but22,but32,but42]
        but13 = Button(text = '100',bg='blue',font = ('Consolas', 30,'bold'),bd = '5',command=command_button13,fg='white')
        but23 = Button(text = '200',bg='blue',font = ('Consolas', 30,'bold'),bd = '5',command=command_button23,fg='white')
        but33 = Button(text = '300',bg='blue',font = ('Consolas', 30,'bold'),bd = '5',command=command_button33,fg='white')
        but43 = Button(text = '400',bg='blue',font = ('Consolas', 30,'bold'),bd = '5',command=command_button43,fg='white')
        button3 = [but13,but23,but33,but43]
        but14 = Button(text = '100',bg='blue',font = ('Consolas', 30,'bold'),bd = '5',command=command_button1,fg='white')
        but24 = Button(text = '200',bg='blue',font = ('Consolas', 30,'bold'),bd = '5',command=command_button2,fg='white')
        but34 = Button(text = '300',bg='blue',font = ('Consolas', 30,'bold'),bd = '5',command=command_button3,fg='white')
        but44 = Button(text = '400',bg='blue',font = ('Consolas', 30,'bold'),bd = '5',command=command_button4,fg='white')
        button4 = [but14,but24,but34,but44]
        button = [button1,button2,button3,button4]
        a,b = 0,0
        for x in button:
            for y in x:
                y.place(relx=b*0.145+0.42,rely=a*0.24+0.02,relwidth=0.135,relheight=0.22)
                b +=1
            a +=1
            b = 0    
        
        root.mainloop()
    except FileNotFoundError : root.quit()
