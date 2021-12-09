
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication
from functools import partial
from board import AmharicKB

class Controller():
    def __init__(self, view):
        self._view = view
        self._signal_connector()

    def _build_word(self, letter):
    
        word = self._view.show_text_to_display() + letter
        self._view.display.setText(word)

    
    def _build_extend_btns(self, let):
   
        let = self._view.show_text_to_display() 
        self._view.display.setText(let)


    def _signal_connector(self):

        command_ctrl = {"Ctr","Del","Tab","Ent","Cmd", "Sht","Alt","Fun","Cap-lock"}
        for key, btn in self._view.button.items():
            if key not in command_ctrl:
                btn.clicked.connect(partial(self._build_word, key))

        
            # btn.clicked.connect(partial(self._build_extend_btns, key))


        self._view.display.returnPressed.connect(self._build_word)
        # self._view.display.returnPressed.connect(self._build_extend_btns)
        self._view.button['Del'].clicked.connect(self._view.back_space)
        self._view.button['Clr'].clicked.connect(self._view.clear_display)
        self._view.button['Sht'].clicked.connect(self._view.show_extend_letters)




def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    
    
    view = AmharicKB()

    Controller(view=view)
    app.exit()
    view.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
