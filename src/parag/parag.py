
import os
import sys

try:
    _path = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
    sys.path.append(_path)
except:
    pass

_path = os.path.split(os.path.split(os.path.abspath("__file__"))[0])[0]
sys.path.append(_path)

from docx                                                              import Document
from PyQt5.QtCore                                                      import *
from PyQt5.QtGui                                                       import *
from PyQt5.QtWidgets                                                   import * 
from parag_widgets.parag_widgets                                       import *
from parag_widgets.parag_css                                           import *
from parag_icons.parag_icons                                           import Parag_Icon

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
class Parag_UI(QMainWindow):

    def __init__(self):

        QMainWindow.__init__(self)

        self.stack_index  = 0
        self.docs         = []        

        self.get_docs()

        self.draw_gui() 

    def draw_gui(self):

        self.setWindowTitle("Licenta Parapanta")
        self.setWindowIcon(Parag_Icon("parag"))
        self.setMinimumSize(1300, 800)       
        self.setMinimumHeight(500)

        self.setStyleSheet(PARAG_CSS)

        self.wdg_central = QWidget()
        
        #selection tree
        self.tree = Parag_WDG_Tree()
        self.tree.setFixedWidth(260)
        self.populate_tree()
        self.tree.currentItemChanged.connect(self.tree_select)

        self.toolbar_layout = QHBoxLayout()

        #left tree layout area
        self.tree_area = QVBoxLayout()   
        self.tree_area.addLayout(self.toolbar_layout) 
        self.tree_area.addWidget(self.tree)   

        #context stack
        self.context = Parag_WDG_Stack()
        self.populate_stack()

        #Layout       
        self.top_layout = QHBoxLayout()
        self.top_layout.addLayout(self.tree_area)
        self.top_layout.addWidget(self.context)

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.top_layout)

        self.wdg_central.setLayout(self.main_layout)  

        self.setCentralWidget(self.wdg_central)
        self.activateWindow() 

    def showEvent(self, event):    

        pass
        
    def mousePressEvent(self,event):

        if event.button() == Qt.LeftButton:
            self.moving = True
            self.offset = event.pos()

    def mouseMoveEvent(self,event):

        if self.moving:
            self.move(event.globalPos()-self.offset) 

    def tree_select(self, current, previous):

        self.context.setCurrentIndex(0) 

        _item_cfg = str(current.data(1,Qt.UserRole))

        #set context widget based on coresponding state     
        self.context.setCurrentIndex(int(_item_cfg))  

    def populate_tree(self):

        self.tree.clear()

        self.stack_index = 0 

        _parent = self.tree.invisibleRootItem()

        for _doc in self.docs:

            _item = QTreeWidgetItem(_parent)
            _item.setData(0, Qt.EditRole, _doc.name)             

            _serial_cfg = self.stack_index                    
            _item.setData(1, Qt.UserRole, _serial_cfg)

            #_item.setIcon(0,SWTW_GetIcon(_report[_key]["icon"]))

            self.stack_index += 1

    def populate_stack(self):

        for _idx in range(len(self.docs)):

            self.context.insertWidget(_idx + 1, Parag_WDG_Desktop()) 

        self.context.setCurrentIndex(0)

    def get_docs(self):

        self.docs = []

        _doc_dir = os.path.split(os.path.abspath("__file__"))[0]
        _doc_dir = os.path.join(_doc_dir,"docs")

        for _file in os.listdir(_doc_dir):

            if os.path.splitext(_file)[1] == ".docx":

                self.docs.append(Parag_Doc(os.path.join(_doc_dir,_file)))
                self.docs[-1].read()

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
class Parag_Doc(object):


    def __init__(self,path):

        self.path = path
        self.name = self.__get_name()

    def __get_name(self):

        _name = os.path.split(self.path)[1]

        _name = os.path.splitext(_name)[0].replace("_"," ").title()

        return _name

    def read(self):

        pass

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
class Parag_Test(QWidget):

    def __init__(self):

        QWidget.__init__(self)

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
class Parag_Question(object):

    def __init__(self):

        pass

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
class Parag_Answer(object):

    def __init__(self):

        pass

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
class Parag_WDG_Desktop(QWidget):

    def __init__(self):

        QWidget.__init__(self)

        self.draw_gui()

    def draw_gui(self):

        self.bt_test  = Parag_WDG_Button("Test",   Parag_Icon("test_normal"),  Parag_Icon("test_hover"),  "#606060")
        self.bt_learn = Parag_WDG_Button("Invata", Parag_Icon("learn_normal"), Parag_Icon("learn_hover"), "#606060")

        self.bt_test.setIconSize(QSize(100,100))
        self.bt_learn.setIconSize(QSize(100,100))

        self.bt_test.clicked.connect(self.clbk_bt_test)
        self.bt_learn.clicked.connect(self.clbk_bt_learn)

        self.wdg_test = Parag_WDG_Desktop_Test(self)

        self.bt_layout = QHBoxLayout()
        self.bt_layout.addWidget(self.bt_learn)
        self.bt_layout.addWidget(self.bt_test)

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.bt_layout)
        self.main_layout.addWidget(self.wdg_test)

        self.setLayout(self.main_layout)  

        self.wdg_test.hide()

    def clbk_bt_test(self,state):

        self.wdg_test.show()

        self.bt_test.hide()
        self.bt_learn.hide()

    def clbk_bt_learn(self,state):

        self.wdg_test.show()

        self.bt_test.hide()
        self.bt_learn.hide()

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
class Parag_WDG_Desktop_Test(QWidget):

    def __init__(self,parent):

        QWidget.__init__(self)

        self.parent = parent

        self.draw_gui()

    def draw_gui(self):

        self.bt_next  = Parag_WDG_Small_Button( Parag_Icon("next_normal"),     Parag_Icon("next_hover"),     self.clbk_next)
        self.bt_prev  = Parag_WDG_Small_Button( Parag_Icon("previous_normal"), Parag_Icon("previous_hover"), self.clbk_prev)
        self.bt_close = Parag_WDG_Small_Button( Parag_Icon("close_normal"),    Parag_Icon("close_hover"),    self.clbk_close)

        self.bt_layout = QHBoxLayout()
        self.bt_layout.addWidget(self.bt_prev)
        self.bt_layout.addWidget(self.bt_close)
        self.bt_layout.addWidget(self.bt_next)

        self.wdg_test = QWidget()

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.bt_layout)
        self.main_layout.addWidget(self.wdg_test)

        self.setLayout(self.main_layout)  

        self.wdg_test.hide()

    def clbk_next(self,state):

        pass

    def clbk_prev(self,state):

        pass

    def clbk_close(self,state):

        pass

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
class Parag(object):

    def __init__(self):

        self.app = QApplication(sys.argv)  

        _ui  = Parag_UI()   

        _ui.show()

        sys.exit(self.app.exec_())

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
if __name__ == "__main__":

    Parag()

