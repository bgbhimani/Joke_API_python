import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QPushButton, QLabel, QCheckBox, QTextEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
import requests


class MainWindow(QMainWindow):
    
    base_url = "https://v2.jokeapi.dev/joke"
    url = "https://v2.jokeapi.dev"
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Random Joke Generator using API")
        self.setGeometry(200,200,500,800)
        self.setWindowIcon(QIcon("Logo.png"))
        self.titlelable = QLabel("Enjoy & Laugh",self)
        
        self.joke_type1 = QRadioButton("ProGramming",self)
        self.joke_type2 = QRadioButton("Dark",self)
        self.joke_type3 = QRadioButton("Christmas",self)
        self.joke_type4 = QRadioButton("Any",self)
        
        self.button = QPushButton("Run!",self)
        self.button.setDisabled(True)
        self.exit_button = QPushButton("Exit",self)
        self.exit_button.setDisabled(True)
        
        self.joke_id = QLabel("Joke Id:",self)
        self.joke = QLabel("Joke:",self)
        
        self.text_edit = QTextEdit(self)
        self.font = QFont()
        self.font.setPointSize(14)
        
        self.initUI()
        self.run()
        
    def close_program(self):
        QApplication.quit()

    def run(self):
        self.joke_type1.toggled.connect(self.select_joke)
        self.joke_type2.toggled.connect(self.select_joke)
        self.joke_type3.toggled.connect(self.select_joke)
        self.joke_type4.toggled.connect(self.select_joke)
        self.button.setDisabled(False)
        self.button.clicked.connect(self.button_click)
        
        self.exit_button.setDisabled(False)
        self.exit_button.clicked.connect(self.close_program)
        
    def button_click(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            # print("Get Connected")
            joke = response.json()
            print(self.url)
            print(joke)
            if joke["error"] == False:
                self.joke_id.setText(f"Joke Id: {joke["id"]}" )
                print(f"Joke-Id:  {joke["id"]}")
                
                if joke["type"] == "single":
                    # self.joke.setText(joke["joke"])
                    self.text_edit.setText(joke["joke"])
                    print(joke["joke"])
                else:
                    self.text_edit.setText(f"{joke["setup"]}\n{joke["delivery"]}")
                    # print(joke["setup"])
                    # print(joke["delivery"])
            else:
                print(f"Joke Not Found on {type[13:]}")
        else:
            print(f"Not Connected Error:{response.status_code}")
            
        self.text_edit.setReadOnly(True)
    
    def select_joke(self):
        if self.sender().isChecked():
            self.url =  f"{self.base_url}/{self.sender().text().lower()}"
            print(self.url)
            print(f"{self.sender().text()} is Selected")
            
    
    def initUI(self):
        self.titlelable.setGeometry(0,0,500,70)
        self.titlelable.setStyleSheet("color:#e03131;"
                                      "font-size: 25px;"
                                      "font-weight: bold;"
                                      "background-color: #212121")
        self.titlelable.setAlignment(Qt.AlignCenter)
        
        self.joke_type1.setGeometry(20,80,200,50)
        self.joke_type2.setGeometry(20,130,200,50)
        self.joke_type3.setGeometry(20,180,200,50)
        self.joke_type4.setGeometry(20,230,200,50)
        self.setStyleSheet("QRadioButton{"
                           "font-size: 25px;"
                           "}")
        
        self.button.setGeometry(20,290,100,50)
        self.button.setStyleSheet("font-size:25px;"
                                  "color: #e03131;"
                                  "font-weight: bold")
        
        self.exit_button.setGeometry(140,290,100,50)
        self.exit_button.setStyleSheet("font-size:25px;"
                                  "color: #e03131;"
                                  "font-weight: bold")
        
        self.joke_id.setGeometry(10,340,500,50)
        self.joke_id.setStyleSheet("color:#e03131;"
                                      "font-size: 20px;"
                                      "font-weight: bold;")
        self.joke.setGeometry(10,390,500,400)
        self.joke.setStyleSheet("color:#e03131;"
                                      "font-size: 20px;")
        self.joke.setAlignment(Qt.AlignTop)
        
        self.text_edit.setGeometry(10,420,480,370)
        self.text_edit.setStyleSheet("font-size=25px;"
                                     "color:#e03131;"
                                     "font-weight=bold")
        self.text_edit.setFont(self.font)
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())