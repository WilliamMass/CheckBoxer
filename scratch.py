'''
This is how to do a simple list widget, so that we don't have to fuck around
with spacing out every item
'''
from PyQt5.QtWidgets import *

import sys


class myListWidget(QListWidget):

    def Clicked(self, item):
        QMessageBox.information(self, "ListWidget", "You clicked: " + item.text())


def main():
    app = QApplication(sys.argv)
    listWidget = myListWidget()

    # Resize width and height
    listWidget.resize(300, 120)

    listWidget.addItem("Item 1");
    listWidget.addItem("Item 2");
    listWidget.addItem("Item 3");
    listWidget.addItem("Item 4");

    listWidget.setWindowTitle('PyQT QListwidget Demo')
    listWidget.itemClicked.connect(listWidget.Clicked)

    listWidget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()