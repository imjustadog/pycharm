# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\GitHub\pycharm\Serialsetting.ui'
#
# Created: Wed May 24 16:36:22 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog_Serial(QtGui.QDialog):
    def setupUi(self, Dialog_Serial):
        Dialog_Serial.setObjectName(_fromUtf8("Dialog_Serial"))
        Dialog_Serial.resize(482, 151)
        Dialog_Serial.setSizeGripEnabled(True)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog_Serial)
        self.buttonBox.setGeometry(QtCore.QRect(120, 110, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.tabWidget = QtGui.QTabWidget(Dialog_Serial)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 441, 81))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.checkBox_com1 = QtGui.QCheckBox(self.tab)
        self.checkBox_com1.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.checkBox_com1.setObjectName(_fromUtf8("checkBox_com1"))
        self.label_11 = QtGui.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(160, 21, 54, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.lineEdit_chno1 = QtGui.QLineEdit(self.tab)
        self.lineEdit_chno1.setGeometry(QtCore.QRect(220, 20, 71, 21))
        self.lineEdit_chno1.setObjectName(_fromUtf8("lineEdit_chno1"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.checkBox_com2 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_com2.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.checkBox_com2.setObjectName(_fromUtf8("checkBox_com2"))
        self.label_10 = QtGui.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(160, 21, 54, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.lineEdit_chno2 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_chno2.setGeometry(QtCore.QRect(220, 20, 71, 21))
        self.lineEdit_chno2.setObjectName(_fromUtf8("lineEdit_chno2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.checkBox_com3 = QtGui.QCheckBox(self.tab_3)
        self.checkBox_com3.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.checkBox_com3.setObjectName(_fromUtf8("checkBox_com3"))
        self.label_5 = QtGui.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(160, 21, 54, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit_chno3 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_chno3.setGeometry(QtCore.QRect(220, 20, 71, 21))
        self.lineEdit_chno3.setObjectName(_fromUtf8("lineEdit_chno3"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.checkBox_com4 = QtGui.QCheckBox(self.tab_4)
        self.checkBox_com4.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.checkBox_com4.setObjectName(_fromUtf8("checkBox_com4"))
        self.label_6 = QtGui.QLabel(self.tab_4)
        self.label_6.setGeometry(QtCore.QRect(160, 21, 54, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit_chno4 = QtGui.QLineEdit(self.tab_4)
        self.lineEdit_chno4.setGeometry(QtCore.QRect(220, 20, 71, 21))
        self.lineEdit_chno4.setObjectName(_fromUtf8("lineEdit_chno4"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.checkBox_com5 = QtGui.QCheckBox(self.tab_5)
        self.checkBox_com5.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.checkBox_com5.setObjectName(_fromUtf8("checkBox_com5"))
        self.label_7 = QtGui.QLabel(self.tab_5)
        self.label_7.setGeometry(QtCore.QRect(160, 21, 54, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lineEdit_chno5 = QtGui.QLineEdit(self.tab_5)
        self.lineEdit_chno5.setGeometry(QtCore.QRect(220, 20, 71, 21))
        self.lineEdit_chno5.setObjectName(_fromUtf8("lineEdit_chno5"))
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.checkBox_com6 = QtGui.QCheckBox(self.tab_6)
        self.checkBox_com6.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.checkBox_com6.setObjectName(_fromUtf8("checkBox_com6"))
        self.label_2 = QtGui.QLabel(self.tab_6)
        self.label_2.setGeometry(QtCore.QRect(160, 21, 54, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_chno6 = QtGui.QLineEdit(self.tab_6)
        self.lineEdit_chno6.setGeometry(QtCore.QRect(220, 20, 71, 21))
        self.lineEdit_chno6.setObjectName(_fromUtf8("lineEdit_chno6"))
        self.tabWidget.addTab(self.tab_6, _fromUtf8(""))
        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName(_fromUtf8("tab_7"))
        self.checkBox_com7 = QtGui.QCheckBox(self.tab_7)
        self.checkBox_com7.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.checkBox_com7.setObjectName(_fromUtf8("checkBox_com7"))
        self.label_8 = QtGui.QLabel(self.tab_7)
        self.label_8.setGeometry(QtCore.QRect(160, 21, 54, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.lineEdit_chno7 = QtGui.QLineEdit(self.tab_7)
        self.lineEdit_chno7.setGeometry(QtCore.QRect(220, 20, 71, 21))
        self.lineEdit_chno7.setObjectName(_fromUtf8("lineEdit_chno7"))
        self.tabWidget.addTab(self.tab_7, _fromUtf8(""))
        self.tab_8 = QtGui.QWidget()
        self.tab_8.setObjectName(_fromUtf8("tab_8"))
        self.checkBox_com8 = QtGui.QCheckBox(self.tab_8)
        self.checkBox_com8.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.checkBox_com8.setObjectName(_fromUtf8("checkBox_com8"))
        self.label_9 = QtGui.QLabel(self.tab_8)
        self.label_9.setGeometry(QtCore.QRect(160, 21, 54, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.lineEdit_chno8 = QtGui.QLineEdit(self.tab_8)
        self.lineEdit_chno8.setGeometry(QtCore.QRect(220, 20, 71, 21))
        self.lineEdit_chno8.setObjectName(_fromUtf8("lineEdit_chno8"))
        self.tabWidget.addTab(self.tab_8, _fromUtf8(""))

        self.retranslateUi(Dialog_Serial)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog_Serial.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog_Serial.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Serial)

    def retranslateUi(self, Dialog_Serial):
        Dialog_Serial.setWindowTitle(_translate("Dialog_Serial", "通道设置", None))
        self.checkBox_com1.setText(_translate("Dialog_Serial", "使能通道", None))
        self.label_11.setText(_translate("Dialog_Serial", "通道编号", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog_Serial", "通道1", None))
        self.checkBox_com2.setText(_translate("Dialog_Serial", "使能通道", None))
        self.label_10.setText(_translate("Dialog_Serial", "通道编号", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog_Serial", "通道2", None))
        self.checkBox_com3.setText(_translate("Dialog_Serial", "使能通道", None))
        self.label_5.setText(_translate("Dialog_Serial", "通道编号", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog_Serial", "通道3", None))
        self.checkBox_com4.setText(_translate("Dialog_Serial", "使能通道", None))
        self.label_6.setText(_translate("Dialog_Serial", "通道编号", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog_Serial", "通道4", None))
        self.checkBox_com5.setText(_translate("Dialog_Serial", "使能通道", None))
        self.label_7.setText(_translate("Dialog_Serial", "通道编号", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Dialog_Serial", "通道5", None))
        self.checkBox_com6.setText(_translate("Dialog_Serial", "使能通道", None))
        self.label_2.setText(_translate("Dialog_Serial", "通道编号", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Dialog_Serial", "通道6", None))
        self.checkBox_com7.setText(_translate("Dialog_Serial", "使能通道", None))
        self.label_8.setText(_translate("Dialog_Serial", "通道编号", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("Dialog_Serial", "通道7", None))
        self.checkBox_com8.setText(_translate("Dialog_Serial", "使能通道", None))
        self.label_9.setText(_translate("Dialog_Serial", "通道编号", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("Dialog_Serial", "通道8", None))

