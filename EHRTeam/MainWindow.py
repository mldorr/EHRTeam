"""
MainWindow.py

Form implementation generated from reading ui file 'MainWindow_rev.ui'
Originally created by: PyQt5 UI code generator 5.11.3, now edited by us
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from QtUI_rev import UiOutput1Window
from output_pdf import get_report as pdf_get_report

class UiMainWindow(object):
    """builds the primary window and makes it work"""

    def open_window(self):
        """opens the window"""
        self.window = QtWidgets.QMainWindow()
        self.ui = UiOutput1Window()
        patient_id = int(self.lineEdit_patientid.text())
        birth_year = int(self.lineEdit_birthyear.text())
        pdf_get_report(patient_id, birth_year)
        self.ui.setup_ui(self.window, patient_id, birth_year)
        self.window.show()

    def setup_ui(self, MainWindow):
        """builds ui"""
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(231, 208)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 20, 191, 131))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_22 = QtWidgets.QLabel(self.groupBox_5)
        self.label_22.setGeometry(QtCore.QRect(10, 30, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.lineEdit_patientid = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_patientid.setGeometry(QtCore.QRect(80, 30, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_patientid.setFont(font)
        self.lineEdit_patientid.setObjectName("lineEdit_patientid")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton.setGeometry(QtCore.QRect(110, 100, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_23 = QtWidgets.QLabel(self.groupBox_5)
        self.label_23.setGeometry(QtCore.QRect(10, 60, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.lineEdit_birthyear = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_birthyear.setGeometry(QtCore.QRect(80, 60, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_birthyear.setFont(font)
        self.lineEdit_birthyear.setObjectName("lineEdit_birthyear")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 231, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.open_window)

        self.retranslate_ui(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslate_ui(self, MainWindow):
        """fixes variable labels"""
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Health Record Input"))
        self.label_22.setText(_translate("MainWindow", "Patient ID"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.label_23.setText(_translate("MainWindow", "Birth Year"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setup_ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
