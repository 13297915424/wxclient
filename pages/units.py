# coding:utf8
# author:Deylies,WangYu
from __future__ import print_function
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from client.MainClient import Page
from pages import BackGroudImg
class Options(Page):
    def __init__(self,client):
        Page.__init__(self,client)
        self.init_window()
    def init_window(self):
        pass

def main():
    pass


if __name__ == "__main__":
    main()