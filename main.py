import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class DBSample(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect("coffee.sqlite")
        self.cur = self.con.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS coff (id INTEGER,Название_сорта STRING,Степень_обжарки INTEGER,Молотый_В_зернах INTEGER,Вкус STRING,Цена INTEGER,Объем_упаковки INTEGER)")
        self.cur.execute("INSERT INTO coff VALUES (1, 'Эcспрессо', 5, 1, 'Мега-супер-сладкий', 200, 100)")
        self.select_data()

    def select_data(self):
        res = self.con.cursor().execute("SELECT * FROM coff").fetchall()

        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DBSample()
    ex.show()
    sys.exit(app.exec())
