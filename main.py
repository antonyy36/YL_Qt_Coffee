import sqlite3
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect("coffee.sqlite3")
        self.adding()

    def adding(self):
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())