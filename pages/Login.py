# coding:utf8
# author:Deylies,WangYu
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from client.MainClient import Client, Page, Font
import Tkinter as tk
from tkMessageBox import showinfo
from pages import BackGroudImg
from .MainPage import UserPage

class LoginPage(Page):
    def __init__(self, client):
        Page.__init__(self, client, BackGroudImg)
        self.init_window()

    def init_window(self):
        self.lx = self.x * 0.2
        self.ly = self.y * 0.35
        self.input_length = int(0.05 * self.x)
        loginFont = self.font.getFont(family="System", size=30)
        self.LoginText = tk.Label(self.master, text="登陆", font=loginFont,
                                  fg='#9ACD32', bg='#8E8E8E')
        self.LoginText.place(x=self.x / 2, y=self.y / 4, anchor='center')
        textFont = self.font.getFont(family="System", size=12)
        self.UserText = tk.Label(self.master, text='用户名', font=textFont, bg='#8E8E8E')
        self.UserEntry = tk.Entry(self.master, width=self.input_length)
        self.PasswdText = tk.Label(self.master, text='密码', font=textFont, bg='#8E8E8E')
        self.PasswdEntry = tk.Entry(self.master, show='*', width=self.input_length)
        self.UserText.place(x=self.lx, y=self.ly)
        self.UserEntry.place(x=(self.lx + 50), y=self.ly)
        self.PasswdText.place(x=self.lx, y=(self.ly + 40))
        self.PasswdEntry.place(x=(self.lx + 50), y=(self.ly + 40))
        self.LoginBtn = tk.Button(self.master, text='登陆',
                                  command=lambda: self.check(self.UserEntry.get(), self.PasswdEntry.get()))
        self.RegistBtn = tk.Button(self.master, text='注册', command=self.regist)
        btn_x = self.lx + self.input_length * 8 + 40
        btn_y = self.ly + self.input_length + 40
        self.LoginBtn.place(x=btn_x, y=btn_y)
        self.RegistBtn.place(x=btn_x, y=btn_y + 40)

    def regist(self):
        self.redirect(RegistPage)

    def check(self, username, passwd):
        if str(username) == 'wangyu' and passwd == '123':
            showinfo('提示', "密码正确")
            self.redirect(UserPage)
        else:
            showinfo('提示', "密码错误")


class RegistPage(Page):
    def __init__(self, client):
        Page.__init__(self, client, BackGroudImg)
        self.init_window()

    def init_window(self):
        self.lx = self.x * 0.2
        self.ly = self.y * 0.35
        self.input_length = int(0.05 * self.x)
        loginFont = self.font.getFont(family="System", size=30)
        self.LoginText = tk.Label(self.master, text="注册", font=loginFont,
                                  fg='#9ACD32', bg='#8E8E8E')
        self.LoginText.place(x=self.x / 2, y=self.y / 4, anchor='center')
        textFont = self.font.getFont(family="System", size=12)
        self.UserText = tk.Label(self.master, text='用户名', font=textFont, bg='#8E8E8E')
        self.UserEntry = tk.Entry(self.master, width=self.input_length)
        self.PasswdText = tk.Label(self.master, text='密码', font=textFont, bg='#8E8E8E')
        self.PasswdEntry = tk.Entry(self.master, show='*', width=self.input_length)
        self.AgainText = tk.Label(self.master, text='再次密码', font=textFont, bg='#8E8E8E')
        self.AgainEntry = tk.Entry(self.master, show='*', width=self.input_length)
        self.UserText.place(x=self.lx, y=self.ly)
        self.UserEntry.place(x=(self.lx + 60), y=self.ly)
        self.PasswdText.place(x=self.lx, y=(self.ly + 40))
        self.PasswdEntry.place(x=(self.lx + 60), y=(self.ly + 40))
        self.AgainText.place(x=self.lx, y=(self.ly + 80))
        self.AgainEntry.place(x=(self.lx + 60), y=(self.ly + 80))
        self.LoginBtn = tk.Button(self.master, text='注册',
                                  command=lambda: self.regist(self.UserEntry.get(), self.PasswdEntry.get(),
                                                              self.AgainEntry.get()))
        btn_x = self.lx + self.input_length * 8 + 40
        btn_y = self.ly + self.input_length + 80
        self.LoginBtn.place(x=btn_x, y=btn_y)

    def regist(self, username, passwd, again):
        if str(username) == 'wangyu' and passwd == again:
            self.redirect(LoginPage)
        else:
            showinfo('提示', "密码错误")


def main():
    client = Client(500, 1000, 'login')
    # RegistPage(client)
    login = LoginPage(client)
    client.start()
    # root = Tk()
    # loginIm = Image.open()
    # img = ImageTk.PhotoImage(loginIm)
    # imLabel = tk.Label(root, image=img)
    # imLabel.pack()
    # root.mainloop()
    # pass


if __name__ == "__main__":
    main()
