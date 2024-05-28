import os
import tkinter as tk
from tkinter import ttk

def get_names() -> list[str]:
    with open('names.txt',encoding='utf-8') as file:
        content:str = file.read()
    names:list[str] = content.split()
    return names
class window(tk.Tk):
    def __init__(self,title:str="Hello Tkinter",**kwargs):
        #**是指代替後續的所有...
        super().__init__(**kwargs)
        #多做一些事
        self.title(title)
        label:ttk.Label = ttk.Label(self,text="Hello! World!",font=('Arial',20,'bold'),foreground='#f00')
        label.pack(padx=100,pady=40)

        #layout有三種,pack是一種,pack是一種實體方法
    #    pack = pack_configure
    # forget = pack_forget
    # propagate = Misc.pack_propagate

if __name__ == '__main__':
    names:list[str] = get_names()
    window:tk.Tk = window(title="我的第一個GUI程式",screenName="abc")
    # window:tk.Tk = window()
    window.mainloop()
    
