import sqlite3
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from UI.UI import *


class MyWidget(QMainWindow, Ui_MainWindow2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("data/coffee.sqlite3")
        self.f = False
        self.AddButton.clicked.connect(self.adding)
        self.AddButton.click()

    def adding(self):
        if self.f:
            self.add_form = AddWidget(self)
            self.add_form.show()
        if True:
            cur = self.con.cursor()
            self.result = cur.execute("SELECT * FROM coffee").fetchall()
            self.tableWidget.setRowCount(len(self.result))
            self.tableWidget.setColumnCount(len(self.result[0]))
            self.titles = ['ID', 'Сорт кофе', 'Степень Обжарки', 'Описание вкуса', 'Цена', 'Объем']
            # Заполнили таблицу полученными элементами
            self.tableWidget.setColumnCount(len(self.titles))
            self.tableWidget.setHorizontalHeaderLabels(self.titles)
            self.tableWidget.setRowCount(0)
            for i, row in enumerate(self.result):
                self.tableWidget.setRowCount(
                    self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(
                        i, j, QTableWidgetItem(str(elem)))
            self.f = True

    def save_result(self, type, obj, mol_zern, taste, price, vol):
        print(type, obj, mol_zern, taste, price, vol)
        cur = self.con.cursor()
        cur.execute("INSERT INTO coffee VALUES(NULL, ?, ?, ?, ?, ?, ?)",
                    (type, obj, mol_zern, taste, price, vol,))
        self.con.commit()
        self.f = False
        self.AddButton.click()


class AddWidget(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent1 = parent
        self.setupUi(self)
        self.SaveButton.clicked.connect(self.get_adding_verdict)

    def get_adding_verdict(self):
        if self.lineEdit.text() == '' or self.plainTextEdit.toPlainText() == '':
            self.statusBar().showMessage('Неверно заполнена форма')
            return False
        else:
            text = ''

            self.statusBar().showMessage('')

            if self.radioButton.isChecked():
                text = self.radioButton.text()
            elif self.radioButton_2.isChecked():
                text = self.radioButton_2.text()
            self.parent1.save_result(str(self.lineEdit.text()), self.spinBox.value(),
                                     str(text), str(self.plainTextEdit.toPlainText()), self.doubleSpinBox.value(),
                                     self.spinBox_2.value())

            self.close()
            return True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())