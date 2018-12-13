"""
MainWindow.py

Form implementation generated from reading ui file 'MainWindow_rev.ui'
Originally created by: PyQt5 UI code generator 5.11.3, now edited by us
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from report_ui import UiOutput1Window
from output_pdf import get_report as pdf_get_report

class UiMainWindow(object):
    """builds the primary window and makes it work"""
    def __init__(self, main_window):
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.group_box_subtitle = QtWidgets.QGroupBox(self.centralwidget)
        self.label_patientid = QtWidgets.QLabel(self.group_box_subtitle)
        self.label_edit_patientid = QtWidgets.QLineEdit(self.group_box_subtitle)
        self.push_button = QtWidgets.QPushButton(self.group_box_subtitle)
        self.label_birthyear = QtWidgets.QLabel(self.group_box_subtitle)
        self.label_edit_birthyear = QtWidgets.QLineEdit(self.group_box_subtitle)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.statusbar = QtWidgets.QStatusBar(main_window)

        self.setup_ui(main_window)

    def open_window(self):
        """opens the window"""
        self.next_window = QtWidgets.QMainWindow()
        patient_id = int(self.label_edit_patientid.text())
        birth_year = int(self.label_edit_birthyear.text())
        self.next_ui = UiOutput1Window(self.next_window, patient_id, birth_year)
        pdf_get_report(patient_id, birth_year)
        # self.next_ui.setup_ui(self.next_window, patient_id, birth_year)
        self.next_window.show()

    def setup_ui(self, main_window):
        """builds ui"""
        main_window.setObjectName("main_window")
        main_window.resize(231, 208)
        self.centralwidget.setObjectName("centralwidget")
        self.group_box_subtitle.setGeometry(QtCore.QRect(20, 20, 191, 131))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.group_box_subtitle.setFont(font)
        self.group_box_subtitle.setObjectName("group_box_subtitle")
        self.label_patientid.setGeometry(QtCore.QRect(10, 30, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_patientid.setFont(font)
        self.label_patientid.setObjectName("label_patientid")
        self.label_edit_patientid.setGeometry(QtCore.QRect(80, 30, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_edit_patientid.setFont(font)
        self.label_edit_patientid.setObjectName("label_edit_patientid")
        self.push_button.setGeometry(QtCore.QRect(110, 100, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.push_button.setFont(font)
        self.push_button.setObjectName("push_button")
        self.label_birthyear.setGeometry(QtCore.QRect(10, 60, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_birthyear.setFont(font)
        self.label_birthyear.setObjectName("label_birthyear")
        self.label_edit_birthyear.setGeometry(QtCore.QRect(80, 60, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_edit_birthyear.setFont(font)
        self.label_edit_birthyear.setObjectName("label_edit_birthyear")
        main_window.setCentralWidget(self.centralwidget)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 231, 18))
        self.menubar.setObjectName("menubar")
        main_window.setMenuBar(self.menubar)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.push_button.clicked.connect(self.open_window)

        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, main_window):
        """fixes variable labels"""
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "MainWindow"))
        self.group_box_subtitle.setTitle(_translate("main_window", "Health Record Input"))
        self.label_patientid.setText(_translate("main_window", "Patient ID"))
        self.push_button.setText(_translate("main_window", "Search"))
        self.label_birthyear.setText(_translate("main_window", "Birth Year"))


if __name__ == "__main__":
    import sys
    APP = QtWidgets.QApplication(sys.argv)
    MAINWINDOW = QtWidgets.QMainWindow()
    UI = UiMainWindow(MAINWINDOW)
    MAINWINDOW.show()
    sys.exit(APP.exec_())
