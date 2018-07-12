# coding:utf8
# author:Deylies,WangYu

import sys
import Tkinter as tk
from PIL import Image, ImageTk
import tkFont
import os
reload(sys)
sys.setdefaultencoding('utf-8')

HEIGHT = 500
WIDTH = 800
TITLE = "DeyLies微信服务"
ABS_PATH = os.getcwd()

class Client(object):
    def __init__(self, height, width, title):
        self.master = tk.Tk()
        self.height = height
        self.width = width
        self.title = title
        self.initiazation()

    def initiazation(self):
        self.master.geometry(self.centerization(self.width, self.height))
        self.master.title(self.title)

    def centerization(self, width, height):
        screen_width = self.master.winfo_screenwidth()
        screen_hight = self.master.winfo_screenheight()
        return '%sx%s+%s+%s' % (width, height, (screen_width - width) / 2, (screen_hight - height) / 2)

    def start(self):
        self.master.mainloop()


class Frame(tk.Frame):
    def __init__(self, master, x=0, y=0, anchor='nw', width=0, height=0, bg='red'):
        tk.Frame.__init__(self, master)
        self.master = master
        self.location = (x, y, anchor)
        if all([width, height]):
            self.size = (width, height)
        else:
            self.master.update()
            self.size = (self.master.winfo_width(), self.master.winfo_height())
        self.bg = bg
        self.frame = self.create(self.size, self.bg)
        self.pack(fill=tk.BOTH, expand=1)
        self.place(self.location)

    def show_login_img(self, path, location=(0, 0, 'nw')):
        loginIm = Image.open(path)
        img = ImageTk.PhotoImage(loginIm)
        imLabel = tk.Label(self.frame, image=img)
        imLabel.image = img
        # imLabel.place(x=location[0],y=location[1],anchor=location[2])
        imLabel.place(x=location[0], y=location[1], anchor=location[2])

    def create(self, size, bg):
        return tk.Frame(width=size[0], height=size[1], bg=bg)

    def backgroud_img(self, path):
        img = Image.open(path)
        img = img.resize((self.size[0],self.size[1]))
        img = ImageTk.PhotoImage(img)
        bgLable = tk.Label(self.frame, text="pic",image=img)
        bgLable.img=img
        bgLable.place(x=0, y=0)
        self.frame.update()

    def place(self, location):
        self.frame.place(x=location[0], y=location[1], anchor=location[2])

    def hide(self):
        self.frame.place_forget()

    def show(self):
        self.place(self.location)
        self.frame.update()

class Page():
    def __init__(self, client,backgroud_img=None):
        self.client=client
        self.page = Frame(client.master, bg='white')
        if backgroud_img:
            self.page.backgroud_img(backgroud_img)
        self.master = self.page.frame
        self.font = Font()
        self.x, self.y = self.page.size


    def redirect(self,page):
        self.page.hide()
        page(self.client)



class Font():
    def __init__(self):
        pass

    def getFont(self, family='Fixdsys', size=20, weight=tkFont.BOLD):
        return tkFont.Font(family=family, size=size, weight=weight)

    def show(self):
        root = tk.Tk()
        for ft in (
                'Arial', ('Courier New',), ('Comic Sans MS',), 'Fixdsys', ('MS Sans Serif',), ('MS Serif',), 'Symbol',
                'System',
                ('Times New Roman',), 'Verdana'):
            tk.Label(root, text=ft, font=ft).grid()
        root.mainloop()


count = True


def main():
    client = Client(HEIGHT, WIDTH, TITLE)
    test = Page(client.master, 0, 0, 'nw', 0, 0, 'yellow')

    def destroy():
        global count
        if count:
            count = False
            test.hide()
        else:
            count = True
            print("??")
            test.show()

    frame = tk.Frame(bg='red', width=200, height=100)
    frame.place(x=0, y=10)
    botton = tk.Button(client.master, text='destroy', command=destroy)
    test.show_login_img("../static/img/login.png", (200, 200, 'nw'))
    botton.place(x=300, y=50)
    client.master.mainloop()
    pass


if __name__ == "__main__":
    main()
