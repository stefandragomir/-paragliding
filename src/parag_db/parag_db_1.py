from parag_model.parag_model  import *

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_category        = Parag_Model_Category()
_category.name   = "meteorologie"
PARAG_CATEGORY_1 = _category

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question()
_question.text  = "Meteorologia este:"
_category.questions.append(_question)

_answer        = Parag_Model_Answer()
_answer.text   = "stiinta care se ocupa cu studiul atmosferei si a fenomenelor din atmosfera"
_answer.corect = True
_question.answers.append(_answer)

_answer        = Parag_Model_Answer()
_answer.text   = "disciplina care se ocupa cu studiul prognozei meteorologice"
_answer.corect = False
_question.answers.append(_answer)

_answer        = Parag_Model_Answer()
_answer.text   = "stiinta care se ocupa cu predictia vremii"
_answer.corect = False
_question.answers.append(_answer)

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question()
_question.text  = "A.N.M este:"
_category.questions.append(_question)

_answer        = Parag_Model_Answer()
_answer.text   = "Inspectoratul National de Meteorologie si Hidrologie"
_answer.corect = False
_question.answers.append(_answer)

_answer        = Parag_Model_Answer()
_answer.text   = "Administratia Nationala de Meteorologie"
_answer.corect = True
_question.answers.append(_answer)

_answer        = Parag_Model_Answer()
_answer.text   = "Interpretarea Nationala de Meteorologie si Hidrologie"
_answer.corect = False
_question.answers.append(_answer)



