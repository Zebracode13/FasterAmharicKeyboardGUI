
# from _typeshed import Self
from PyQt5.QtCore import  Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import (QApplication, QBoxLayout, QButtonGroup, QGridLayout, QLineEdit, QMainWindow, QMessageBox, QPushButton, QTextEdit, QVBoxLayout, QWidget, 
                        QShortcut, QLabel, QHBoxLayout)


class AmharicKB(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.boardLayout = QVBoxLayout()
        self.boardWidget = QWidget(self)
        self.palette = QPalette()
        self.setCentralWidget(self.boardWidget)
        self.boardWidget.setLayout(self.boardLayout)


        self.palette.setColor(QPalette.ButtonText, Qt.red)
        self.palette.setColor(QPalette.Button, Qt.yellow)
        self.palette.setColor(QPalette.Text, Qt.blue)
        self.palette.setColor(QPalette.Background, Qt.green)

        self.buttons= {
            '1': ((0,0),()),
            '2': ((0,1),()),
            '3': ((0,2),()),
            '4': ((0,3),()),
            '5': ((0,4),()),
            '6': ((0,5),()),
            '7': ((0,6),()),
            '8': ((0,7),()),
            '9': ((0,8),()),
            '0': ((0,9),()),
            "Del":((0,10),()),
            "Clr":((0,11),()),
            "Tran": ((0,12),()),
            "Tab":((1,0),()),
            'ሀ': ((1,1),('ሁ','ሂ','ሃ','ሄ','ህ','ሆ')),
            'ለ': ((1,2),('ሉ','ሊ','ላ','ሌ','ል','ሎ')),
            'ሐ': ((1,3),('ሑ','ሒ','ሓ','ሔ','ሕ','ሖ')),
            'መ': ((1,4),('ሙ','ሚ','ማ','ሜ','ም','ሞ')),
            'ሠ': ((1,5),('ሡ','ሢ','ሣ','ሤ','ሥ','ሦ')),
            'ረ': ((1,6),('ሩ','ሪ','ራ','ሬ','ር','ሮ')),
            'ሰ': ((1,7),('ሱ','ሲ','ሳ','ሴ','ስ','ሶ')),
            'ሸ': ((1,8),('ሹ','ሺ','ሻ','ሼ','ሽ','ሾ')),
            'ቀ': ((1,9),('ቁ','ቂ','ቃ','ቄ','ቅ','ቆ')),
            'በ': ((1,10),('ቡ','ቢ','ባ','ቤ','ብ','ቦ')),
            'ተ': ((1,11),('ቱ','ቲ','ታ','ቴ','ት','ቶ')),
            
            "Ent": ((1,12),()),
            "Cap" :((2,0),()),
            'ቸ':  ((2,1),('ቹ','ቺ','ቻ','ቼ','ች','ቾ')),
            'ኀ': ((2,2),('ኁ','ኂ','ኃ','ኄ','ኅ','ኆ')),
            'ነ': ((2,3),('ኑ','ኒ','ና','ኔ','ን','ኖ')),	
            'ኘ': ((2,4),('ኙ','ኚ','ኛ','ኜ','ኝ','ኞ')),
            'አ': ((2,5),('ኡ','ኢ','ኣ','ኤ','እ','ኦ')),
            'ከ': ((2,6),('ኩ','ኪ','ካ','ኬ','ክ','ኮ')),
            'ኸ': ((2,7),('ኹ','ኺ','ኻ','ኼ','ኽ','ኾ')),
            'ወ': ((2,8),('ዉ','ዊ','ዋ','ዌ','ው','ዎ')),
            'ዐ': ((2,9),('ዑ','ዒ','ዓ','ዔ','ዕ','ዖ')), 
            'ዘ': ((2,10),('ዙ','ዚ','ዛ','ዜ','ዝ','ዞ')),
            'ዠ': ((2,11),('ዡ','ዢ','ዣ','ዤ','ዥ','ዦ')),
            # add r_shit(2,12)
            "Sht": ((3,0),()),
            # add l_shift(3,0)
            'የ': ((3,1),('ዩ','ያ','ዬ','ይ','ይ','ዮ')), 
            'ደ': ((3,2),('ዱ','ዲ','ዳ','ዴ','ድ','ዶ')),
            'ጀ': ((3,3),('ጁ','ጂ','ጃ','ጄ','ጅ','ጆ')),
            'ገ': ((3,4),('ጉ','ጊ','ጋ','ጌ','a','b')),
            'ጠ': ((3,5),('ጡ','ጢ','ጣ','ጤ','ጥ','ጦ')),
            'ጨ': ((3,6),('ጩ','ጪ','ጫ','ጬ','ጭ','ጮ')),
            'ጰ': ((3,7),('ጱ','ጲ','ጳ','ጴ','ጵ','ጶ')),
            'ጸ': ((3,8),('ጹ','ጺ','ጻ','ጼ','ጽ','ጾ')),
            'ፀ': ((3,9),('ፁ','ፂ','ፃ','ፄ','ፅ','ፆ')),
            'ፈ': ((3,10),('ፉ','ፊ','ፋ','ፌ','ፍ','ፎ')),
            'ፐ': ((3,11),('ፑ','ፒ','ፓ','ፔ','ፕ','ፖ')),   
            # add <up,down,left,right movers> (3,12)
            # add comand 4,0
            "Cmd": ((4,0),()),
            'ቨ': ((4,1),()),
            'ሏ': ((4,2),()),
            'ቈ': ((4,3),()),
            'ኈ': ((4,4),()),
            'ኰ': ((4,6),()),
            ' ' : ((4,5),()),
            'ራ': ((4,7),()),
            'ጐ': ((4,8),()),
            "Alt": ((4,9),()),
            "Fun": ((4,10),()),
            "Enter": ((4,11),()),
            # "=":(0,12),  
            "+":((3,12),()),
            '/':((4,12),()),
            "*": ((2,12),()),
             "-":((1,12),()),         
        }
        

        self.boardWidget.setPalette(self.palette)
        # key functions
        self._create_main_display()
        self._creat_board()
        # self.show_extend_letters()


    def _create_main_display(self):
        self.display = QLineEdit()

        self.display.setAlignment(Qt.AlignLeft)

        self.boardLayout.addWidget(self.display)

    # def _create_hint_display(self):
    #     self.display_hinter =  QGridLayout()
    #     self.display.setAlignment(Qt.AlignLeft)

    #     self.boardLayout.addWidget(self.display)


    def show_extend_letters(self):

        for key, extend in self.buttons.items():
            if len(extend[1]) > 1:
                for x in range(0,6):
                    pos_x_y = (0, x)
                    self.ext_buttons[extend[1][x]] = QPushButton(extend[1][x])
                    self.ext_buttons[extend[1][x]].setFixedSize(50,30)
                    for let in range(len(self.display.text())):
                        if self.display.text()[let] == key:
                            self.buttonsLayout.addWidget(self.ext_buttons[extend[1][x]],  pos_x_y[0], pos_x_y[1])
            
        self.boardLayout.addLayout(self.buttonsLayout)
    
    def _creat_board(self):
        self.button = {}
        self.ext_buttons = {}

        self.buttonsLayout = QGridLayout()

        for key, extend in self.buttons.items():
            self.button[key] = QPushButton(key)
            self.button[key].setFixedSize(50,30)
            self.buttonsLayout.addWidget(self.button[key], extend[0][0], extend[0][1])

        self.boardLayout.addLayout(self.buttonsLayout)
            
    def back_space(self):
        return self.display.backspace()

    def clear_display(self):
        self.display.setText("")


    def show_text_to_display(self):
        return self.display.text()

