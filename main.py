from curses import window
from email import message
from re import T
import sys
import rospy
from std_msgs.msg import Bool,Int8,String
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets

class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI,self).__init__()
        uic.loadUi("interface_2.ui",self)

        self.show()
        self.login_btn.clicked.connect(self.Login)

    def Login(self):
        if self.username_txt.text()=="gokulks" and self.password_txt.text()=="password":
            self.Menu_btn.setStyleSheet("QPushButton"
                                "{"
                                "background-color : lightblue;"
                                "}")
            self.Menu_btn.setEnabled(True)
            self.home_btn.setStyleSheet("QPushButton"
                                "{"
                                "background-color : lightblue;"
                                "}")
            self.home_btn.setEnabled(True)
            self.home_btn_2.setStyleSheet("QPushButton"
                                "{"
                                "background-color : lightblue;"
                                "}")
            self.home_btn_2.setEnabled(True)
        else:
            message = QMessageBox()
            message.setText("Invalid Login")
            message.exec_()


def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()
    
if __name__=='__main__':
    homebtn_pub=rospy.Publisher('/home_btn',Bool,queue_size=1)
    homebtn_2_pub=rospy.Publisher('/home_btn_2',Bool,queue_size=1)
    menubtn_pub=rospy.Publisher('/Menu_btn',Bool,queue_size=1)
    rospy.init_node('main',anonymous=True)
    main()
