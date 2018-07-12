#encoding:utf-8
'''''Tkinter教程之Font篇'''
# Tkinter中其它常用的一些功能  
'''''1.字体使用'''
# -*- coding: utf-8 -*-  
# 改变组件的显示字体  
from Tkinter import *

root = Tk()
# 创建一个Label  
for ft in (
'Arial', ('Courier New',), ('Comic Sans MS',), 'Fixdsys', ('MS Sans Serif',), ('MS Serif',), 'Symbol', 'System',
('Times New Roman',), 'Verdana'):
    Label(root, text=ft, font=ft).place(x=1,y=2)

root.mainloop() 