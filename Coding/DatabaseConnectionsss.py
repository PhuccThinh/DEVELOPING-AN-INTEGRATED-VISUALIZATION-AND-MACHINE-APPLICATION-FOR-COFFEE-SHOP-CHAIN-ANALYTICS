# Form implementation generated from reading ui file 'D:\GitHub\UEL-Course\MLBA\final_project\1. Coding\4. App\Test\DatabaseConnections.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(377, 340)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\GitHub\\UEL-Course\\MLBA\\final_project\\1. Coding\\4. App\\Test\\../0. Icon/ic_logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 341, 271))
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 321, 241))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.labelServer = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.labelServer.setObjectName("labelServer")
        self.gridLayout.addWidget(self.labelServer, 0, 0, 1, 1)
        self.pushButtonConnect = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:\\GitHub\\UEL-Course\\MLBA\\final_project\\1. Coding\\4. App\\Test\\../0. Icon/ic_connect.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonConnect.setIcon(icon1)
        self.pushButtonConnect.setObjectName("pushButtonConnect")
        self.gridLayout.addWidget(self.pushButtonConnect, 5, 1, 1, 1)
        self.labelPort = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.labelPort.setObjectName("labelPort")
        self.gridLayout.addWidget(self.labelPort, 1, 0, 1, 1)
        self.labelDatabase = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.labelDatabase.setObjectName("labelDatabase")
        self.gridLayout.addWidget(self.labelDatabase, 2, 0, 1, 1)
        self.labelUser = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.labelUser.setObjectName("labelUser")
        self.gridLayout.addWidget(self.labelUser, 3, 0, 1, 1)
        self.labelPassword = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.labelPassword.setObjectName("labelPassword")
        self.gridLayout.addWidget(self.labelPassword, 4, 0, 1, 1)
        self.pushButtonExit = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("D:\\GitHub\\UEL-Course\\MLBA\\final_project\\1. Coding\\4. App\\Test\\../0. Icon/ic_exit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonExit.setIcon(icon2)
        self.pushButtonExit.setObjectName("pushButtonExit")
        self.gridLayout.addWidget(self.pushButtonExit, 5, 2, 1, 1)
        self.lineEditPassword = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEditPassword.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.gridLayout.addWidget(self.lineEditPassword, 4, 1, 1, 2)
        self.lineEditUser = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEditUser.setObjectName("lineEditUser")
        self.gridLayout.addWidget(self.lineEditUser, 3, 1, 1, 2)
        self.lineEditDatabase = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEditDatabase.setObjectName("lineEditDatabase")
        self.gridLayout.addWidget(self.lineEditDatabase, 2, 1, 1, 2)
        self.lineEditPort = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEditPort.setObjectName("lineEditPort")
        self.gridLayout.addWidget(self.lineEditPort, 1, 1, 1, 2)
        self.lineEditSever = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEditSever.setAutoFillBackground(False)
        self.lineEditSever.setReadOnly(False)
        self.lineEditSever.setObjectName("lineEditSever")
        self.gridLayout.addWidget(self.lineEditSever, 0, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 377, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BMS"))
        self.groupBox.setTitle(_translate("MainWindow", "Connections Settings:"))
        self.labelServer.setText(_translate("MainWindow", "Server:"))
        self.pushButtonConnect.setText(_translate("MainWindow", "Connect"))
        self.labelPort.setText(_translate("MainWindow", "Port:"))
        self.labelDatabase.setText(_translate("MainWindow", "Database:"))
        self.labelUser.setText(_translate("MainWindow", "User:"))
        self.labelPassword.setText(_translate("MainWindow", "Password:"))
        self.pushButtonExit.setText(_translate("MainWindow", "Exit"))
        self.lineEditPassword.setText(_translate("MainWindow", "@Obama123"))
        self.lineEditPassword.setPlaceholderText(_translate("MainWindow", "Please enter your password here..."))
        self.lineEditUser.setText(_translate("MainWindow", "root"))
        self.lineEditUser.setPlaceholderText(_translate("MainWindow", "Please enter your user name here..."))
        self.lineEditDatabase.setText(_translate("MainWindow", "final_project"))
        self.lineEditDatabase.setPlaceholderText(_translate("MainWindow", "Please enter your database name here..."))
        self.lineEditPort.setText(_translate("MainWindow", "3306"))
        self.lineEditPort.setPlaceholderText(_translate("MainWindow", "Please enter your port here..."))
        self.lineEditSever.setText(_translate("MainWindow", "localhost", "DJDSJKDSJKDS"))
        self.lineEditSever.setPlaceholderText(_translate("MainWindow", "Please enter your server here..."))
