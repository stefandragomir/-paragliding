
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

from docx                         import Document
from PyQt5.QtCore                 import *
from PyQt5.QtGui                  import *
from PyQt5.QtWidgets              import * 
from parag_widgets.parag_widgets  import *
from parag_widgets.parag_css      import *
from parag_icons.parag_icons      import Parag_Icon
from mammoth                      import convert_to_html
from bs4                          import BeautifulSoup
from bs4.element                  import NavigableString
from pprint                       import pprint
from datetime                     import datetime
from xhtml2pdf                    import pisa
from docx                         import Document
from docx.enum.text               import WD_BREAK
from docx.enum.style              import WD_STYLE_TYPE
from docx.oxml                    import OxmlElement
from docx.oxml.ns                 import qn

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""

PARAG_NUMBER_OF_TEST_QUESTIONS = 10
PARAG_MIN_CORECT_QUESTIONS     = 8
PARAG_TAG_QUESTION             = "[@_Q]"
PARAG_TAG_ANSWER               = "[@_A]:"           
PARAG_TAG_ANSWER_CORRECT       = "[@_AX]:"   

PARAG_FILES = {
                "cunoasterea_aeronavei.docx":  None, 
                "legislatie.docx":             None,
                "meteorologie.docx":           None,
                "navigatie.docx":              None,
                "performante_umane.docx":      None,
                "principiile_zborului.docx":   None,
                "proceduri_operationale.docx": None,
                "debug.docx":                  None,
              }

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

        self.stack_index = 1 

        _parent = self.tree.invisibleRootItem()

        for _doc in self.docs:

            _item = QTreeWidgetItem(_parent)
            _item.setData(0, Qt.EditRole, _doc.name)             

            _serial_cfg = self.stack_index                    
            _item.setData(1, Qt.UserRole, _serial_cfg)

            _item.setIcon(0,Parag_Icon("test"))

            self.stack_index += 1

    def populate_stack(self):

        self.context.insertWidget(0, QWidget())

        for _idx in range(len(self.docs)):

            self.context.insertWidget(_idx + 1, Parag_WDG_Desktop(self.docs[_idx])) 

        self.context.setCurrentIndex(0)

    def get_docs(self):

        global PARAG_FILES

        self.docs = []

        _doc_dir = os.path.split(os.path.abspath("__file__"))[0]
        _doc_dir = os.path.join(_doc_dir,"docs")

        if os.path.exists(_doc_dir):

            for _file in os.listdir(_doc_dir):

                if _file in list(PARAG_FILES.keys()):

                    self.docs.append(Parag_Model_Doc(os.path.join(_doc_dir,_file)))
                    self.docs[-1].read()

            for _doc in self.docs:

                self.docs[-1].test_learn.questions += _doc.test_learn.questions

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
class Parag_Model_Doc(object):

    def __init__(self,path):

        self.path       = path
        self.name       = self.__get_name()
        self.test_learn = Parag_Model_Test()
        self.test_exam  = Parag_Model_Test()
        self.parser     = None 

    def __get_name(self):

        _name = os.path.split(self.path)[1]

        _name = os.path.splitext(_name)[0].replace("_"," ").title()

        return _name

    def read(self):

        self.parser = Parag_Docx_Interpretor(self.path)

        _questions = self.parser.read()

        for _question in _questions:

            _q        = Parag_Model_Question(_question["text"])
            _q.number = _question["number"]
            _q.image  = _question["images"]

            for _answer in _question["answers"]:

                _q.answers.append(Parag_Model_Answer(_answer["text"],_answer["status"]))

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
        self.number  = -1
        self.image   = ""
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

        self.bt_test  = Parag_WDG_Button("Test",   Parag_Icon("test_normal"),   Parag_Icon("test_hover"),  "#606060")
        self.bt_learn = Parag_WDG_Button("Invata", Parag_Icon("learn_normal"),  Parag_Icon("learn_hover"), "#606060")
        self.bt_gen   = Parag_WDG_Button("Genereaza Test", Parag_Icon("generate_test"), Parag_Icon("generate_test"), "#606060")
        

        self.bt_test.setIconSize(QSize(100,100))
        self.bt_learn.setIconSize(QSize(100,100))
        self.bt_gen.setIconSize(QSize(100,100))

        self.bt_test.clicked.connect(self.clbk_bt_test)
        self.bt_learn.clicked.connect(self.clbk_bt_learn)
        self.bt_gen.clicked.connect(self.clbk_bt_gen)

        self.wdg_test = Parag_WDG_Desktop_Test(self,self.doc)

        self.bt_layout = QHBoxLayout()
        self.bt_layout.addWidget(self.bt_learn)
        self.bt_layout.addWidget(self.bt_test)
        self.bt_layout.addWidget(self.bt_gen)

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

    def clbk_bt_gen(self,state):

        self.doc.parser.generate()

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
        self.lbl_result = Parag_WDG_Label()

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
        self.main_layout.addWidget(self.lbl_result)

        self.setLayout(self.main_layout) 

        self.lbl_result.hide()

        self.bt_next.hide()
        self.bt_prev.hide()
        self.bt_close.hide()
        self.bt_result.hide()

    def start(self,test_type):

        self.test_type = test_type

        self.question_number = 0

        self.wdg_question.show()

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

        self.lbl_result.hide()
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

            self.lbl_result.show()

            if _corect > PARAG_MIN_CORECT_QUESTIONS:
                self.lbl_result.setText("ADMIS")
                self.lbl_result.setStyleSheet("QLabel { background-color : #14c941; font: 18pt; color: #ffffff}")
                self.lbl_result.setAlignment(Qt.AlignCenter)
            else:
                self.lbl_result.setText("PICAT")
                self.lbl_result.setStyleSheet("QLabel { background-color : #ba2012; font: 18pt;  color: #ffffff}")
                self.lbl_result.setAlignment(Qt.AlignCenter)

    def set_status(self):

        if self.test_type == "learn":
            self.lbl_status.setText("Intrebarea[%s/%s] " % (self.question_number + 1,len(self.doc.test_learn.questions)))
        else:
            self.lbl_status.setText("Intrebarea[%s/%s]" % (self.question_number + 1,len(self.doc.test_exam.questions)))

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
class Parag_Docx_Interpretor(object):

    def __init__(self,path):

        self.path_doc  = path
        self.raw_data  = ""

    def read(self):

        _questions = []

        _html = self.__get_html()

        _questions_obj = self.__get_questions(_html)    

        _count = 1

        for _question_obj in _questions_obj:

            _question = self.__interpret_question(_question_obj,_count)
            _count += 1
            _questions.append(_question)

        #pprint(_questions)

        return _questions

    def generate(self):

        global PARAG_FILES

        _questions       = []
        _nr_of_questions = 1
        _started         = False

        _document = Document(self.path_doc)

        self.__remove_empty_paragrphs_from_document(_document)

        for _paragraph in _document.paragraphs:

            if self.__is_paragraph_question(_paragraph):

                _started = True
                _questions.append(
                                    {
                                        _nr_of_questions: {
                                                            "question"        : _paragraph,
                                                            "answers"         : [],
                                                            "answers_correct" : [],
                                                            "others"          : [],
                                                          }
                                    }
                                )
                _nr_of_questions += 1
            else:

                if self.__is_paragraph_answer(_paragraph):
                    _questions[-1][_nr_of_questions - 1]["answers"].append(_paragraph)
                else:
                    if self.__is_paragraph_answer_correct(_paragraph):
                        _questions[-1][_nr_of_questions - 1]["answers_correct"].append(_paragraph)
                    else:
                        if _started:
                            _questions[-1][_nr_of_questions - 1]["others"].append(_paragraph)

        print("number of questions: %s" % (_nr_of_questions,))

        _used_questions = self.__generate_random_questions(_nr_of_questions)

        self.__delete_unused_paragraphs(_questions,_used_questions)

        self.__generate_table(_document,_questions,_used_questions)

        _document.save(self.__get_report_path())

    def __delete_unused_paragraphs(self,questions,used_questions):

        for _question in questions:

            _question_number = list(_question.keys())[0]

            if _question_number not in used_questions:  

                self.__delete_paragraph(_question[_question_number]["question"])              

                for _paragraph in _question[_question_number]["answers"]:
                    self.__delete_paragraph(_paragraph)

                for _paragraph in _question[_question_number]["answers_correct"]:
                    self.__delete_paragraph(_paragraph)

                for _paragraph in _question[_question_number]["others"]:
                    self.__delete_paragraph(_paragraph)

            else:
                _paragraph = _question[_question_number]["question"]
                _paragraph.text = _paragraph.text.replace(PARAG_TAG_QUESTION,"")

                for _paragraph in _question[_question_number]["answers"]:
                    _paragraph.text = _paragraph.text.replace(PARAG_TAG_ANSWER,"")

                for _paragraph in _question[_question_number]["answers_correct"]:
                    _paragraph.text = _paragraph.text.replace(PARAG_TAG_ANSWER_CORRECT,"")

    def __generate_random_questions(self,nr_of_questions):

        return random.sample(range(nr_of_questions), PARAG_NUMBER_OF_TEST_QUESTIONS)

    def __is_paragraph_question(self,paragraph):

        return PARAG_TAG_QUESTION in paragraph.text

    def __is_paragraph_answer(self,paragraph):

        return PARAG_TAG_ANSWER in paragraph.text

    def __is_paragraph_answer_correct(self,paragraph):

        return PARAG_TAG_ANSWER_CORRECT in paragraph.text

    def __remove_bold_from_document(self,document):

        for _paragraph in document.paragraphs:

            for _run in _paragraph.runs:

                _run.bold = False

    def __remove_empty_paragrphs_from_document(self,document):

        for _paragraph in document.paragraphs:

            if _paragraph.text.strip() == "":

                self.__delete_paragraph(_paragraph)

    def __generate_table(self,document,questions,used_questions):

        document.add_page_break()

        _table = document.add_table(rows=11, cols=4)

        _table.cell(0, 0).text = "Numar Intrebare Test"
        self.set_cell_border(
                                _table.cell(0, 0),
                                top={"sz": 5, "val": "single", "color": "#000000", "space": "0"},
                                bottom={"sz": 5, "val": "single", "color": "#000000", "space": "0"},
                                start={"sz": 5, "val": "single", "color": "#000000", "space": "0"},
                                end={"sz": 5, "val": "single", "color": "#000000", "space": "0"})

        _table.cell(0, 1).text = "Numar Intrebare Documentatie"
        self.set_cell_border(
                                _table.cell(0, 1),
                                top={"sz": 5, "val": "single", "color": "#000000", "space": "0"},
                                bottom={"sz": 5, "val": "single", "color": "#000000", "space": "0"},
                                start={"sz": 5, "val": "single", "color": "#000000", "space": "0"},
                                end={"sz": 5, "val": "single", "color": "#000000", "space": "0"})

        _table.cell(0, 2).text = "Corect"
        self.set_cell_border(
                                _table.cell(0, 2),
                                top={"sz": 5, "val": "single", "color": "#000000", "space": "0"},
                                bottom={"sz": 5, "val": "single", "color": "#000000", "space": "0"},
                                start={"sz": 5, "val": "single", "color": "#000000", "space": "0"},
                                end={"sz": 5, "val": "single", "color": "#000000", "space": "0"})

        _table.cell(0, 3).text = "Incorect"
        self.set_cell_border(
                                _table.cell(0, 3),
                                top={"sz": 5, "val": "single", "color": "#000000", "space": "0"},
                                bottom={"sz": 5, "val": "single", "color": "#000000", "space": "0"},
                                start={"sz": 5, "val": "single", "color": "#000000", "space": "0"},
                                end={"sz": 5, "val": "single", "color": "#000000", "space": "0"})

        for _index in range(1,11):

            _table.cell(_index, 0).text = str(_index)  

            self.set_cell_border(
                                    _table.cell(_index, 0),
                                    top={"sz": 5, "val": "single", "color": "#000000", "space": "0"},
                                    bottom={"sz": 5, "val": "single", "color": "#000000", "space": "0"},
                                    start={"sz": 5, "val": "single", "color": "#000000", "space": "0"},
                                    end={"sz": 5, "val": "single", "color": "#000000", "space": "0"})

        for _index in range(1,11):

            _table.cell(_index, 1).text = str(used_questions[_index - 1])  

            self.set_cell_border(
                                    _table.cell(_index, 1),
                                    top={"sz": 5, "val": "single", "color": "#000000", "space": "0"},
                                    bottom={"sz": 5, "val": "single", "color": "#000000", "space": "0"},
                                    start={"sz": 5, "val": "single", "color": "#000000", "space": "0"},
                                    end={"sz": 5, "val": "single", "color": "#000000", "space": "0"})

        for _index in range(1,11):

            self.set_cell_border(
                                    _table.cell(_index, 2),
                                    top={"sz": 5, "val": "single", "color": "#000000", "space": "0"},
                                    bottom={"sz": 5, "val": "single", "color": "#000000", "space": "0"},
                                    start={"sz": 5, "val": "single", "color": "#000000", "space": "0"},
                                    end={"sz": 5, "val": "single", "color": "#000000", "space": "0"})

        for _index in range(1,11):

            self.set_cell_border(
                                    _table.cell(_index, 3),
                                    top={"sz": 5, "val": "single", "color": "#000000", "space": "0"},
                                    bottom={"sz": 5, "val": "single", "color": "#000000", "space": "0"},
                                    start={"sz": 5, "val": "single", "color": "#000000", "space": "0"},
                                    end={"sz": 5, "val": "single", "color": "#000000", "space": "0"})

    def __chunks(self,lst, size):

        for _index in range(0, len(lst), size):

            yield lst[_index:_index + size]

    def __delete_paragraph(self,paragraph):

        p = paragraph._element

        p.getparent().remove(p)

        p._p = p._element = None

    def __get_html(self):

        self.__convert()

        _html = BeautifulSoup(self.raw_data,'html.parser')

        return _html

    def __interpret_question(self,question_obj,_count):


        _question = {"text"   : "","number" : _count,"images"  : [],"answers": [],}

        _question["images"]  = self.__interpret_questin_image(question_obj)
        _question["text"]    = str(question_obj.contents[0])

        _answers_obj = question_obj.find_all("li")

        for _answer_obj in _answers_obj:

            _answer = self.__interpret_answer(_answer_obj)

            _question["answers"].append(_answer)

        return _question

    def __interpret_questin_image(self,question_obj):

        _images = []

        _imgs = question_obj.find_all("img")

        if len(_imgs) > 0:

            for _img in _imgs:

                _images.append(_img["src"])

        return _images

    def __interpret_answer(self,answer_obj):

        _answer = {"text":"","status":False}

        _content = answer_obj.contents[0]

        if isinstance(_content,NavigableString):
            _answer["text"] = str(_content)
        else:
            if _content.name == "strong" or _content.name == "em":

                _answer["text"]   = _content.contents[0]
                _answer["status"] = True

        return _answer
            
    def __get_questions(self,html):

        _questions = []

        _html_lis = html.find_all('li')

        for _html_li in _html_lis:

            _inner_lis = _html_li.find_all("li")

            if len(_inner_lis) > 0:

                _questions.append(_html_li)

        return _questions

    def __get_report_path(self):

        _timestamp = str(datetime.now()).replace(":","_").replace(" ","_").replace("-","_").replace(".","_")

        _dir,_file = os.path.split(self.path_doc)

        _dir  = os.path.join(os.path.abspath(_dir), "parag_tests")

        if not os.path.exists(_dir):

            os.makedirs(_dir)

        _path = os.path.join(_dir,"%s_%s.docx" % (os.path.splitext(_file)[0],_timestamp))

        return _path

    def __convert(self):

        _doc   = open(self.path_doc, 'rb')
        self.raw_data  = convert_to_html(_doc)
        self.raw_data  = self.raw_data.value
        _doc.close()

    def set_cell_border(sefl, cell, **kwargs):
        """
        Set cell`s border
        Usage:

        set_cell_border(
            cell,
            top={"sz": 12, "val": "single", "color": "#FF0000", "space": "0"},
            bottom={"sz": 12, "color": "#00FF00", "val": "single"},
            start={"sz": 24, "val": "dashed", "shadow": "true"},
            end={"sz": 12, "val": "dashed"},
        )
        """
        tc = cell._tc
        tcPr = tc.get_or_add_tcPr()

        # check for tag existnace, if none found, then create one
        tcBorders = tcPr.first_child_found_in("w:tcBorders")
        if tcBorders is None:
            tcBorders = OxmlElement('w:tcBorders')
            tcPr.append(tcBorders)

        # list over all available tags
        for edge in ('start', 'top', 'end', 'bottom', 'insideH', 'insideV'):
            edge_data = kwargs.get(edge)
            if edge_data:
                tag = 'w:{}'.format(edge)

                # check for tag existnace, if none found, then create one
                element = tcBorders.find(qn(tag))
                if element is None:
                    element = OxmlElement(tag)
                    tcBorders.append(element)

                # looks like order of attributes is important
                for key in ["sz", "val", "color", "space", "shadow"]:
                    if key in edge_data:
                        element.set(qn('w:{}'.format(key)), str(edge_data[key]))

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

    #Parag()

    _parser = Parag_Docx_Interpretor(r"d:\projects\paragliding\src\docs\legislatie.docx")

    #_parser = Parag_Docx_Interpretor(r"d:\projects\paragliding\src\docs\navigatie.docx")
    
    _parser.generate()
