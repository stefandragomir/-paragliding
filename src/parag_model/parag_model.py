
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
class Parag_Model_Category(object):

    def __init__(self):

        self.name      = ""
        self.questions = []

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
class Parag_Model_Question(object):

    def __init__(self):

        self.text    = ""
        self.image   = None
        self.answers = []

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
class Parag_Model_Answer(object):

    def __init__(self):

        self.text     = ""
        self.corect   = False
        self.image    = None
        self.selected = False