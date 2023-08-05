from translate import Translator
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox, QShortcut
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt

# Load the UI file
Form, Window = uic.loadUiType("dictionary.ui")

# Create the application
app = QApplication([])

# Create the main window
window = Window()
form = Form()
form.setupUi(window)


# Create a translator object
translator = Translator(from_lang='en', to_lang='es')




# Connect translation functionality to the "Enter" key press event
def translate_text():
    try:
        text = form.inputLineEdit.text()
        translation = translator.translate(text)
        translated_text = translation
        form.outputTextEdit.setText(translated_text)  # Set the translated text in the outputTextEdit
    except Exception as ex:
        QMessageBox.critical(window, "Error", str(ex))





# Create a shortcut for the "Enter" key
shortcut = QShortcut(QKeySequence(Qt.Key_Return), window)
shortcut.activated.connect(translate_text)





# Show the window
window.show()

# Start the event loop
app.exec_()



