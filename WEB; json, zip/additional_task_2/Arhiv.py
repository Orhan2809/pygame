from PyQt5.QtWidgets import QLabel, QApplication, QWidget, QMainWindow, QLineEdit, QPushButton
import datetime
import shutil


class Arhivator(QMainWindow):
    def __init__(self):
        super().__init__()
        Form.resize(600, 450)
        self.label = QLabel(Form)
        self.label.setGeometry(180, -200, 300, 450)
        self.label.setText("Путь к каталогу, который надо архивировать")
        self.label_2 = QLabel(Form)
        self.label_2.setGeometry(180, -140, 300, 450)
        self.label_2.setText("Путь к каталогу, в который необходимо поместить архив")
        self.textedit = QLineEdit(Form)
        self.textedit.setGeometry(180, 45, 250, 20)
        self.textedit_2 = QLineEdit(Form)
        self.textedit_2.setGeometry(180, 100, 250, 20)
        self.pushbutton = QPushButton(Form)
        self.pushbutton.setGeometry(200, 200, 200, 50)
        self.pushbutton.setText("Начать процесс")
        self.pushbutton.clicked.connect(lambda: self.make_reserve_arc(self.textedit.text(), self.textedit_2.text()))

    def make_reserve_arc(self, source, dest):
        if source != "" and dest != "":
            now_word = str(datetime.datetime.now()).replace(':', ';').replace(' ', '')[:-7]
            now_word = now_word[0:10] + "_" + now_word[10::]
            word = source.strip()
            word = word.split('/')[-1]

            shutil.make_archive(word + now_word, 'zip', root_dir=source)
            shutil.move(source + now_word + '.zip', dest)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Arhivator()
    Form.show()
    sys.exit(app.exec_())