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
_question       = Parag_Model_Question("Meteorologia este:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "stiinta care se ocupa cu studiul atmosferei si a fenomenelor din atmosfera"))
_question.answers.append(Parag_Model_Answer(False, "disciplina care se ocupa cu studiul prognozei meteorologice"))
_question.answers.append(Parag_Model_Answer(False, "stiinta care se ocupa cu predictia vremii"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("A.N.M este:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Inspectoratul National de Meteorologie si Hidrologie"))
_question.answers.append(Parag_Model_Answer(True,  "Administratia Nationala de Meteorologie"))
_question.answers.append(Parag_Model_Answer(False, "Interpretarea Nationala de Meteorologie si Hidrologie"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce este atmosfera?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "invelisul gazos al globului pamantesc, cunoscut sub denumirea de aer"))
_question.answers.append(Parag_Model_Answer(False, "invelisul gazos al pamantului pana la o inaltime de 30.000m"))
_question.answers.append(Parag_Model_Answer(False, "invelisul gazos al pamantului pana la stratosfera"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Aerul este compus din")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "vapori de apa, particule microscopice, fum"))
_question.answers.append(Parag_Model_Answer(False, "praf, micrometeoriti, saruri, bacterii"))
_question.answers.append(Parag_Model_Answer(False, "amestec de gaze"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Dintre gazele componente ale atmosferei, procentajul cel mai mare in componenta aerului uscat il are")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "oxigenul"))
_question.answers.append(Parag_Model_Answer(False, "bioxidul de carbon"))
_question.answers.append(Parag_Model_Answer(True,  "azotul"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Zonele atmosferei sunt")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "troposfera, stratosfera, mezosfera, termosfera"))
_question.answers.append(Parag_Model_Answer(False, "troposfera, stratosfera, mezosfera"))
_question.answers.append(Parag_Model_Answer(False, "stratosfera, mezosfera, termosfera"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("In care zona a atmosferei au loc toate fenomenele obisnuite din natura: ploaie, fulgere, trasnete?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "mezosfera"))
_question.answers.append(Parag_Model_Answer(True,  "troposfera"))
_question.answers.append(Parag_Model_Answer(False, "tropopauza"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("In ce zona a atmosferei zburam cu parapanta?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "ionosfera"))
_question.answers.append(Parag_Model_Answer(False, "strat de ozon"))
_question.answers.append(Parag_Model_Answer(True,  "troposfera"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Factorii care caracterizeaza aerul atmosferic sunt")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "vantul, presiunea si temperatura"))
_question.answers.append(Parag_Model_Answer(False, "umiditatea, presiunea si vantul"))
_question.answers.append(Parag_Model_Answer(True,  "presiunea, temperatura si umiditatea"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Aerul poate fi caracterizat ca si")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "omogen"))
_question.answers.append(Parag_Model_Answer(False, "regulat"))
_question.answers.append(Parag_Model_Answer(False, "neregulat"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Presiunea atmosferica este")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "apasarea exercitata de o coloana de aer avand suprafata bazei de 1cm2 si inaltimea egala cu inaltimea atmosferei"))
_question.answers.append(Parag_Model_Answer(False, "apasarea exercitata de o coloana de aer avand suprafata bazei de 1cm2 si inaltimea egala cu inaltimea troposferei"))
_question.answers.append(Parag_Model_Answer(False, "apasarea exercitata de o coloana de aer avand suprafata bazei de 1cm2 si inaltimea egala cu inaltimea tropopauzei"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Unitatea de masura a presiunii atmosferice este")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "hectopascal"))
_question.answers.append(Parag_Model_Answer(True, "milibari"))
_question.answers.append(Parag_Model_Answer(True, "milimetrul coloana de mercur"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Masurarea presiunii atmosferice se poate realiza cu ajutorul")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "hectometrul"))
_question.answers.append(Parag_Model_Answer(False, "variometrul"))
_question.answers.append(Parag_Model_Answer(True,  "barometrul"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Presiunea atmosferica scade in altitudine datorita")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "scaderii densitatii aerului in inaltime"))
_question.answers.append(Parag_Model_Answer(True, "scurtarii coloanei de aer odata cu cresterea inaltimii"))
_question.answers.append(Parag_Model_Answer(False, "scaderii umiditatii"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Prin definitie, treapta barica reprezinta")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "distanta pe verticala, in metri, pentru care se inregistreaza o crestere a presiunii atmosferice cu 1 milibar"))
_question.answers.append(Parag_Model_Answer(True,  "distanta pe verticala, in metri, pentru care se inregistreaza o descrestere a presiunii atmosferice cu 1 milibar"))
_question.answers.append(Parag_Model_Answer(False, "distanta pe orizontala, in metri, pentru care se inregistreaza o descrestere a presiunii atmosferice cu 1 milibar"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Vantul este miscarea aerului pe")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "orizontala"))
_question.answers.append(Parag_Model_Answer(False, "verticala"))
_question.answers.append(Parag_Model_Answer(False, "diagonala"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Miscarile verticale si/sau inclinate ale aerului se numesc")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "curenti"))
_question.answers.append(Parag_Model_Answer(False, "vanturi"))
_question.answers.append(Parag_Model_Answer(False, "rafale"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("De ce este provocat vantul")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "de diferenta de presiune pe verticala"))
_question.answers.append(Parag_Model_Answer(False, "de diferenta de presiune pe diagonala"))
_question.answers.append(Parag_Model_Answer(True,  "de diferenta de presiune pe orizontala"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Incalzirea suprafetei terestre deci si a maselor de aer din vecinatatea acestora este")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "egala"))
_question.answers.append(Parag_Model_Answer(False, "omogena"))
_question.answers.append(Parag_Model_Answer(True,  "inegala"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
