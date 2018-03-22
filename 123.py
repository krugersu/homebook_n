import sys
import sqlite3
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, qApp, QApplication, QDialog, QVBoxLayout, QTableView, QPushButton, QMdiArea, QMdiSubWindow
from PyQt5 import QtCore, QtSql, QtGui
from PyQt5.QtGui import QIcon

import meshandler
import dbpool

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        parent=None
        super(Example, self).__init__(parent)
        self.mdiArea = QMdiArea(self)
        self.setCentralWidget(self.mdiArea)

        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        addAction = QAction(QIcon('exit.png'), '&Показать', self)
        # addAction.setShortcut('Ctrl+Q')
        addAction.setStatusTip('Показать библиотеку')

        addAction.triggered.connect(self.m_showlibrary)

        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Библиотека')
        # fileMenu.addAction("ss")

        fileMenu.addAction(exitAction)
        fileMenu.addAction(addAction)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        self.toolbar.addAction(addAction)

        self.setGeometry(100, 100, 800, 800)
        self.setWindowTitle('Menubar')

        self.show()

    def m_showlibrary(self):

        print("111")
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('homebook.db')
        model = QtSql.QSqlTableModel()
        delrow = -1
        initializeModel(model)

        view1 = createView("Table Model (View 1)", model)
        view1.clicked.connect(findrow)

        dlg = QDialog()

        layout = QVBoxLayout()
        layout.addWidget(view1)

        button = QPushButton("Add a row")
        button.clicked.connect(addrow)
        layout.addWidget(button)

        btn1 = QPushButton("del a row")
        btn1.clicked.connect(lambda: model.removeRow(view1.currentIndex().row()))
        layout.addWidget(btn1)


        dlg.setLayout(layout)
        dlg.setWindowTitle("Database Demo")
        #dlg.setModal(self)
        self.mdiArea.addSubWindow(dlg)
        #self.mdiArea.addSubWindow(dlg)
        dlg.show()

        #dlg.exec_()
        #dlg.show()
        print("444")



def initializeModel(model):
    model.setTable('test2')
    model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
    model.select()

def addrow():
    print (model.rowCount())
    ret = model.insertRows(model.rowCount(), 1)
    print (ret)

def findrow(i):
    delrow = i.row()


def createView(title, model):
    view = QTableView()
    view.setModel(model)
    view.setWindowTitle(title)
    return view



if __name__ == '__main__':
    app = QApplication(sys.argv)


    ex = Example()
    sys.exit(app.exec_())
