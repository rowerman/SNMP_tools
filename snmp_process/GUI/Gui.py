# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1068, 755)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 200, 211, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(280, 40, 741, 651))
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayoutWidget = QtWidgets.QWidget(self.page)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 50, 721, 601))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 100))
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 4, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 3, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 0, 1, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 1, 1, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.page_3)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 50, 721, 601))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 2, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 3, 1, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_2.addWidget(self.lineEdit_4, 6, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 6, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_2.addWidget(self.lineEdit_8, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_9.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 3, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 4, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_2.addWidget(self.lineEdit_9, 1, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 4, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_2.addWidget(self.pushButton_9, 5, 0, 1, 2)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_13 = QtWidgets.QLabel(self.page_4)
        self.label_13.setGeometry(QtCore.QRect(0, 20, 711, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.tableWidget = QtWidgets.QTableWidget(self.page_4)
        self.tableWidget.setGeometry(QtCore.QRect(0, 70, 741, 341))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideLeft)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.textEdit_7 = QtWidgets.QTextEdit(self.page_4)
        self.textEdit_7.setGeometry(QtCore.QRect(0, 446, 741, 201))
        self.textEdit_7.setObjectName("textEdit_7")
        self.pushButton_10 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_10.setGeometry(QtCore.QRect(0, 410, 741, 28))
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_8 = QtWidgets.QLabel(self.page_4)
        self.label_8.setGeometry(QtCore.QRect(30, 20, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.page_5)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 50, 741, 601))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_21 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout_3.addWidget(self.label_21, 6, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 2, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_3.addWidget(self.lineEdit_2, 3, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 4, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 1, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_3.addWidget(self.lineEdit_5, 6, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_3.addWidget(self.lineEdit_3, 4, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_18.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 2, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 3, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_17.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 0, 0, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_3.addWidget(self.pushButton_11, 5, 0, 1, 2)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_3.addWidget(self.lineEdit_10, 0, 1, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_3.addWidget(self.lineEdit_11, 1, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_5)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.widget_2 = QtWidgets.QWidget(self.page_2)
        self.widget_2.setGeometry(QtCore.QRect(710, 270, 120, 80))
        self.widget_2.setObjectName("widget_2")
        self.widget = QtWidgets.QWidget(self.page_2)
        self.widget.setGeometry(QtCore.QRect(10, 130, 221, 131))
        self.widget.setObjectName("widget")
        self.groupBox_4 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 0, 211, 131))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.widget_3 = QtWidgets.QWidget(self.page_2)
        self.widget_3.setGeometry(QtCore.QRect(260, 130, 221, 131))
        self.widget_3.setObjectName("widget_3")
        self.groupBox_5 = QtWidgets.QGroupBox(self.widget_3)
        self.groupBox_5.setGeometry(QtCore.QRect(0, 0, 221, 141))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.widget_4 = QtWidgets.QWidget(self.page_2)
        self.widget_4.setGeometry(QtCore.QRect(500, 130, 221, 131))
        self.widget_4.setObjectName("widget_4")
        self.groupBox_6 = QtWidgets.QGroupBox(self.widget_4)
        self.groupBox_6.setGeometry(QtCore.QRect(0, 0, 221, 141))
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_22 = QtWidgets.QLabel(self.page_2)
        self.label_22.setGeometry(QtCore.QRect(80, 70, 72, 15))
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.page_2)
        self.label_23.setGeometry(QtCore.QRect(320, 70, 72, 20))
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.page_2)
        self.label_24.setGeometry(QtCore.QRect(520, 70, 121, 20))
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.page_2)
        self.label_25.setGeometry(QtCore.QRect(40, 90, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.page_2)
        self.label_26.setGeometry(QtCore.QRect(290, 90, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.page_2)
        self.label_27.setGeometry(QtCore.QRect(510, 90, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.widget_5 = QtWidgets.QWidget(self.page_2)
        self.widget_5.setGeometry(QtCore.QRect(20, 360, 321, 141))
        self.widget_5.setObjectName("widget_5")
        self.groupBox_7 = QtWidgets.QGroupBox(self.widget_5)
        self.groupBox_7.setGeometry(QtCore.QRect(-10, 0, 341, 141))
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.widget_6 = QtWidgets.QWidget(self.page_2)
        self.widget_6.setGeometry(QtCore.QRect(370, 360, 321, 141))
        self.widget_6.setObjectName("widget_6")
        self.groupBox_8 = QtWidgets.QGroupBox(self.widget_6)
        self.groupBox_8.setGeometry(QtCore.QRect(0, 0, 321, 151))
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.label_28 = QtWidgets.QLabel(self.page_2)
        self.label_28.setGeometry(QtCore.QRect(170, 280, 72, 15))
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.page_2)
        self.label_29.setGeometry(QtCore.QRect(460, 280, 72, 20))
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.page_2)
        self.label_30.setGeometry(QtCore.QRect(120, 310, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.page_2)
        self.label_31.setGeometry(QtCore.QRect(440, 310, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.page_2)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(0, 510, 721, 141))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget_4)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_4.addWidget(self.comboBox_2, 1, 0, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_32.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.gridLayout_4.addWidget(self.label_32, 0, 0, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_33.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.gridLayout_4.addWidget(self.label_33, 0, 1, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.gridLayoutWidget_4)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout_4.addWidget(self.comboBox_3, 1, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_4.addWidget(self.pushButton_6, 2, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_4.addWidget(self.pushButton_7, 2, 1, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.page_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 721, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_34 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_34.setObjectName("label_34")
        self.horizontalLayout.addWidget(self.label_34)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.horizontalLayout.addWidget(self.lineEdit_12)
        self.pushButton_12 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout.addWidget(self.pushButton_12)
        self.stackedWidget.addWidget(self.page_2)
        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        self.label_35.setGeometry(QtCore.QRect(30, 20, 201, 151))
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1068, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "获取Agent信息"))
        self.pushButton_2.setText(_translate("MainWindow", "设置Agent信息"))
        self.pushButton_3.setText(_translate("MainWindow", "监听trap包"))
        self.pushButton_4.setText(_translate("MainWindow", "发送trap包"))
        self.pushButton_5.setText(_translate("MainWindow", "Agent数据监控"))
        self.label.setText(_translate("MainWindow", "输入Agent的ip"))
        self.label_2.setText(_translate("MainWindow", "输入Oid"))
        self.label_4.setText(_translate("MainWindow", "得到的内容"))
        self.label_3.setText(_translate("MainWindow", "说明"))
        self.pushButton_8.setText(_translate("MainWindow", "点我查询"))
        self.label_5.setText(_translate("MainWindow", "默认社区为public，发送端口为161，超时限制为100s"))
        self.label_10.setText(_translate("MainWindow", "默认社区为public，发送端口为161，超时限制为100s"))
        self.comboBox.setItemText(0, _translate("MainWindow", "integer"))
        self.comboBox.setItemText(1, _translate("MainWindow", "unsigned_integer"))
        self.comboBox.setItemText(2, _translate("MainWindow", "time_ticks"))
        self.comboBox.setItemText(3, _translate("MainWindow", "ip_address"))
        self.comboBox.setItemText(4, _translate("MainWindow", "object_identifier"))
        self.comboBox.setItemText(5, _translate("MainWindow", "string"))
        self.comboBox.setItemText(6, _translate("MainWindow", "hex_string"))
        self.comboBox.setItemText(7, _translate("MainWindow", "decimal_string"))
        self.comboBox.setItemText(8, _translate("MainWindow", "bit_string"))
        self.label_20.setText(_translate("MainWindow", "发送结果"))
        self.label_6.setText(_translate("MainWindow", "输入Oid"))
        self.label_7.setText(_translate("MainWindow", "说明"))
        self.label_9.setText(_translate("MainWindow", "输入Agent的ip"))
        self.label_11.setText(_translate("MainWindow", "选择设置值的类型"))
        self.label_12.setText(_translate("MainWindow", "待设置的值"))
        self.pushButton_9.setText(_translate("MainWindow", "点我设置！"))
        self.label_13.setText(_translate("MainWindow", "说明：接收所有发往本机的trap包"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "来源IP"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "来源社区"))
        self.pushButton_10.setText(_translate("MainWindow", "开始监听！"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
        self.label_21.setText(_translate("MainWindow", "发送结果"))
        self.label_15.setText(_translate("MainWindow", "说明"))
        self.label_19.setText(_translate("MainWindow", "额外指定的值"))
        self.label_14.setText(_translate("MainWindow", "输入Oid"))
        self.label_18.setText(_translate("MainWindow", "默认社区为public，对方接收端口为162，超时限制为100s"))
        self.label_16.setText(_translate("MainWindow", "额外的oid"))
        self.label_17.setText(_translate("MainWindow", "输入Agent的ip"))
        self.pushButton_11.setText(_translate("MainWindow", "点我发送！"))
        self.label_22.setText(_translate("MainWindow", "CPU使用率"))
        self.label_23.setText(_translate("MainWindow", "内存使用率"))
        self.label_24.setText(_translate("MainWindow", "磁盘使用率"))
        self.label_25.setText(_translate("MainWindow", "我是CPU使用率"))
        self.label_26.setText(_translate("MainWindow", "我是内存使用率"))
        self.label_27.setText(_translate("MainWindow", "我是磁盘使用率"))
        self.label_28.setText(_translate("MainWindow", "上传流量"))
        self.label_29.setText(_translate("MainWindow", "下行流量"))
        self.label_30.setText(_translate("MainWindow", "我是上传流量"))
        self.label_31.setText(_translate("MainWindow", "我是下行流量"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "30"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "40"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "50"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "60"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "70"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "80"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "90"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "99"))
        self.label_32.setText(_translate("MainWindow", "设置CPU阈值"))
        self.label_33.setText(_translate("MainWindow", "设置内存阈值"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "30"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "40"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "50"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "60"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "70"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "80"))
        self.comboBox_3.setItemText(6, _translate("MainWindow", "90"))
        self.comboBox_3.setItemText(7, _translate("MainWindow", "99"))
        self.pushButton_6.setText(_translate("MainWindow", "Configure"))
        self.pushButton_7.setText(_translate("MainWindow", "Configure"))
        self.label_34.setText(_translate("MainWindow", "要监听的IP"))
        self.pushButton_12.setText(_translate("MainWindow", "开始监听"))
        self.label_35.setText(_translate("MainWindow", "我是logo"))
