# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'readWidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 206)
        Form.setMinimumSize(QtCore.QSize(600, 206))
        Form.setMaximumSize(QtCore.QSize(600, 206))
        self.pB_close = QtWidgets.QPushButton(Form)
        self.pB_close.setGeometry(QtCore.QRect(500, 160, 81, 31))
        self.pB_close.setObjectName("pB_close")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 561, 131))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(1, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(2, 5, item)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pB_close.setText(_translate("Form", "确认"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "紧急程度"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "数值区间"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "重要程度"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "数值区间"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "时间系数（天）"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "数值区间"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Form", "可暂缓"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("Form", "1~3"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("Form", "拓展"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("Form", "1~3"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("Form", "短期"))
        item = self.tableWidget.item(0, 5)
        item.setText(_translate("Form", "1~15"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("Form", "尽快完成"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("Form", "4~6"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("Form", "辅助"))
        item = self.tableWidget.item(1, 3)
        item.setText(_translate("Form", "4~6"))
        item = self.tableWidget.item(1, 4)
        item.setText(_translate("Form", "中期"))
        item = self.tableWidget.item(1, 5)
        item.setText(_translate("Form", "16~30"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("Form", "急需完成"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("Form", "7~10"))
        item = self.tableWidget.item(2, 2)
        item.setText(_translate("Form", "必要"))
        item = self.tableWidget.item(2, 3)
        item.setText(_translate("Form", "7~10"))
        item = self.tableWidget.item(2, 4)
        item.setText(_translate("Form", "长期"))
        item = self.tableWidget.item(2, 5)
        item.setText(_translate("Form", "30+"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
