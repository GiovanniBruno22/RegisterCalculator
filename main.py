# type: ignore
import os
import sys

from PyQt5 import QtWidgets, uic


class Register(QtWidgets.QMainWindow):
    def __init__(self):
        """Initializes the Register and sets up the user interface."""
        super(Register, self).__init__()
        self.ui_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "ui"))
        starting_ui_path = self.ui_path + "/Register.ui"
        uic.loadUi(starting_ui_path, self) 
        self.listlabel = self.findChild(QtWidgets.QLabel, "label_list")
        self.listlabel.setText("")
        self.totallabel = self.findChild(QtWidgets.QLabel, "label_total")

        for num in range(1,10):
            self.button = self.findChild(QtWidgets.QPushButton, f"Button_{num}")
            self.button.clicked.connect(self.menuItemPressed)
        
        self.checkoutButton = self.findChild(QtWidgets.QPushButton, f"Button_bill")
        self.checkoutButton.clicked.connect(self.checkTotal)

        self.show()
    

    def menuItemPressed(self):
        """Handles the button press event and sends a signal to update the list of items."""
        button = self.sender()
        button_text = button.text()
        button_text_split = button_text.split("\n")
        self.button_text_cleaned = button_text_split[0] + button_text_split [1]
        self.menuItemList()


    def menuItemList(self):
        """Handles and updates the list of items selected."""
        current_list = self.listlabel.text()
        self.listlabel.setText(current_list + self.button_text_cleaned + "\n")


    def checkTotal(self):
        """Checks the total of all the added items and updates the label accordingly."""
        list_text = self.listlabel.text().split("\n")
        total = 0
        for item in list_text:
            if item:
                price = [i.strip("$") for i in item.split(" ") if "$" in i]
                total += float(price[0])
                print(price)
        self.totallabel.setText(str(total)+"0")


app = QtWidgets.QApplication(sys.argv)
window = Register()
app.exec_()