# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtUI_rev3.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import query as qu
from database_build import main as ma

class Ui_Output1Window(object):
    def loadData(self, df):
        layout = QtWidgets.QGridLayout() 
        i = 0
        for key in df.keys():
            key = QtWidgets.QTableWidgetItem(key)
            key.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setHorizontalHeaderItem(i, key)
            i+=1

        i = 0
        for value in df.values():
            value = QtWidgets.QTableWidgetItem(value)
            value.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(0, i, value)
            i+=1

    def setupUi(self, Output1Window, PATIENT_ID, BIRTHYEAR):
        Output1Window.setObjectName("Output1Window")
        Output1Window.resize(884, 824)
        self.centralwidget = QtWidgets.QWidget(Output1Window)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 90, 421, 241))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAcceptDrops(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_29 = QtWidgets.QLabel(self.groupBox_2)
        self.label_29.setGeometry(QtCore.QRect(10, 146, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 26, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_20 = QtWidgets.QLabel(self.groupBox_2)
        self.label_20.setGeometry(QtCore.QRect(10, 50, 35, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_18 = QtWidgets.QLabel(self.groupBox_2)
        self.label_18.setGeometry(QtCore.QRect(10, 100, 35, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        self.label_17.setGeometry(QtCore.QRect(10, 115, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(10, 130, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(10, 160, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(10, 175, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_21 = QtWidgets.QLabel(self.groupBox_2)
        self.label_21.setGeometry(QtCore.QRect(30, 80, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_19 = QtWidgets.QLabel(self.groupBox_2)
        self.label_19.setGeometry(QtCore.QRect(10, 70, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.subject_id = QtWidgets.QLabel(self.groupBox_2)
        self.subject_id.setGeometry(QtCore.QRect(130, 26, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.subject_id.setFont(font)
        self.subject_id.setObjectName("subject_id")
        self.hadm_id = QtWidgets.QLabel(self.groupBox_2)
        self.hadm_id.setGeometry(QtCore.QRect(130, 40, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hadm_id.setFont(font)
        self.hadm_id.setObjectName("hadm_id")
        self.age = QtWidgets.QLabel(self.groupBox_2)
        self.age.setGeometry(QtCore.QRect(130, 50, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.age.setFont(font)
        self.age.setObjectName("age")
        self.expire_flag = QtWidgets.QLabel(self.groupBox_2)
        self.expire_flag.setGeometry(QtCore.QRect(130, 70, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.expire_flag.setFont(font)
        self.expire_flag.setObjectName("expire_flag")
        self.age_death = QtWidgets.QLabel(self.groupBox_2)
        self.age_death.setGeometry(QtCore.QRect(130, 80, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.age_death.setFont(font)
        self.age_death.setObjectName("age_death")
        self.gender = QtWidgets.QLabel(self.groupBox_2)
        self.gender.setGeometry(QtCore.QRect(130, 100, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gender.setFont(font)
        self.gender.setObjectName("gender")
        self.ethnicity = QtWidgets.QLabel(self.groupBox_2)
        self.ethnicity.setGeometry(QtCore.QRect(130, 110, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ethnicity.setFont(font)
        self.ethnicity.setObjectName("ethnicity")
        self.language = QtWidgets.QLabel(self.groupBox_2)
        self.language.setGeometry(QtCore.QRect(130, 130, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.language.setFont(font)
        self.language.setObjectName("language")
        self.marital_status = QtWidgets.QLabel(self.groupBox_2)
        self.marital_status.setGeometry(QtCore.QRect(130, 139, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.marital_status.setFont(font)
        self.marital_status.setObjectName("marital_status")
        self.religion = QtWidgets.QLabel(self.groupBox_2)
        self.religion.setGeometry(QtCore.QRect(130, 160, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.religion.setFont(font)
        self.religion.setObjectName("religion")
        self.insurance = QtWidgets.QLabel(self.groupBox_2)
        self.insurance.setGeometry(QtCore.QRect(130, 170, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.insurance.setFont(font)
        self.insurance.setObjectName("insurance")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(20, 20, 841, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setWordWrap(False)
        self.label_23.setObjectName("label_23")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(450, 90, 411, 131))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setAcceptDrops(True)
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_22 = QtWidgets.QLabel(self.groupBox_4)
        self.label_22.setGeometry(QtCore.QRect(30, 40, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_56 = QtWidgets.QLabel(self.groupBox_4)
        self.label_56.setGeometry(QtCore.QRect(10, 26, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_56.setFont(font)
        self.label_56.setObjectName("label_56")
        self.label_57 = QtWidgets.QLabel(self.groupBox_4)
        self.label_57.setGeometry(QtCore.QRect(10, 50, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_57.setFont(font)
        self.label_57.setObjectName("label_57")
        self.label_58 = QtWidgets.QLabel(self.groupBox_4)
        self.label_58.setGeometry(QtCore.QRect(10, 100, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_58.setFont(font)
        self.label_58.setObjectName("label_58")
        self.label_63 = QtWidgets.QLabel(self.groupBox_4)
        self.label_63.setGeometry(QtCore.QRect(10, 80, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_63.setFont(font)
        self.label_63.setObjectName("label_63")
        self.label_64 = QtWidgets.QLabel(self.groupBox_4)
        self.label_64.setGeometry(QtCore.QRect(10, 70, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_64.setFont(font)
        self.label_64.setObjectName("label_64")
        self.Code = QtWidgets.QLabel(self.groupBox_4)
        self.Code.setGeometry(QtCore.QRect(170, 26, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Code.setFont(font)
        self.Code.setObjectName("Code")
        self.Descriptor = QtWidgets.QLabel(self.groupBox_4)
        self.Descriptor.setGeometry(QtCore.QRect(170, 40, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Descriptor.setFont(font)
        self.Descriptor.setObjectName("Descriptor")
        self.long_title = QtWidgets.QLabel(self.groupBox_4)
        self.long_title.setGeometry(QtCore.QRect(170, 50, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.long_title.setFont(font)
        self.long_title.setObjectName("long_title")
        self.admission_type = QtWidgets.QLabel(self.groupBox_4)
        self.admission_type.setGeometry(QtCore.QRect(170, 70, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.admission_type.setFont(font)
        self.admission_type.setObjectName("admission_type")
        self.admit_new = QtWidgets.QLabel(self.groupBox_4)
        self.admit_new.setGeometry(QtCore.QRect(170, 80, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.admit_new.setFont(font)
        self.admit_new.setObjectName("admit_new")
        self.disch_new = QtWidgets.QLabel(self.groupBox_4)
        self.disch_new.setGeometry(QtCore.QRect(170, 100, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.disch_new.setFont(font)
        self.disch_new.setObjectName("disch_new")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(450, 230, 411, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setAcceptDrops(True)
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_67 = QtWidgets.QLabel(self.groupBox_5)
        self.label_67.setGeometry(QtCore.QRect(10, 26, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_67.setFont(font)
        self.label_67.setObjectName("label_67")
        self.subject_id_7 = QtWidgets.QLabel(self.groupBox_5)
        self.subject_id_7.setGeometry(QtCore.QRect(80, 26, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.subject_id_7.setFont(font)
        self.subject_id_7.setObjectName("subject_id_7")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_5)
        self.textBrowser.setGeometry(QtCore.QRect(90, 30, 311, 61))
        self.textBrowser.setObjectName("textBrowser")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 340, 851, 381))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setAcceptDrops(True)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_31 = QtWidgets.QLabel(self.groupBox_3)
        self.label_31.setGeometry(QtCore.QRect(20, 216, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.label_33 = QtWidgets.QLabel(self.groupBox_3)
        self.label_33.setGeometry(QtCore.QRect(10, 170, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.label_62 = QtWidgets.QLabel(self.groupBox_3)
        self.label_62.setGeometry(QtCore.QRect(20, 185, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_62.setFont(font)
        self.label_62.setObjectName("label_62")
        self.label_68 = QtWidgets.QLabel(self.groupBox_3)
        self.label_68.setGeometry(QtCore.QRect(20, 200, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_68.setFont(font)
        self.label_68.setObjectName("label_68")
        self.label_69 = QtWidgets.QLabel(self.groupBox_3)
        self.label_69.setGeometry(QtCore.QRect(20, 230, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_69.setFont(font)
        self.label_69.setObjectName("label_69")
        self.label_70 = QtWidgets.QLabel(self.groupBox_3)
        self.label_70.setGeometry(QtCore.QRect(20, 245, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_70.setFont(font)
        self.label_70.setObjectName("label_70")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_3)
        self.tableWidget.setGeometry(QtCore.QRect(10, 30, 831, 121))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(35)
        self.tableWidget.setRowCount(1)
        self.label_71 = QtWidgets.QLabel(self.groupBox_3)
        self.label_71.setGeometry(QtCore.QRect(20, 260, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_71.setFont(font)
        self.label_71.setObjectName("label_71")
        self.label_72 = QtWidgets.QLabel(self.groupBox_3)
        self.label_72.setGeometry(QtCore.QRect(20, 270, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_72.setFont(font)
        self.label_72.setObjectName("label_72")
        self.label_73 = QtWidgets.QLabel(self.groupBox_3)
        self.label_73.setGeometry(QtCore.QRect(20, 290, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_73.setFont(font)
        self.label_73.setObjectName("label_73")
        self.label_74 = QtWidgets.QLabel(self.groupBox_3)
        self.label_74.setGeometry(QtCore.QRect(20, 300, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_74.setFont(font)
        self.label_74.setObjectName("label_74")
        self.label_75 = QtWidgets.QLabel(self.groupBox_3)
        self.label_75.setGeometry(QtCore.QRect(20, 320, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_75.setFont(font)
        self.label_75.setObjectName("label_75")
        self.label_76 = QtWidgets.QLabel(self.groupBox_3)
        self.label_76.setGeometry(QtCore.QRect(20, 330, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_76.setFont(font)
        self.label_76.setObjectName("label_76")
        self.label_77 = QtWidgets.QLabel(self.groupBox_3)
        self.label_77.setGeometry(QtCore.QRect(350, 330, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_77.setFont(font)
        self.label_77.setObjectName("label_77")
        self.label_32 = QtWidgets.QLabel(self.groupBox_3)
        self.label_32.setGeometry(QtCore.QRect(350, 216, 291, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.label_78 = QtWidgets.QLabel(self.groupBox_3)
        self.label_78.setGeometry(QtCore.QRect(350, 300, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_78.setFont(font)
        self.label_78.setObjectName("label_78")
        self.label_79 = QtWidgets.QLabel(self.groupBox_3)
        self.label_79.setGeometry(QtCore.QRect(350, 230, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_79.setFont(font)
        self.label_79.setObjectName("label_79")
        self.label_80 = QtWidgets.QLabel(self.groupBox_3)
        self.label_80.setGeometry(QtCore.QRect(350, 245, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_80.setFont(font)
        self.label_80.setObjectName("label_80")
        self.label_81 = QtWidgets.QLabel(self.groupBox_3)
        self.label_81.setGeometry(QtCore.QRect(350, 185, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_81.setFont(font)
        self.label_81.setObjectName("label_81")
        self.label_82 = QtWidgets.QLabel(self.groupBox_3)
        self.label_82.setGeometry(QtCore.QRect(350, 290, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_82.setFont(font)
        self.label_82.setObjectName("label_82")
        self.label_83 = QtWidgets.QLabel(self.groupBox_3)
        self.label_83.setGeometry(QtCore.QRect(350, 200, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_83.setFont(font)
        self.label_83.setObjectName("label_83")
        self.label_84 = QtWidgets.QLabel(self.groupBox_3)
        self.label_84.setGeometry(QtCore.QRect(350, 270, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_84.setFont(font)
        self.label_84.setObjectName("label_84")
        self.label_85 = QtWidgets.QLabel(self.groupBox_3)
        self.label_85.setGeometry(QtCore.QRect(350, 260, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_85.setFont(font)
        self.label_85.setObjectName("label_85")
        self.label_86 = QtWidgets.QLabel(self.groupBox_3)
        self.label_86.setGeometry(QtCore.QRect(350, 320, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_86.setFont(font)
        self.label_86.setObjectName("label_86")
        self.label_87 = QtWidgets.QLabel(self.groupBox_3)
        self.label_87.setGeometry(QtCore.QRect(670, 230, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_87.setFont(font)
        self.label_87.setObjectName("label_87")
        self.label_88 = QtWidgets.QLabel(self.groupBox_3)
        self.label_88.setGeometry(QtCore.QRect(670, 216, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_88.setFont(font)
        self.label_88.setObjectName("label_88")
        self.label_89 = QtWidgets.QLabel(self.groupBox_3)
        self.label_89.setGeometry(QtCore.QRect(670, 185, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_89.setFont(font)
        self.label_89.setObjectName("label_89")
        self.label_90 = QtWidgets.QLabel(self.groupBox_3)
        self.label_90.setGeometry(QtCore.QRect(670, 245, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_90.setFont(font)
        self.label_90.setObjectName("label_90")
        self.label_91 = QtWidgets.QLabel(self.groupBox_3)
        self.label_91.setGeometry(QtCore.QRect(670, 270, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_91.setFont(font)
        self.label_91.setObjectName("label_91")
        self.label_92 = QtWidgets.QLabel(self.groupBox_3)
        self.label_92.setGeometry(QtCore.QRect(670, 290, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_92.setFont(font)
        self.label_92.setObjectName("label_92")
        self.label_93 = QtWidgets.QLabel(self.groupBox_3)
        self.label_93.setGeometry(QtCore.QRect(670, 260, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_93.setFont(font)
        self.label_93.setObjectName("label_93")
        self.label_94 = QtWidgets.QLabel(self.groupBox_3)
        self.label_94.setGeometry(QtCore.QRect(670, 300, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_94.setFont(font)
        self.label_94.setObjectName("label_94")
        self.label_95 = QtWidgets.QLabel(self.groupBox_3)
        self.label_95.setGeometry(QtCore.QRect(670, 200, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_95.setFont(font)
        self.label_95.setObjectName("label_95")
        self.label_97 = QtWidgets.QLabel(self.groupBox_3)
        self.label_97.setGeometry(QtCore.QRect(670, 320, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_97.setFont(font)
        self.label_97.setObjectName("label_97")
        Output1Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Output1Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 884, 18))
        self.menubar.setObjectName("menubar")
        Output1Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Output1Window)
        self.statusbar.setObjectName("statusbar")
        Output1Window.setStatusBar(self.statusbar)

        self.retranslateUi(Output1Window)
        QtCore.QMetaObject.connectSlotsByName(Output1Window)

        self.query_values(PATIENT_ID, BIRTHYEAR)

    def retranslateUi(self, Output1Window):
        _translate = QtCore.QCoreApplication.translate
        Output1Window.setWindowTitle(_translate("Output1Window", "MainWindow"))
        self.groupBox_2.setTitle(_translate("Output1Window", "Patient Information"))
        self.label_29.setText(_translate("Output1Window", "Marital Status"))
        self.label_2.setText(_translate("Output1Window", "Hospital Visit ID"))
        self.label.setText(_translate("Output1Window", "Patient ID"))
        self.label_20.setText(_translate("Output1Window", "Age"))
        self.label_18.setText(_translate("Output1Window", "Gender"))
        self.label_17.setText(_translate("Output1Window", "Ethnicity"))
        self.label_14.setText(_translate("Output1Window", "Primary Language"))
        self.label_15.setText(_translate("Output1Window", "Religion"))
        self.label_13.setText(_translate("Output1Window", "Insurance"))
        self.label_21.setText(_translate("Output1Window", "Age of Death"))
        self.label_19.setText(_translate("Output1Window", "Deceased"))
        self.subject_id.setText(_translate("Output1Window", ": "))
        self.hadm_id.setText(_translate("Output1Window", ":"))
        self.age.setText(_translate("Output1Window", ":"))
        self.expire_flag.setText(_translate("Output1Window", ":"))
        self.age_death.setText(_translate("Output1Window", ":"))
        self.gender.setText(_translate("Output1Window", ":"))
        self.ethnicity.setText(_translate("Output1Window", ":"))
        self.language.setText(_translate("Output1Window", ":"))
        self.marital_status.setText(_translate("Output1Window", ":"))
        self.religion.setText(_translate("Output1Window", ":"))
        self.insurance.setText(_translate("Output1Window", ":"))
        self.label_23.setText(_translate("Output1Window", "PATIENT CASE REPORT FORM"))
        self.groupBox_4.setTitle(_translate("Output1Window", "Disease Information"))
        self.label_22.setText(_translate("Output1Window", "Descriptor"))
        self.label_56.setText(_translate("Output1Window", "Condition Diagnosis Code"))
        self.label_57.setText(_translate("Output1Window", "All Diagnoses"))
        self.label_58.setText(_translate("Output1Window", "Discharge Date"))
        self.label_63.setText(_translate("Output1Window", "Admission Date"))
        self.label_64.setText(_translate("Output1Window", "Hospital Admission Type"))
        self.Code.setText(_translate("Output1Window", ": "))
        self.Descriptor.setText(_translate("Output1Window", ":"))
        self.long_title.setText(_translate("Output1Window", ":"))
        self.admission_type.setText(_translate("Output1Window", ":"))
        self.admit_new.setText(_translate("Output1Window", ":"))
        self.disch_new.setText(_translate("Output1Window", ":"))
        self.groupBox_5.setTitle(_translate("Output1Window", "Prescription Information"))
        self.label_67.setText(_translate("Output1Window", "Medication"))
        self.subject_id_7.setText(_translate("Output1Window", ": "))
        self.groupBox_3.setTitle(_translate("Output1Window", "NARMS Data"))
        self.label_31.setText(_translate("Output1Window", "ATM Aztreonam"))
        self.label_33.setText(_translate("Output1Window", "Dictionary"))
        self.label_62.setText(_translate("Output1Window", "AMI Amikacin"))
        self.label_68.setText(_translate("Output1Window", "AMP Ampicillin"))
        self.label_69.setText(_translate("Output1Window", "AUG Amoxicillin-clavulanic acid"))
        self.label_70.setText(_translate("Output1Window", "AXO Ceftriaxone"))
        self.label_71.setText(_translate("Output1Window", "AZM Azithromycin"))
        self.label_72.setText(_translate("Output1Window", "CAZ Ceftazidime"))
        self.label_73.setText(_translate("Output1Window", "CCV Ceftazidime-clavulanic acid"))
        self.label_74.setText(_translate("Output1Window", "CEP Cephalothin"))
        self.label_75.setText(_translate("Output1Window", "CEQ Cefquinome"))
        self.label_76.setText(_translate("Output1Window", "CHL Chloramphenicol"))
        self.label_77.setText(_translate("Output1Window", "GEN Gentamicin"))
        self.label_32.setText(_translate("Output1Window", "COT Trimethoprim-sulfamethoxazole"))
        self.label_78.setText(_translate("Output1Window", "FIS Sulfisoxazole"))
        self.label_79.setText(_translate("Output1Window", "CTC Cefotaxime-clavulanic acid"))
        self.label_80.setText(_translate("Output1Window", "CTX Cefotaxime"))
        self.label_81.setText(_translate("Output1Window", "CIP Ciprofloxacin"))
        self.label_82.setText(_translate("Output1Window", "FFN Florfenicol"))
        self.label_83.setText(_translate("Output1Window", "CLI Clindamycin"))
        self.label_84.setText(_translate("Output1Window", "FEP Cefepime"))
        self.label_85.setText(_translate("Output1Window", "ERY Erythromycin"))
        self.label_86.setText(_translate("Output1Window", "FOX Cefoxitin"))
        self.label_87.setText(_translate("Output1Window", "NAL Naladixic acid"))
        self.label_88.setText(_translate("Output1Window", "MER Meropenem"))
        self.label_89.setText(_translate("Output1Window", "IMI Imipenem"))
        self.label_90.setText(_translate("Output1Window", "PTZ Piperacillin-tazobactam"))
        self.label_91.setText(_translate("Output1Window", "STR Streptomycin"))
        self.label_92.setText(_translate("Output1Window", "TEL Telithromycin"))
        self.label_93.setText(_translate("Output1Window", "SMX Sulfamethoxazole"))
        self.label_94.setText(_translate("Output1Window", "TET Tetracycline"))
        self.label_95.setText(_translate("Output1Window", "KAN Kanamycin"))
        self.label_97.setText(_translate("Output1Window", "TIO Ceftiofur"))

    def query_values(self, PATIENT_ID, BIRTHYEAR):
        variable, table_narms = self.get_report(PATIENT_ID, BIRTHYEAR)
        self.subject_id.setText(": " + str(variable['subject_id']))
        self.hadm_id.setText(": " + str(variable['hadm_id']))
        self.age.setText(": " + str(variable['age']))
        self.expire_flag.setText(": " + str(variable['expire_flag']))
        self.age_death.setText(": " + str(variable['age_death']))
        self.gender.setText(": " + str(variable['gender']))
        self.ethnicity.setText(": " + str(variable['ethnicity']))
        self.language.setText(": " + str(variable['language']))
        self.marital_status.setText(": " + str(variable['marital_status']))
        self.religion.setText(": " + str(variable['religion']))
        self.insurance.setText(": " + str(variable['insurance']))

        self.Code.setText(": " + str(variable['Code']))
        self.Descriptor.setText(": " + str(variable['Descriptor']))
        self.long_title.setText(": " + str(variable['long_title']))
        self.admission_type.setText(": " + str(variable['admission_type']))
        self.admit_new.setText(": " + str(variable['admit_new']))
        self.disch_new.setText(": " + str(variable['disch_new']))
        self.textBrowser.setText(str(variable['drug']))
        self.loadData(table_narms)

    def get_report(self, subject_id, birth_year):
        '''main report generator program'''
        df1 = pd.read_csv('test_file.csv')
        list_tolist = reversed(['hadm_id', 'Code', 'Descriptor', 'icd9_code',
                                'long_title', 'admission_type', 'diagnosis', 'insurance',
                                'language', 'religion', 'marital_status', 'ethnicity',
                                'gender', 'expire_flag', 'age', 'age_death',
                                'age_group', 'admit_year', 'admit_new', 'disch_new', 'description',
                                'drug_type', 'drug', 'formulary_drug_cd'])

        table = qu.query_single(df1, 'subject_id', int(subject_id), ["subject_id"],
                               list_tolist, ["subject_id"])

        ages = table['age'].tolist()
        patient_age = int(ages[0][0])
        year = birth_year + patient_age

        if patient_age <= 4 :
            age = '0-4'
        elif patient_age <= 9:
            age = '5-9'
        elif patient_age <= 19:
            age = '10-19'
        elif patient_age <= 29:
            age = '20-29'
        elif patient_age <= 39:
            age = '30-39'
        elif patient_age <= 49:
            age = '40-49'
        elif patient_age <= 59:
            age = '50-59'
        elif patient_age <= 69:
            age = '60-69'
        elif patient_age <= 79:
            age = '70-79'
        elif patient_age >= 80:
            age = '80+'

        for column in list_tolist:
            if column not in list(table.columns.values):
                table[column] = 'Nah'
        narms = qu.narms_query("narm's processed.csv", year, age)

        data_row = table.iloc[0]
        list_content = (data_row.tolist())

        list_name = ['subject_id', 'hadm_id', 'Code', 'Descriptor', 'icd9_code',
                     'long_title', 'admission_type', 'diagnosis', 'insurance', 'language', 'religion',
                     'marital_status', 'ethnicity', 'gender', 'expire_flag', 'age', 'age_death',
                     'age_group', 'admit_year', 'admit_new', 'disch_new', 'description',
                     'drug_type', 'drug', 'formulary_drug_cd']

        list_narms = ['Data_Year', 'Age_Group', 'Specimen_ID', 'Resistance_Pattern', 'AMI_Concl',
                      'AMP_Concl', 'ATM_Concl', 'AUG_Concl', 'AXO_Concl', 'AZM_Concl', 'CAZ_Concl',
                      'CCV_Concl', 'CEP_Concl', 'CEQ_Concl', 'CHL_Concl', 'CIP_Concl', 'CLI_Concl',
                      'COT_Concl', 'CTC_Concl', 'CTX_Concl', 'ERY_Concl', 'FEP_Concl', 'FFN_Concl',
                      'FIS_Concl', 'FOX_Concl', 'GEN_Concl', 'IMI_Concl', 'KAN_Concl', 'NAL_Concl',
                      'PTZ_Concl', 'SMX_Concl', 'STR_Concl', 'TEL_Concl', 'TET_Concl', 'TIO_Concl']

        variable = {}
        table_narms = {}

        for count in range(0, len(list_name)):
            cell = list_content[count]
            if isinstance(cell, list):
                if (len(cell) > 1 and list_name[count] != 'drug'):
                    list_content[count] = list_content[count][:1]
                elif list_name[count] == 'drug':
                    list_content[count] = list_content[count][:50]
            list_content[count] = str(list_content[count])
            variable[list_name[count]] = list_content[count]

        for count in range(0, len(list_narms)):
            table_narms[list_narms[count]] = str(narms.iloc[0][count])

        for item in variable.keys():
            values_tem = variable[item]
            if (values_tem[0] == '[' and values_tem[1] == "'" and
               values_tem[len(values_tem) - 2] == "'" and
               values_tem[len(values_tem) - 1] == ']') :
               variable[item] = values_tem[2:(len(variable[item]) - 2)]
            elif (values_tem[0] == '[' and
               values_tem[len(values_tem) - 1] == ']') :
               variable[item] = values_tem[1:(len(variable[item]) - 1)]
        variable['drug'] = variable['drug'].replace("'"," ")
        variable['age'] = int(float(variable['age']))
        variable['age'] = str(variable['age'])
    
        if (variable['age_death'] != 'nan'):
            variable['age_death'] = int(float(variable['age_death']))
            variable['age_death'] = str(variable['age_death'])
        if variable['expire_flag'] == '1' :
            variable['expire_flag'] = 'Death'
        else :
            variable['expire_flag'] = 'Live'

        return variable, table_narms

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Output1Window = QtWidgets.QMainWindow()
    ui = Ui_Output1Window()
    ui.setupUi(Output1Window)
    ui.query_values(Output1Window)
    Output1Window.show()
    sys.exit(app.exec_())
