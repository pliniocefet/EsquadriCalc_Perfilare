import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QVBoxLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        # Set up the window
        self.setWindowTitle('Message Box Example')
        self.setGeometry(100, 100, 300, 200)
        
        # Set up the layout and button
        layout = QVBoxLayout()
        
        self.button = QPushButton('Show Message Box', self)
        self.button.clicked.connect(self.show_message_box)
        
        layout.addWidget(self.button)
        self.setLayout(layout)
    
    def show_message_box(self):
        # Create a QMessageBox
        msg_box = QMessageBox()
        msg_box.setWindowTitle('Information')
        msg_box.setText('This is a message box!')
        msg_box.setIcon(QMessageBox.Information)  # You can use different icons (Information, Warning, Critical, etc.)
        
        # Optional: Add buttons to the message box
        msg_box.setStandardButtons(QMessageBox.Ok)
        
        # Show the message box and get the response
        response = msg_box.exec_()
        
        if response == QMessageBox.Ok:
            print('OK clicked')

# Run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
