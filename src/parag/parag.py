
import os
import sys
import random

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

PARAG_NUMBER_OF_TEST_QUESTIONS = 10
PARAG_MIN_CORECT_QUESTIONS     = 8


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

            _item.setIcon(0,Parag_Icon("test"))

            self.stack_index += 1

    def populate_stack(self):

        for _idx in range(len(self.docs)):

            self.context.insertWidget(_idx + 1, Parag_WDG_Desktop(self.docs[_idx])) 

        self.context.setCurrentIndex(0)

    def get_docs(self):

        self.docs = []

        _doc_dir = os.path.split(os.path.abspath("__file__"))[0]
        _doc_dir = os.path.join(_doc_dir,"docs")

        if os.path.exists(_doc_dir):

            for _file in os.listdir(_doc_dir):

                if os.path.splitext(_file)[1] == ".docx":

                    self.docs.append(Parag_Model_Doc(os.path.join(_doc_dir,_file)))
                    self.docs[-1].read()

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
class Parag_Model_Doc(object):

    def __init__(self,path):

        self.path       = path
        self.name       = self.__get_name()
        self.test_learn = Parag_Model_Test()
        self.test_exam  = Parag_Model_Test()

    def __get_name(self):

        _name = os.path.split(self.path)[1]

        _name = os.path.splitext(_name)[0].replace("_"," ").title()

        return _name

    def read(self):

        _q = Parag_Model_Question("Care este riscul asociat zborului cu acceleratorul actionat")
        _q.answers.append(Parag_Model_Answer("risc marit de inchideri ale voalurii",True))
        _q.answers.append(Parag_Model_Answer("risc marit de angajare in limita de viteza",False))
        _q.answers.append(Parag_Model_Answer("nici un risc, acest regim de zbor prezinta maximum de siguranta",False))

        self.test_learn.questions.append(_q)

        _q = Parag_Model_Question("In timpul unui viraj strans ")
        _q.answers.append(Parag_Model_Answer("viteza de angajare creste",True))
        _q.answers.append(Parag_Model_Answer("viteza de angajare scade",False))
        _q.answers.append(Parag_Model_Answer("viteza de angajare ramane neschimbata",False))

        self.test_learn.questions.append(_q)

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
class Parag_Model_Test(object):

    def __init__(self):

        self.questions = []

    def clear(self):

        for _question in self.questions:

            for _answer in _question.answers:

                _answer.is_selected = False

    def get_result(self):

        _total    = len(self.questions)
        _corect   = 0
        _incorect = 0

        for _question in self.questions:

            _is_corect = True

            for _answer in _question.answers:

                if _answer.is_corect:
                    if _answer.is_selected:
                        _is_corect = True
                    else:
                        _is_corect = False
                        break
                else:
                    if _answer.is_selected:
                        _is_corect = False
                        break
                    else:
                        _is_corect = True

            if _is_corect:
                _corect += 1
            else:
                _incorect += 1

        return _total,_corect,_incorect

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
class Parag_Model_Question(object):

    def __init__(self,text):

        self.text    = text
        self.answers = []

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
class Parag_Model_Answer(object):

    def __init__(self,text,is_corect):

        self.text        = text
        self.is_corect   = is_corect
        self.is_selected = False

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
class Parag_WDG_Desktop(QWidget):

    def __init__(self,doc):

        QWidget.__init__(self)

        self.doc = doc

        self.draw_gui()

    def draw_gui(self):

        self.bt_test  = Parag_WDG_Button("Test",   Parag_Icon("test_normal"),  Parag_Icon("test_hover"),  "#606060")
        self.bt_learn = Parag_WDG_Button("Invata", Parag_Icon("learn_normal"), Parag_Icon("learn_hover"), "#606060")

        self.bt_test.setIconSize(QSize(100,100))
        self.bt_learn.setIconSize(QSize(100,100))

        self.bt_test.clicked.connect(self.clbk_bt_test)
        self.bt_learn.clicked.connect(self.clbk_bt_learn)

        self.wdg_test = Parag_WDG_Desktop_Test(self,self.doc)

        self.bt_layout = QHBoxLayout()
        self.bt_layout.addWidget(self.bt_learn)
        self.bt_layout.addWidget(self.bt_test)

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.bt_layout)
        self.main_layout.addWidget(self.wdg_test)

        self.wdg_test.hide()

        self.setLayout(self.main_layout)  

    def clbk_bt_test(self,state):

        self.wdg_test.show()

        self.bt_test.hide()
        self.bt_learn.hide()

        self.wdg_test.start("test")

    def clbk_bt_learn(self,state):

        self.wdg_test.show()

        self.bt_test.hide()
        self.bt_learn.hide()

        self.wdg_test.start("learn")

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
class Parag_WDG_Desktop_Test(QWidget):

    def __init__(self,parent,doc):

        QWidget.__init__(self)

        self.doc             = doc
        self.question_number = 0
        self.parent          = parent
        self.test_type       = ""

        self.draw_gui()

    def draw_gui(self):

        self.bt_next   = Parag_WDG_Small_Button( Parag_Icon("next_normal"),       Parag_Icon("next_hover"),     self.clbk_next , "Intrebare urmatoare")
        self.bt_prev   = Parag_WDG_Small_Button( Parag_Icon("previous_normal"),   Parag_Icon("previous_hover"), self.clbk_prev, "Intrebarea precedenta")
        self.bt_result = Parag_WDG_Small_Button( Parag_Icon("results_normal"),    Parag_Icon("result_hover"),   self.clbk_result, "Rezultat")
        self.bt_close  = Parag_WDG_Small_Button( Parag_Icon("close_normal"),      Parag_Icon("close_hover"),    self.clbk_close, "Inchide")

        self.bt_next.setIconSize(QSize(50,50))
        self.bt_prev.setIconSize(QSize(50,50))
        self.bt_result.setIconSize(QSize(50,50))
        self.bt_close.setIconSize(QSize(50,50))

        self.lbl_status = Parag_WDG_Label()

        self.bt_layout = QHBoxLayout()
        self.bt_layout.addWidget(self.bt_prev)
        self.bt_layout.addWidget(self.bt_close)
        self.bt_layout.addWidget(self.bt_result)
        self.bt_layout.addWidget(self.bt_next)

        self.wdg_question = Parag_WDG_Question()

        self.main_layout = QVBoxLayout()
        
        self.main_layout.addLayout(self.bt_layout)
        self.main_layout.addWidget(self.wdg_question)
        self.main_layout.addWidget(self.lbl_status)

        self.setLayout(self.main_layout) 

        self.bt_next.hide()
        self.bt_prev.hide()
        self.bt_close.hide()
        self.bt_result.hide()

    def start(self,test_type):

        self.test_type = test_type

        self.question_number = 0

        if self.test_type == "learn":            
            self.doc.test_learn.clear()
            self.wdg_question.populate(self.doc.test_learn.questions[self.question_number])
            self.bt_next.show()
            self.bt_close.show()
            self.bt_result.show()
            self.bt_prev.show()
        else:            
            self.doc.test_exam.clear()
            self.bt_next.show()
            self.bt_prev.show()
            self.bt_result.show()
            self.get_test_questions()
            self.wdg_question.populate(self.doc.test_exam.questions[self.question_number])

        self.set_status()

    def get_test_questions(self):

        global PARAG_NUMBER_OF_TEST_QUESTIONS

        if PARAG_NUMBER_OF_TEST_QUESTIONS < len(self.doc.test_learn.questions):

            _questions_indexes = random.sample(range(len(self.doc.test_learn.questions)), PARAG_NUMBER_OF_TEST_QUESTIONS)

            self.doc.test_exam.questions = [self.doc.test_learn.questions[_index] for _index in _questions_indexes]
        else:
            self.doc.test_exam.questions = self.doc.test_learn.questions

    def clbk_next(self,state):

        if not self.is_end(self.question_number):

            self.question_number += 1

            if self.test_type == "learn":
                self.wdg_question.populate(self.doc.test_learn.questions[self.question_number])
            else:
                self.wdg_question.populate(self.doc.test_exam.questions[self.question_number])

            self.set_status()
        else:
            pass
            #TODO complete test

    def clbk_prev(self,state):

        if not self.is_begining(self.question_number):

            self.question_number -= 1

            if self.test_type == "learn":
                self.wdg_question.populate(self.doc.test_learn.questions[self.question_number])
            else:
                self.wdg_question.populate(self.doc.test_exam.questions[self.question_number])

            self.set_status()

        else:

            pass

    def clbk_close(self,state):

        self.parent.bt_test.show()
        self.parent.bt_learn.show()
        self.parent.wdg_test.hide()

    def clbk_result(self,state):

        _corect   = 0
        _incorect = 0
        _total    = 0

        if self.test_type == "learn":

            if self.doc.test_learn.questions[self.question_number].answers[0].is_corect:
                self.wdg_question.rd_answer_a.setStyleSheet("QCheckBox { color: green }")
            else:
                self.wdg_question.rd_answer_a.setStyleSheet("QCheckBox { color: red }")

            if self.doc.test_learn.questions[self.question_number].answers[1].is_corect:
                self.wdg_question.rd_answer_b.setStyleSheet("QCheckBox { color: green }")
            else:
                self.wdg_question.rd_answer_b.setStyleSheet("QCheckBox { color: red }")

            if self.doc.test_learn.questions[self.question_number].answers[2].is_corect:
                self.wdg_question.rd_answer_c.setStyleSheet("QCheckBox { color: green }")
            else:
                self.wdg_question.rd_answer_c.setStyleSheet("QCheckBox { color: red }")

        else:
            _total,_corect,_incorect = self.doc.test_exam.get_result()

            self.lbl_status.setText("Intrebari[%s] Corecte[%s] Incorecte[%s]" % (_total,_corect,_incorect))

            self.bt_next.hide()
            self.bt_prev.hide()
            self.bt_result.hide()
            self.bt_close.show()
            self.wdg_question.hide()

    def set_status(self):

        if self.test_type == "learn":
            self.lbl_status.setText("Intrebarea[%s/%s] " % (self.question_number + 1,len(self.doc.test_learn.questions)))
        else:
            self.lbl_status.setText("Intrebarea[%s/%s]" % (self.question_number + 1,len(self.doc.test_learn.questions)))

    def is_end(self,question_number):

        _state = False

        if self.test_type == "learn":
            _state = (question_number + 1) >= len(self.doc.test_learn.questions)
        else:
            _state = (question_number + 1) >= len(self.doc.test_exam.questions)

        return _state

    def is_begining(self,question_number):

        return question_number <= 0

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
class Parag_WDG_Question(QWidget):

    def __init__(self):

        QWidget.__init__(self)

        self.draw_gui()

        self.question = None

    def draw_gui(self):

        self.lbl_question = Parag_WDG_Label()
        self.rd_answer_a  = Parag_WDG_CheckBox("")
        self.rd_answer_b  = Parag_WDG_CheckBox("")
        self.rd_answer_c  = Parag_WDG_CheckBox("")

        self.rd_answer_a.stateChanged.connect(self.clbk_answer_a)
        self.rd_answer_b.stateChanged.connect(self.clbk_answer_b)
        self.rd_answer_c.stateChanged.connect(self.clbk_answer_c)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.lbl_question)
        self.main_layout.addWidget(self.rd_answer_a)
        self.main_layout.addWidget(self.rd_answer_b)
        self.main_layout.addWidget(self.rd_answer_c)

        self.setLayout(self.main_layout)

        self.lbl_question.hide()
        self.rd_answer_a.hide()
        self.rd_answer_b.hide()
        self.rd_answer_c.hide()

    def populate(self,question):

        self.rd_answer_a.setStyleSheet("QCheckBox { color: #b1b1b1 }")
        self.rd_answer_b.setStyleSheet("QCheckBox { color: #b1b1b1 }")
        self.rd_answer_c.setStyleSheet("QCheckBox { color: #b1b1b1 }")


        self.question = question

        self.lbl_question.show()
        self.rd_answer_a.show()
        self.rd_answer_b.show()
        self.rd_answer_c.show()

        self.lbl_question.setText(self.question.text)
        self.rd_answer_a.setText(self.question.answers[0].text)
        self.rd_answer_b.setText(self.question.answers[1].text)
        self.rd_answer_c.setText(self.question.answers[2].text)

        if self.question.answers[0].is_selected:
            self.rd_answer_a.setCheckState(Qt.Checked)
        else:
            self.rd_answer_a.setCheckState(Qt.Unchecked)

        if self.question.answers[1].is_selected:
            self.rd_answer_b.setCheckState(Qt.Checked)
        else:
            self.rd_answer_b.setCheckState(Qt.Unchecked)

        if self.question.answers[2].is_selected:
            self.rd_answer_c.setCheckState(Qt.Checked)
        else:
            self.rd_answer_c.setCheckState(Qt.Unchecked)

    def clbk_answer_a(self,state):
        
        self.question.answers[0].is_selected = state == Qt.Checked

    def clbk_answer_b(self,state):
        
        self.question.answers[1].is_selected = state == Qt.Checked

    def clbk_answer_c(self,state):
        
        self.question.answers[2].is_selected = state == Qt.Checked

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

