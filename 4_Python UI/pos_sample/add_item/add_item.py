#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.25
#  in conjunction with Tcl version 8.6
#    Jul 03, 2022 09:33:56 AM +0630  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import add_item_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    add_item_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    add_item_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("563x595+315+173")
        top.title("Add item")
        top.configure(background="#b8d879")
        top.configure(highlightcolor="#5e1663")

        self.txt_item_id = tk.Entry(top)
        self.txt_item_id.place(relx=0.302, rely=0.101, height=30, relwidth=0.593)

        self.txt_item_id.configure(background="white")
        self.txt_item_id.configure(disabledforeground="#a3a3a3")
        self.txt_item_id.configure(font="TkFixedFont")
        self.txt_item_id.configure(foreground="#000000")
        self.txt_item_id.configure(insertbackground="black")

        self.txt_item_name = tk.Entry(top)
        self.txt_item_name.place(relx=0.302, rely=0.218, height=30
                , relwidth=0.593)
        self.txt_item_name.configure(background="white")
        self.txt_item_name.configure(disabledforeground="#a3a3a3")
        self.txt_item_name.configure(font="TkFixedFont")
        self.txt_item_name.configure(foreground="#000000")
        self.txt_item_name.configure(insertbackground="black")

        self.btn_add_item = tk.Button(top)
        self.btn_add_item.place(relx=0.302, rely=0.706, height=44, width=347)
        self.btn_add_item.configure(activebackground="#ececec")
        self.btn_add_item.configure(activeforeground="#000000")
        self.btn_add_item.configure(background="#d9d9d9")
        self.btn_add_item.configure(command=add_item_support.btn_add_item_action)
        self.btn_add_item.configure(disabledforeground="#a3a3a3")
        self.btn_add_item.configure(foreground="#000000")
        self.btn_add_item.configure(highlightbackground="#d9d9d9")
        self.btn_add_item.configure(highlightcolor="black")
        self.btn_add_item.configure(pady="0")
        self.btn_add_item.configure(text='''Save to File''')


        self.cal_profic = tk.Button(top)
        self.cal_profic.place(relx=0.302, rely=0.8, height=44, width=347)
        self.cal_profic.configure(activebackground="#ececec")
        self.cal_profic.configure(activeforeground="#000000")
        self.cal_profic.configure(background="#d9d9d9")
        self.cal_profic.configure(command=add_item_support.cal_profic)
        self.cal_profic.configure(disabledforeground="#a3a3a3")
        self.cal_profic.configure(foreground="#000000")
        self.cal_profic.configure(highlightbackground="#d9d9d9")
        self.cal_profic.configure(highlightcolor="black")
        self.cal_profic.configure(pady="0")
        self.cal_profic.configure(text='''Calculate Profic''')




        self.txt_ratail_price = tk.Entry(top)
        self.txt_ratail_price.place(relx=0.302, rely=0.319, height=30
                , relwidth=0.593)
        self.txt_ratail_price.configure(background="white")
        self.txt_ratail_price.configure(disabledforeground="#a3a3a3")
        self.txt_ratail_price.configure(font="TkFixedFont")
        self.txt_ratail_price.configure(foreground="#000000")
        self.txt_ratail_price.configure(insertbackground="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.053, rely=0.101, height=31, width=124)
        self.Label1.configure(background="#b8d879")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Item ID''')

        self.Label1_3 = tk.Label(top)
        self.Label1_3.place(relx=0.071, rely=0.218, height=31, width=124)
        self.Label1_3.configure(activebackground="#f9f9f9")
        self.Label1_3.configure(activeforeground="black")
        self.Label1_3.configure(background="#b8d879")
        self.Label1_3.configure(disabledforeground="#a3a3a3")
        self.Label1_3.configure(foreground="#000000")
        self.Label1_3.configure(highlightbackground="#d9d9d9")
        self.Label1_3.configure(highlightcolor="black")
        self.Label1_3.configure(text='''Item Name''')

        self.Label1_4 = tk.Label(top)
        self.Label1_4.place(relx=0.071, rely=0.319, height=31, width=124)
        self.Label1_4.configure(activebackground="#f9f9f9")
        self.Label1_4.configure(activeforeground="black")
        self.Label1_4.configure(background="#b8d879")
        self.Label1_4.configure(disabledforeground="#a3a3a3")
        self.Label1_4.configure(foreground="#000000")
        self.Label1_4.configure(highlightbackground="#d9d9d9")
        self.Label1_4.configure(highlightcolor="black")
        self.Label1_4.configure(text='''Retail price''')

        self.Label1_5 = tk.Label(top)
        self.Label1_5.place(relx=0.071, rely=0.42, height=31, width=124)
        self.Label1_5.configure(activebackground="#f9f9f9")
        self.Label1_5.configure(activeforeground="black")
        self.Label1_5.configure(background="#b8d879")
        self.Label1_5.configure(disabledforeground="#a3a3a3")
        self.Label1_5.configure(foreground="#000000")
        self.Label1_5.configure(highlightbackground="#d9d9d9")
        self.Label1_5.configure(highlightcolor="black")
        self.Label1_5.configure(text='''Whole sale price''')

        self.txt_sale_price = tk.Entry(top)
        self.txt_sale_price.place(relx=0.302, rely=0.42, height=30
                , relwidth=0.593)
        self.txt_sale_price.configure(background="white")
        self.txt_sale_price.configure(disabledforeground="#a3a3a3")
        self.txt_sale_price.configure(font="TkFixedFont")
        self.txt_sale_price.configure(foreground="#000000")
        self.txt_sale_price.configure(highlightbackground="#d9d9d9")
        self.txt_sale_price.configure(highlightcolor="black")
        self.txt_sale_price.configure(insertbackground="black")
        self.txt_sale_price.configure(selectbackground="#c4c4c4")
        self.txt_sale_price.configure(selectforeground="black")

        self.txt_category_name = tk.Entry(top)
        self.txt_category_name.place(relx=0.302, rely=0.521, height=30
                , relwidth=0.593)
        self.txt_category_name.configure(background="white")
        self.txt_category_name.configure(disabledforeground="#a3a3a3")
        self.txt_category_name.configure(font="TkFixedFont")
        self.txt_category_name.configure(foreground="#000000")
        self.txt_category_name.configure(highlightbackground="#d9d9d9")
        self.txt_category_name.configure(highlightcolor="black")
        self.txt_category_name.configure(insertbackground="black")
        self.txt_category_name.configure(selectbackground="#c4c4c4")
        self.txt_category_name.configure(selectforeground="black")

        self.Label1_6 = tk.Label(top)
        self.Label1_6.place(relx=0.053, rely=0.521, height=31, width=124)
        self.Label1_6.configure(activebackground="#f9f9f9")
        self.Label1_6.configure(activeforeground="black")
        self.Label1_6.configure(background="#b8d879")
        self.Label1_6.configure(disabledforeground="#a3a3a3")
        self.Label1_6.configure(foreground="#000000")
        self.Label1_6.configure(highlightbackground="#d9d9d9")
        self.Label1_6.configure(highlightcolor="black")
        self.Label1_6.configure(text='''Category Name''')

if __name__ == '__main__':
    vp_start_gui()





