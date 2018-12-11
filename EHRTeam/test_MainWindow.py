"""
This test file is used to test function in MainWindow.py in EHRTeam
"""
import sys
import unittest
import os.path
from PyQt5 import QtCore, QtGui, QtWidgets
from QtUI_rev import UiOutput1Window
from output_pdf import get_report as pdf_get_report

class TestFunctions(unittest.TestCase):
    """
    Unittest class
    """
    def test_setup_ui(self):
        """
        This function test whether the "setup_ui" function set a correct object name for each
        attributes and check if they are in the correct postition.
        """
        self.assertEqual(MainWindow.objectName(), "MainWindow")
        self.assertEqual(MainWindow.size(), QtCore.QSize(231, 208))
        self.assertEqual(centralwidget.objectName(), "centralwidget")
        self.assertEqual(groupBox_5.geometry(), QtCore.QRect(20, 20, 191, 131))
        self.assertEqual(groupBox_5.objectName(), "groupBox_5")
        self.assertEqual(label_22.geometry(), QtCore.QRect(10, 30, 71, 21))
        self.assertEqual(label_22.objectName(), "label_22")
        self.assertEqual(lineEdit_patientid.geometry(), QtCore.QRect(80, 30, 101, 20))
        self.assertEqual(lineEdit_patientid.objectName(), "lineEdit_patientid")
        self.assertEqual(pushButton.geometry(), QtCore.QRect(110, 100, 71, 20))
        self.assertEqual(pushButton.objectName(), "pushButton")
        self.assertEqual(label_23.geometry(), QtCore.QRect(10, 60, 71, 21))
        self.assertEqual(label_23.objectName(), "label_23")
        self.assertEqual(lineEdit_birthyear.geometry(), QtCore.QRect(80, 60, 101, 20))
        self.assertEqual(lineEdit_birthyear.objectName(), "lineEdit_birthyear")
        self.assertEqual(menubar.geometry(), QtCore.QRect(0, 0, 231, 18))
        self.assertEqual(menubar.objectName(), "menubar")
        self.assertEqual(MainWindow.menuBar(), menubar)
        self.assertEqual(statusbar.objectName(), "statusbar")
        self.assertEqual(MainWindow.statusBar(), statusbar)


    def test_open_window(self):
        """
        This function test whether the "open_window" function get a write values from text
        editor for patient_id & birth year. Check if pdf is generated by the function.
        Check if the new window is opened after calling the function.
        """
        self.window = QtWidgets.QMainWindow()
        self.ui = UiOutput1Window()
        lineEdit_patientid.setText("61")
        lineEdit_birthyear.setText("1947")
        patient_id = int(lineEdit_patientid.text())
        birth_year = int(lineEdit_birthyear.text())
        pdf_get_report(patient_id, birth_year)
        self.ui.setup_ui(self.window, 61, 1947)
        self.window.show()

        self.assertEqual(patient_id, int(lineEdit_patientid.text()))
        self.assertEqual(birth_year, int(lineEdit_birthyear.text()))
        self.assertTrue(self.window.isActiveWindow)
        self.assertTrue(os.path.isfile('html2pdf.pdf'))

    def test_retranslate_ui(self):
        """
        This function test whether the "test_retranslate_ui" set a write title
        for each attributes.
        """
        self.assertEqual(MainWindow.windowTitle(), "MainWindow")
        self.assertEqual(groupBox_5.title(), "Health Record Input")
        self.assertEqual(label_22.text(), "Patient ID")
        self.assertEqual(pushButton.text(), "Search")
        self.assertEqual(label_23.text(), "Birth Year")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setObjectName("MainWindow")
    MainWindow.resize(231, 208)
    centralwidget = QtWidgets.QWidget(MainWindow)
    centralwidget.setObjectName("centralwidget")
    groupBox_5 = QtWidgets.QGroupBox(centralwidget)
    groupBox_5.setGeometry(QtCore.QRect(20, 20, 191, 131))
    font = QtGui.QFont()
    font.setPointSize(15)
    groupBox_5.setFont(font)
    groupBox_5.setObjectName("groupBox_5")
    label_22 = QtWidgets.QLabel(groupBox_5)
    label_22.setGeometry(QtCore.QRect(10, 30, 71, 21))
    font = QtGui.QFont()
    font.setPointSize(10)
    label_22.setFont(font)
    label_22.setObjectName("label_22")
    lineEdit_patientid = QtWidgets.QLineEdit(groupBox_5)
    lineEdit_patientid.setGeometry(QtCore.QRect(80, 30, 101, 20))
    font = QtGui.QFont()
    font.setPointSize(10)
    lineEdit_patientid.setFont(font)
    lineEdit_patientid.setObjectName("lineEdit_patientid")
    pushButton = QtWidgets.QPushButton(groupBox_5)
    pushButton.setGeometry(QtCore.QRect(110, 100, 71, 20))
    font = QtGui.QFont()
    font.setPointSize(10)
    pushButton.setFont(font)
    pushButton.setObjectName("pushButton")
    label_23 = QtWidgets.QLabel(groupBox_5)
    label_23.setGeometry(QtCore.QRect(10, 60, 71, 21))
    font = QtGui.QFont()
    font.setPointSize(10)
    label_23.setFont(font)
    label_23.setObjectName("label_23")
    lineEdit_birthyear = QtWidgets.QLineEdit(groupBox_5)
    lineEdit_birthyear.setGeometry(QtCore.QRect(80, 60, 101, 20))
    font = QtGui.QFont()
    font.setPointSize(10)
    lineEdit_birthyear.setFont(font)
    lineEdit_birthyear.setObjectName("lineEdit_birthyear")
    MainWindow.setCentralWidget(centralwidget)
    menubar = QtWidgets.QMenuBar(MainWindow)
    menubar.setGeometry(QtCore.QRect(0, 0, 231, 18))
    menubar.setObjectName("menubar")
    MainWindow.setMenuBar(menubar)
    statusbar = QtWidgets.QStatusBar(MainWindow)
    statusbar.setObjectName("statusbar")
    MainWindow.setStatusBar(statusbar)

    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
    groupBox_5.setTitle(_translate("MainWindow", "Health Record Input"))
    label_22.setText(_translate("MainWindow", "Patient ID"))
    pushButton.setText(_translate("MainWindow", "Search"))
    label_23.setText(_translate("MainWindow", "Birth Year"))

    unittest.main()
