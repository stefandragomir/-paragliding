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
_question       = Parag_Model_Question("Marimile ce definesc vantul sunt")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "directia"))
_question.answers.append(Parag_Model_Answer(True, "intensitatea (si viteza)"))
_question.answers.append(Parag_Model_Answer(False, "densitatea"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Prin directia vantului, in meteorologie se intelege:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, 'directia inspre care "sufla" (vine) vantul'))
_question.answers.append(Parag_Model_Answer(True, 'directia de unde "sufla" (vine) vantul'))
_question.answers.append(Parag_Model_Answer(False, 'nordul magnetic'))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("1m/s este egal cu")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "2,8 km/h"))
_question.answers.append(Parag_Model_Answer(True,  "3,6 km/h"))
_question.answers.append(Parag_Model_Answer(False, "12km/h"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Liniile care unesc punctele cu aceeasi presiune atmosferica")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "izometre"))
_question.answers.append(Parag_Model_Answer(False, "izoterme"))
_question.answers.append(Parag_Model_Answer(True,  "izobare"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Distanta pe verticala masurata de la nivelul mediu al marii pana la punctul considerat unde se afla aeronava se numeste")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "altitudine"))
_question.answers.append(Parag_Model_Answer(False, "inaltimea reala"))
_question.answers.append(Parag_Model_Answer(False, "inaltime"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care din urmatoarele afirmatii sunt corecte")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "QNH = presiunea redusa la nivelul marii"))
_question.answers.append(Parag_Model_Answer(True, "QFE = presiunea la nivelul pistei"))
_question.answers.append(Parag_Model_Answer(True, "QNE (Std) = presiunea de referinta de 760 mm col Hg sau 1013.25Mb (HPa)"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Pamantul se incalzeste de la soare printr-un fenomen numit")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "conductie"))
_question.answers.append(Parag_Model_Answer(False, "convectie"))
_question.answers.append(Parag_Model_Answer(True,  "radiatie"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Izotermele reprezinta")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "liniile ce unesc toate punctele cu aceeasi temperatura"))
_question.answers.append(Parag_Model_Answer(False, "liniile ce unesc toate punctele cu aceeasi presiune"))
_question.answers.append(Parag_Model_Answer(False, "liniile ce unesc toate punctele cu aceeasi altitudine"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Masa calda de aer este obligata sa urce pe panta aerului rece, si prin detenta are loc racirea adiabatica, conditie care determina ajungerea masei de aer la saturatie, fenomen denumit")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "convectie frontala"))
_question.answers.append(Parag_Model_Answer(False, "convectie orografica"))
_question.answers.append(Parag_Model_Answer(False, "convectie orizontala"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Variatia temperaturii pentru o diferenta de nivel de 100 m se numeste")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "gradientul termic vertical"))
_question.answers.append(Parag_Model_Answer(False, "gradientul orizontal"))
_question.answers.append(Parag_Model_Answer(False, "gradientul adiabatic"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Masa calda de aer este obligata sa urce pe panta montana, si prin detenta are loc racirea adiabatica, conditie care determina ajungerea masei de aer la saturatie, fenomen denumit")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "convectie frontala"))
_question.answers.append(Parag_Model_Answer(True,  "convectie orografica"))
_question.answers.append(Parag_Model_Answer(False, "convectie orizontala"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Valoarea gradientului termic vertical mediu este")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "1C/100 m"))
_question.answers.append(Parag_Model_Answer(False, "0,5C/100 m"))
_question.answers.append(Parag_Model_Answer(True,  "0,65C/100m"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Spunem despre atmosfera ca este stabila daca")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "curentii ascendenti formati in urma unui impuls oarecare se vor opri din miscarea acensionala"))
_question.answers.append(Parag_Model_Answer(False, "curentii ascendenti tind sa-si continue miscarea impulsionati de o accelaratie noua"))
_question.answers.append(Parag_Model_Answer(False, "miscarile orizontale produse la un moment dat, nu pot sa se dezvolte si deci inceteaza"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Zona din troposfera in care temperatura creste odata cu cresterea de inaltime se numeste zona de")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "Inversiune termica"))
_question.answers.append(Parag_Model_Answer(False, "izotermie"))
_question.answers.append(Parag_Model_Answer(False, "condensare"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Spunem despre atmosfera ca este instabila daca")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "miscarile verticale produse la un moment dat, nu pot sa se dezvolte si deci inceteaza"))
_question.answers.append(Parag_Model_Answer(True,  "miscarile verticale care se produc se propaga de la un nivel la altul"))
_question.answers.append(Parag_Model_Answer(False, "curentii ascendenti formati in urma unui impuls oarecare se vor opri din miscarea acensionala"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Izotermia se defineste ca zona")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "in care temperatura este stationara cu cresterea de inaltime"))
_question.answers.append(Parag_Model_Answer(False, "in care temperatura creste odata cu cresterea de inaltime"))
_question.answers.append(Parag_Model_Answer(False, "in care temperatura scade odata cu cresterea de inaltime"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("In cazul in care avem inversiune termica la sol se poate produce")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "polei"))
_question.answers.append(Parag_Model_Answer(False, "chiciura"))
_question.answers.append(Parag_Model_Answer(True,  "ceata"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care din urmatoarele afirmatii este falsa?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "o masa de aer cald urca peste o masa de aer rece"))
_question.answers.append(Parag_Model_Answer(False, "o masa de aer rece in miscare disloca o masa de aer cald pe care o obliga sa urce"))
_question.answers.append(Parag_Model_Answer(True,  "o masa de aer cald coboara sub o masa de aer rece"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Temperatura standard in aviatie este")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "15C la 760 mm Hg"))
_question.answers.append(Parag_Model_Answer(False, "10C la 760 mm Hg"))
_question.answers.append(Parag_Model_Answer(False, "0C la 760 mm Hg"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Temperatura punctului de roua este")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "temperatura la care aerul devine saturat prin racire la o presiune constanta"))
_question.answers.append(Parag_Model_Answer(False, "temperatura la care aerul devine saturat prin racire la o presiune in crestere"))
_question.answers.append(Parag_Model_Answer(False, "temperatura la care aerul devine saturat prin incalzire la o presiune constanta"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce se intampla cu o masa de aer in urcare datorita scaderii presiunii")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "aerul se contracta"))
_question.answers.append(Parag_Model_Answer(True,  "aerul se dilata"))
_question.answers.append(Parag_Model_Answer(False, "aerul nu-si modifica volumul"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce reprezinta nivelul de condensare?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Inaltimea la care apar norii"))
_question.answers.append(Parag_Model_Answer(True,  "altitudinea la care umezeala relativa devine 100%"))
_question.answers.append(Parag_Model_Answer(False, "inaltimea la care umezeala relativa devine 100%"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("In mod obisnuit, ploaia cade din")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "Nimbostratus"))
_question.answers.append(Parag_Model_Answer(False, "Stratus"))
_question.answers.append(Parag_Model_Answer(False, "Stratocumulus"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Centru de minima presiune caracterizata prin descresterea presiunii catre centrul sistemului se numeste")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "anticiclon"))
_question.answers.append(Parag_Model_Answer(True,  "ciclon"))
_question.answers.append(Parag_Model_Answer(False, "anticiclon, ciclon"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Vantul are o miscare de la exterior spre centru sau in sens invers acelor de ceasornic (pentru emisfera nordica).")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "in cazul ciclonului"))
_question.answers.append(Parag_Model_Answer(False, "in cazul izotermei"))
_question.answers.append(Parag_Model_Answer(False, "in cazul anticiclonului"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Centru de maxima presiune caracterizata prin cresterea presiunii de la exterior spre centrul sistemului se numeste")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "anticiclon"))
_question.answers.append(Parag_Model_Answer(False, "ciclon"))
_question.answers.append(Parag_Model_Answer(False, "anticiclon, ciclon"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Vantul are o miscare de la centru spre exterior sau in sensul acelor de ceasornic (pentru emisfera nordica).")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "in cazul ciclonului"))
_question.answers.append(Parag_Model_Answer(False, "in cazul izotermei"))
_question.answers.append(Parag_Model_Answer(True,  "in cazul anticiclonului"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Forta care produce miscarea orizontala, in cazul aerului este")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "umiditatea"))
_question.answers.append(Parag_Model_Answer(True,  "diferenta de presiune"))
_question.answers.append(Parag_Model_Answer(False, "temperatura"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Norii convectivi formati prin convectie termica sau dinamica sunt")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "Cu, Cb"))
_question.answers.append(Parag_Model_Answer(False, "Ci, As, St"))
_question.answers.append(Parag_Model_Answer(False, "As, Ns"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Norii se clasifica dupa inaltimea bazei fata de sol in cate categorii")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "3"))
_question.answers.append(Parag_Model_Answer(False, "4"))
_question.answers.append(Parag_Model_Answer(False, "5"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Norii cumulus sunt nori de")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "inalta inaltime"))
_question.answers.append(Parag_Model_Answer(True,  "joasa inaltime"))
_question.answers.append(Parag_Model_Answer(False, "medie inaltime"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("In care nori intalnim descarcari electrice")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Cumulus humilis"))
_question.answers.append(Parag_Model_Answer(True,  "Cumulonimbus"))
_question.answers.append(Parag_Model_Answer(False, "Altocumulus"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Frontul in lungul caruia aerul rece in deplasare inlocuieste aerul cald este")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "frontul rece"))
_question.answers.append(Parag_Model_Answer(False, "frontul cald"))
_question.answers.append(Parag_Model_Answer(False, "frontul oclus"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Frontul cald se dezvolta atunci cand")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "masa de aer cald impinge si inlocuieste o masa de aer rece"))
_question.answers.append(Parag_Model_Answer(False, "masa de aer rece impinge si inlocuieste o masa de aer cald"))
_question.answers.append(Parag_Model_Answer(False, "masa de aer rece impinge si inlocuieste o masa de aer mai rece"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce este gradientul termic vertical ?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "gradientul termic vertical reprezinta variatia temperaturii pentru o diferenta de nivel de  100 m"))
_question.answers.append(Parag_Model_Answer(False, "miscarea orizontala a aerului"))
_question.answers.append(Parag_Model_Answer(False, "diferenta de viteza a vantului pe diferite altitudini din 100 in 100 de metri"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Atunci cand aerul rece si cel cald din doua mase de aer invecinate se deplaseaza paralel, in acelasi sens sau chiar in sens invers, dar niciuna dintre ele nu o poate inlocui pe cealalta, avem parte de un")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "front oclus"))
_question.answers.append(Parag_Model_Answer(True,  "front stationar"))
_question.answers.append(Parag_Model_Answer(False, "front rece"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cand se poate afirma ca este vant laminar ?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "cand nu sunt rafale"))
_question.answers.append(Parag_Model_Answer(False, "iarna"))
_question.answers.append(Parag_Model_Answer(True,  "in situatia cand vantul are o miscare uniforma, atat in ce priveste viteza cat si directia,scurgerea aerului facandu-se in straturi paralele "))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Din ce sunt constituiti norii ?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "din aer cald"))
_question.answers.append(Parag_Model_Answer(True,  "din picaturi fine de apa sau cristale de gheata in suspensie in atmosfera"))
_question.answers.append(Parag_Model_Answer(False, "din bule termice"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Este indicat sa zburam in apropierea unui Cumulonimbus (CB) ?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "da"))
_question.answers.append(Parag_Model_Answer(True,  "nu"))
_question.answers.append(Parag_Model_Answer(False, "depinde de directia vantului"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cirrus, cirrocumulus si cirrostratus sunt nori periculosi pentru parapantism ?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "da"))
_question.answers.append(Parag_Model_Answer(True,  "nu"))
_question.answers.append(Parag_Model_Answer(False, "uneori"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Aerul este un amestec de diferite gaze. Cele mai importante gaze și proporțiile lor sunt")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "aproximativ 78% oxigen și 21% azot"))
_question.answers.append(Parag_Model_Answer(True,  "aproximativ 78% azot și 21% oxigen"))
_question.answers.append(Parag_Model_Answer(False, "aproximativ 78% dioxid de carbon și 21% oxigen"))
_question.answers.append(Parag_Model_Answer(False, "aproximativ 78% oxigen și 21% dioxid de carbon"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cum variază temperatura aerului în troposferă cu creșterea altitudinii?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Scade liniar cu 0,65C/100m până la tropopauză."))
_question.answers.append(Parag_Model_Answer(False, "Scade liniar cu 1C/100m până la tropopauză"))
_question.answers.append(Parag_Model_Answer(False, "Scade, nu liniar, dar depinzând de straturile de aer variază între 0,1C și 1,2C"))
_question.answers.append(Parag_Model_Answer(True,  "Depinzând de stratul de aer poate scădea, rămâne la fel sau crește, dar în medie scade cu 0,65C/100m"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Pentru a se asigura că toți utilizatorii spațiului aerian au altimetrele reglate la fel, atmosfera a fost standardizată. Care sunt valorile pentru atmosfera standard în regiunea troposferei? Presiunea la nivelul mării și temperatura/gradientul termic")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "1033,6  hPa  15°C  1C/100m"))
_question.answers.append(Parag_Model_Answer(False, "1013,2  hPa  15°C  0.65C/100m"))
_question.answers.append(Parag_Model_Answer(False, "033,6  hPa  15°C  0,5C/100m"))
_question.answers.append(Parag_Model_Answer(True,  "1013,2  hPa  15°C  1C/100m"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Altitudinea medie a tropopauzei la latitudinea noastră este")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "4.000 m deasupra nivelului mării."))
_question.answers.append(Parag_Model_Answer(False, "5.500 m deasupra nivelului mării."))
_question.answers.append(Parag_Model_Answer(True,  "11.000 m deasupra nivelului mării"))
_question.answers.append(Parag_Model_Answer(False, "50.000 m deasupra nivelului mării"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Presiune aerului rezultă din")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "rotația pământului"))
_question.answers.append(Parag_Model_Answer(False, "polii magnetici"))
_question.answers.append(Parag_Model_Answer(False, "particulele de apă și de praf ce plutesc în aer"))
_question.answers.append(Parag_Model_Answer(False, "gravitație"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cum variază presiunea aerului o dată cu creșterea altitudinii?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Se reduce la jumătate până la tropopauză și după aceea rămâne constant"))
_question.answers.append(Parag_Model_Answer(False, "Se reduce cu aproximativ 80hPa / 100m de altitudine"))
_question.answers.append(Parag_Model_Answer(True,  "Se reduce cu jumătate la aproximativ fiecare 5.500 m de altitudine"))
_question.answers.append(Parag_Model_Answer(False, "Se reduce cu jumătate la aproximativ fiecare 11.000 m de altitudine"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care este presiunea medie de la nivelul măriii (atmosfera standard) folosită de meteorologiști?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "1013,2  hPa "))
_question.answers.append(Parag_Model_Answer(False, "1033,6  hPa  "))
_question.answers.append(Parag_Model_Answer(False, "760,0  hPa  "))
_question.answers.append(Parag_Model_Answer(False, "998,7  hPa  "))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Presiunea la nivelul mării")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "este întotdeauna constantă"))
_question.answers.append(Parag_Model_Answer(False, "poate în cazuri mai rare să crească față de medie"))
_question.answers.append(Parag_Model_Answer(False, "poate în cazuri mai rare să scadă față de medie"))
_question.answers.append(Parag_Model_Answer(True,  "poate fi mai mare sau mai mică față de valoarea medie depinzând de situația vremii."))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Presiunea intr-un punct dat la nivelul mării depinde de")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "maree"))
_question.answers.append(Parag_Model_Answer(True,  "circulația globală a aerului"))
_question.answers.append(Parag_Model_Answer(False, "caracteristicile suprafeței"))
_question.answers.append(Parag_Model_Answer(False, "longitudine"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Un copil elibereaza un balon cu volum aproximativ de 5 dm3 la nivelul mării. Care este volumul aproximativ al balonului când ajunge la altitudinea de 5.500 m deasupra nivelului mării")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "2,5 dm3"))
_question.answers.append(Parag_Model_Answer(False, "5 dm3"))
_question.answers.append(Parag_Model_Answer(True,  "10 dm3"))
_question.answers.append(Parag_Model_Answer(False, "20 dm3"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Barometrul arată o presiune de 980 hPa la nivelul mării. Care este cea mai probabilă presiune la o altitudine de 5.500 mdeasupra nivelului mări?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "1035 hPa"))
_question.answers.append(Parag_Model_Answer(False, "980 hPa"))
_question.answers.append(Parag_Model_Answer(False, "650 hPa"))
_question.answers.append(Parag_Model_Answer(True,  "490 hPa"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care este partea atmosferei unde condițiile meteorologice ne determină vremea?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Ionosfera"))
_question.answers.append(Parag_Model_Answer(False, "Mezosfera"))
_question.answers.append(Parag_Model_Answer(False, "Stratosfera"))
_question.answers.append(Parag_Model_Answer(True,  "Troposfera"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Temperatura stratului de aer de lângă sol este influențată cel mai mult de")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "temperatura solului."))
_question.answers.append(Parag_Model_Answer(False, "acțiunea radiației solare supra particulelor de aer"))
_question.answers.append(Parag_Model_Answer(False, "umiditatea relativă a aerului."))
_question.answers.append(Parag_Model_Answer(False, "unghiul de incidență a razelor solare asupra particulelor de aer."))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Pentru aceeași intensitate și unghi de incidență a razelor solare, care din următoarele tipuri de sol încălzește cel mai mult stratul de aer adiacent?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Solul pietros."))
_question.answers.append(Parag_Model_Answer(False, "Pădure tânără."))
_question.answers.append(Parag_Model_Answer(False, "O mlaștină."))
_question.answers.append(Parag_Model_Answer(True,  "Pășune uscată"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("La aceeași altitudine deasupra nivelului mării")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "aerul cald e mai dens decât aerul rece."))
_question.answers.append(Parag_Model_Answer(False, "aerul cald are aceeași densitate ca aerul rece"))
_question.answers.append(Parag_Model_Answer(True,  "aerul cald e mai puțin dens ca aerul rece."))
_question.answers.append(Parag_Model_Answer(False, "densitatea aerului depinde de gradientul adiabatic"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cum variază temperatura unei bule de aer pe măsură ce se ridică de la sol fără a creea un nor?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Temperatura crește cu aproximativ 0.5°C /100m pentru că radiația solară devine tot mai intensă"))
_question.answers.append(Parag_Model_Answer(False, "Nu se poate determina, pentru că temperatura se egalizează cu cea a aerului din jur"))
_question.answers.append(Parag_Model_Answer(False, "Temperatura se reduce cu aproximativ 0.65°C /100m, cum de fapt e cazul în toată troposfera"))
_question.answers.append(Parag_Model_Answer(True,  "Temperatura se reduce cu aproximativ  1°C /100m pentru că presiunea se reduce o dată cu creșterea altitudinii."))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cum variază temperatura unei bule de aer care urcă?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "Pentru că presiunea scade o dată cu creșterea altitudinii rezultă extinderea bulei și pierdere de energie sub formă de căldură"))
_question.answers.append(Parag_Model_Answer(False, "Bula se va răci pentru că s-a îndepărtat de sursa de căldură, adică suprafata solului."))
_question.answers.append(Parag_Model_Answer(False, "Pentru că unghiul radiației solare se reduce o dată cu creșterea altitudinii, deci bula de aer primește mai puțină căldură de cât la nivelul solului"))
_question.answers.append(Parag_Model_Answer(False, "Din cauză că bula de aer trebuie să evapore apă pe măsură ce urcă, există o relație între creșterea altitudinii și reducerea temperaturii."))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cum variază volumul și temperatura unei mase de aer care coboară?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Volumul crește, temperatura scade"))
_question.answers.append(Parag_Model_Answer(False, "Volumul crește, temperatura crește."))
_question.answers.append(Parag_Model_Answer(True,  "Volumul scade, temperatura crește"))
_question.answers.append(Parag_Model_Answer(False, "Volumul scade, temperatura scade"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care este principalul mod de încălzire în timpul zilei a unei mase de aer la 100m deasupra solului?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "Aerul adiacent solului se încălzește și urcă în timp ce aerul de la altitudine coboară la sol unde este încălzit."))
_question.answers.append(Parag_Model_Answer(False, "Radiația UV solară este absorbită de sol iar spectrul infraroșu este reflectat de sol, încălzind aerul mai mult sau mai puțin, proporțional cu distanța de la suprafața solului."))
_question.answers.append(Parag_Model_Answer(False, "Radiația solară încarcă particulele de aer cu energie (ionizare), care este ulterior eliberată bub formă de căldură"))
_question.answers.append(Parag_Model_Answer(False, "Stratul de aer adiacent solului se încălzește și, fiind un bun conductor termic, transferă căldura straturilor superioare de aer"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("În medie temperatura din troposferă se reduce o dată cu creșterea altitudinii. Totuși, se poate întâmpla ca în anumite zone temperatura să crească. Cum se numește acest fenomen?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Superadiabatic"))
_question.answers.append(Parag_Model_Answer(False, "Izoterm"))
_question.answers.append(Parag_Model_Answer(False, "Restitutie"))
_question.answers.append(Parag_Model_Answer(True,  "Inversiune"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("În medie temperatura din troposferă se reduce o dată cu creșterea altitudinii. Totuși, se poate întâmpla ca în anumite zone temperatura să rămănă constantă. Cum se numește acest fenomen?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Superadiabatic"))
_question.answers.append(Parag_Model_Answer(True,  "Izotermă"))
_question.answers.append(Parag_Model_Answer(False, "Restituție"))
_question.answers.append(Parag_Model_Answer(False, "Inversiune"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("O bulă de aer se încălzește, se desprinde de sol și începe să se ridice. Cât de sus se poate ridica bula?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Până se reduce transferul de căldură de la sol"))
_question.answers.append(Parag_Model_Answer(False, "Până când presiunea bulei este mai mică de cât cea a aerului din jur"))
_question.answers.append(Parag_Model_Answer(True,  "Până când diferența dintre temperatura ei si a aerului din jur se reduce la  0."))
_question.answers.append(Parag_Model_Answer(False, "Până când diferența dintre temperatura ei și punctul de rouă se reduce la 0"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("O inversiune este un strat de aer în care temperatura")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "scade o dată cu creșterea altitudinii"))
_question.answers.append(Parag_Model_Answer(True,  "crește o dată cu creșterea altitudinii."))
_question.answers.append(Parag_Model_Answer(False, "este deasupra nivelului de îngheț"))
_question.answers.append(Parag_Model_Answer(False, "este constantă"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("O izotermă este un strat de aer în care temperatura")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "scade o dată cu creșterea altitudinii"))
_question.answers.append(Parag_Model_Answer(False, "crește o dată cu creșterea altitudinii"))
_question.answers.append(Parag_Model_Answer(False, "este deasupra nivelului de îngheț"))
_question.answers.append(Parag_Model_Answer(True,  "este constantă"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Inversiunile și izotermele sunt")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "puncte de origine și declanșare ale aerului termic care urcă"))
_question.answers.append(Parag_Model_Answer(False, "elemente instabile stratificate ale troposferei"))
_question.answers.append(Parag_Model_Answer(False, "stabile sau instabile depinzând de temperatură"))
_question.answers.append(Parag_Model_Answer(True,  "bariere pentru masele de aer termic care urcă"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Gradientul de temperatură este definit ca fiind ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "diferența de altitudine per °C într-o masă de aer."))
_question.answers.append(Parag_Model_Answer(False, "diferența de presiune per km între două puncte geografice diferite"))
_question.answers.append(Parag_Model_Answer(False, "unitatea de măsură a temperaturii"))
_question.answers.append(Parag_Model_Answer(True,  "diferența de temperatură pentru o creștere de 100 m a altitudinii"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Gradientul temperaturii unui strat izotermic este")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "0C / 100m"))
_question.answers.append(Parag_Model_Answer(False, "0.5C / 100m"))
_question.answers.append(Parag_Model_Answer(False, "0.65C / 100m"))
_question.answers.append(Parag_Model_Answer(False, "1C / 100m "))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Unde găsim de obicei o inversiune?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "La baza norilor cumulus"))
_question.answers.append(Parag_Model_Answer(True,  "La granița dintre un strat de aer cețos de la sol și un strat de aer clar de la altitudine"))
_question.answers.append(Parag_Model_Answer(False, "Unde este o diferență temperatură-punct de rouă de 0"))
_question.answers.append(Parag_Model_Answer(False, "Deasupra unei convergențe"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care din următoarele semne indică prezența unei inversiuni?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Un nor cumulus"))
_question.answers.append(Parag_Model_Answer(False, "Un nor lenticular"))
_question.answers.append(Parag_Model_Answer(True,  "Un strat de ceață"))
_question.answers.append(Parag_Model_Answer(False, "Un nor cirus"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care din următoarele sondaje de temperatură măsurate la ora 02:00 indică prezența unei inversiuni la altitudine")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "1"))
_question.answers.append(Parag_Model_Answer(False, "2"))
_question.answers.append(Parag_Model_Answer(False, "3"))
_question.answers.append(Parag_Model_Answer(False, "4"))
_question.image = "iVBORw0KGgoAAAANSUhEUgAAAUMAAABbCAIAAABmo3ASAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAE++SURBVHhe7d1nsF3VeTdwTz5lEqc7mYydfEg8ZhLbMxibamOaRJcQEpIoKkgCJBDI9CpCk0QzECCiSEQ4KIjeDaEYjGiiFyFRDKJIVGNMM2Cw88L7O/t/tNicc+69Eva9tm/0n9Getdd+1lpPX886Z9+jz/3v//7vRx999PEqrMIq/EHh/1Vo3nz88eeE8Ycffvjyyy8///zzL7zwwrJ+jeeee+6VV1556aWXCNvs6r9YunTpq6++Gss2u/ovyEhSxv0/YlmS/vrXv/5UJPt33XXXbb755rvvvvvkyZP36NfYc889t9hii8GDB2s0u/opmHKvvfYaOHDgiBEj+r2wQNhBgwZttdVWGs2u/gvGFbA33nij4C0FdSOSzz333OOOO06I25z7DFm+ND744IP09yrIeMIJJ5xzzjl9IOyvfvWrNCIgpJ0iqA/kJeOhhx565ZVX9o1lSeSkFkk19BRh+wBkPOOMM0466aS+ETYgcuTVdo3UfQAyzpgx47//+78t2hrJp556au77DK+99toTTzyh8fTTTyt609kHOO200+bOndu86U0Utybg//zP/6j6tB977LGf/vSnGsUAvYojjjgimbu3UcS544475s+fn/aiRYveeeedtPsA3FgwN296GUVeBmVfjYcffrgEdh9AzkokFzQi+Qc/+MG///u/5773QHhlfVQgdP/1X/912LBh2rNnz95www1/+ctfepSnvQqS/td//VfzpjcRu86ZM+cf//EfCfvlL3954cKF06dPV+6GoA+E/bd/+zdJpHnTmyCLvUIZ//nPf/5LX/rSpEmT3O62227qQE+VJyHrVfznf/7nf/zHfzRvehPcOGnaefVv//ZvR48era22P/HEE/MUGnS9ie9///u/s0iGSHjTTTd98Ytf/NznPjdy5Ei3L7/88he+8IVLL720Iul19E0kV0npI1WQY/nUqVO59T/8wz9MnDjRzvynf/qnCxYsQNMH9u6bSI6wb7/9thLg9ttv52R/9Ed/9Morr1x//fV/8zd/s2TJEk+bpL2JvolkspRqSwxz47Fjx2qffvrp//zP//zGG29o9/9IjkUVt47lm2222eDBg9O/zTbbSGlp9zb6JpLZUhgzeXZmAfznf/7ntK+97rrrTpkyRaMP/LtvIjlixn3vu+++P/uzP/ve976nrbT+yle+csopp1RUvY4+i+QYTi05ZMiQ9dZbLxsSE//FX/zF5Zdfrt3/I7mOTTfddKuttkp7jz32+Kd/+qe+qcH6JpIhwazx7LPPKrCdIN566y23W2655cCBAyuSXkefRTLEv3/2s585rArgW265xa1jhRq7oup19E0kJ0oXLVq0wQYbKDdsSDkuvfvuu3/yJ38ybdo07aiiV/F7FMkDBgwokczYjpF9kMmgbyKZLTm3hrMDby6Sgnp7k002ad70MvomkhmOsKrr00477aWXXtLjBHHIIYdo/Mu//Es/i+REKek+//nPM6XrX/3VXzlT0IBInj59uqf/t/bkb3/72xtvvHHaO+64I+fug0wGfRPJbBlzqjMdpUSUc9Sdd96pRy6fMGFCRdXr6JtIDmxKDg7f+ta3DjzwwD/+4z++6667lCSrrbZanLsPjNtnezI8+eSTF1988bx58/7+7//+a1/72tKlS19//fW//Mu/PP/885t0vYwuI7nPDjMFxx9//EknnaTxxhtvfPGLX5w1a1b6ext9tie7cmXJe9SoUTvssMPWW2/NzK+++qosfsMNN4SstyGSr7vuuuZNr4GwkXfZsmUyl9Pjtdde6/a2227767/+64ULF4amQdqb6ONzcnDssceeffbZGuedd96XvvQlJVj6exudI/ncc8/t+z25QGKTyPvsuzgVYJ8lznbko77mTe/DfnjTTTc1b/ockyZNksWaN72Pvvw+uR3yl7zZvOl92HpbXotoRLKuww477Lnnnnvqqaee7is8U2HJkiUiGZ599lmdbvO0l0DGqVOnnnDCCRrNrl5GkSgCzpkz55prriE4Vfe2tq04ZcoU/q3RZ5aNXIrPn/zkJ2eeeeaPfvSjCOu2SdE7IKPtUSz1mWWDyLV48WKhdffdd0d8yNPegMmff/55td4FF1wgeEuB0IjkSy65ZL311uv7t3MnT55s0X333Xf//ffX3m233ZoPeg2W+853vuNMrmHFZm8vIwtFvfvttx9h++YVdyuuueaagwYN6stXke3DpAONAw44QLGdzjztPRB24403Xn/99aPnvkFdLmaVN5s3vQwyCtirrroqMRw0q+u+f1uzHfXjR+9Bde1I07zp7zjyyCOvv/765k1/xw9+8IPfYXUd8OF80tnbOPnkk1sOic1PvDqekxtH+yq6lBBXXHHFlVdeeeutt+aRxg9/+MNf/OIXuX3ooYcQ/PznP9eOJK4Z/uvqb6/ymgSksxr0CQpx874NefTiiy++9tpr2q+88gpmrr766htvvDE8hEAbV2gaYz7++J577sHV7bffntvQkLQ9kjFWDECWyy67zPyGu8W5YFAlaoRgwYIF1157bd4oDue5RrpKykYjE2qXmQOPQuba7Po0Qq+CevPNN0OzaNEiddPrr7+uHX1qEJMG3n33XW1kxLz88svvuusut+lxVW12H8lqUandPAQ0xGxEu+222zyyirUcs+GDDz7wVI9rGNAoPYWYUNWsnyBPe4SKsegTOBLxy8yuv/zlL1lWZ4P6448feeQRwv74xz+OUbKuk8vMmTOr559Cg9Fqqscff5xl4xLpvOWWW+jH5J5iwBLmrAY1RrWIE94Cj7J0Afq8EOFpetqBxtWBK7p66aWXaJ6n0fD777+fGQznxvp/9rOfZdSdd95J2DvuuCO3mX8l3rs2bxa2xvDhww888EDHy3zCPG3aNPv74Ycfroj68MMPDd95552POOKI0aNHxwARtZqmFXlUlxZ9eiJGs7cNb7zxxoYbbkjX2vvss8+YMWPsruQhcMVpY1GHh2233VYxySqceLvttrMpqd7xWcK7/bPrjA3DcsRmm2121FFHTZ8+XfDwYFWTaRWKgPK4445T3hDWWYDD6enowYF+QqFp3i/3hqwIzd42OFtusMEG999/v7bTprVIwQrLli3LbEJOfT506FBivv3224rY7bffPnZhKa4QMk/bv4XK6ho4ZzLq+v73v3/WWWfJFBTFrCaZMWMGAoI7Dhx88MF777133J1EdXEKdJrNtPWn2rFsrs3eNhBzo402Wrp0afP+44+33nprGtYoo5yBWXbChAksazsiOD5ZZNdddy066eqz61iHlow69NBDubEi1MyWIN1hhx3GnWwSdDh16lTaYH0TApqObytFIsi6gbYej7rxB+DA3BiNNm3vsssuDthA+VnRI7bGKq7wjD12P/roo5mAXeJyxq7E98mZVyMfnNigHn30UbcyiuVjV7qYN28eFeTDd6GVpIgbwx9++GG5RCxdc801N9xww0EHHWS787RdBa733nsv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"

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care din următoarele sondaje de temperatură măsurate la ora 02:00 indică prezența unei inversiuni la nivelul solului")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "1"))
_question.answers.append(Parag_Model_Answer(False, "2"))
_question.answers.append(Parag_Model_Answer(False, "3"))
_question.answers.append(Parag_Model_Answer(False, "4"))
_question.image = "iVBORw0KGgoAAAANSUhEUgAAAUMAAABbCAIAAABmo3ASAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAE++SURBVHhe7d1nsF3VeTdwTz5lEqc7mYydfEg8ZhLbMxibamOaRJcQEpIoKkgCJBDI9CpCk0QzECCiSEQ4KIjeDaEYjGiiFyFRDKJIVGNMM2Cw88L7O/t/tNicc+69Eva9tm/0n9Getdd+1lpPX886Z9+jz/3v//7vRx999PEqrMIq/EHh/1Vo3nz88eeE8Ycffvjyyy8///zzL7zwwrJ+jeeee+6VV1556aWXCNvs6r9YunTpq6++Gss2u/ovyEhSxv0/YlmS/vrXv/5UJPt33XXXbb755rvvvvvkyZP36NfYc889t9hii8GDB2s0u/opmHKvvfYaOHDgiBEj+r2wQNhBgwZttdVWGs2u/gvGFbA33nij4C0FdSOSzz333OOOO06I25z7DFm+ND744IP09yrIeMIJJ5xzzjl9IOyvfvWrNCIgpJ0iqA/kJeOhhx565ZVX9o1lSeSkFkk19BRh+wBkPOOMM0466aS+ETYgcuTVdo3UfQAyzpgx47//+78t2hrJp556au77DK+99toTTzyh8fTTTyt609kHOO200+bOndu86U0Utybg//zP/6j6tB977LGf/vSnGsUAvYojjjgimbu3UcS544475s+fn/aiRYveeeedtPsA3FgwN296GUVeBmVfjYcffrgEdh9AzkokFzQi+Qc/+MG///u/5773QHhlfVQgdP/1X/912LBh2rNnz95www1/+ctfepSnvQqS/td//VfzpjcRu86ZM+cf//EfCfvlL3954cKF06dPV+6GoA+E/bd/+zdJpHnTmyCLvUIZ//nPf/5LX/rSpEmT3O62227qQE+VJyHrVfznf/7nf/zHfzRvehPcOGnaefVv//ZvR48era22P/HEE/MUGnS9ie9///u/s0iGSHjTTTd98Ytf/NznPjdy5Ei3L7/88he+8IVLL720Iul19E0kV0npI1WQY/nUqVO59T/8wz9MnDjRzvynf/qnCxYsQNMH9u6bSI6wb7/9thLg9ttv52R/9Ed/9Morr1x//fV/8zd/s2TJEk+bpL2JvolkspRqSwxz47Fjx2qffvrp//zP//zGG29o9/9IjkUVt47lm2222eDBg9O/zTbbSGlp9zb6JpLZUhgzeXZmAfznf/7ntK+97rrrTpkyRaMP/LtvIjlixn3vu+++P/uzP/ve976nrbT+yle+csopp1RUvY4+i+QYTi05ZMiQ9dZbLxsSE//FX/zF5Zdfrt3/I7mOTTfddKuttkp7jz32+Kd/+qe+qcH6JpIhwazx7LPPKrCdIN566y23W2655cCBAyuSXkefRTLEv3/2s585rArgW265xa1jhRq7oup19E0kJ0oXLVq0wQYbKDdsSDkuvfvuu3/yJ38ybdo07aiiV/F7FMkDBgwokczYjpF9kMmgbyKZLTm3hrMDby6Sgnp7k002ad70MvomkhmOsKrr00477aWXXtLjBHHIIYdo/Mu//Es/i+REKek+//nPM6XrX/3VXzlT0IBInj59uqf/t/bkb3/72xtvvHHaO+64I+fug0wGfRPJbBlzqjMdpUSUc9Sdd96pRy6fMGFCRdXr6JtIDmxKDg7f+ta3DjzwwD/+4z++6667lCSrrbZanLsPjNtnezI8+eSTF1988bx58/7+7//+a1/72tKlS19//fW//Mu/PP/885t0vYwuI7nPDjMFxx9//EknnaTxxhtvfPGLX5w1a1b6ext9tie7cmXJe9SoUTvssMPWW2/NzK+++qosfsMNN4SstyGSr7vuuuZNr4GwkXfZsmUyl9Pjtdde6/a2227767/+64ULF4amQdqb6ONzcnDssceeffbZGuedd96XvvQlJVj6exudI/ncc8/t+z25QGKTyPvsuzgVYJ8lznbko77mTe/DfnjTTTc1b/ockyZNksWaN72Pvvw+uR3yl7zZvOl92HpbXotoRLKuww477Lnnnnvqqaee7is8U2HJkiUiGZ599lmdbvO0l0DGqVOnnnDCCRrNrl5GkSgCzpkz55prriE4Vfe2tq04ZcoU/q3RZ5aNXIrPn/zkJ2eeeeaPfvSjCOu2SdE7IKPtUSz1mWWDyLV48WKhdffdd0d8yNPegMmff/55td4FF1wgeEuB0IjkSy65ZL311uv7t3MnT55s0X333Xf//ffX3m233ZoPeg2W+853vuNMrmHFZm8vIwtFvfvttx9h++YVdyuuueaagwYN6stXke3DpAONAw44QLGdzjztPRB24403Xn/99aPnvkFdLmaVN5s3vQwyCtirrroqMRw0q+u+f1uzHfXjR+9Bde1I07zp7zjyyCOvv/765k1/xw9+8IPfYXUd8OF80tnbOPnkk1sOic1PvDqekxtH+yq6lBBXXHHFlVdeeeutt+aRxg9/+MNf/OIXuX3ooYcQ/PznP9eOJK4Z/uvqb6/ymgSksxr0CQpx874NefTiiy++9tpr2q+88gpmrr766htvvDE8hEAbV2gaYz7++J577sHV7bffntvQkLQ9kjFWDECWyy67zPyGu8W5YFAlaoRgwYIF1157bd4oDue5RrpKykYjE2qXmQOPQuba7Po0Qq+CevPNN0OzaNEiddPrr7+uHX1qEJMG3n33XW1kxLz88svvuusut+lxVW12H8lqUandPAQ0xGxEu+222zyyirUcs+GDDz7wVI9rGNAoPYWYUNWsnyBPe4SKsegTOBLxy8yuv/zlL1lWZ4P6448feeQRwv74xz+OUbKuk8vMmTOr559Cg9Fqqscff5xl4xLpvOWWW+jH5J5iwBLmrAY1RrWIE94Cj7J0Afq8EOFpetqBxtWBK7p66aWXaJ6n0fD777+fGQznxvp/9rOfZdSdd95J2DvuuCO3mX8l3rs2bxa2xvDhww888EDHy3zCPG3aNPv74Ycfroj68MMPDd95552POOKI0aNHxwARtZqmFXlUlxZ9eiJGs7cNb7zxxoYbbkjX2vvss8+YMWPsruQhcMVpY1GHh2233VYxySqceLvttrMpqd7xWcK7/bPrjA3DcsRmm2121FFHTZ8+XfDwYFWTaRWKgPK4445T3hDWWYDD6enowYF+QqFp3i/3hqwIzd42OFtusMEG999/v7bTprVIwQrLli3LbEJOfT506FBivv3224rY7bffPnZhKa4QMk/bv4XK6ho4ZzLq+v73v3/WWWfJFBTFrCaZMWMGAoI7Dhx88MF777133J1EdXEKdJrNtPWn2rFsrs3eNhBzo402Wrp0afP+44+33nprGtYoo5yBWXbChAksazsiOD5ZZNdddy066eqz61iHlow69NBDubEi1MyWIN1hhx3GnWwSdDh16lTaYH0TApqObytFIsi6gbYej7rxB+DA3BiNNm3vsssuDthA+VnRI7bGKq7wjD12P/roo5mAXeJyxq7E98mZVyMfnNigHn30UbcyiuVjV7qYN28eFeTDd6GVpIgbwx9++GG5RCxdc801N9xww0EHHWS787RdBa733nsvNtLTDosOGzZstdVWu/nmm92S6rrrrrv77rvzNHy+9957vPmtt97CD5mdYcrn4cJv7ty5Wag9ksEMmeTBBx+kQcLaJdziylQVyceUIJ2Ln1QBwubiiy/WiLCYufTSS7mXpC6h5hPEMm0LmLPlkFOHfZUrr7HGGosXL5anuO+rr76qnw7tRZlQxtTPz7gySblg+unW0iV62yMZq4G27EZXkn2qD9JxYg2a1M9qXKoxppI9GzUYS0ayiwr6oVir4FB/VBEySFtB182XQ/Hs7373u2IpPTKXs31SSWYg1KhRoywhpySJxwRg5tNPPz3tjpGc6NJ48sknCSVrPPbYY26feOKJ8soK/uXrrEil3BvP2lY31qatjuXqCxcu5N7HH3+8bGJaqAsb2OS7+WZEMbj22mtvvvnm9j/D5RE2pcM81ePKgXfYYQeZuny6UbIJl7vooovSXtFIjgxhlK7tDwKSOaVGhucrIbvgggs4OovmloHpWiMDHVqcy1VrAwYMEAAWtgOkGqwDozzJ/J7Onz9fSamzRUc25Keffto+KZJlDfxQvbUmTpwomcVUhkgWkpm1GD4GK/NIPUmEXUVy9Ghrwi1mRMg555zDufOlN2hQfV7HA3Eb22d13qAEQL/WWmuJB/PIuEWHBZKL0o6RPFU1FW3UyRRdNijSieT77rvPXmSbFbfKME+znGAjphUlNYZXSpRHQKURp+OeDFlO9ll//fVlH3IRmWjl71iOOeYYGrb75ZbS6g46duxYHoZ49dVXF0h2jPiAaeuC4Ec2t+EQgeHy55wtkO/Iay32dStsFAJ4jp4jBVD14MGDxd5OO+2Uvz8paTpRodFVJOepCkvKYJrUIJRf/JY/sJrCO7cYyIYRCDxqVLp//etfF4p01b7tAe+iT5aiHFkvbtwCpZYKn+poxlax7rrroue0gqicpDySQFkWnzvuuGPJKdUEnwi7cpEcMIBtOf3cSzglc8OFF14oz5E8t8p9bpE2iITkS8I/8MADGixRqv8CMWZ1xpaYDWdRi9YdokBetBUzYf6wGVQBMV5Y5d+SHIb5d85UOiN5JNLoGMmeBi+88ELKPMEg/fOn8lngiSeeSO95YwlkR+k5bUBpE9OwQ5oEJ4TN0nWol1Aq4OULjbzbmKVDUMC5JSNhP3DgQCypIe0VKUNCTEweL4Z5hkxHOs4UGV3T6BjJHmUGpVocBTDD0VUT5Zat82d6wG/ynUfA6DHouHHjKMoxnondtkhB/NmzZ0s04oS/KigQhLEWcGVKk6NVktydEXkC4kLP6DoRUIvl9BC2bFbJ0R0jOTO4GptkAUQjUXFj/iCoynbHn3ly2sbK6eoFkaah58YbbywD68ChObfYYgtqpPbixtCkqGDLNQ/OeUI2G+BICn6NDPGI1VIxUUv640saoLGikQwZA+xdtg5nDIWcHJxbuiMVI+WWH/AAjXDvaV5/ifalE16ej23qCDHdlcAoHtmCRLJ58rdjoHqPWk1SHyKF1z/G5IVyatrdRLIZhIf508mZoOzJ5lSl68ktpckjGga6ivDEDKeURMxj122P5IDZpLm00ZA3k9RBafZkoVsqIGkxBxD09ZmlrXqtrgJMToHuI5nH5I86gLF4s5oit1St/krRAaSj6rTBijZb88hW77//vpIqPtAiRW5RllxvSFm9wC2l0Zgg+eY3v+n0Kx7WWWcdyStPDQklqL3rCZSksQJ0jGTIohyvuLEZ2LG48axZs7baaqsSGPJ1/eMliRInbCqz66HqopY6YpF6ERc3bhFWfCaS5XqRlU7+qXLRQJ+sFOAwER6wfmFy5SI5TChm7PIKBklRjWd/xopaxXFOv+pIlcJ7lPsqn3y4bawrpac8E8DOnyJE/dy+JyMmmFOQekObRqBjMLOxWp38zsNKO16Ok/JBaxmLbZv2kCFDnOWcbRzkpEnsZcL2SI6vGKgtGTmGEc383MuWpVB3auBk+pmB76oz6cRWkw8OAp4RX7dNsbqtkrCZs44sRGlO/g1eq1MctNgbOJBVxIkNRDTyLTNnO8okhmQUMpWnQxB+GMJuX2qo7qtre8KIESOIxmpsRPadd95Z2Tlv3jy3LEUE5S7xkWVzyEBqd+DEBos7suJNKVieFoRP8ygp3VbiNqA/BIFRRKMQ2xo3sAHaADDAYTxCnHkyytaqfOOx0pyScKONNiqVcMdILgPJyGS8haLwbzmLSgSqnvHjx/Ntt2R3hGFoMR9ZDKcE+lQWIdDD80s2rwMlp8U8NzbWbXqyeoGEhQ2PZAcltOU4m2orH1VkFGQUgw4aNIgrEpbIhNWoplmZSI4kmVGmYSoulZqKP2lLUSlCcG9jVNyLHDFpYMbS0S233KJN4xSBP8eM8llFgf6ShyyHvkX4AmJL8BrEdkpU0bGK22rBBgzMDDoVaQ578ivO5RE9FnLtuCdDRhlut1TVsFYqT9a14dgh88kE77dJWlp1UK3ZGOWKk7xgLM6lf9sdRWfFOlDWhU1PkM4CxV6qQUlBrpTF8qs6LcRpK1xZhLD45KN5BF1FcgEPVjsYSEy3hGJHy6Xwc0o3LfGzR0W3gDcGdUuTws+K/BtBmKmjCJuBZYZ0BjopjYs37ysPzpvbIQ5y6+pIYlfEFR8omyd0jOQyFvghZ1AgxItcSUrebAYyAu2xexJ0rOPKaRnU/iHBuTUqXtcCq7SYu6xbB8cQbjkXMCjlWzTfFKKPftJuUFcf1DEiK/DJhHEerUQkf2ZYqfAB9XafoZtFu4rkjlhB5rsi6xvZ21cpPT1GcjfoyHz3EnnaPUFH1If0ODwB1hFdVdefAZUcPYjfFc0KYkXGttNUazY6P3skt0/axygMrAgnLTRuS88KRnJ9hnq7oJqydZVmq4shK46VmqqdoPSsSCR3NX/p1yh7RUfkUTcEK4LffJIVieQVmR9Nj2QrMk/36CYlFbSvUno+YySX8WnUr3Xoae+EdHZ89NmwslPVGegxksvkK7JKR5oVGdg9VoqHOlroe4zk7hdq6ex423FgHyM89BjJhdWV5byXZPxNpv0tVNc9HgaSbFzrx30NQFyQfqj3N7va4BGy0k6jIDPUGWunKT0ruCcHZdGgRfas6xpoR+S0g7SbAyp01V9QX6Wa7BPKamgT6YF6OyhDVqq6bp+njsJJaQRp49kVWa5B4/FyNLva4JEZ0khPQTWuiWZX12Qa3Udyy8AWU7agLiDk1jViQpG3jo6ddWQejazuFqonjXZLD9TbgZ7M8Bkj+dFHHz3ssMOOOeaYfEn79NNPT5s2TU8+b3j11VdPPvlkt9dddx0WebPF4MMPPyyspOEpOO7XWUSps7TTaEH6zY8TYz/44APReMABB1x44YX6rZgQuvvuu6dMmXJD9Xf8y5Ytw+QhhxyC7Xz/nK+Xeoxkkxh17LHH5mP2Rx555PDDDz/iiCPyQchzzz03Y8YMws6fP78hZMV8+C8yuqYB0UZ6giJ7S38LrrjiimeeeSbzu8VVeaUsM9x000177LFH+Rzu4IMPnjp16oknnpiXpTJ5j5FsCdIZGBURiuz0lk+/Fy1aZAZ48MEHTZils3rmL9LFpljN06Awn3YaHXHJJZdE21dfffV+++131FFHvfnmm9VSzRAi4F577ZVvB15//fXjjz+evGFMT1bpcU9euHAh6Y4++ui48ZNPPsk3yJ7PjRcsWHDooYeSPa/3RZYw0Bi83KAahAXtulBUAWl3I6yB559/vquZXVHyKwFoNj2ZHyd77rlnvgbibzjkb9OnT88noKH5LJH8xhtv8Bh+c9lll+2zzz7vvPPOLrvsIhh+9KMfjRw58oUXXqBQmhXVw4cPz0eg+INETvkCOd+e6S/mL3D72muv8armfRsMsfoXvvCFfGxI4/yPwKNHj7722msbi330kfAeM2bMqaeeOn78+AceeABvuOLol1566RZbbMFHacrY7iNZGOy2226UeM455zAqf7KERfnQTjvt9Pbbb+++++5z5sy55ZZbRowYwRUMiThW1y5fdKdhRU+zboDS1Sr5srQjfvnLX55xxhlf+tKX8t41vPfee9/5znd22GEH7cxGXaNGjTr77LPxwxG32WYbct13331MueWWWybpANN0E8nvVq8EXnPNNTfeeKP4ERVk1CbgxIkTCUufV155JQ2zbHmNjAgNR/7Vr/CQnnwpzcNaLKsNdFj/OL0FVhG3X/7yl5ERxEISMbnYt8xmCR540kkn4YdOxo0b56nUhvNBgwZdddVV0Un3kcz9Jk2adPPNN8+bN88eYLkJEyZcdNFF+f7p9ttvNzknF2ZuuS5xgJiRK977/vvvs4WGFbNoATLc/vSnP02a6Ii8ZfC1r30tw9EbtfXWWw8YMMDT9HAkLnfWWWdhj7DcTHammQsuuGCrrbbi85nqs0Tyyy+/zMwCWNDSoIiliDyaNWuWrHbQQQdhwi2rH3fccRoxgC2U7kAiZK3tttvOQh7RTgjqEDyYa960QczIUkOGDPnxj3+cL3Vvq0BrooKi0QgAvs6brWit+psheOagWbT7SLY1kY42bcX2XmFQXgPQUHpIkLk1Sfwm086dO3fvvffmBI0trHpzM69nVCb7lMkBcTc8kEtlMWzYMLKkhwLBtLkFtmDvxYsX8794c/PBxx/jmb3DlSHdRDKbSs1KKuFkp2LK8v6MGuSUU04p705IahEn8IhLWJpZMSZpigT98ebQFGDSbM2bNvAZlmU4ErEsZnQ+9NBD++67L4OaDSiQsHfddRcNC/X4WCBlYyyLdh/J5sezOMwuZ8spbixspMJiEf0JGOuSiIwG7rzzzpSAge233z5fYnmadYNYGTPlTZV28H8eQhYhkB5zWo4OtTPDL37xC/q0hP1y6NCh9TdDxIhMlEU/Y3VtsW233ZbHyIvyRF7oAekt3zPn1jLhKaAgPElmIvCEE05QsNFC2ZlDA8JGDvZoo402Ei1JaXUCiOQmEclqDJTcjn9Y3Z5PBdEC2Wy/hBTqmUd/4hxYxbX7SLYuXXOsjTfe2D5MImV2Hlmd4PW3NcsjEDP777+/EnGDDTaQPlnCnpkV67KwE/Zo0s5JmSlYwnwBD3aNt2koqtlbZilJxITAazfbbLOZM2cyeXbFSg3NqbJ095EMFC7TM5Al5D4GTb9bwpbXlTTKy4yg6qFGKX6NNdaQd+SRydX/NVGXFGhezrK3KCgkhXxHHeZDALHs9773vfLeqCFf/epXMYbMDJHIEvYuCmfZVBx1YTNJj9W1VeTHTTfd1A6kADnwwAPTzx/WWWedHF5Av3ozbTwIcrKrzL/xjW9Ymq8mMXlUGABubHVhYoNVDJYX1PI0II5d3bbs6lY5YC27lLTl1mwIDJFPWVZ1ueuuu7a/z5tFVzSSDWvoqRrDVDK34kooSk7i88gjjwwZCSXUEr1qzhLVgCHK1cBujmHsXYrtApWMZMNvBLNCLm8IZOkW8EuRzCFQRrDTTz+dK2uwZYbkjTx85mv0uII9x9Ydgo6R7FGeOp0q3aWbbM7mL5rhzaaVQXLraJdIDiciXNhr2E5tLEJLQWh1PZk5YELVAQvxb4bEWFRd7FQgL0gHS5cu/eY3vyka2YjUakIhCqEnrCXUIILKbToV9owV5+4YyZWsDZb4pSraEuidxHhhee+amKwmeeWWEvKRRMDzikEtKirqdi/Ap41UTMoU9l4L6SyrF7ilq3K2IlSSfg4XnkaulLWcTV2tESXIesWyHSMZWZ5yTirlXSbH/+zZsyknNPxh7bXXdgrLLQdgo7QNt1soFmg48abSJFGehrGAwi3B+ji//vrrc+xvkRT0S0b6sW1RSd+GYe9lAp2F27ixuMuhPZ1qKIEdp1qJPdmkoOFpsahtQeRw8UzNfe3+JMyxUJAnrgJHzWgWgS2FqDy4PZKzCvPUX0Wu66hALqRiYcbwOZfirfxnPJknyEmveVNppBTbHSO5IWo1XOVWKkxxKy9y8dzyA9Grvsr5H2W2qbCqBkv9KeNyWR7DYAmnuixpM17xG5xHmQWhKZHMk2xoygQhnRdak7bKKI5VymCd6kAH+0zSMZJJmqce8dp08gyFa/7ihYBMJqnFd4EquGnawF+VteZRDshNaoeyv9WFDWy2ZW/HXhyxDkNkBJvYokWLymZo/8xniugLw4ArVX2MBTYVmk+7PZIzPGPPPPPMvNsMpOYPlsgtN6ZkG2luWbB80GCh1HcxhB4pKXVZYSnIbT5lKD2FzwJZXhL3SEzSqoBS4Ky++upJW/orwzYti+csGmiXH8lYiUg2KWjkEy++YlXuhTnOrcGVMcGQahXSUoTTeVJIBgrsaJb3Mzz/Y/hEcggCfHMdKA4ay9VpAgxk0xBRNgFbIq/lASgNYbPArVQtesHJVvoYO3YsKTJhx0g2yroaTlOIZS48E5B0ig4ZhLswvBm0GcAj/pTyIdPSTw6rVIElBtMglJ46rCIH6c+KxhY0KZYDA6muA5mOzjWiH8OpK4qiUtsyhUhqSnoDsR1xOkZyWQ4Z4sOrvyWgKwdITkY0AazTDGmQXVpEnOFglDO81TmA3cOpMry1wCpo8ElkDRNCWb1AJ/5pfsmSJY5j4oQsUgMZjSoDNTIhN+CQ7Mizywvh0NWenIE2ACFqctWfSGYCq4Aes5kEDzzKLpWNKkway39ohk0R6BHJJXfUgd6cJCWvdoGpmhQV+IzjWw5QgUyHAY3I6FosaxOWNFmBG1M1j0oRh3glIhkqThrDnO7sIWSgXLcWU2PYkcxbETY+UjJvS01P/vJlhmrTKDtznDsE7cjYoNlVgxNFPkEFpazKpOSFAqtAaBTtRMt3Y27T3zGSm4OrRc3puFjqK0q3hdoKUgWgURWTPQf+9LiyRz6tkc45PWInq8JJQbVIq2jtPWCesgTIROWc6Wrmaqamo2ikAnf6aFAvJ+sYyXUwh+TIuKldrUirBMxwT6Wnyy67LE8L8KbOtzSD0i3e8qcdHZGpXIN0tsA8qSf5rvOqmiImq6M+Vu4gLN7iTkFX5+SyrslJavIoTcA4zdkV8rcAnNnS+Soko1wjI4NCNmoemO8s2pEhHRsFFlVq1aXDVSkBijWDdKpTVL6MktvQrFwk90t0jOT+ih4juT+hq0jul1gVyasiud9iVSSviuR+i1WR3F/RQyQ3y/PlJ4THH3887RdffNHJMH+NDGp9h09HDoel9Nx2220I8tlDZnASMANol0Y6Dc+oQH+O36F0DfI00O+6dOnSfN3i7Op4U85vjdkrAsc8XOXbDnBovPDCC7FajveuJZItgR/IWg66hTGUTzzxROgdohySHcmclNyid4QmbL5mqDhtsG2JzFMm1JlH4LagEATtBMGSJUtyTraQ85vTbCHL8Jdeekl/PimwuoglbPmE2SquJZLdGl7WJWwIDM+5NJO/9tprRHMky1N6vuaaay6//PKcJA0PGhx/Wro0QKfbgnKbhmuQzgL8WKL0F8crYGhslG+q7rjjjnnz5tFJHCDEJZIbC1TQphnH2rSff/550uWPgcEZm+C8KN/Gu3Ie6ireEnHKtegw12qOT6AnSks71yCdBVyLpyHOo6eeeirqDXTG4vnUyVrijrCMoh0C1x4i2exgACGnTZs2svovnrnUrrvueuSRR44ZMybfUkydOvWAAw5AsMsuu1DlrFmzJk6cePLJJ6MvrwoDynboJ0Z4CrTpzopCxVPD9bhCk6ICM6y33nrMYEXrTpky5aCDDjr88MPfeecd9AaaZJ999hk1atTu1W/iHnzwwTvssMPMmTNxi/9ly5Zl0RLJGZVOJlx33XUTq+Y57rjjhg4digE9+exaSOxX/VTVUUcdtffee0+fPn3nnXcuX33XP3epw/xQF0Sb+CIE8jRsNB8vx8KFC9daa62HH374jTfemFT9dOaECROOPvrokmvYnlAswhAMj2bs2LFnnHHGvvvuiz2jIleJ5KyS5bj71ltvrf3KK6+QzuTjxo07/vjjJQ6rMCs15uNZjXyyPXnyZGrHfGZocNCGavpPCRJiPBtbGGgxK0i4lG+30EYwe/bszTbbrIUMPzvuuGO+L5gxY8aIESNOOeUUnTxBJIS4RLK1shzz0YBROsUPjRnLK84++2xD+A+Ql3T8do899vCUPvPNHIJMot0Cj/RnlWbXcjeOcctTaBFE+K2//vooM/Pdd9+9zjrr5IXqwCP8jB49Gj8sy6AEP+ussw455BBRRkuZsIdItnCYOPbYY9dcc01q0rl48eK8Yi5/b1+9qpbvY/Qgo779998/O4OQrqsyrwELA/un5GfUvffeayBe0RRkKkvUi17D6yqgaKG1+uqr2/zlThOmnwfnTwjg3XffZSTuKMj3qlBmIPa5556b2xLJJI025elvf/vbm2yyCRug4SLf+ta3BKpHd911VwIY2Fim5NwZdcIJJ5xf/dxkbm+99da5c+dKH6lWCJt3JzytCxLQxpXVD2V6BIRNf8C6Q4YMYeBFixZJzPOX/1QIDZQXmJ999lnhJ4OwURw0/VCvqLWzBYUNkNrMTFEWpdVMziLkpaV8Oe+WmPZAIjdmqWTPp+Jh9dprr7VL0IzhlCke8l1giyB6XK1y5plnpidmTX9gKprfeOONswWJMSkMe3kaGMWzEVgIY4xeMpqwLxV1PZJdiWz74caylVvemO9s5a+ddtrpwQcfTD/QHm/JSxPGmj+2w6dbepgzZ46l77zzzlNPPdWc+UbT/FkoiFC0VAIsjlGHR5Q/aNCg8M9Vttpqq+9+97vPPfdcCODtt98WuvYnG5KQ5lHNB9UrDDww7Z4jGUMMKUmIWFqraJp49NFHeQaXLbNzZWFT3vEqb2tGQluE9KMWZSfpRMBIBCkk6iqwHB3ZGehXISEpeAp1e4tPhpQ48p0tPPbYY9x9/Pjx8dGoVdagGizRRf0dLw1XbY16JOsxVlQ4F0iB+WaF59kSmRaNlFFeGGBp5sxbAUCctGMw/G+33XZswxHtY/mO3WxQkTdhl1AA8xXQYLZwWBeWpOQ1YV5mDoQKu6YOBEmHdWgASzaoVAcREMq69T0ZsEo6mxgVmaGibYAnHXbYYXz0guU/oHnMMcewMnfJrYIrL3KGT0mEn7HFV7/6VWWaSMCGfkvUBbGcPHvSSScNGzZMcUguPVCnUWoR1maQfUmqCnvIQhBIr+oINhLk0queSJSnIa6fky0hWsz2yCOP2NYKJdgzSGdLKG/F8If6r+Tq58lh0nXTTTflV9L0aqutJlIktbzo4lF9WsuZU3bjxoYTClcIWoQFUuRQoC0pYC/fLwZGCaJtttkmu3Fe0DBPZDRbJuwhkusQCVyn8PHqq69yUOcZO0Z5oYfhbT6xIhAg2smq8mWSMeHzjRn3VfdqlGnhgw8+4A2MvcEGG6iXYtE6QQGFltcJ8aMtVef0Hp2aijZph5cnz4WTNJIISyQHGSi/2NxoP+s6WXEmDdbNNgV0x+HK25pkT5BnBlEtjDXYyWGeqfh6MkXhAYQuv99iiy0UkBr5CtoMmaQOSitvhsjQZE9gmzDEOilc9pF0EuH6E8waEaS+P+tJZ5ypnAjIbnKJmxVKJBOHWcu7fWRPJGdmBbxk51a2cqsdl4i8jQEVCH7OOeewkWMR5+FRnta1UUAEdo9cCkiqS7vAKJblPBYSnHoKgTkjdUskgwZi3GqUyelEhDtpl0gWpcr7UujpL6+amZnTMiinEg56pCTq0mjhkO9JN4MHD84fBVCyTjQtZESgtBxV0kP2eiSDdG9vjxvngyHiR298OBOuRCQzjyjNMO5iZ88upywpBadaKK/ah0zF6FYjtzSblzdll4ceeoioZCgfFLkGIbZ1Z2x6KkO00tCgYoyceeEE1LH2Lo0WH7J7l9+pBqGrQApBSyQHYtgR0TW3yWIawsApMZ0aTJXlQLmePJVphSXeNAy0f9oklSFExnmYD0Isx0FuAUH6g9DzP96mwerMlt9ChBZiYA4VYPOm2j/DCdQjucC2LFQSyTiUqvJHVw5jSomKpFFiUFSxCNdMDuVPVucYDIoTBpUIJPdSi9V5S5sjlSIuotWBRqdC1+aTp1Iw1bXIWEDnJZkCl5OAQlyP5AIZivulzfc4RrYKG7tcmX7FowgUBbmlzxwnTUtLdLW0+r1xUuu0YqnF2pnkkIylEVW0KATU9pTGhz1KcHKYlkguIKkQa95UbqMKzoQrEcmSGefWsG/Y5RGolFiF7ceOHSuNOSOp65LkxDm3Gz58eCqfLEZBXF9D1uGIBo4ZMyaRHJsFEVi/+NSGdh1FZimDj4o3C2FA3lLmZcWWIZzVaYRpORnbK+9ZNI+6imRbR4lkYppZQwa1lmOtSlJdJ6NxMu5uaUVETlORRZbJ0VfBn8/YnTz5QSXQJ4xpo6c0pWbaQfNxhdxybsw7/DO8JLJgwQI5NAkLQhk4/qk8naDQ89TNN9/cYSE0HSOZKzMEjSkQnLGFK+vQD39yQCBa3lon7KhRo6644gq7kP68XRfebOmCHzMIOCXTZ99rQVhVLzBH2tAibHqwodxLj0imuli8HVLk0KFDRS+FsO+AAQPs1XnUMZIpRyhqcOORI0faWrjxokWLVDTKYEpT17CsMyMn11aVRChc4c0eiBks2WMTDpJmeRUfQRqgTSFWYX1t/JshkzQpKlAjTzO//jziadkj2/H4449zY3sGJyfywIEDy8d7KxHJvC3Ha2JzJtURa5lOj+LEmUpKy59xUq55ZSzlJcmtFAEUh/lAhYtLaeS88MIL81FzuAm0i9kif5khnZBbEZUqXcxLV2pdbpenBtbpQajIL3i2XeT3lpG5doxkG4vqMZ94uTW2/OmPzccGxXhZmkUtTfbyQVSmVeTHHpQmI3BfM0QbmTNAnCI/7SC3BaHnMUwgJqN8wjqe5XzVPkQYsAgTiHmj9ISmYySzV6SjRqWjye1CTgp0KCaVr2I7H62RyFOySyJuIwvYeRgUPb+XoAWqTJdHjQVq0BNOGnJ2siy4veiii3LU13799dexhyxP2yHpK7hYVmZPqRLijpFMgSxiWpQSEFPSkj3GI1FBaeqFlCQi3IR6yI4+SdPMmFHosimpkUl5UamnoFFQ3NgoKLcF6ItjuEXjSofJkh1Bz8o9PLNCjJJpVyKSfxO0C1lHN48K2mlWZNSKoGMkf2Z0z5WnHQlKZ8enPaLHUYWgYySvIOJnLTBzV6t39Uhnx6k6ouMMK4iOkRz8JtP2HnrkqhuCPork32f8diP59xy/SST/waGbSO5/WBXJqyK532JVJK+K5H6LVZHcX9FDJOeYnlONU3hIFy9evNdee02pXpw6rvoxtCeffPLQQw/Vc3P1ezcvvfTStGnTJk6ceNVVVxmuuAeTtFf5OoOWR/XbMNCR4Mrl/y/Us88+i4E999zzhuqPNrOoxoIFCyZMmPDD6vc3n3vuuUMOOWT33XdHWf8GskSyUb9e/tKcR5TwfvW25o033mjmY4455p133nF7//3377vvvvvvv38+9Xn66adNiyDfYxsO7QyDnsxff6RdbjUMDNLTjhBfdtll1Ev5eZ3DnK5kHzt27N3VT+Gw0X777YfmyCOPzBfpGViP5Cyn8cYbb5x33nlpP/DAAwcccAAB8/0noZiVxvJJ8qOPPmpaT/OZUGaoy5srFElLD2iH1bQhAyGd7fjwww9ZhxHPOuus0IN+ApIuH9S9/PLLR1U/foDziB+USK4v8eKLL+abcLj33nv58MEHH5xvSR6rflp47733zge3t1f/r7We8vloJC0ilEZ5VFaBFso8dU1PRyxdujRxlBcHjMqEbsePHx8He+aZZw488MDddtvtsMMOC2NZpedIhl/96lcUt+mmm2677bY633rrLU6s59RTT83bLWPGjLn44ovpZfvtt6cUa5x22mlohg0bVr4TMkm+sczXTpA3Opnco7qE4V7i4D3aEDbyNDDV3Llz/+7v/u7a6g/Bx40bh2fuNWLEiHyxCWh22mknfuApqwwePBhXYlhkbr755uW7/vZItvQee+zxla98xSSUyI1E7xVXXMEzXn31VTLeeuut1LrjjjtSBRXToKWHDx/OFTBjXQNNpR1htdMgafRegNL1hRdeoDcNTyOva/W8A7AhH8kgHJf99CD+afVf/vFsj4i2xRZbIFu4cOFFF1202Wabla/cRHLe1rQEWG7JkiVDhw7dcMMNTSLm6eqWW26544476IpQhBUbF1xwQd6TIbJ8QXzCyteZAWLEfGmnQS1peFQXBL1bZPm+tGLhE3fviBkzZoglnkCu/NJNJuTKc+bMwe1tt92GSUmN3Qm+9dZb5yNlqEdy1qKH9ddfn1foZBGTkI5l5aZf/OIX8uDVV1/NY0eNGkUJhNWWNEePHv1B9asSkZR9QfrT89577+UXERpaaBMWZBkaTjsEdZo6PLU9WE4yxZhMGkpLY5iP8TRcDRo06IwzziCI/UlIEj9kPUeyK5OceOKJ36vQIKlgg8qeYOHyjhfdHXHEEVSfW4vlPQrzWO/yyy+nnV133dUOJtqHDBnCXSoNNDJWhkDa4q28F1m0kFuQR/bZZx8SCtGnnnpK7ky/8D55+f+7TwUCWyjywu222+7c2s+L4plSzKldItkqWZpGTBh7Ky5YWiNtO3OCB4499lgaOHz5/7hp6bx8kmlnz55tXfIyz9SpU3lYtoIki8aAGvBWfrSMmNioC1uHMgFvih1gbJklE8oFGJanZNVtttmm/H0PzJ8/X0xGtLInFzZmzpxpF+I62vyYgBrABwYMGFCiwkDy0kBuCR61ZNrp06ezqVRy0EEHyS8YEPBE4DkVeRMhxmR5nQYPOOlKWOlJSuUJ1113nb1U6kcftnfeeWdyWVROyVehgRyBOAuVSM4tX+VRgjYvHdOY+kJAqig5reSFef0wa9YsqTBv0QOJsiHFNG6tK32kFpMHuZOnHrULwueLQ4agnSYgFwYo5+2338Zh+aJYsrAWCxLZWilDAmloRSO5WrdZEdUDBgRhXkuSoUskm4tblEhmA9WCRmZQIElvGB05cqS8IqmzfXJbuAlo/MwzzxSEG2ywgUQQkeoEEBfhQNJwojr9l3z6By55G68ym4yecrEeSDFwPZI9ylXAGCL1SkYmt42oZOhR3JajFwsxalIVqEr4t0aW5hyI33zzTVsicz7xxBNSvgnND9WIBmxf3GvLLbdUJkiXfNfwwmE7JFCUXFA9KUnbdRuqqTyM4+b/7xaW2RUJW2JJ27VEcoZYSMO+IWA0hIFdTv2mx7605pprllJchPOz8ramWiwvchrlahSDvvbaa2uttdY999xDaUn6mb8xoIJbG6lcs9566+GE13oKdYXUoe5QLKB0RlAZiT3EEcQ5jjmkzvobUUVvoanvyRBV2N7Dmx5xaDuhfJ6p7CqRzB++/e1vl7c1+bO8r5F5DHGs43XrrLMOXQkW7HnaIqyNRIrhfhtttBGfVO94StI6TQu4Im+Rm+wBuEUczXAtW3HezxE1eqzVImwPkVwHvZM8bXmixAYhiwpYF02JZEGeR+Fe5FOuhshPiW9/To1dB854A/vZZOyoqdk6yo+GRRnSvpcexUl5dS49qYtkYk6vEbFVViwaNZVIDrKQRWlT0tGmDemQT+ixmdQjWUSVTYzhs2VlBmzkYOPYIz6JSWNxpros2COjFCmWpFg1XvNBF5AaZOi8NUH2kkODHOw5dwiiBIeFnAO1SyTXofzjIuFNZiQmt8CteCvERJPR8ooeaJTTJniUcJo0aRKt2kDiAy1Wc6ss5N+OaTaTMNkNOAlhIwVvjqqLZaVFV8VdNsxYln7Kr2qVSK7Doc9mo0FS2mPiZcuWycjSveQYGuXVGmusUeoRuxFiDaLREksphWiVU+mkogwkXV3euDE9yOAO3tmx4nIdIZponqVk4fKCYBE2H4jwt/p7hNzYPpf2ykUyGdJetGhRbKYtcQrILEkkWmDXGEnKpKDGgAoiOZqlAqcalrB7tAdq2ty6Xg9XWmqlsekpI20FIi1vO4mf8mZ/g245SGQHa95UpyxpOO2WSA5whV5gCDPnfz1Lly5lb8FJm6EhJnVL8EkWlk7lE97c5ldyKc1Ytu8YyYGyFtLO03aawKlMasjnT9wLSxrF3oFNnn+njTfBkL/lgI6RbGOJNblRKLXplgipMrAt1yhwyvGK7PU/zNIvQvBMsQzBdsng5qkLkjbnawmwroTlqbSXXG+TSKJsEdb+r7KLCYBCUpRBx0jmeCktbXH5lAfE29lnn02o3HJjSs48luPeJTuITzIKfjbNxuaYQ1EaHaWwz5UqPQRdCasokE/TluwSOC3EIoilmjcffyzyS/SuXCRL9plaujJSIwGjuhCc5DG15OHIp+GWinlJMSc+8lqcLVRu5h/Yat+TEYM4N1Xa0OITAW9LtMjWeGNpZZ4J2+nFpMzKVDNmzFCn8Q+ZLwRdRTL7YcARaPDgwYzK/Pl0TUaXMp2RkpItzY8Ja1qjEGRa4ZSowBjDSzdmILKnUVqBHv18sRr6CZqP28AX+at15a98ysq96vQ0QEAbDraFsai2YgKgYyQLYPQI7DM56xrCiFQknTk+EDD7Yc78xOfElFOUTLEi2W0i2V5EP/r1QGONCpVYDWGzw+Q2CEE71B0WpV6c5JyVvbfALd7wz7LciU5IkUdd7cnJR7RECq4rjAllHldrCWMETGZOMxONm6GPApExqP1TqS/a9cjmpRarC6uth7B8ryFhDU2KTwM9VWPAbJZ2wEGZSZoU1dmK1wHL2uq5IrcJYysRyQo/O3vmpSzClJVcHYkvqv1Krq1MKsrOXLh5cfn/Y2YePOnUELF5WoeedKYR5FEdygFpmySWsEEpwJIX0hOaOubPn3/eeeel6IXQdIxkXDkIxeGccOgo2yCwjf3TVlBciuyWVtdpN3n96CMpLOIrO9mSxjWiCqjGNaCN23R6GgLX5uM2eOqqJiJITjcZVT38BMhwhe3snAjCbcdIxp46NgSKQIazqeYRgzo1mErbnFglON+NZrK0fltWDEpG80gBZRMLw4F2kHbpqR52QB4pnhU7ihptyyUbVs8bSBvDFEI0T90ic+0YyeEtBJFOwk0wuCrxSEchbknkafnssJiJjMQHSjOPHF2+54MQg3aGpF2Qp13hhhtuKL5keJmhDg6s8i1H9xhuJSL59xY9aqd7dIzk/oqOkfzZ8Buq/beFbtjoGMnBb4v5PlZC+3Klpz9E8m+IVZHcX9FNJPc/rIrkVZHcb7Eqkj+J5LJ3Ozc6KDo55DZwnMh5A5wJc1oIUDooNm+Wz+NaJiwNqLfrqMg7P2qBQ9RTTz317LPPOjrmnZsCJ/PCpHMRKVq+/OgYyUuWLMnBrI4cn8CBP1/rBeWkFLTzXHq6EWcFJQ1+9rOfPV37+cUyts4GGgfCfPlR0B7JTllU10LmEOiEljatEjBtIPgLy//jpazbwnnHzjo86uZpHXhgULYAOi8fUAd6ckSE9957j2Vfrn4Zp6A9krkxYetf9Zm/fEIG2vkoJ/C0xQ0K53URKoFWSKIe0eJLBflMJGAswhajZOkeIpmm0FHZnnvuOXbs2OHDhz9YvWwMzv0777xzVGkK7d2q/9XNrbP4uHHj3B588MH5kkksBY2Rn4YZftXpV3JLO6h01VlZ+hlswoQJ++6779Zbb3159cM3hrieccYZG2+8cV7euOSSS4YOHbrrrrtOnDgRPYI4a4nkDGHmY445ZtSoUdtuu+0Pqxe2gx133DGaMucuu+xCunyPdeGFF7qdNGmSVRLqpi38tyCS1gVxy71Ku5Ky8bRO04Krr74ab/iZPn16vntDbMVp06Ztsskm+fZi5syZgwcPxhU+586dGxrXEslZ6/XXX99///1Hjx5NM/lWFph7zJgxsh5uqYK6KC3vgcyePVsbTjvtNMNNYl3XDKwjLIWm2VV1lltagtzqT2cLuOzhhx+Ogb322mvLLbcUz80HlcsNGDAgX8Jde+21w4YNwxVKHkifmbZEsltL2Fp23333nXbaaeTIkfn88sQTT6QfnsPh3XKD8dV/m8Yl5DKxQYF64h5mwHBHVs0fPdSfahfLtvQ3W2244YYbrM6duJbZQKcrflg23wgSfJtttoll2bqQ9RzJrlddddXF1c8sXHrppQTTc80116y77rrf+c53tOUGhpe5Ee+xxx7CeJ999rnnnnssQNHlK1aQzh9//HFT2U/Qn3/++fmoucUbsuiiRYvKt6DRIOS2BejziaX5eTN+9CAWV/nB7SlTppCT9y+ufgLOZlXMAyWSs+7dd99Nj9qPPvrokCFDkr8Fw9e+9rV58+ZJ2IJcxfHmm2+a5P7776d3aR69ZFfeHwBJ1HKUu3TpUlmPsIoFq7d4Q9q3Vyg9QW5bYF86ovq5PG2Ni5b/d+T0KZkqNzj0scceKzhxhQ0Mi/l8+AwlkrHhimG2RoaAXHpuu+22DTbY4Jvf/CaVzp8/n8cQTQjxG0k8X/IRhMUfqf4KxVNTWcstGSXue++9l58kZ0FdkLQppLx0gaCr8ACPEgyMIurqgUFAWt17772Zb9CgQQ888ICpZJ/JkyfnnVkokRxhL6uAjE8aSBxCmVOJwZRmcLWr07DEcfrpp3+velPAU8FPjRY1D7l4r7E0/9Zbb1GgxKo/krpWKzcQoXhIUX4LQQtMYrNkR216jnoNsQoGpFdpiBLk3Ceq/0SBrdGTqBrdUySTk6mgetR4Xdm+p/HjH//YFidutdk+L/SAzC2M810iiOq8ohABTLveeuvJmptvvrlEaJQYK7tKY0AFy3GXc845h7qxKyC7V0F5ZOb8+g910wszCLOp1e+wy9l3Vn9fkoX4In/KwBLJhlg6SQFokO7Q2KzwKf8xHqvQZgjojgjlbU0KSUliHlf9CgSZZeDAgQQxg+0lgmTdwHIyi63vyCOPlIMoHE2Y7Iiwh+zcc88VuvYWxFYUQpz7qKOOIqycJbSQZSFJhx+EK5Fc/wuKEhu8M+9LLFiwQOLmxNQuJLIVAw6ZMtsClHe8TIIB8WN1Imy44YbIhET8J0+rEQ24xaf52UXaTWproanDI1c7Mz2XyjnE3Oyggw6KsPm9wRDTj+o0wrbsySEAeYE4cyqkR+479NBDdeaWP9ilGDS35R0vMA9fkuCwJOURWaKUwjwq8wd44Mb0IGRY1iav03AIQQv0Iz755JPNZnLuF2I2kjctRKuEzXtK+l3FDjVm3Z4juXg2vVugfNPIJNK/hkguoYsJToAstzfddFPeu85i9rr4ve0rIYe5bMvhLOBDyNRO3/rWt7hI+WayK2RyiQox9ZlKT2xpM5kxYwbhGZ43h7gkpjRKJJPUqAw0CSeQ8OzJMreULPWqJm699VYqawyu/oqA4Erc3IrzOHr4IUI0y9J2D9rjdomcurAMxtLrr7++HLfffvvlzBYeOiJjHd6woeCUKyOvzoceekjisF3QQ0oJ/cV8EbYlkkEbV5w4f5EayNHyYLwqPQiYtcgunWVfzQzoM5yX2xjtJ5JXeVqAGXNutdVW3/jGNzjPfcv/NDJCtSPDaZ4fl9sQ82DhJ8lSGvXmaRE2CqxHMvEzXD0lBXAqTx0WGtRVJEtAxZTZcpg7twceeGBRjpkVL0pLYo4YMUIPfdKqhtWzRMCN7SJS21prrSWP52hQJ2iBR+aRIwjLVQR/0QwBubF9VHDFQxDnEUTYHiIZUdZmVxsOP9aOT3AmLq5xxx13lNA1F78stzJZhMyqdJdfXVV1q11lKZueSG4Rzy2lcBRxYt2Wp+3I5AKpvHzXDvshh2jeVDVPKd1Jmj+XsxCfznI0ABq2PnU1G9tgyUvAsgrdMVXZkxm+/IEBiGrHHg17nSRCXQKMOA3jLLcBWE6nLc60Vq8/6ojQp63KYPJ0pieQKBMkgWjPrwVCiWRGZFzLadBAXpWrWPtI0nHg5IiiLmdsoAHCpugAssfR0bsyuug1FYNiz9mqvG8fgkCbZaV+HBZVd4P4KNt183k7PYfJEIuxvLEMJZItmqfCOPGvrcgqvwEsThxVyp7M9HJrObnYjeL54Z8d5RHJPdmK6pICKlk/ZVky2vbNvCJuLAWnLAJ7Xn4N16j6nDhJrZ7ZFFDlNacVimTbLw+4/PLLcWZDjw1UO6o7BIo3WcqZEJmqyaZNQk7MIXBW/9s3/OUMw5D4Jl5yTyGoQ90Y9fWIjOVn3djbKVRJL7dZ1AlcxVsCu0RyhJVfnJHwiZIIDCYfCwbbjtyMK4cTPCvONUxIZKdWW6s4T8BE9SJcGamBQL0nku1C/KAy9ye2CWSWeux1AwGWLYIVZs6cmVJfCNXnVBZut912FiUCY3PKMnlLJPNsXkh80xJWj3ns584+rgIS8+y7cOFC1ZMgITKFML1CQxFknqxLOZYwJwIDs1Xmad2yITZDKVa7B3qJHg8tH0rXgbdNN93U6oRlnfyIbB6VSKYrUznFcBKBh5IhlDDcL58D82QOjHk7JzLi2K5FLJf2VHHL4gQxCRmpgvVJYf80ucLNoUYDQV1YynTlbLa69HQPJ2QMPP/88xTOxHGeFsvSm4omb0byOhs+TwhBz5GMzva4ySabyLucNQWJTidYZUCqf0FOKhqP4gSzpE4RvFkRUiTkYclz9i7c0KYsSFlmA/0F0QK09HcEGvObquPH9wWSmR1DnaMoqh9sSJrq2q2pGJiC5CD8y6aNkRV+WEGDcuiBgJnE3q5NfDsYF2lIUvEs3wtsbaHCEXkkDhnAo6xbEPoVhLHiRCqULmXofKMWM4UgcL5lDsIOHz48aTuLiuTkOy7iyjNY1tGD70peDdY/+kiyxjO7MBDlmAdyFnU2JjthBYkZzJl5uJE4R8+nDRdd8R+z1YV1u7KWfeaZZ8pW2RWkaQrhn/n9aj1ZpURyeGBlRzbFAhFs42hsLWwH+b6Df3ok4bIdWWza2nryNJK6OsLYk1W5tIRDWR59JK0LhXKlhAW7C91aMRuJUSZpGcsQuGJ9B5kccLJKD5GMOZCwJVq5it/I4noMdiUtZCIZne0bE1TAB/q0CzeIizq0dVbTN2eraBtIT562iNERjSkqZrqhT79AsjeWz9gM0SiRjCszoCEsWaRhCbuau5mMQ4BS1rQJaxTZc9qHELuaJywBMtCTdguToYGW/o5A5oqTxHDpCTJDrqQgLEOkJ2QlktMjETMoYRmLsHjTCeYvfBINTYa4kh1lbkMG0UzRj56SszIq0A5a+rsCmkyVaTsij9AIrWLZdJZIxpjOCEscqov5gCyRLkOijepJA57aijQiWvjRcNUuPpxOyKjAo4wC7WZv1whN3Zf0tAzMEgQplrW0VTR6iOSOqC/QslI7eiToPWTp6LGFjfptieSOaB/bDVaK+LeL2NjqHeUtKJHcFcrAbiYJun/aB+gxQkok98hqQ9RP0/Q4pDfQ1aIVdw007zuh50huH99xxtJZf9r92n2Arriq33aM5EJTpyzoqrNj/28dWaV9rQQzVIx05qS+J6cHOtK39wQhDppdvYayRPta1fqfdOY2aHbVIrmOFpoWtDzKbTf0v0WUVdp56Pio3obPuCc3W7836JGldoLS0+Oe3GxV6H6hHtn4raDHVdoJSpC37MkrJU73t72BFVmiG5ru9+Sik6D7tX6Hwtb722lKTw+RXOgeeuihc889N1+rgGOVYRdffLHDmFvF/WWXXSYeXqreRqaj66+/Hn39/YQWmBk8yrXZWyGdaadRbrtCCBwe6m8jAz6ZM2w4TlxzzTW4uvTSS5389WTdEsllleeff37OnDkXXXRRCJYtW0Yh+cgHnJ0uuOCC888/P2cth5YrrrjCDPm+2iRBRdtAS7t++xlQZlhSvYqczkDPOeeck495CXjJJZdgm8iRItf6npx5HnvsMTrJt1BOaIYA6fLxntmIRsBozKHxwgsvJH45KmeSgtKTRpBHoB02CloI2mHdefPmMUf5HtXVEMd1bOe/5oIf/ehHbjGm323ISiS7Tc+CBQtMlXcZ4LXXXiNd8QdurD137tx8n8KdzjvvPD05fmeSOsOlnf50FpSnKw4HeOxhACfNrgoMTZa8/uVwfuWVVxI23yXpsbprz5944eb222/fbLPNKGXSpElmcdQeP368kUdW/4cYgv333//QQw896aSTxo0bJ7ZR7rnnnmYYPnz4448/jiDnctdqiU8hj+oyWxSLVqFB7XyckGuT4tPIB1fibfPNNz95+e8YAvq99torL4TzyP3220+brx999NGjR4/m91kUn/kWKnqRC9BPmzZt1113Pe6440T1hAkTTjnlFMIKZjSUoN8kJrcEwQ+o/i/sUaNGJYqwGmi3IEqoC7uyiK4wucYaa5QvTkFaiaSYeeGFF/CMf/Y+5JBDdqm+xcmiIjnfQoU9CXrMmDFMOWLEiLPPPlsYnH766TNnzjziiCMM58rmJNpBBx00derU6POYY4459thjzSmqzYmfruziqUd1YUMv9/FU7UpJHT4rKnjnnXf22WcfPnbUUUdpcPRMCPjB+dixY4l22GGH7bTTTvjHmIbwRmB4ieR8NHXLLbewEVNyy8SngTNmzDAVt0Gz7777Epw2dt9995/85Cc0QPbDDz9cPz5jO9eKtU/B5IWxZlflfoitQooQVOJ2aX3pY8qUKVgir0b5TM4k+GFQV+mMHkgdN9YQ3pmwh0g2CwnvuOOOJL8nnnhC0NqZ884NWFgiPHD578KdeOKJs2fPRpOkQpWnnXaaRiSREXkJYolHop04cWJeUbKEp9UEn+Cee+4xPG1sQFcqMJaN+da6665b3toBHrPDDjtwR3rh4oVJmDVrVhG77MnmAaknr7wKWr4iUAvl9OnTca4nt4JE+oyZ3fKGZAR8wk033XTWWWexir0dGbfItN3YcgUhjAXeWmutVV7oheeq/5qUyEwuT3HB5oPqdzATvVAiOcLef//9KVjkQXMmJwL9cBG7Ov9wi1KCIEV550ds178Ttj8IJHEu2QkeUueVJpIaGxqI4FaMd4GnFFKnqePnP/95SgOQiHmLBmIgoxjGD8vusfzn5YBfYT7tEsmcx5X7EVNj4cKFvIXG7DduKQ3n9957Lz9xCyeccAJ7SWq5RVbeguYV/OGMM87Ye++96f/444+nmezhcYOCLHrzzTfLp+lBAF1ZX/4t797LRw8u/1MliUACkmRFMq7q34yKJikp7Z4jOTsVcOKvf/3r1113ncH5gxsgM1cu3/jl3fT6O15CXSNCMvZGG21EoQMGDJBaGGnkyJFJ7RV5E/xJGEgHfIuLMFg38oOnCgHBzPOKi4AhMq5qIn/uk7c+GylheVoNVyWS3aYnENKyNUllcbdyE6fhwXEOoDvuVWR31rAnaMQvxYw8Igmuvfba+vNdpfnjiNWIzwJjVbZODZJmfU8mlFRFWImGsPkmo54io8BSXaMvcQuckotEfKGOTIOb5uVqUKRw2QQ2aNS/k7c5UAWv/epXv8pxTz311ORNq9QNh3j+/Pk2ky233JJC1Due9qgNITekQr53Cb1YIqyUIds+UP3cNHGKZbNoieTKsJ9YlgPHphzVcG7G4SW1+CrIyKxWgoRKkzRNax6lH81Q/mqrrebcQVd5tw9jdWHxQ5OTJ0/mBtzYdmosgjpNR3B4o9CbMLBxDhw4ELcsm5cmRGWLG/cQyZmo6m/8lzGyMt3hu+yWxjNwPBjsPxJY0Ygkmh0s3Nsw8w6aIYsWLdKQZpLP6uIxmOJBWsK9+dlbZzfyN3RTPY0PlR4grQJSnEscOWYUiegiKqhHMvp02smF8eLFi5FJVTTL9ttss43O/KggRHYbdW65psShkRnoJOY3lm0kAmV5fBFjrnXwRaWNHJdbHLbTBKVfPNQjGRz2zKMqs0e1nGNLSNcjuQhrk5ehoh892rdV/5k4QxfnaIlk2kgkZ367Wao22UqPTc8kbs0WggAPUoP9cP3116c3uVJnnaAFeSTXS4hmzt/VhWd4+OGHPZIyyoYZGYuw9UjWmdn4g2KKlhjXFkfSq6++WhoSbMlfkEhm0NyiTzlgBkrjtLaNFMM6lajJ5oWxgK0VZdtttx03Vq8tXbpUZzfChmc7sNmifz1RIOZt0VyIG5c/H8hy/DMDe4jkTOTMwLOrp40gdHJISgP+RFkldHk589sDCez2suW/Ph0BxGc2c4qjUFUN526P5LTprvzVUfcgSYThW2HMDHrqc1JlSTeAT1pOu0SyIdGOHY8UpNaWAulO3uHoshLNlNCVKZ0dSgFS8lSYEdX5kExqk4zYPpEc3hoDahCTPJIlMOBpcbt2FCbZu0Qy4jq9qeTc5k31m6959Q9KJKOPjRScjv35qBIUtGImH2QSp2iJiRm6FCDsng/Jsi4P42oYM9bJ8O7lv5Ib/2kMqJC2wCsO0z2wkSgFG76UqtGiHE4l0po31cttxW1KJBeliV7baaRTPJezGBWxV4lkZnWWNnNulZnZ9qM0dmRQUJPrlAKkOQ2rQGNADTbtEiw9QkQgdq7MreXqkgIfrn8SZN+K60LPkewqaalA+KVleAnb2zDVHmZRVrGcLMXkmFYti3lmjscMGzYsf4QVCZX1kcqmwfD4VttwcezWVaBNX7Kmk0OLJB0Reg31f+qcdKYRiEbZkfHU7Wg23XRTgRqa+p6sh09jm20cDe68804F0vbbb28USxsuLyqWFNK0Rgn2BLKYwUmBivLJeaZVrCbSHF+feeYZxdL48eM7RnKUHHjUTlAH4ggrGFL+tavosccey+vHqZOVEinVPCqRbB4DKUGtyN0JGwdyVOO4mVPy4tAiluGIKQDIIkcQn6EZDk0Y9pSh7Q90YlexhYrt8lQjcIt5BFyone12OBxSGt91puNp+cy5ri5wjnCMFJ9sJAId3HASYeuR7KrkISzDqZWEtOM6ceQ4biMBUdGECRMojRtzS9pw5fnS2bjlf8RmHg2j5HeRrLjQaetOCvA0CwXaWMVejofN3q5BLWa2C7IF8DQqatESiwwdOpRQRJB/uTFOQtNDJIcbDbbhOnIAgd0qpXgqd09JJuTMS56kLnnd3itT3nrrrZYxg3k07rrrLvNocA6hxag2bQI0FFBTQYaEv1y7B5rMf99995U/Qq5PGOCKpWUibOeXiRISLZHMudUdaCKvftzaDRwc7AZuxYlUZWfOpi3yzUB2B60yiQa3Uz1qi2ceKQw0zFAIAqyGW/AI3DafdQKeUaKxR3FHPR3phYqEpYhwTaUd5uuR7GrzJKydFiUn1ikZCYmwhEBUMLQ4yabtKWLI0pgBxDyeDxguuchW3CufVFVifUrYctuR7XaIBFZgC/IaW5+hgG5nzZpFEFsr6+jBlWu9ujaK4PlcQ72QJGvDpxA5OqUvr+DG5HU6cGuz8VRPvaClRsFvm2HTVDpUkQ9uWxhzm/hPO41uILLUd9iz6EknnZSXRk0LIQjslJ6yV2E7puwcyc4JieT/CxDeLSrox+DrOb33Blp87ncOual8qPE7RN+oRSSXjyeDRiSrN1TkEpsM1BHdPOoGn21UrwJLdi3npT7g7XcuPgZsbkqM5v1y9AZjvw/CCmOVeTsn3fC2Umz/zmUMsAGKxHJmDhqRrDQaOHDg5MmTHYD7N/bcc09npyFDhmg0u/ovyOhkNWzYMMdaaPb2UxB20KBBW265Zb+3rDiFLbbYwrEoMRx8TtmtvncucgZWiPdvPP/8805BhNVodvVfMKjDGHn/LwhLRmYFh/ZmV/8FGUlqf64fyD/3+3baWYVVWIXPgEZ1vQqrsAp/6FgVyauwCv0BqyJ5FVahP2BVJK/CKvzh4+OP/z91Xv0N/hyI7gAAAABJRU5ErkJggg=="

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care din următoarele sondaje de temperatură măsurate la ora 02:00 indică prezența unei zoterme")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "1"))
_question.answers.append(Parag_Model_Answer(False, "2"))
_question.answers.append(Parag_Model_Answer(False, "3"))
_question.answers.append(Parag_Model_Answer(False, "4"))
_question.image = "iVBORw0KGgoAAAANSUhEUgAAAUMAAABbCAIAAABmo3ASAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAE++SURBVHhe7d1nsF3VeTdwTz5lEqc7mYydfEg8ZhLbMxibamOaRJcQEpIoKkgCJBDI9CpCk0QzECCiSEQ4KIjeDaEYjGiiFyFRDKJIVGNMM2Cw88L7O/t/tNicc+69Eva9tm/0n9Getdd+1lpPX886Z9+jz/3v//7vRx999PEqrMIq/EHh/1Vo3nz88eeE8Ycffvjyyy8///zzL7zwwrJ+jeeee+6VV1556aWXCNvs6r9YunTpq6++Gss2u/ovyEhSxv0/YlmS/vrXv/5UJPt33XXXbb755rvvvvvkyZP36NfYc889t9hii8GDB2s0u/opmHKvvfYaOHDgiBEj+r2wQNhBgwZttdVWGs2u/gvGFbA33nij4C0FdSOSzz333OOOO06I25z7DFm+ND744IP09yrIeMIJJ5xzzjl9IOyvfvWrNCIgpJ0iqA/kJeOhhx565ZVX9o1lSeSkFkk19BRh+wBkPOOMM0466aS+ETYgcuTVdo3UfQAyzpgx47//+78t2hrJp556au77DK+99toTTzyh8fTTTyt609kHOO200+bOndu86U0Utybg//zP/6j6tB977LGf/vSnGsUAvYojjjgimbu3UcS544475s+fn/aiRYveeeedtPsA3FgwN296GUVeBmVfjYcffrgEdh9AzkokFzQi+Qc/+MG///u/5773QHhlfVQgdP/1X/912LBh2rNnz95www1/+ctfepSnvQqS/td//VfzpjcRu86ZM+cf//EfCfvlL3954cKF06dPV+6GoA+E/bd/+zdJpHnTmyCLvUIZ//nPf/5LX/rSpEmT3O62227qQE+VJyHrVfznf/7nf/zHfzRvehPcOGnaefVv//ZvR48era22P/HEE/MUGnS9ie9///u/s0iGSHjTTTd98Ytf/NznPjdy5Ei3L7/88he+8IVLL720Iul19E0kV0npI1WQY/nUqVO59T/8wz9MnDjRzvynf/qnCxYsQNMH9u6bSI6wb7/9thLg9ttv52R/9Ed/9Morr1x//fV/8zd/s2TJEk+bpL2JvolkspRqSwxz47Fjx2qffvrp//zP//zGG29o9/9IjkUVt47lm2222eDBg9O/zTbbSGlp9zb6JpLZUhgzeXZmAfznf/7ntK+97rrrTpkyRaMP/LtvIjlixn3vu+++P/uzP/ve976nrbT+yle+csopp1RUvY4+i+QYTi05ZMiQ9dZbLxsSE//FX/zF5Zdfrt3/I7mOTTfddKuttkp7jz32+Kd/+qe+qcH6JpIhwazx7LPPKrCdIN566y23W2655cCBAyuSXkefRTLEv3/2s585rArgW265xa1jhRq7oup19E0kJ0oXLVq0wQYbKDdsSDkuvfvuu3/yJ38ybdo07aiiV/F7FMkDBgwokczYjpF9kMmgbyKZLTm3hrMDby6Sgnp7k002ad70MvomkhmOsKrr00477aWXXtLjBHHIIYdo/Mu//Es/i+REKek+//nPM6XrX/3VXzlT0IBInj59uqf/t/bkb3/72xtvvHHaO+64I+fug0wGfRPJbBlzqjMdpUSUc9Sdd96pRy6fMGFCRdXr6JtIDmxKDg7f+ta3DjzwwD/+4z++6667lCSrrbZanLsPjNtnezI8+eSTF1988bx58/7+7//+a1/72tKlS19//fW//Mu/PP/885t0vYwuI7nPDjMFxx9//EknnaTxxhtvfPGLX5w1a1b6ext9tie7cmXJe9SoUTvssMPWW2/NzK+++qosfsMNN4SstyGSr7vuuuZNr4GwkXfZsmUyl9Pjtdde6/a2227767/+64ULF4amQdqb6ONzcnDssceeffbZGuedd96XvvQlJVj6exudI/ncc8/t+z25QGKTyPvsuzgVYJ8lznbko77mTe/DfnjTTTc1b/ockyZNksWaN72Pvvw+uR3yl7zZvOl92HpbXotoRLKuww477Lnnnnvqqaee7is8U2HJkiUiGZ599lmdbvO0l0DGqVOnnnDCCRrNrl5GkSgCzpkz55prriE4Vfe2tq04ZcoU/q3RZ5aNXIrPn/zkJ2eeeeaPfvSjCOu2SdE7IKPtUSz1mWWDyLV48WKhdffdd0d8yNPegMmff/55td4FF1wgeEuB0IjkSy65ZL311uv7t3MnT55s0X333Xf//ffX3m233ZoPeg2W+853vuNMrmHFZm8vIwtFvfvttx9h++YVdyuuueaagwYN6stXke3DpAONAw44QLGdzjztPRB24403Xn/99aPnvkFdLmaVN5s3vQwyCtirrroqMRw0q+u+f1uzHfXjR+9Bde1I07zp7zjyyCOvv/765k1/xw9+8IPfYXUd8OF80tnbOPnkk1sOic1PvDqekxtH+yq6lBBXXHHFlVdeeeutt+aRxg9/+MNf/OIXuX3ooYcQ/PznP9eOJK4Z/uvqb6/ymgSksxr0CQpx874NefTiiy++9tpr2q+88gpmrr766htvvDE8hEAbV2gaYz7++J577sHV7bffntvQkLQ9kjFWDECWyy67zPyGu8W5YFAlaoRgwYIF1157bd4oDue5RrpKykYjE2qXmQOPQuba7Po0Qq+CevPNN0OzaNEiddPrr7+uHX1qEJMG3n33XW1kxLz88svvuusut+lxVW12H8lqUandPAQ0xGxEu+222zyyirUcs+GDDz7wVI9rGNAoPYWYUNWsnyBPe4SKsegTOBLxy8yuv/zlL1lWZ4P6448feeQRwv74xz+OUbKuk8vMmTOr559Cg9Fqqscff5xl4xLpvOWWW+jH5J5iwBLmrAY1RrWIE94Cj7J0Afq8EOFpetqBxtWBK7p66aWXaJ6n0fD777+fGQznxvp/9rOfZdSdd95J2DvuuCO3mX8l3rs2bxa2xvDhww888EDHy3zCPG3aNPv74Ycfroj68MMPDd95552POOKI0aNHxwARtZqmFXlUlxZ9eiJGs7cNb7zxxoYbbkjX2vvss8+YMWPsruQhcMVpY1GHh2233VYxySqceLvttrMpqd7xWcK7/bPrjA3DcsRmm2121FFHTZ8+XfDwYFWTaRWKgPK4445T3hDWWYDD6enowYF+QqFp3i/3hqwIzd42OFtusMEG999/v7bTprVIwQrLli3LbEJOfT506FBivv3224rY7bffPnZhKa4QMk/bv4XK6ho4ZzLq+v73v3/WWWfJFBTFrCaZMWMGAoI7Dhx88MF777133J1EdXEKdJrNtPWn2rFsrs3eNhBzo402Wrp0afP+44+33nprGtYoo5yBWXbChAksazsiOD5ZZNdddy066eqz61iHlow69NBDubEi1MyWIN1hhx3GnWwSdDh16lTaYH0TApqObytFIsi6gbYej7rxB+DA3BiNNm3vsssuDthA+VnRI7bGKq7wjD12P/roo5mAXeJyxq7E98mZVyMfnNigHn30UbcyiuVjV7qYN28eFeTDd6GVpIgbwx9++GG5RCxdc801N9xww0EHHWS787RdBa733nsv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"

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce presupune condensarea?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Trecerea din stare lichidă în stare solidă"))
_question.answers.append(Parag_Model_Answer(False, "Trecerea din stare lichidă în stare gazoasă."))
_question.answers.append(Parag_Model_Answer(True,  "Trecerea din stare gazoasă în stare lichidă"))
_question.answers.append(Parag_Model_Answer(False, "Trecerea din stare gazoasă în stare solidă"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care din următoarele schimbări de stare necesită energie sub formă de căldură? ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Trecerea din stare lichidă în stare solidă"))
_question.answers.append(Parag_Model_Answer(True,  "Trecerea din stare solidă în stare lichidă."))
_question.answers.append(Parag_Model_Answer(False, "Trecerea din stare gazoasă în stare lichidă."))
_question.answers.append(Parag_Model_Answer(False, "Trecerea din stare gazoasă în stare solidă."))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care din următoarele schimbări de stare necesită energie sub formă de căldură? ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Trecerea din stare lichidă în stare solidă."))
_question.answers.append(Parag_Model_Answer(False, "Trecerea din stare gazoasă în stare lichidă."))
_question.answers.append(Parag_Model_Answer(False, "Trecerea din stare gazoasă în stare solidă."))
_question.answers.append(Parag_Model_Answer(True,  "Trecerea din stare lichidă în stare gazoasă."))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care din următoarele schimbări de stare cedează energie sub formă de căldură? ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Trecerea din stare lichidă în stare gazoasă"))
_question.answers.append(Parag_Model_Answer(False, "Trecerea din stare solidă în stare gazoasă"))
_question.answers.append(Parag_Model_Answer(True,  "Trecerea din stare gazoasă în stare lichidă"))
_question.answers.append(Parag_Model_Answer(False, "Trecerea din stare solidă în stare lichidă."))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care din următoarele schimbări de stare cedează energie sub formă de căldură? ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "Trecerea din stare lichidă în stare solidă"))
_question.answers.append(Parag_Model_Answer(False, "Trecerea din stare solidă în stare gazoasă"))
_question.answers.append(Parag_Model_Answer(False, "Trecerea din stare lichidă în stare gazoasă"))
_question.answers.append(Parag_Model_Answer(False, "Trecerea din stare solidă în stare lichidă."))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care din următoarele schimbări de stare cedează energie sub formă de căldură? ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Trecerea din stare lichidă în stare gazoasă"))
_question.answers.append(Parag_Model_Answer(False, "Trecerea din stare solidă în stare gazoasă."))
_question.answers.append(Parag_Model_Answer(False, "Trecerea din stare solidă în stare lichidă"))
_question.answers.append(Parag_Model_Answer(True,  "Trecerea din stare gazoasă în stare solidă."))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Termenul de ”punct de rouă” este definit în meteorologie ca fiind")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "temperatura specifică substanței la care se face trecere din stare solidă în stare lichidă"))
_question.answers.append(Parag_Model_Answer(True,  "temperatura la care trebuie răcit aerul ca vaporii de apă să îceapă să condenseze"))
_question.answers.append(Parag_Model_Answer(False, "cantitatea de umiditate din aer când este atinsă temperatura de condensare"))
_question.answers.append(Parag_Model_Answer(False, "temperatura radiației solului de pe timpul nopții necesară ca să apară condensarea pe solul rece"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cât de mare este gradientul temperaturii al aerului saturat (umed) în România în nivelele joase ale troposferei?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "< 1°C / 100 m"))
_question.answers.append(Parag_Model_Answer(False, "1,0°C / 100 m"))
_question.answers.append(Parag_Model_Answer(False, "1,5°C / 100 m"))
_question.answers.append(Parag_Model_Answer(False, "> 2°C / 100 m"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce are cea mai mare influență asupra gradientului temperaturii aerului saturat (umed) în timp ce acesta se ridică?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Umiditatea relativă."))
_question.answers.append(Parag_Model_Answer(True,  "Volumul de vapori care condendează."))
_question.answers.append(Parag_Model_Answer(False, "Diferența temperaturii bulei și temperaturii aerului din jur"))
_question.answers.append(Parag_Model_Answer(False, "Intensitatea radiației solare."))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("De ce aerul saturat (umed) care se ridică se răcește mai lent dacât aerul nesaturat (uscat) care se ridică.")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Pentru că apa se răcește mai lent de cât aerul"))
_question.answers.append(Parag_Model_Answer(True,  "Pentru că aerul saturat (umed) se ridică mai repede , răcirea este ușor întârziată"))
_question.answers.append(Parag_Model_Answer(True,  "Pentru că energia eliberată prin condensare influențează masa de aer care se ridică."))
_question.answers.append(Parag_Model_Answer(False, "Pentru că vaporii de apă sunt mai ușori ca aerul, prin urmare aerul saturat (umed) care se ridică are nevoie de mai puțină energie sub formă de căldură"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce formă de nor este un semn de termici bune?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Cirrus"))
_question.answers.append(Parag_Model_Answer(True,  "Cumulus"))
_question.answers.append(Parag_Model_Answer(False, "Stratus"))
_question.answers.append(Parag_Model_Answer(False, "Lenticular"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Apariția norilor altocumulus castellanus la două ore după răsărit indică")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "un strat instabil de aer la înălțimea norilor"))
_question.answers.append(Parag_Model_Answer(False, "apropierea unui front cald."))
_question.answers.append(Parag_Model_Answer(False, "centrul unui anticiclon"))
_question.answers.append(Parag_Model_Answer(False, "o regiune mare de stabilitate în straturile de jos ale troposferei"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Vreme însorită la altitudini mai mari  cu ceață la altitudine mică în același timp înseamnă")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "un nivel mic de stabilitate în partea de jos a troposferei"))
_question.answers.append(Parag_Model_Answer(False, "un front rece care se apropie"))
_question.answers.append(Parag_Model_Answer(False, "centrul unu ciclon"))
_question.answers.append(Parag_Model_Answer(True,  "un nivel mare de stabilitate în partea de jos a troposferei."))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Pentru care din următoarele condiții meteorologice este cea mai probabilă formarea ceții la sol (ceață de radiație)?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Cer acoperit, vânt zero, diferență mică temperatură-punct de rouă."))
_question.answers.append(Parag_Model_Answer(False, "Cer senin, vânt zero, diferență mare temperatură-punct de rouă"))
_question.answers.append(Parag_Model_Answer(True,  "Cer senin, vânt zero, diferență mică temperatură-punct de rouă"))
_question.answers.append(Parag_Model_Answer(False, "Cer senin, vânt 270° 10m/s, diferență mică temperatură-punct de rouă"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Norii se formează când")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "se evaporă mari cantități de apă (de exemplu peste ocean)."))
_question.answers.append(Parag_Model_Answer(False, "aerul cald continental este împins peste ocean."))
_question.answers.append(Parag_Model_Answer(True,  "aerul este răcit pânâ atinge punctul de rouă"))
_question.answers.append(Parag_Model_Answer(False, "aerul care se ridică este oprit de o inversiune"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Baza norului este")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "nivelul de jos al norului și este la înălțimea la care temperatura aerului care urcă atinge punctul de rouă"))
_question.answers.append(Parag_Model_Answer(False, "nivelul de sus al norului și este la înălțimea la care temperatura aerului care urcă atinge temperatura aerului din jur"))
_question.answers.append(Parag_Model_Answer(False, "nivelul de jos al norului și este la înălțimea la care temperatura aerului care urcă atinge temperatura aerului din jur"))
_question.answers.append(Parag_Model_Answer(False, "nivelul de sus al norului și este la înălțimea la care temperatura aerului care urcă atinge punctul de rouă"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cum se numește stratul de nori care acoperă cerul și are o altitudine de 4.000 m?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Cirostratus"))
_question.answers.append(Parag_Model_Answer(False, "Altocumulus"))
_question.answers.append(Parag_Model_Answer(False, "Nimbostratus"))
_question.answers.append(Parag_Model_Answer(True,  "Altostratus"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cum se numesc norii care au formă de mici aglomerații cu baza la o altitudine de 4.500 m?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Cirostratus"))
_question.answers.append(Parag_Model_Answer(True,  "Altocumulus"))
_question.answers.append(Parag_Model_Answer(False, "Nimbostratus"))
_question.answers.append(Parag_Model_Answer(False, "Altostratus"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cum se numește stratul de nori care acoperă cerul, are o altitudine de 1.000 m și generează precipitații?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Cirostratus"))
_question.answers.append(Parag_Model_Answer(False, "Altocumulus"))
_question.answers.append(Parag_Model_Answer(True,  "Nimbostratus"))
_question.answers.append(Parag_Model_Answer(False, "Altostratus"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care din următoarele tipuri de nori are baza cel mai sus?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Cumulus"))
_question.answers.append(Parag_Model_Answer(True,  "Cirocumulus"))
_question.answers.append(Parag_Model_Answer(False, "Stratocumulus"))
_question.answers.append(Parag_Model_Answer(False, "Cumulonimbus"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care din următorii  nori nu au partea de sus la același nivel cu ceilalți?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Cirrus"))
_question.answers.append(Parag_Model_Answer(False, "Cirocumulus "))
_question.answers.append(Parag_Model_Answer(True,  "Cumulus humilis"))
_question.answers.append(Parag_Model_Answer(False, "Cirostratus"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cum se numește tipul de nori care generează precipitații?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Cirostratus"))
_question.answers.append(Parag_Model_Answer(False, "Stratocumulus "))
_question.answers.append(Parag_Model_Answer(False, "Cumulus humilis"))
_question.answers.append(Parag_Model_Answer(True,  "Nimbostratus "))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care din următorii nori sunt formați în principal din cristale de gheață?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "Cirocumulus"))
_question.answers.append(Parag_Model_Answer(False, "Stratocumulus "))
_question.answers.append(Parag_Model_Answer(False, "Cumulus humilis"))
_question.answers.append(Parag_Model_Answer(False, "Nimbostratus "))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care din următoarele tipuri de nori indică prezența termicilor bune pentru zborul cu parapanta și deltaplanul?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Cirocumulus"))
_question.answers.append(Parag_Model_Answer(False, "Cumulonimbus"))
_question.answers.append(Parag_Model_Answer(True,  "Cumulus humilis"))
_question.answers.append(Parag_Model_Answer(False, "Lenticularis"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("În apropierea cărui tip de nori este periculos zborul cu parapanta și deltaplanul?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Cirocumulus"))
_question.answers.append(Parag_Model_Answer(True,  "Cumulonimbus"))
_question.answers.append(Parag_Model_Answer(False, "Cumulus humilis"))
_question.answers.append(Parag_Model_Answer(False, "Stratocumulus"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Norii lenticulari apar când")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "masa de aer curge peste un teren muntos cu viteză mare"))
_question.answers.append(Parag_Model_Answer(False, "termicile puternice se ridică și se răcesc urmărind  adiabata uscată"))
_question.answers.append(Parag_Model_Answer(False, "aer instabil de la sufrafață se ridică repede"))
_question.answers.append(Parag_Model_Answer(False, "termicile puternice cauzează un efect de foehn"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Norii lenticulari")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "sunt formați exclusiv din apă, niciodată din gheață."))
_question.answers.append(Parag_Model_Answer(False, "apar în România numai pe timpul iernii"))
_question.answers.append(Parag_Model_Answer(True,  "își schimbă foarte puțin poziția în ciuda vânturilor puternice."))
_question.answers.append(Parag_Model_Answer(False, "generează precipitații."))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care din următoarele sunt semne vizibile din depărtare că un cumulus congestius sau cumlonimbus generează precipitații?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "O perdea gri care atârnă sub nor, orientată spre sol. "))
_question.answers.append(Parag_Model_Answer(False, "Dezvoltarea pe verticală a norului este mai mare de cât cea pe orizontală"))
_question.answers.append(Parag_Model_Answer(False, "Urme fibroase de condensare între baza norului și sol"))
_question.answers.append(Parag_Model_Answer(False, "Baza norului are culoarea neagră"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("De îndată ce precipitațiile sunt vizibile sub un nor cumulus congestus sau cumulonimbus")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "ei devin inofensivi pentru parapantele din zona pentru că se află într-o stare de disipare"))
_question.answers.append(Parag_Model_Answer(True,  "aerul va fi răcit de evaporarea apei și vor apărea local vânturi puternice și rafaloase"))
_question.answers.append(Parag_Model_Answer(False, "înseamnă că sub norl nu mai este termică"))
_question.answers.append(Parag_Model_Answer(False, "vor apărea întotdeuna și descărcările electrice"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care din următoarele afirmații este falsă?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Norii cumulus congestus și cumulonimbus pot produce curenți ascendenți sau descendenți cu rafale de peste 30 m/s"))
_question.answers.append(Parag_Model_Answer(True,  "Apariția norilor cumulus congestus și cumulonimbus duce întotdeauna la căderi de grindină"))
_question.answers.append(Parag_Model_Answer(False, "Norii cumulonimbus pot produce bucați de grindină de mărimea pumnului"))
_question.answers.append(Parag_Model_Answer(False, "Norii cumulus congestus și cumulonimbus pot produce, prin evaporare, mari volume de aer rece care se înfundă cu viteze mari până la sol în zonele din jurul norului"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("de la nivelul mării nu e întotdeauna la fel")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "pentru că sunt variații de temperatură pe suprafațata pământului care răcesc sau încălzesc aerul, cauzând schimbări în densitatea aerului"))
_question.answers.append(Parag_Model_Answer(False, "pentru că masele de aer oceanice sunt mai umede și deci mai grele de cât masele de aer continentaleși deci produc o presiune atmosferică mai mare"))
_question.answers.append(Parag_Model_Answer(False, "pentru că masele de aer continentale sunt mai uscate și deci mai grele de cât cele oceanice și produc o presiune mai mare"))
_question.answers.append(Parag_Model_Answer(False, "pentru că presiunea scade o dată cu cresterea vitezei fluxului de aer și vice versa"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("O presiunea atmosferică mărită poate fi întâlnită într-o zonă care")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "este mai uscată decât zonele învecinate, pentru o perioadă mai lungă"))
_question.answers.append(Parag_Model_Answer(True,  "este mai rece decât zonele învecinate, pentru o perioadă mai lungă"))
_question.answers.append(Parag_Model_Answer(False, "primește radiație solară mai intensă decât zonele învecinate, pentru o perioadă mai lungă"))
_question.answers.append(Parag_Model_Answer(False, "este mai caldă decât zonele învecinate, pentru o perioadă mai lungă"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("O presiunea atmosferică mai mică poate fi întâlnită într-o zonă care")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "este mai uscată decât zonele învecinate, pentru o perioadă mai lungă"))
_question.answers.append(Parag_Model_Answer(False, "este mai rece decât zonele învecinate, pentru o perioadă mai lungă"))
_question.answers.append(Parag_Model_Answer(False, "primește radiație solară mai puțin intensă decât zonele învecinate, pentru o perioadă mai lungă"))
_question.answers.append(Parag_Model_Answer(True,  "este mai caldă decât zonele învecinate, pentru o perioadă mai lungă. "))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("În regiunea noastră, presiunea atmosferică la nivelul mării al unui ciclon însemnat poate fi")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "1.035 hPa"))
_question.answers.append(Parag_Model_Answer(False, "1.055 hPa"))
_question.answers.append(Parag_Model_Answer(True,  "955 hPa"))
_question.answers.append(Parag_Model_Answer(False, "915 hPa"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("În regiunea noastră, presiunea atmosferică la nivelul mării al unui anticiclonciclon însemnat poate fi")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "1.035 hPa"))
_question.answers.append(Parag_Model_Answer(False, "1.055 hPa"))
_question.answers.append(Parag_Model_Answer(False, "955 hPa"))
_question.answers.append(Parag_Model_Answer(False, "915 hPa"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Într-un ciclon în emisfera nordică")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "masele de aer se învârt în sensul acelor de ceasornic și se înfundă pe o zonă mare"))
_question.answers.append(Parag_Model_Answer(True,  "masele de aer se învârt invers sensului acelor de ceasornic și se ridică pe o zonă mare"))
_question.answers.append(Parag_Model_Answer(False, "masele de aer se învârt în sensul acelor de ceasornic și se ridică pe o zonă mare"))
_question.answers.append(Parag_Model_Answer(False, "masele de aer se învârt invers sensului acelor de ceasornic și se înfundă pe o zonă mare"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Într-un anticiclon în emisfera nordică")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "masele de aer se învârt în sensul acelor de ceasornic și se înfundă pe o zonă mare"))
_question.answers.append(Parag_Model_Answer(False, "masele de aer se învârt invers sensului acelor de ceasornic și se ridică pe o zonă mare"))
_question.answers.append(Parag_Model_Answer(False, "masele de aer se învârt în sensul acelor de ceasornic și se ridică pe o zonă mare"))
_question.answers.append(Parag_Model_Answer(False, "masele de aer se învârt invers sensului acelor de ceasornic și se înfundă pe o zonă mare"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("O izobară este o linie care unește punctele care")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "au aceeași temperatură redusă la nivelul mării"))
_question.answers.append(Parag_Model_Answer(True,  "au aceeași presiune redusă la nivelul mării"))
_question.answers.append(Parag_Model_Answer(False, "au aceeași înălțime cu o presiune de 500 hPa"))
_question.answers.append(Parag_Model_Answer(False, "au presiune egală pe exa dintre ciclon și anticiclon"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Din distribuția  izobarelor pe harta sinoptică se pot face următoarele previziuni")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "direcția predominantă a vântului și tendința de precipitații."))
_question.answers.append(Parag_Model_Answer(False, "gradientul temperaturii și intensitatea vântului."))
_question.answers.append(Parag_Model_Answer(False, "direcția și intensitatea predominantă avantlui"))
_question.answers.append(Parag_Model_Answer(False, "tendința de precipitații."))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Vântul de suprafață bate")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "direct de la anticiclon spre ciclon"))
_question.answers.append(Parag_Model_Answer(True,  "aproape paralel cu izobarele de la anticiclon spre ciclon"))
_question.answers.append(Parag_Model_Answer(False, "direct de la"))
_question.answers.append(Parag_Model_Answer(False, "aproape paralel cu izobarele de la ciclon spre anticiclon"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Când distanța dintre izobare este mică")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "gradientul presiunii este mai abrupt și este probabilitate mare de vânturi slabe"))
_question.answers.append(Parag_Model_Answer(False, "gradientul presiunii este mai plat și este probabilitate mare de vânturi slabe"))
_question.answers.append(Parag_Model_Answer(True,  "gradientul presiunii este mai abrupt și este probabilitate mare de vânturi puternice"))
_question.answers.append(Parag_Model_Answer(False, "gradientul presiunii este mai plat și este probabilitate mare de vânturi puternice"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Când distanța dintre izobare este mare")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "gradientul presiunii este mai abrupt și este probabilitate mare de vânturi slabe"))
_question.answers.append(Parag_Model_Answer(True,  "gradientul presiunii este mai plat și este probabilitate mare de vânturi slabe"))
_question.answers.append(Parag_Model_Answer(False, "gradientul presiunii este mai abrupt și este probabilitate mare de vânturi puternice"))
_question.answers.append(Parag_Model_Answer(False, "gradientul presiunii este mai plat și este probabilitate mare de vânturi puternice"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Termicele se dezvoltă cel mai bine")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "în centrul unui ciclon, unde masele de aer au tendința să se ridice sub influența acestuia"))
_question.answers.append(Parag_Model_Answer(False, "unde gradientul presiunii este mai abrupt, și aerul rece este suflat în continu pe o suprafață încălzită, eliminând nevoia ca masele de aer termic să coboare din nou"))
_question.answers.append(Parag_Model_Answer(False, "în centrul unui anticiclon, unde datorită cerului senin radiația solară este cea mai intensă"))
_question.answers.append(Parag_Model_Answer(True,  "unde gradientul presiunii este mai plat, aerul poate fi încălzit fără a fi agitat de vânt, și nu există inversiune"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Vântul care bate din direcția 135° este")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "vânt nordvestic"))
_question.answers.append(Parag_Model_Answer(False, "vânt nordestic"))
_question.answers.append(Parag_Model_Answer(False, "vânt sudvestic"))
_question.answers.append(Parag_Model_Answer(True,  "vânt sudestic"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Vântul din nordvest are ununghi de")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "45°"))
_question.answers.append(Parag_Model_Answer(True,  "315°"))
_question.answers.append(Parag_Model_Answer(False, "225°"))
_question.answers.append(Parag_Model_Answer(False, "135°"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Vântul care bate cu 25 kt are ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "15 km/h"))
_question.answers.append(Parag_Model_Answer(False, "25 km/h"))
_question.answers.append(Parag_Model_Answer(False, "35 km/h"))
_question.answers.append(Parag_Model_Answer(True,  "45 km/h"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Un vânt din 270°/10kt este")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "vânt estic cu o intensitate de aproximativ 18 km/h."))
_question.answers.append(Parag_Model_Answer(False, "vânt vestic cu o intensitate de aproximativ 10 km/h"))
_question.answers.append(Parag_Model_Answer(False, "vânt estic cu o intensitate de aproximativ 10 km/h"))
_question.answers.append(Parag_Model_Answer(True,  "vânt vestic cu o intensitate de aproximativ 18 km/h"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care din următoarele afirmații este în concordanță cu prognoza direcției și intensității vântului la 1.000 m altitudine.  1000 m: 070°/15kt, 2000 m: 080°/10kt, 3000 m: 230°/10 kt, 4000 m: 240°/10 kt ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Vânt din sudvest, 28 km/h"))
_question.answers.append(Parag_Model_Answer(False, "Vânt din nordest, 15 km/h"))
_question.answers.append(Parag_Model_Answer(False, "Vânt din sudvest, 15 km/h"))
_question.answers.append(Parag_Model_Answer(True,  "Vânt din nordest, 28 km/h"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Avem progoza direcției și intensității vântului pentru planoare: 070°/15kt, 2000 m: 080°/10kt, 3000 m: 230°/10 kt, 4000 m: 240°/10 kt La ce nivel este un vânt  de forfecare sesizabil?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Între 1.000m și 2.000m"))
_question.answers.append(Parag_Model_Answer(True,  "Între 2.000m și 3.000m"))
_question.answers.append(Parag_Model_Answer(False, "Între 3.000m și 4.000m"))
_question.answers.append(Parag_Model_Answer(False, "Pe toate nivelele"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Dacă comparăm vântul de suprață cu vântul de la 3.000 m ASL pe un teren plat, vântul de suprață este în general")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "mai puternic și mai turbulent"))
_question.answers.append(Parag_Model_Answer(True,  "mai slab și mai turbulent"))
_question.answers.append(Parag_Model_Answer(False, "mai puternic și mai puțin turbulent"))
_question.answers.append(Parag_Model_Answer(False, "mai slab și mai puțin turbulent"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Dacă comparăm vântul de suprață cu vântul de la 3.000 m ASL pe un teren plat, vântul de la 3.000 m ASL este în general")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "mai puternic și mai turbulent"))
_question.answers.append(Parag_Model_Answer(False, "mai slab și mai turbulent"))
_question.answers.append(Parag_Model_Answer(True,  "mai puternic și mai puțin turbulent"))
_question.answers.append(Parag_Model_Answer(False, "mai slab și mai puțin turbulent"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Vântul de munte (catabatic) bate")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "în timpul zileli și la vale (în jos)"))
_question.answers.append(Parag_Model_Answer(False, "în timpul zileli și la deal (înspre munți)."))
_question.answers.append(Parag_Model_Answer(True,  "în timpul nopții și la vale (în jos)."))
_question.answers.append(Parag_Model_Answer(False, "în timpul nopții și la deal (înspre munți)"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Vântul de vale (anabatic) bate")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "în timpul zileli și la vale (în jos)."))
_question.answers.append(Parag_Model_Answer(True,  "în timpul zileli și la deal (înspre munți)"))
_question.answers.append(Parag_Model_Answer(False, "în timpul nopții și la vale (în jos)"))
_question.answers.append(Parag_Model_Answer(False, "în timpul nopții și la deal (înspre munți). "))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Când este vânt de vale, putem gâsi termicile")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "în general pe mijlocul văii"))
_question.answers.append(Parag_Model_Answer(True,  "în general pe partea de sus a fețelor văii"))
_question.answers.append(Parag_Model_Answer(False, "pe mijlocul văii cât și pe partea de sus a fețelor văii."))
_question.answers.append(Parag_Model_Answer(False, "nu pe mijlocul văii și nici pe partea de sus a fețelor văii"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Când este vânt de munte, putem gâsi termicile")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "în general pe mijlocul văii"))
_question.answers.append(Parag_Model_Answer(False, "în general pe partea de sus a fețelor văii"))
_question.answers.append(Parag_Model_Answer(False, "pe mijlocul văii cât și pe partea de sus a fețelor văii"))
_question.answers.append(Parag_Model_Answer(False, "nu pe mijlocul văii și nici pe partea de sus a fețelor văii"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Vântul de vale se creează din cauză că aerul")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "se încălzește mai repede în vale decât în munți în timpul zilei"))
_question.answers.append(Parag_Model_Answer(False, "se răcește mai repede în munți de cât în vale când slăbește radiația solară"))
_question.answers.append(Parag_Model_Answer(False, "se răcește mai repede în vale de cât în munți când slăbește radiația solară"))
_question.answers.append(Parag_Model_Answer(True,  "se încălzește mai repede în munți decât în vale în timpul zilei"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Vântul de munte se creează din cauză că aerul")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "se încălzește mai repede în vale decât în munți în timpul zilei"))
_question.answers.append(Parag_Model_Answer(True,  "se răcește mai repede în munți de cât în vale când slăbește radiația solară"))
_question.answers.append(Parag_Model_Answer(False, "se răcește mai repede în vale de cât în munți când slăbește radiația solară."))
_question.answers.append(Parag_Model_Answer(False, "se încălzește mai repede în munți decât în vale în timpul zilei"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Aproximativ de la ce oră este probabil vântul de vale în munții Carpați?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "ora 08:00"))
_question.answers.append(Parag_Model_Answer(True,  "ora 11:00"))
_question.answers.append(Parag_Model_Answer(False, "ora 18:00"))
_question.answers.append(Parag_Model_Answer(False, "ora 22:00"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Aproximativ de la ce oră este probabil vântul de munte în munții Carpați?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "ora 08:00am"))
_question.answers.append(Parag_Model_Answer(False, "ora 11:00am"))
_question.answers.append(Parag_Model_Answer(True,  "ora 18:00pm"))
_question.answers.append(Parag_Model_Answer(False, "ora 22:00pm"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Vântul de vale în munții Carpați")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "e mai puternic în perioada iulie-septembrie de cât în perioada decembrie-aprilie"))
_question.answers.append(Parag_Model_Answer(False, "e mai puternic în perioada octombrie-februarie de cât în perioada iulie-septembrie"))
_question.answers.append(Parag_Model_Answer(False, "e mai puternic în perioada decembrie-aprilie de cât în perioada decembrie-aprilie"))
_question.answers.append(Parag_Model_Answer(False, "are aceași intensitate indiferent de perioada anului"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care din următoarele afirmații este corectă?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Vântul de vale bate mai slab lângă sol și crește în intensitate continuu o dată cu creșterea altitudinii"))
_question.answers.append(Parag_Model_Answer(False, "Vântul de vale are aceeași intensitate la 50 m deasupra solului cu intensitatea de la 800 m deasupra solului"))
_question.answers.append(Parag_Model_Answer(True,  "Intensitatea vântului de vale crește o dată cu scăderea altitudinii"))
_question.answers.append(Parag_Model_Answer(False, "Vântul de vale e cel mai puternic la  aproximativ 500 m deasupra solului și se reduce deasupra și sub acest nivel"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("În care din următoare condiții este cea mai probabilă apariția vântului de vale în zonele alpine?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "30 decembrie, 14:00pm, cer fără nori"))
_question.answers.append(Parag_Model_Answer(False, "30 iulie, 14:00pm, cer acoperit total"))
_question.answers.append(Parag_Model_Answer(True,  "30 august, 15:00pm, acoperire 3/8 până la 5/8 cu nori cumulus"))
_question.answers.append(Parag_Model_Answer(False, "30 iunie, 20:00pm, cer fără nori"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Termenul de ”turbulență mecanică” descrie, din punct de vedere al meteorologiei, mișcarea maselor de aer cauzată de")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "bule de aer cald care se desprind de sol și se ridică"))
_question.answers.append(Parag_Model_Answer(True,  "o masă de aer care se mișcă aproape de sol și care este perturbată de teren, case, pomi, etc"))
_question.answers.append(Parag_Model_Answer(False, "echipamente tehnice cum ar fi aeronavele care se mișcă în masa de aer"))
_question.answers.append(Parag_Model_Answer(False, "frecarea a două mase de aer alăturate care de deplasează în direcții diferite sau cu viteze diferite"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Termenul de ”tubulență de forfecare” descrie, din punct de vedere al meteorologiei, mișcarea maselor de aer cauzată de")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "bule de aer cald care se desprind de sol și se ridică."))
_question.answers.append(Parag_Model_Answer(False, "o masă de aer care se mișcă aproape de sol și care este perturbată de teren, case, pomi, etc"))
_question.answers.append(Parag_Model_Answer(False, "un flux de aer care este separat în straturi de către un obstacol"))
_question.answers.append(Parag_Model_Answer(True,  "frecarea a două mase de aer alăturate care de deplasează în direcții diferite sau cu viteze diferite"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Termenul de ”tubulență termică” descrie, din punct de vedere al meteorologiei, mișcarea maselor de aer cauzată de")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "bule de aer cald care se desprind de sol și se ridică"))
_question.answers.append(Parag_Model_Answer(False, "o masă de aer care se mișcă aproape de sol și care este perturbată de teren, case, pomi, etc"))
_question.answers.append(Parag_Model_Answer(False, "două mase de aer care, freacându-se între ele, se încălzesc și se ridică "))
_question.answers.append(Parag_Model_Answer(False, "frecarea a două mase de aer alăturate care de deplasează în direcții diferite sau cu viteze diferite"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("La ora 14 pm într-o zonă montană, zi de vară, cu vânt general de nordvest de după trecerea unui front rece, vântul de vale are intensitea de 25 km/h pe fundul văii. La ce fel de turbulență ne putem aștepta în mijlocul văii la 500m deasupra solului?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "turbulență mecanică"))
_question.answers.append(Parag_Model_Answer(False, "nici un fel de turbulență"))
_question.answers.append(Parag_Model_Answer(False, "turbulență de inversiune"))
_question.answers.append(Parag_Model_Answer(True,  "turbulență de forfecare"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("La ora 14 pm într-o zi de vară, vântul de vale are intensitea de 25 km/h pe fundul văii. La ce fel de turbulență ne putem aștepta în mijlocul văii la 20m deasupra solului?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "turbulență mecanică"))
_question.answers.append(Parag_Model_Answer(False, "nici un fel de turbulență"))
_question.answers.append(Parag_Model_Answer(False, "turbulență de gradient"))
_question.answers.append(Parag_Model_Answer(False, "turbulență de forfecare"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce tip de turbulență putem întâlni în văile alpine cu vânt puternic de vale, pe o față sudică, la o altitudine de 2000m ASL, într-o zi de vară la ora 13:00pm")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "turbulență mecanică"))
_question.answers.append(Parag_Model_Answer(True,  "turbulență termică"))
_question.answers.append(Parag_Model_Answer(False, "turbulență de gradient"))
_question.answers.append(Parag_Model_Answer(False, "turbulență de forfecare"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Când ne putem aștepta la cele mai puține turbulențe, într-o zi cu vreme frumoasă de iulie, în văile alpine în care este de obicei vânt puternic de vale")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "În jur de ora 9 am"))
_question.answers.append(Parag_Model_Answer(False, "În jur de ora 11 am"))
_question.answers.append(Parag_Model_Answer(False, "În jur de ora 13 pm"))
_question.answers.append(Parag_Model_Answer(False, "În jur de ora 18 pm"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Când ne putem aștepta la cele mai puternice turbulențe, într-o zi cu vreme frumoasă de iulie, în văile alpine în care este de obicei vânt puternic de vale")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "În jur de ora 9 am"))
_question.answers.append(Parag_Model_Answer(False, "În jur de ora 11 am"))
_question.answers.append(Parag_Model_Answer(True,  "În jur de ora 13 pm"))
_question.answers.append(Parag_Model_Answer(False, "În jur de ora 18 pm"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Când ne putem aștepta la mai multe termici și cele mai puține turbulențe de forfecare, într-o zi cu vreme frumoasă de iulie, în văile alpine în care este de obicei vânt puternic de vale. ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "În jur de ora 9 am"))
_question.answers.append(Parag_Model_Answer(True,  "În jur de ora 11 am"))
_question.answers.append(Parag_Model_Answer(False, "În jur de ora 13 pm"))
_question.answers.append(Parag_Model_Answer(False, "În jur de ora 18 pm"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce se înțelege prin ”masă de aer”?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "Un corp de aer cu aceleași caracteritici"))
_question.answers.append(Parag_Model_Answer(False, "Greutatea unui metru cub de aer la temperatura de 15°."))
_question.answers.append(Parag_Model_Answer(False, "O zonă cu o concentrație mai mare de aer în centrul unui anticiclon"))
_question.answers.append(Parag_Model_Answer(False, "O parte a atmosferei cu aceeași densitate a aerului"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("În ceea ce privește dezvoltarea frontală, masa de aer este definită ca fiind caldă atunci când temperatura acesteia este mai mare decât ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "15°C la nivelul mării cu 1013,2 hPa"))
_question.answers.append(Parag_Model_Answer(True,  "temperatura maselor de aer din jur"))
_question.answers.append(Parag_Model_Answer(False, "temperatura medie pentru sezon"))
_question.answers.append(Parag_Model_Answer(False, "temperatura care a avut-o de unde provenit masa de aer"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("În meteorologie, se descrie termenul de 'front' ca fiind")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "linia de separare la nivelul mării dintre două mase de aer"))
_question.answers.append(Parag_Model_Answer(False, "o linie de zone de precipitații"))
_question.answers.append(Parag_Model_Answer(False, "o zonă de precipitații cu vânturi mari"))
_question.answers.append(Parag_Model_Answer(True,  "suprafața de separare dintre două mase de aer diferite"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care afirmație este adevărată?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Trecerea fronturilor calde și reci începe la altitudine mare și apoi la nivelul solului."))
_question.answers.append(Parag_Model_Answer(False, "Trecerea fronturilor calde și reci începe la nivelul solului și apoi la altitudine"))
_question.answers.append(Parag_Model_Answer(True,  "Trecerea unui front cald are loc la început la altitudine, apoi la nivelul solului. Trecerea unui front rece are loc la început la nivelul solului, apoi la altitudine"))
_question.answers.append(Parag_Model_Answer(False, "Trecerea unei front cald are loc la început la nivelul solului, apoi la altitudine. Trecerea unui front rece are loc la început la altitudine, apoi la nivelul solului"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care afirmație este adevărată?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Un front cald se mișcă mai repede decât un front rece"))
_question.answers.append(Parag_Model_Answer(False, "Fronturile calde și reci se mișcă la aproximativ aceeași viteză"))
_question.answers.append(Parag_Model_Answer(True,  "Un front rece se mișcă mai repede decât un front cald"))
_question.answers.append(Parag_Model_Answer(False, "În timpul iernii, frontul rece se mișcă mai repede, iar vara, frontul cald se mișcă mai repede"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care ordine a tipurilor de nor este tipică pentru trecerea unei front cald?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Cumulus, cumulus congestus, cumulus calvus, cumulonimbus"))
_question.answers.append(Parag_Model_Answer(False, "Altocumulus, stratocumulus, altostratus, nimbostratus"))
_question.answers.append(Parag_Model_Answer(True,  "Cirrus, cirstratus, altostratus, nimbostratus"))
_question.answers.append(Parag_Model_Answer(False, "Lenticular, cumulus congestus, cirocumulus, altocumulus"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cum arată de obicei vremea cu o oră înainte de sosirea unui front cald? ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Cer albastru, fără vânt, turbulențe nu prea mari, briză constantă la decolare, termici bune, largi și line, cumulus congestius și cumulonimbus în depărtare"))
_question.answers.append(Parag_Model_Answer(False, "Cerul este acoperit 5/8 cu cumulus, vânt puternic, termici putermici cu înfundare puternică în jurul lor. "))
_question.answers.append(Parag_Model_Answer(True,  "Vizibilitate slabă, baza norilor scăzută, ploaie, vânt constant"))
_question.answers.append(Parag_Model_Answer(False, "AAAANori acoperă munții din depărtare, nori cumulus și lenticulari în porțiunea albastră a cerului, schimbări de direcție de vânt pe pământ, vânt puternic de sud-vest la decolare.A"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce semne indică fohn-ul de sud pe partea de nord a Alpilor?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Cerul albastru, fără vânt, turbulențe mici, vânt constant la decolare, ascendență uniformă pe suprafețe mari, cumulus congestius și cumulonimbus la orizont."))
_question.answers.append(Parag_Model_Answer(False, "Cerul este acoperit cu 5/8 cumulus, vânturi puternice crescânde, termici puternice cu înfundări mari în jur"))
_question.answers.append(Parag_Model_Answer(False, "Vizibilitate proastă, bază norilor joasă, ploaie și vânt constant"))
_question.answers.append(Parag_Model_Answer(True,  "Munții de pe orizontul sudic au nori în jurul lor. Există nori cumulus și lenticulari în partea albastră a cerului. Vântul la sol vine din toate direcțiile și e preponderent din sud-vest la locul de decolare"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Vremea de după front este ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "între fronturi calde și reci"))
_question.answers.append(Parag_Model_Answer(False, "pe partea protejată a Carpaților în timpul vântului puternic nordic sau sudic"))
_question.answers.append(Parag_Model_Answer(False, "după trecerea unui front rece."))
_question.answers.append(Parag_Model_Answer(False, "după trecerea unei zone de precipitații"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Un front oclus apare când ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "un front cald depășește un front rece la altitudine"))
_question.answers.append(Parag_Model_Answer(False, "un front rece trece peste un front cald la altitudine"))
_question.answers.append(Parag_Model_Answer(False, "un front cald depășește un front rece la nivelul solului"))
_question.answers.append(Parag_Model_Answer(True,  "un front rece trece peste un front cald la nivelul solului"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Un front oclus are")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "caracteristicile unui front cald"))
_question.answers.append(Parag_Model_Answer(False, "caracteristicile unui front rece"))
_question.answers.append(Parag_Model_Answer(False, "caracteristicile inofensive ale unui front cald și rece, pe măsură ce ambele se neutralizează reciproc"))
_question.answers.append(Parag_Model_Answer(True,  "caracteristicile meteorologice ale unei front fie cald fie rece, în funcție de temperatura fluxului de aer rece"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce reprezintă următoarea imagine?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Un front cald"))
_question.answers.append(Parag_Model_Answer(True,  "Un front rece"))
_question.answers.append(Parag_Model_Answer(False, "O ocluzie cu caracteristicile unei front cald"))
_question.answers.append(Parag_Model_Answer(False, "O ocluzie cu caracteristicile unui front rece"))
_question.image = "iVBORw0KGgoAAAANSUhEUgAAAUcAAACYCAIAAAD4NLxyAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAFiUAABYlAUlSJPAAAJgqSURBVHhe7f0H3BZFsr8Pq5hzwBxAMQfEhDmsAXPErLhgXMWEOWLAiDliRlTUNYtZzAkDBswJdc1ZYV3dPed3dt9r+uq7mDvysHvO8+r+9/v5MFRXV1f39HR1Vc3MPc9Ef/3rX3/66ae///3v/+///b//+Z//gfjHP/4BEYAj4JcBp1zbDFm6WmegXJUbJFi0Sg5QWKQWtYCPWC5UYNsaqKSMMhPats7Jf//3f//Xf/3X3/72N4oCZlJTTJoEMoCiYtIKSACU2DCYUSWKLqsHbNEhRRHEIOMYMv8EWrelVuRyc8RIIAK2BbmcoHxbkBtUmkBkdQky24jcphq5LsFiubtmsC2AVr4MBaJKyfbERPyje1ahg4gBBZJYA1ClfGtk6WqdAavSuVepsmiVHKCwyKxqyE/KxsGqGqgkAKdG0rZAAcwPm4RvsS3QYrOWtEE4ybk6Ab4cZaAbAgGJkJFj0WPI/BNo3ZZakcvN0XAktgW53AbkBgmZVVFLF/KFVW1EblONXJdgkS48kRawrcisashXj2LtiYk8B6gJHUTIt0aWbok0hCpVFq2SAxRuDcSSsnGIhklHhhxBEbGga2r/8pe/BAfL/Pbbb++6667jjz/+uOOO+8Mf/nDCCSf079//nHPOGTJkyNNPP03ggxj2r3xD4MxRyDGXK6jpVwQTAng6QI7FOMei4p9C67ZF9wm53Bzl2W4N5ZshC9UB/SAXEnKDtiG3qUauS7BoL3KawbatgVjNaNsNhVU7UCCda1qiLN8auUFzIIOeGlUWqS3zQz7oelCVlFUh11W0eaSoO7Vq7NixP/74ozT8MWPGfPfddw888MB666238sorn3XWWZdddtkee+wx77zzTtQcSK6++urdunXbfffd//jHP95zzz0PP/zw888/f/fdd19//fUnnnjiOuuss8EGG2y99dbdu3fv0aPHhRdeeMkll7BNFOH7f/83W8bnn3/+5ptvMpKXX375mWeeCffOEThyIKfmdIqKCkKy7Shrq9Fco7wZyvKtoXwzZKE6oB/kQkJuUAdHImwFEfK2FXICCoNcboLcuDmQUU8uty8mcpSBzB4fsnQbkBs0BzL1kyjHWsUCqb6pWmvxliBM4oYbbthvv/0++OADZeqBp+3atev888+/99579+vXD3ruhGysJXTu3LlPnz4XX3wxTW699dY77rjj8ssvP/fcc3HdWOykk07aoUOH6aefPkvXYdppp5144okhZp555sknn1wmWGmlldZYYw2Ud+rUaZZZZll44YWnmWYatD300EMMz5MCMVEyLcZcldGQCacFQpuAjl0vascLOxovsnQTZKE6OLBcSMgNGoHBK5/LlRORCMgJlOXrkdu0AQiHqsxqR/wbWjVtjYGx6mHDhvXs2VPLWWCBBYiWcbnXXHMNbhBfigsdNGgQHliBGWaYQWK55Zb73e9+h3WtvfbaaHjqqaeOPfZYgu2hQ4fiwO2oHj/88ANGfueddz7++ON9+/ZFHuyzzz7QvXv3Puyww+gX13377bcTAhxyyCG47ptvvpnahRZayH5rMMUUU+Cx0ez5emrFyVcXY67KaMiEM15k0UbIEi2RRceHLN0EWagOnBTIhYTW8s1QbqKGgPPWDLlNG4BwqMqsdsSv3arroUAu1IEq2gJC2fXXX1/HiBvcZJNNcI/QOMDJJpsMn5kMJ6NLly5PPvnkZ599hplB0BxVX3755U8//aRagGai9KA5kkVjqIMHDyYWYHe49tpr//SnP8G/7777TjrppCRYCzYaQgbs+eijj8bDE4Fvu+22iy++eB5HBbPPPjuDP//88yPcYEieGkc5UfSY1I9DQyacQKgK4NyUYQZuu+02trz333//l19++fnnn2GqQSTxzJEOyKxBmV8jkxqNQ8NhB6gFuTA+oOdvf/sbp8BGzC7PicD0gpa7KHotwQE0Q27TBiAcqjKrHVHcAxcxjlweH5TPhX8B0W8ZrjDM5vvvv4dAQFDlUchMajLkQxx11FFaCJ7wDwnkuuS0JLRkvxtvvPHmm2+OGydyJq396KOPbB5gQZDcYleHHnoojvrss8/+/e9/v+mmmw4cOBD6L3/5CwIDBgzYcsst8cZbbbUVxx122AH7RGaJJZagd5QwNuNAjJPiCy+8QNCOtkUWWWTddddlGJNMMgkjZKOZc845if+XXnrpAw44gGjirbfe+vjjj7/44otiKAmeF6ok5ERRUATKB3JdNRBzYBxBFv3HP954440tttgiUgMIRsUEErwceeSRzz777Ntvv/3n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"


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce reprezintă următoarea imagine?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Un front cald"))
_question.answers.append(Parag_Model_Answer(False, "Un front rece"))
_question.answers.append(Parag_Model_Answer(True,  "O ocluzie cu caracteristicile unei front cald"))
_question.answers.append(Parag_Model_Answer(False, "O ocluzie cu caracteristicile unui front rece"))
_question.image = "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"

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce reprezintă următoarea imagine?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "Un front cald"))
_question.answers.append(Parag_Model_Answer(False, "Un front rece"))
_question.answers.append(Parag_Model_Answer(False, "O ocluzie cu caracteristicile unei front cald"))
_question.answers.append(Parag_Model_Answer(False, "O ocluzie cu caracteristicile unui front rece"))
_question.image = "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"

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce reprezintă următoarea imagine?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Un front cald"))
_question.answers.append(Parag_Model_Answer(False, "Un front rece"))
_question.answers.append(Parag_Model_Answer(False, "O ocluzie cu caracteristicile unei front cald"))
_question.answers.append(Parag_Model_Answer(True,  "O ocluzie cu caracteristicile unui front rece"))
_question.image = "diVBORw0KGgoAAAANSUhEUgAAAUcAAAB6CAIAAACjuAb7AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAFiUAABYlAUlSJPAAAEIJSURBVHhe7Z13gBVF1vaHDC9JYAkisOQw5AwzhCFnJEcBSYLknEFHguScEZFBERAdQASUoEhSgiTJcQBBJAgSFL/d5fvdfpqy987AAjIwoZ8/+lZVnwpdXU+dc7qr6/rcv3//X//613/+859///vfhF24cBHZ4RMSEiJKc7TTXLhwEZnhc+HCBfgs2GkuXLiIzPD5+eef4TO62rXAXbj4OzCqUUfh7t279+7dU9iZHq7w+NVWYzxQkgsXERmoHz0JsuMRBjSJtnGkef/v//0/qUkCu3bt2rx5840bN55bm31u3brFj1qjJBcuIjJ+//13FCDDNaKNWNrjZfBu3769Z8+eKVOm9PHxGTNmjJ0a/vC5efOmHXThIjIA5kRYJYRChskTJkyYOHFiixYtIDNInjz5yy+//PHHH9tC4Q+fO3fuWLOeB3aaCxfRG8waWNG3b9++du0aUcMOJ0ckozAkOnPmzMyZM/38/OLHjy8yg1SpUg0fPvzs2bPnzp2z5qJ/Y5A7Cwkn+FATPxyfQ2UuXEQKiA6XLl06fPgwAXHEiatXr3KE1atXr+7QoUPu3LkTJkwoJvv7+9eoUQNdjTt95MgRyQuGYn/++WdISIjC4QGfX3/9lR/qM1W6cBHNARfu3bunR04GaOOVK1cuXbq0a9euhQoV2rFjBx5+pUqVYHLixInz5MnTvXv3+fPnh54CnECrf//9961atUqRIoWdFA7wWOB20IWL6IdH6zNOXbly5bvvvmvXrl3q1KmljQUSETh48OCiRYsuXryIR01UlHaWef36dcz48+fPr1mz5s0338yaNauyJ0qUSALhAZ/ffvtNjQB2mgsXURo4t8B4ncY9duKPP/6AjdLM//jHP+BhrFixAgICYCaadsGCBcj8T8pgwI8fP75KlSrJkiUTmdHqdevW7d+//8aNG22hcICPngeYK3ThIspDrHaSefv27R9//DEk3LRp0+TJk2HdzJkzM2bMKCriJ0+bNu2HH35wcoQwkHL2mhdQ4MiXL1+eiUAlvPLKK0wHK1asOHnypC0UnvCR3++y2kU0BGRetmxZ7969pY2TJ08uEoIBAwbgKvfq1Qt6z549m1nAzmMBGovPBn/++SeTwsSJE/39/e0ifHxy5szZoUMHbG+xTIBoZA9XuvnQXM+c41I6ksC9WQ+DNJM6x4tyoQGfYazWhwC83Ny5c8eIESNFihTVq1d/5513bt++jREuYRgrVodWfj/99BNKvkePHobMSZIkqVmz5rBhw3bv3u18aKW2AYXNMtLwgI+mDVXmIoKDUSXT0b1fgmEyfQL3OALSr1y5cuDAAXgFzp8/j/E8ZsyYOXPmIDN//vzChQuLgQDruk+fPnv37r158+aWLVvQtypZUMl25AFIxMaeMmUKeV966SWVg42NWg4ODobnttyLg8/169cVoq0KuIiY8Aze//yH6V8vI10Ao5PhnnMAYwnrAVX8+PGTJk0q4pUuXfr48eMJEyYk0c/Pr1+/fnjRdoYHgNtexrbB5cuXN2/ePGnSJPKqQHR7oUKFsNV37NihZ+ARBJ5VKBoudoKLiArdJoYvCsdOcmGpZZnKjGQCn332Wdu2bcW6rFmzQmms6+LFi2NXb9y4kd7bunUr3GZydH5KZUAJZqYQfv/9948++qhdu3Y5cuRQscwLDRs2HDdu3KFDh7yEASmAouz4i4D9zZYiLiI4IvWdUuM5moBGP4BswJLyLPZYs2YN2u/s2bNKERBA0o5YjnFQUBDGc968eYsVK9a/f//27dsb0zpDhgwYwz///PPOnTuPHDmiKuycDyD6Cc6SAYSH+evXr+/UqVPmzJlVJk44UwMMD70szGRXgKNJeSHw+eWXX/h54e1wEbWhAQa1RCGBsJOr586dGzp0KKpVLEqePHlAQECDBg1q166NxysZhivaePLkyUbMCzB8woQJX3zxxbVr1yhfubzg4bH1hMIIqA1Y0TB51KhRFGKWc6PwO3fuvGrVKixw09QIDp+LFy/yo+tUkgsXzxNQ5dtvv0XryhNOly7diBEj6tatGydOHPEK4M0ePnx40KBBWbJkUQo+bcuWLYcMGbJr1y44jABUX7lypdyTu3fv3r59WyTkCJwEBgoDJC9cuLBkyZIePXoYhzlmzJj+/v7Dhg376quvfvvtN1vUAuU4s0dMuH61i2eMMIcT5Dl58iTs3bdvH1oU7pGyefPmmTNnopDFJYg0Z84czGZlwXJet27dhx9+uHr1arLo1RFmcK1atVCeGNgSCw0RGCtA2pjGhKYipw4ePDhr1qxy5cqZhV8JEiTAYV6wYMGJEydUiEBRxqZQaUqPsPDBhaChgp3mwsXTghEPYYCiUPeDDz7AHc2RI0fs2LFFHrRx6dKlCxYsqCho3Ljx3r17H/0Kd+vWrcuWLUOv/v7770p5GLsYyZzSiy4CzoFNFId59uzZxYsXt+t+sPALtUzhttx/I9JRw/1my8WzBESSDXz06NFevXqZx1dp0qRp1qxZ79698+fPnzRpUqzrJEmSVKhQ4Y033sCVNVauUYlOhB6cinox1oDE0GTGgEcJo5m1ihMD3tfXt2/fvpgPXt9mPazYSATPM3AQ2S/DRURDo0aNxGeIvXDhQrNkEk175cqVn376yShGvOi5c+eKzzBKiQIpZmRyChNAKQY69TBcv359586do0aNMpNLokSJGjRoMGHCBCYdp8NM4Qb/s9iID48FbgdDQR0nKKp0F9ENZgw8An/88QfuKPZtSEjIuHHjxKJp06bdvn3blngwhHCnT58+rRRM9Jw5c+JdEw5dizNK2KadBUvWWycLkHnLli3t27d/+eWX1YwMGTI0bdr0888/N067oEKAKdA+8eRQXo5hNuk5w6dIkSJcMN26YcMGpk/aZJ/5bzCVajYV7NRIjihzIeEKhgTg7puxsXv3brzcS5cuHThwYMCAAV26dNG7YozbxIkTay2Xn58fg0ra1bjZKuG1117DlZWuPn/+vL+//48//midfyxQoNUiT1GUrAA4e/ZsUFBQ8+bN//nPf4rMRYsW1SpOLxv72cLDBwviCDBNelHwSZEihboAJEuWrEyZMq+//vrYsWOXLFlCX8tKMXcF2FcQafkQqRv/QkB3mcVbs2bNqlatmkZLcgsKAygNnVKmTJk6deoxY8YYIpELk3vIkCEMJ8KMJfRzw4YNO3bsyFmcavSKyn9M0B7KAYru2LEDh7lq1apmj6Hs2bMHBgairr0W4em+P9u7r9Kc7SHwbKt4Cnh2+ef6+/fvTy9D6QQJEqhrQIwYMbJkycIN6NOnzxdffPHrr7++8Oa6eP7gpkNFVFC3bt00MEqWLFm2bFn0LWjTps348eNXrFhx6NAhjG2Gk9Y1Mbhx7shF+Msvv8ycOfPly5cJi2lY4Hny5EHbo/Znz55NyhMBZYMZz7DEe9eIjRs3bq1atZh0mDuYNWy5BxzTuNXR0O+ZwFk4F8VcRvnPtoqngI9zmiRMy9atW8dc27lzZ2wqpybHSylXrtxbb721a9cuWm9eMAhcFRdjXaPdd85oeICSnbUIRO3TD8fVq1cHDRpUs2bNKlWqYJhoVwo7f7i19kVBF6WOAnbq/fswEOvXaYV5wWRUtHfv3oyBdOnSrVy5knRSrl27JgI/DKrx3LlzqNO8efNqwwBT4OjRo5kIFHZCuYAaYKc+AKVNmjSpcuXKRv1UrFhx4sSJZ86csSUeIHTe0CnPBCqWI7ygTwgo5QXC5xGNuHPnDjMfmhxF3b17d26M+hFgaxUsWLBfv36rVq0KvZGiuSXh6mOELl8qRWFG7fXr10+dOvXNN9+stoBb0aBBA24/ExaXED9+fK1ewg/ct28fWVQUxVoFRB1wXcYWZdgNHTq0dOnSWbNmTZIkSfHixRs3btykSRPUL3pv5MiR27Ztc070ov38+fPpqHjx4n377bdKfxyoP1HIWHnDhg2rU6eOSdcpa4x49zannOncUOYO3HhKKF++vMjMLcOEnDNnjjYPe7FwXoJarqt7gbDfbAE1yAn7xANg2NCJw4cPZxBky5bNfFkKPfBq2rdvv3DhQjwoLx0efjB9B4GZd2TgASjatGnTXLlyYVwwENVIAxy57du363EoE7+synr16umSNaRUThQD9jC2Lj6n+gFKm9WXXihWrBj0pnOUkb7CZYVOzIxK0WT6PzsKMSYF3SZs5qJFi+LlmVVPklEYKOoEcwFmFBa+2cEvZ86clIA9b+61QEVhlvDcYC6BI9f7OJ0TrvDRLG616i/QLPUUICAog8B0zhy8aNGiUaNGoQDxr9TvyZMnL1KkCDqc+3HgwAFbOixQsjk+GlYrwhajGagRPDSqzp8//6effrp8+XK9z4DPvr6+hQoV0uZvWNotWrRgQNg5H+Cjjz5COCAggEsmymU+oklqCbDjD4ct99jX+BQIs1irTu90zJPPPvsMS9Vzh3x82rVrh+rD/MYW27t378GDB7/++mtmZGR69OhRoEABieF8YSQziceIEYPo22+/TVEq3Bq3/1sdadiYJh07doyKTIqBhA1OnDgxZcoULAgt5OQ+lipVKjAwEA/c+fSLjCof0JjQ5TwfWFfgqVoBoM4hIIEXAg+r1ZSnaIfpZaZV7PD333+/WrVq5iVh3Lhx8X+mTp26efNmM/EDlDl1aRbnljjrNS1ROlAiUQkwSTM4cIypbv/+/dxv1aV9pwywJk6fPk1RyvUw0IaePXsij6FBVO1RAzgqACSsUyYRKAo4BUyKJJVFiRwJq5xnAhVrKhJMXUApwcHB3BHzeRPT3Lp165xZANNiUFAQ6VooglIlXLNmTWUB5Fq2bJmEvfI+PkyTCNBsr964efMm7jrKADMhZsyYVIp6aN68Oe33+h7TC6ZYF07YX2I+KTwD5wHllGJw69YtpuQRI0ZwV/7v//5PIyNx4sRoy+nTp4d+QOK8wSoWeN11sGTJEhy/jBkz5suXD3MAl1hL/yAwzl5ISMjEiRMHDx7cp08f1K9zUvcChdshC5gbFII5ipK3kxxAWDzhSJMUts89gGeEPpibnIPeqw1PzYdHw9kewrRE4QsXLrzxxhtW33vWYNBLvXr1wunYsGGD3CXcVLlL48aNq127dqVKlehVzio7RX3yySfcr1WrViGmRC7h6a6C0gSyc7RTreUizCC9e/c2u3lmzpy5ZcuWS5cuxf+3hSw4c7n4n7B3+VePK+kx4blLD6CRjeojbJ+2cPz4cdg4adIks2QP+Pv7Y7d///33ZnMlA9pAOWoJ8zcOM80D2IFkRPMXL16cWRxKMw5mzpyJFaCMXqAZoRvjaeh/p1ARQEVQOBPQjBkz7t69i1XPOMYu1ao75ZKkchGFHnv27GFEhn56BJkXL14Mc8qWLYsJQy7ni5ZnCCoK8xHGyZMn6fB06dJxUalTpx46dKh5dQzQuphUtLBZs2avvvqqs23bt2/npuhi7aQHoDN1f0OfelJQDjP7rFmz6tWrp0aCXLlyMSRQ185VnMDqext2kovHgOcZuGfAhqWFHgGrn/+SV1TlENXRCRhy9OhRRhumHYpR9xId0qFDBwYZLrot9wB4yEWLFoW62bNnz5Qpk+RbtWrFgMC/YvCZVcTUZVriFXZGnVA6IECUAP6kqsiRIwcjjNGGIVCmTBn9j6HEwI0bNz744APSU6VKJXl8zvr168OQzp07owAbNmyIe69TMAo3HuEsWbK0bdtWPojqBSpQUNSkm2abIymmDdo0j7ooNk+ePDg4SgewbsWKFXoeFjt27ICAAPTzoEGDtHKLcmCUJAU60/m4W1BdCBuYqAK2XFiQmKCoqZG24TFhIGBjq3+YRsuXL79gwQLSpVoMnCWYo4vHh2ePUfA/b9gzBBxmVmbA5cyZUzc4WbJkEGPOnDlaHgxvZbprPwocrZQpUzI6ve79/wTaDOCYjR8/ftq0aRiTaGCGF6d0yQTMVTOPFCpUyGqOh5BqW7x48YxfZx7LgTRp0tSpUweu4lkoxQA6YVngCxw4cIArUgrH0qVLozOpTvUakOIEZwVOcSSFS6C1El67dq2Z48zzi6ZNm2JsM+WZpwz4PtROOj5Lly5dsmXLNmXKFJWvcp451GD6Vt1rgFHD1MbcbTb9ojG0lt42hr2LZw4fjdpwveUGXrVgYG/btm3u3Ln6IB7EjRsXw1WPYRmajAk0/JEjR8xurBo9jwmEsej8/Pz0MharmIow/PQogfGn9pgyUcWowTVr1qBXCWsgLly4EF69/fbbVgM9y+YZo2bnqr1796LPg4KCsGmZqoKDg3fu3KlT4OLFi1u3bmUq0XQgvap6JQCcV6TGmBSnGEDRqQ3MgBj/XBp+L/OLEgH2BXMHxq2eezFFyolgOqtevfqTzomPD2cfCmfOnMGoad26tdn0K2/evHg669evd3oNukCOCrh4VvD8Kz19Cn+c3lc4gYp0+zka/SNADzwrTDLzhtnX1xfP+cSJE7aEhSe6/R5+/Pvfn3/+Of6tUrhYjOTXXnuNsGcoWe3R0UvJgL59+9IMqKJZhgA63zSbXF6X4IRV9l9N1fszuG0+SHQC7u3bt89rMY9AIfgaOPx169alBFwS89JYYALCH9Zaq969e5NCFgjsbCdHpXCZSgwnMAXPnj2bOVTmCT2G+cAsw811di9NojGC5w49RzsxmsDe5R+NHfrZVTjB3MIw7yXTPLZupUqV9JoU4GAPHTpUxrmBBihHtV+JgjVOPAMFELBTHwC1D7t27NhBWGKU4KU/BXzOd999V3/vULx4cXxvpSuLSvbUYYEUIAGBKHpJoxltr803ChcujOurROaapUuXYqqgYDmFMT9v3jzSMWFg+HfffQdLMQ3Map8SJUqEXhcpHDt2DHsBOk2aNEkpNMkcnwk8fWr1ttdlMlFij2DhlylTRu1EP7do0YLrCt1aq6vsJilgoi6eIXyeg4p+CjCADh06xMSPwax30XHixMGVhQamwdYI8fDWOc5IIaqjUgh46WHMbOcfLCAM6+xIKDA0UTWmEALW8PZQ2lQBCAOKYvYZO3Ys5kCtWrVq165dsWJF3Ei8XIgH6zTu8+XLh6PhXNql1bhMZNAYz1OJIH78+KlSpWJGCAwMhO1UhOresGEDfumyZcsw+50vJjH1CxUqdPz4cTXvWYHSuDSvMq9du7Zx40YuzVwFzWby3bRpUzg983fx+LD3A+eecVTSC4RGD0c7buHy5ctO3ztTpkyDBw+GaWacOeWdgw9VqaiT1UYY23758uX4nF5vU5zw6hP1EkcUFNZ4tWrVWrZs2b17dz2QV11NmzYtVqwYxN62bRszAnzu2bNnjRo1OIWv3rFjRywFuJo0adLkyZPD7WnTpq1duxYmTJ48GU8ePzlnzpw1a9ZkUuAUJaDSnZMOrmn+/PmxbLHJUY/Y3uSlVWoqrmyvXr0kGR64dOnSkiVLUMXOZT/MOBgXXo/T1R4XLwSeb7a4ARqvdtqLg2dsPoBI4gSWHtpAD2BixoxZpUoVDE6vR6lkxJVYsGBB27ZtNeillkk3AhzRclCI0Yn+x8J3PuIyUBvUMyYMOIVCxj//7LPPNm/e3L9/fzQk+l9Z8C1Dmz8hISF6cAUInD9/nmbjY3vZCHi/cNjLshAomfmIIxr74sWLeubEvQsICPj+++8Ja7b68ssvR40a5cnwhKBkOxQW8N6xm3CLzAfVjRo1wligE4AtZBUC1EWPLtBFuMLzT7carJHlNsCZ1atXo8o0vNKmTTtmzBjnU6hmzZoVLFgQwqOHO3XqhGWIaUq6WKHL7NOnj/ms9+233+7atavCElCHAAk7oUTBTrp/HzWbNWtWrydhSNohC2GWBsJMfBxAbMzvChUqaEGYrk6nngjkom1k92owwFIYOXIkXa0NCZIlS0bg5Zdf3r59O2cxdnANmMUk7CLiwAdVptHw1MPrRQEd1bt3b31YgvOJjtL3JKdOncJClgzAPkS9r1mzRgOXywQYwxrEumo9KdQp4Bzi2OfMDuPGjZsxY4bUvjklYQLYpQx9ObTmLIB1ffv2xS4wTyIloFx/B2ohvkmJEiW0vk0l6yx4oiqcwj///DN91b59ezwF7VUEiGIoHTt2DO8AnksSa2j69OkKu4hQ8MErYzR4huffHmrPAaGbCmHmz5+vBSQxYsTAcQ29jJTxhwNMgOzwASg9THjIYdED85hRi+tbv359fGO8aAa6/upEDeCItYwYR4iN8lTJjP4VK1ZAaQxvWIebnTdvXiwCmdZW8/9uV1MRhWDML1q0iLlG0b9TLIp35syZzE1axRkrVqxy5coxIaKf33zzTckMHz4cj0ads3z58tKlS2vwKMVFxMFf68AVj+BwttMaxnYUaq1fv758+fKWavEsNYdX5vkNmhlXFmFGP9RiFIp+BLZt2/buu+/qrbgKBITXrl1bqlSpqlWr4jx7irBQsWJFTHoCttwD25WABJTILODr61ugQIHRo0cTVdvy588/ceJEIyP5pwYlULUpxxkWPHVYIMxZk6iAAdb7+PHjq1Spon5j2nrppZcgtl6eBwcHcxVob8J0EYp67969hJm/4PzKlSsJh67axQuHj542RZkbs2XLliZNmmiM+vn5OffKYPxBMDPEMVzRPGjg1157rWTJklizdILO7t+/X+66JIHSv/rqq0yZMjFHmBQD8io7wFjFgsAdyJ49u/kUDG4w6WClE/bKGx4wjQFqm33C8gvwKXBe9AodpEmThtlq9erVFy5cgLp6bY7rgYnB5KhcTZs2HTx4sMLTpk174403FHaW7CKCwEdvQbk33H4lRUagMKV+BXjVqlUrxmvMmDEhOUNTj6C5TMR0pSjSyZMnS59jTEon6xQWe5cuXQgoBSgjCh83Xp98AK8BTRSoBAGNh4pTOtGBAwcuXLiQgFMmnGAqNWBawVXp3LmzFpnSMzVr1sSmSJ48+alTpyTTqFEjph6Fhw0bRlRhPO2CBQvq2T5uBT6FyeJVi4uIAB8sUm6MBq6dFtlAy8VV4OQ2DrZ5y123bl0UlLlGAuhtEz548KBZ2k20cePGesyrkpWLjiJcr149pgOiXj1GWCDs1RLZ/AS0HzMBiT0fQOZZs2Y1bNjQvGHG3HjvvfdOnz6NQ54yZUrzxAvqxokTR+/JsCmgsSwLJkSoboyOrl27jhgxgsDzvAoXTwTPf2LyYw3ISHaTTINDN95EsUTgNpY2o5khi2NsvojmwhFz0k8g8ezZs+K8s1jCSEIGeGIyAgJAKRwFk8UcASzSinST8tTw1GHVaGCfsEDjcYD79etXqlQpyIxaxlXGUvj0008TJUoEySWGEY7WNbMbBjlGisItW7YUdQFTQIsWLRSG85UqVZIP8vevwkU44b92Do5cYFShRh7RfjPWkfn888+1tjF27Ng9evQwa1dCU0KwWPNfo9YZ9ToFLHEPwiztmUPNVo12krWYFF/jtddey58/f9y4cS3F7FOlSpVdu3bJzxo/fnyBAgW0ovPYsWNp06Y1y28wInAutAPJN998g6LW27g7d+5A4927d1tS96F3UFAQAdWuRBcRDfaK0ch4h2jzo1kNkGH8KYxbiA2sL6KxQteuXat06+r/i7GKOhOBV/TSpUvbtm3DLgXmmZyXTJh4HJknArYDSrhq1ar6HB1kz54dTduxY0d8ZuNZIJYxY0ZmN0WbNWvWpk0bheF8rly5tCwH6wOLZu7cuTo1aNAg81kLU0adOnWk2xFToosIiEj8n5imzY9ovGUje8af4fapU6dat26tD8IY1mZTBApxlhO6TCOAnzxhwgRs17JlyzZp0gRjFRpg7uoJhWTCxCNOecFZjsJAUYNDhw4FBgbWr19f/8SQKlWq2rVr0x74iTamMVjdtNOWvn+/Q4cOzZs3V3j//v1FixalK1TstGnTML/VRR988EHp0qXJTvjgwYNFihTRK3qUNvb8unXrCIfZnigDM1QiL/5idRS+T6HRsGFDS6t5/ozi/fffVyJDGTysH4zNOXr06GTJkm3dutXoq5s3b/r7+8+ZM4ew1ZF/tyepS9VxNLUAmoeJAZkhmNoPqPqrr75C32K2wNWZ1v9LDhgwICAgAHll3LJlS44cOfRaHjRu3Ni09vLly3nz5uVyiOL2Q+lNmzZZUp5vRcy6Wipt166dwtYlRsHR8ssvvzDfOTs8ksLeOThK3qSHgcGdJk0arPExY8ZoE7UuXbrIpXwYq51dNGzYMP2Jj/P2f/jhh5UrV6YzxUY79WlBIXbIAlF4279//woVKojJuMdYBz179syWLZsxN2bNmuXn50ftjE5ca/0hCSAFy2L48OGK0tRChQrp+xDQvXt3bSMBmAsMdeF2uXLlJPbjjz9iveuROPj7FxgxwbTIBO3V+ZERf61Ciaq3KjRatGjR3toAHDB2Y1obUKOvVq1apcTQoHNEV45SgLj0SpHAgQMH0HJ6xP2s8NNPP3388ceYFdpEzQCbXyOvU6dOei9FFHM6a9as33zzDVE8al2gmoeBDcm1Np5jwYIFzYYqO3fu9PX11bywd+/e3Llz69+wuLpq1appCQqF1KtXb8iQIQqrzKgHrku96rytkRSeN1vWnYrilDa3ateuXYxj+YrgvffegwyDBw+GLdB74sSJEkPe2TMcw4x6irCAl4vSgwyEnelOeDI7ThF2lmlw/fr1cePGoSf1YI8jfvsnFrRJI54zM8u5c+emTJmCelF2POpWrVoRQKOWKFFCK2SJYmBnzpxZ/jAYNGiQ8a4RqFmz5uTJkxVt1KjR+PHjFUaxY6UrzEVhnmjtnaD0KIaodGmenYPtYNQF1yjTGpsZO3nGjBlKR7WmTp1aj5QWL15MGM6gG823WZ77/ABWjrDBWYa+ll49TJhEClSZNMNLhpYcO3aMKQbHOHny5LFixUqbNm2PHj2+/vprzGlb6P79Xr16xY4dG68BzQw/5QgALI7s2bNL8tVXX50/fz4BOQgY1Whaj5D1kAxD2iwLW7BgQZUqVfRMOzg4mLCynDlzhmaYv7AEHmmrQBN2EZHx17/nRW1ovDLcS5YsKY0KunXrliNHDvNurG/fvrLG06VLZ2xUD0cfTmmvUwx6VRQmEPZiRUhICMzs3bu3tgFOkCABxjYO8+HDh/VW2UDFHjx4MF68eHHixMHaHzp0KCmUiesLCbW2BIu9VKlSRoEzU2CJGH+4evXqZiUs8wi5NC/89ttveNpGn6PzBw4cSECX43WUjIuIDM9uhNHkVjF28+XLZ15T//jjj/Hjx1+zZg1hOHDt2rVXXnkFN3X06NEQDAQGBopLj9k/6knBTgoL1HXkyJGgoKAGDRporUiyZMlq1KhB1dDPrPQCSFKmKZaU5cuXq234yWZjpjlz5pQvXx4BTHc/Pz+51pLHLO/Tp48ldX/p0qWY7loWBvr372+2McHgl/UOtm7dSiH0hmq3araBvUOKxFxEZNjrwAnpGIXx9ttvm5WPjFHUnUxTXfjChQvhhsJQTpvpN23aFH+SFI1vzkogTOisIGH7hAXs8w0bNmDtBwQEYGDD5yJFivTs2ROjQFU4obxeJYBPP/2UViVKlEgbKoHTp08XKFBg165dhClNOlZYsmQJehvyc4uvXr2KmHmHx7RSsGBBPSTDXkBR69NL5gW6RUtQuASP6AM8rEkuIiAi8TrwJ8Lu3buzZctmbFGsTRxXuY7gypUrEEDvbOEAR+xbSyl6PufUFisgNFcN1IGhBWALXGrfvj0sEiGZSqSWbQkHVIIdCQt79+6lEJS8HbfWlmDAE/jhhx/Kli1rVDFGOIaJ+Y5SOyKatr322mvvvvuuwrgh2PwKM+mUKVOGQpwmg4tIB3sduNdYjHpA6+ofmAHMgavm0yuOXbt21XYIRFHL+Jy+vr6wBTLAovTp05vnUo9mnYAM9BszZkyFChW03z3IkiXLsGHDpBINqAsQwGzW5mrk5V487HYwN1GUdl8AO3fuLF68uB6SNW/efNq0aQTUQmo331Gik7Nnz65/2wI4HSVKlJDfTjtppOaCPXv2JE+eXLugaWpzEUnh2eGInyjJakOPHTt2lCtXTl84AJRn4cKFf7f+Rpso1mzu3LnNKhSOeNSZM2cWPSZPnhwnTpwkSZLowTJQOnkVMMDWhfz4qyhJMTlhwoQ1a9aEbNu3bze1W42ye5sSwJkzZzJkyODch0ACRszg+++/p1j0M2HOUvh7771HmEmhTp06TBDKQoF58uQ5fPiwJ8/9+23atEEhK3zv3j1s7I8++khRlLYxy2l89+7dCVAIrQpdu4vIAs+bLQM7LapAnCHw+uuvL168WInMYnnz5sVBVZRR7u/vr3dd6gE0G2w08oCxLpaGuSnv+fPng4OD27Vrp30RQa5cuTp37rx8+XK9IQuNS5cuoUsx+8VDnF5tqPSztZcQKSIVZvCXX35pFoEBdHWMGDEyZsxI4oIFC7A4kGQmql27tp4C6hJguNkVnBJQ1KYl48ePN6b4ypUr0eeEAS2hZ9xPLKMG7P/E1K2106IKROlNmzahBs0FYr7CAQKKTpkypUiRImKOUlq1alWlShVL3BOF9riagwcPlgamKIRRvPixkyZNqly5svlbTGaHRYsWHTp0yLw5E1SOE3g9qFl9PqVGAjQq2ZWiLLD62LFjThf33Llz2pF76dKlqFztyoIzjK9ucq1atYqmapkNTS1UqNBbb73lyfzAFNdK0ps3b5YvX157JJBXrNY20qR4Lj5Us11EFvg4B3QUAxcFf+rXr2++Ikav4jCbp18hISHovW3bthGW7b1+/XpSECOs8d2nTx88TwKnT58uZv33Mq4sStIisgdo/kGDBkFyiIGYQF5BHWsCAlHM9Tt37pBIWBmHDx+OG6+znonWgiX+FzTFUCl2gb6jxFGnPc6NXND5Zg8mjH/pc0WxIFQFGDJkiNl3lWs31VGCgSXoIvLB51dr6bK58ZEdjEWuxYxINHPfvn2VzhFNqw39db0dO3bUuy4GNAJMcOht/R+thvjBgwdTpEhhtk85fvx4ggQJRGbYMnLkyM8++wx1qrOAYlWUQIoJ6KyBUnQWEF6xYoW+rFAKMko3YUVbt25N7fgIcpsbNGhgnmaDefPmYT7oCShWd86cObHAdQoVXalSJe2FcOrUqcKFC+vRnRqj8oHCHF1EXvigNHQ7gZ0WmcEYleYhfO3aNQa9FC/YsmVLgQIFzC4oWOZp06aVpSr56dOno3ixeOkKpWCr672Rhj6TQp48edq2bQuvKlasKIaIxjoSBQ/rSQoBKjk04Fjz5s1Dv1JSFpWJjLYf02MtLAst+USGKFeaOXNm/d0nYP6SNlbzXn31VedDsrFjxxIwfeUiKsGHocldF+y0yAzGNxeiUY7fqwe8iuLKKooAQxm/VFpOF45XiTuKv2rkUZ6QRNQFOMxoSKm+/v37Q61cuXJJYapGGILhwzTxaJ48rJ+PHj2K4SA16wQlqz20hKmEerGx8ZApp0mTJnpIJgFscqjryWNpZpqH16DowoULuV6JffDBB5jxzAW0EzysPS4iL+y1ZYKdFplhLmT//v2vv/46jqiiuJrVq1c3g3jGjBm4o1LLSunRo4fZNBfcunULD1yrrCRQrVo18+0xnaavI42XDmEQQ4Wav+wSlFdgRujQoUOY60/AzZs39d2FF9MUZr7AfqZGLGd9Uwk5mzVrZgQ2btyYLl06FU7zqlatOm7cOMIA8wQa68EY9ku2bNm0OkXEdtblImrA82ZLI/JF3V1V7QX73JPDZO/cuTM2thLRciVKlDAeJgyBG3oEzbDm+MMPP6RMmdL8VT3HwMDA/Pnz61Ei+PDDD+GM3jyBr7/+OnXq1KhWaAZJULNUSkZ8bPONJyBREwfh+fPnY72PHj3arN8W1PmqVFCUhhnKQeM6depQV+LEiffs2UPKpUuXuCKabeXw0LhQoUKDBg1SFMJzgTdu3FD2d955RxY7GDhwoF4BAJ11EfXw126EQEnPH87aCWigK/qkUMbly5c7debIkSO1ckPkGTZsGNY4AU+tlnxAQACzAAGRHGZmypRJn0mAy5cvJ0uWzLmBUdmyZbUtASVDthw5cjifmalMBVTgrl278NhFSKWbgEVeD0wiMOmEmUEKFChALcBsEkhrtVROVzR16tQMGTLobTPaGDsiODjYI2etGMuSJYusAIRXr16t5d8uojBsv9prVD1nqGoUjqJ/E1evXsXhNF8R41tCWvPMDBsVJSx/WLRZtWpV1qxZtU5DKWg2PRtXw0aMGEEJnBKFPvnkEyhk/G3YBd8g3pkzZ4h69SRhjHmMZz2p4iyXqVp0ljJx6Zk4nH+Uq3QCzCx6QZ0qVSpDaRKxqGWHA/K+8sorTGSKduzYUR9jqRkVKlTQZ1tUauol4GykiygGzzNwBhD3+CluszOLV3arPO8Cw0wBGsEM7unTp0OSUaNGBQUFbd++PfRnxqERukwGsVZKq9jmzZtrSz1F69Wrp/3rYRd5oVy+fPmcf5SDbsyePfuFCxcIgxMnTqCo5ZSCP/74o2DBgtLbIsn69eu12BujV3OHmmSui7y1atVSIllING0mACihd+/eXm/IODLRaA9zjlrFrcfdWOPOlWQY1Xp7B7DJUdRmtfmyZcuKFCmixaqqmiMXDiTwDKFrsSMuXihsC9w51B4H1h0MI5fSgR1/MPIMwqxIKfBHO/gIMWLEwI3MnTs3gxibedasWUuWLIHqISEhxt0NDU7BYWxRKiK6aNEishNWFLVMgdq0RCljx44tXbo0AUAzoE3RokW10Y9a1bRpU30moei4ceNgNWJKuXPnDt5yr169mEpos5+fn3S4ahTtaTb6k8DD8O233+IVO3U1IDvzEWWaOUWVckXmu2iwe/du2m86pH79+kalk1isWDHz2RagTDv0ECBAa998800cln79+s2cOXPNmjW4D8wvZh37w+A1Ybl4gXjKdeB2hmd6CzEpzVLqhyF+/PgpU6ZE/1StWhXfcvTo0Vie0uo0xoxaBSgQy1kLyziL2sdOhhVGAPKjqPWVklJmzJgBS83rpU2bNmFsG72Nv50xY0ZUK2HJY1ykTp36ypUrlK/XTq+++qpOoQ8VmDdv3sNYjQBkIC8munHjBeqS7a3F54iRcunSJTj81VdfSQZQspbNALqCGcc8jRszZszrr7+u8GMC6mp3cSfo8zRp0mACVK5cuWXLlsOHD1+wYAE9c+jQoV9++UVzjYsIBc/OwXbwScBAZNTeu3cPe7VTp044oj179uzRoweBwYMHM9a7deuGVTlgwIC33nqLUwIKDbX27rvvcuQsUQYl5OzSpQspXbt2hbHaf59jzJgxY8WKpYA5apx5AQMYhcZwL1u2bKtWrRhtNI9GUqaWQItdI0eOrFatGgNXWoUUrH2Umy6HIxopc+bM5sMPxKpUqeL88IOmUoKJoqjRseYPrnfs2KEWtmnTRm/UVMvixYuZhmQgeAEZGcMTJkwwT+wFCENjKE2Tjm4THQtRmTiqV6+OEdG6dWtI2KBBAzqQu5DWQs2aNVHyIGnSpHnz5oWHNJtc2Cwo4Xbt2uGD0ELkUcj0P8c33niDQPv27Zs0aYK5pN4WrA4OG0imS5eOHqhRowYNQLe///77oXeAcPH84Xlaxg/jTyP1MYEwwMZj3Ns3+RlBg8kMLMNngTBUt0UfAu2/tW3btvLlyxu3HMZmypRJ765EpNOnT6N/zFfNHLHzmRdMFAqZlRuA+eull16SfwvhOeLQOjcwYFgzyvU/suYlE6CHaZKX10CxQN1IdMuWLeZDC6UwC2TLlo2iPvnkE08Ga/kqfH7nnXesqwwv0MPMks6e5yhYd8CGLR0K+i9RFy8Wf/17HuNJgceBGY6NGzfW7YwXL16SJEnQmbAOfxi7FMULUqVKxUBHbyCAYsGqTJAgAQEEIIkGkLIgQECjR4kU+4gBxCkKz5EjB9wLDAwcMmQItrFYhxbFRNf+3rouVBaaSlGl4J2SywicOnUKl9tsLXD+/HlIpc0SuFJoXLhwYZS/ohyPHTuWPn16s5M+AZr08ccfo1q5QNqvJ3BhghpVCMUqcObMGfNIT2c5hT9PmWokQCViOHCN9BtWcZw4cRIlSkQP/OMf/0BtUiP9/PLLLzOz6PEEp3LlyuXr66sjkxoCJNLzgICBUshLgWSkKKC7wBGQGBrc7ixZstD/LVq0oGGY5d9++y2NV2tdvED46Mshja3HhwYfSu/s2bO4eViPe/fuhRLHjx9HHzLiQ0JCOMXx3LlzDNkjR47s2rWL9BMnTuzfvx83mHSiKCiU6nfffYcA5TC27CHjAKOKQcxgLVasGJYnoxy6Qh4qonzary8fzXiiVShGzkIMJW7evBn/WXuGSM2uWLGiePHi5CWsa8f+FGkFbFTnRvl44yh2Y0VjAtAYfArCEqhVq5a/v7+qw5ql2drf1yMdCmShzc7FoRQIh/XpladnrXLQe1w7LSccFBRUoEAB7HBAsStXrsyePfvq1avpWzwOeIsVTZcCCqFtuB4EaDBuNkf8Dpx/3Y6HAXNm7dq1InaYYApmBuEysbfnzp179OjRq1evei2qedKB5CI84HkGzhjiZjzR/UDYcOZZAdbpiyhUCmoTX7Rv375ogDVr1sD5S5cuiZCPBjIQxjRMF4WW0/JJzpICnRia5gUyR334oe1QAOMVFWQ4Cflpj5aIS54wKs68stYuaLRQ0bp164oGeukdJoKDg5mh5CCokbi+MrbVt0rEoMBmQQfSPOdGDlQBFMY1wCYya0uY8sxq8CcFXrE8iLhx42JVMaHgn48fP56+4hqZl3Fb5L94gQYDDSQ7ycWLg2fXBH50S5T01Hi6O2oGMbP+yJEjGUDoDcJ6PhQmHl0RZyWgK4IMjE6pZaVMnTrVPPTyDMZ//QsP3PxXO4CNTmN74sSJ+sRaUYY1M47kycuxYsWKtJwAwGjHAMYnx7iAHnqxpHrJiImh50lcYJ06dbQNoM5279590qRJigKRh6opBENXHr4a8OGHH5KoZ+YkYhqY99UYKTTVbGb+pGBCxAr48ssvRWB12iOg9giEnVEXLxA+2F38vNhbQtXWSP670wpwXgVhjE/8YeeXWzdu3CDF6XJDPJxw+Kkoqi9z5sxmLRoWRMmSJc2jLI7vvfeen58fk47qwjgvUaKEmTU4JdN98uTJcA872Xz7iY3QoUMH87X2nj17MAGMjh02bJj+zpJigeoaPnw4haRIkUJbOwCIlz9/fvOf0hMmTMBhNmYwhaBdFX4K6IqcCJ3iIuLDB49Ld+4F3j+qBoxjtUFRnXpSmIwqBA+wTJky0qg6NWjQILOgEkB7lBuOt1LQkOXKldPSMfEK/mgNuZQnkyAOttmOG8bmzZvX/NX7smXLsmbNqo0ooJ/2TtGCTQpXMzgSJnDT+iM7Q9c333zTKHZPyywZ3GlKyJAhgzHvp02bRgO0JgR1mixZMvOQ/NixY8wv5u9snwJUSvMEtQHY51xEHjylX/1sodoZSSLSMwFFoT+hinPRyOHDhzNmzOh8OzV27NgmTZoQ0OXPnj1bL7cEfaUsnqiEbt266ftHRQcMGKA33oAJAm8c85iwSkPJw8mECRNK1WteIKOqxmoICAiAioQhLbMJrocEyK7ymUT0Zz16XYfhkD59evOGfODAgc6vR1u1aoWuJqC8TwHPbXgwvQr2CReRCvb/VxOKerfQXJEhUu3ateXK6hSaFn8VkisKqdC02utf8jVq1HCuHj1w4AAuLiRX9Pjx49myZdMbbzB06FBYKkoQxTJPnTq13ufDPfqZMjkFxLqrV6+izPV5NuzdtGmTTiFmGnzt2jWmIUoQkzEc9EQAnDx5EqVtvgNDzxctWhR5U4vSXURD2E/LoiTM4BaLVq9ejS41nzoBFK+ecqkTiGqJpXItWLAAvS0FqxTIqf92VxTT3TymOnXqFHayWYNx8eLFJEmSoMkxkvWuSNY1GQ3tz5w5w6QgXS3orAEpCxculLYPCQk5dOgQNDZP5hs1aqQ38ACrxNfXV5sQalJQuovoib90dZQEl6ar4zJRZRCVsAY9vrSfn5/5pmLv3r1wzDy7wjfmrFZxivPkda6yxptF3mTHDu9oLfbWLDBkyJDs2bNLWB9+VK5cWeVYhPU0AKMaGb0eo5FKV0BtxgrQolH5CHXr1jX/Nb1hwwb0vBx48M477+htFnmpRdldRFt4/mdLwyhKDgVdHQH4UKJECSinFC4WUzYoKEgyHPGWoSIBcQ+d3LZtWwJi6d27d/PkyaMn5+D333+H4eZfL9asWYPpbnZKQT+nSJFi2bJliuIMy4p2viEHNMD8bYD6n5ZwVu2BsXCeXGnTpr18+XJwcHChQoWYmzil53AffPCBldVjimOD7N+/n7DKATrlInrChyGisRL1hgJXBCc56lsr7XAkUs2fP1/fPItCqD40s3k9izwUcj4kGz16tPM7kKlTp2J+6xRV5M+f3/lFN2oTB9tEAXnhJz68FCn8b926NfOIEQCEKUr34vbt2507dyYLnrmetNEes8v33LlzKV8tARgR+mLcpLiI+DCTe3jAo6uj6mgQhQi0adOmadOmSuGI8ixXrpw2/eLy0cNQVCu3RDNsaVxiI49ZniVLFrPk+/z583nz5t29e7eis2fP9vf3Nx9vfPfdd3jUeoil0pgd0Lfx4sVLkCCBvhjt0qVL+/btjTEvkK7qoHEZayv/TJky6eU27S9VqpQl5akdV0Llk4Uq9JaLvKrORaSAlhWGEzxvtgDjAygcZSBFTWDSpEl6KCXaDBw4UEvHRIPx48fXqVPHRDdu3Fi4cGGtAFN2s3hL0e7du+sPNMGVK1dQ1DCZsM6WLFlSj9mpSymNGjXCYA4MDISoWjpu/GG1R5Dw119/Df+RpAqthMHhjxs3rnkpTe39+/cnoPKVi6OpzkWkQLjeLJvVURKwlL4zH1HIQz569Cjm608//SQOnzt3DuNWTilAvnLlys4Nj9CWuXLlunbtmm4DHMOJNSvP4Bi2NAHxk4z422adGUcID0WZKagRcsaPH988kFOBiAmK6hs42fMC7r357OSbb77BvddiNeSVxYULL0RlVmvQX79+/cKFC4RhDlE0pzZCUBRLGPvWRJcuXYoPbNQgE0HFihW9tj3TH18DzGBfX1+53wijgbNly7ZkyRKilCCe16hRw7xhZr6AsfPmzVNUoAojvHXrVgSw53UKrF69GnvbfEZCCeYxuAsXD0MUZzVUFG2kqKEcLqt5mbdjx44CBQqgRSV89epVzpqHyZLH5SavKL1u3Tr8W6P8sdv17x86iytevnx5MgKlwMnUqVObN8zBwcGQ1mzHLSCpunC5caRR5ualN7568eLF9TYOBAUFVa1alcarcBcuHoYozmoRUjSDtEWKFNlgbRgk3VipUqXp06cTEE/wt43LyhGrO3fu3Po0ihIgM6a72f9o5cqVpUuXNgw/cuTIP//5Tz3EUnbKxLZ32gW7du2C1YkSJZKTT5lqmATQyZx1/iXQhAkTUPXIEL506RIOvPMjExcuHoaozGovvPXWW3oFLVbMnz+/WLFi6EPRBkLC+YvWP29IsQ8ePFjGuQSmTp0qFxr89ttvaNE1a9YoCrDbu3TpQoDCVf7777/vZ33aRVQlQFHtK+JlhIMhQ4aQbjYPRJ6W4KJDY73r6tSpk1aSccoU6MJFmIgWrBYHUJXG2L59+zYusRSjzkI5aExAnMQeRjdqcxJw+fJlKGr2PzKvryW8bdu2LFmymMI5oudz5MihN+SSwZhPmDAh6hdi6zUb6Tdv3sRnHjp0KJTGVjcfZgHmCPP3I9SbJ08elU8u4LLaxSMQXVgtq1hhjujGatWqEVYU+uXLl+/XX38lKskWLVpo4RcU4ti5c2e9wQawC0UthiOPEY43bjY8sEQ83znr0y7h7t272bJl69evH4o3bdq02OrUiP2fMWPGlClTQmmgfbxVws6dO5l0zNPyBg0a6I9paZuH0w9qceEiTEQXVhsQPXr0KHTSKhRSbt26hSlu/gSX4xdffIFmhoqKouRLlChhXjJDTifhp0yZwoygRQWaEc6dO4fLfejQISMzZsyYFClSaNF4kyZNYseO/dJLL8HkWLFioaL9/f3NfgmSr1Klyvjx401jcA3Ie8/ano1EpbuILNAtE+ykByMtnBCN/GoBbpQtW9a5gdHIkSNhkXxpUlCncFJ/WwXHSMHYNg+iMbaZAn6xNjYE6G2UanBwMHxGUpzEew8MDCSs6MmTJ5MlS6ZF4GD27NnwmVxQnfnCrB4Hkv/ss88qVKggDuMpwHmtP1eKi0gHbiv37tSpU3pEIpjnrOGBaMdqPOSWLVvqn+4ApMIBNnuhcJw1a1a9evUISPEuW7YMU9mcxf2WXhUDe/bsaf5eUylbt24tWbKk1LKytGnTBhedgLB//34Udbp06ZwrRpHUvMDtx7xHPyt9xIgRehNG4SrNReQCdw1wc7HmNEKEaw+2vgwPeP6Rxw5GD4irBrisetAtoIQxtvfu3UuYewDx8JnNTmPz5s2rXr26uTeHDx82+xaQCORjayGKxMRh56xx6dKl9OnTo661vYkyCkSnT59u/jmA2T1Xrlxy4DElotudijLgxnFzOTrvoPmUKDzgY5ZYRCuof7ds2YJbK70ttnfs2FF/uyGBAQMGtGvXjgC4ceNGoUKFtM2YzjZt2tSsD1fKtGnTKleubFIAJG9k/fkeUBXjxo3zPBzz8dFuRCRajPbcAlpCFeYzkmbNmpkF5y4iOxgMdij8Ee10NdcLkThie2fMmFHLTkSqDRs2FCxY0Cz5RkniQpsl34MHD3bujrR27VrO6hGaUs6ePYue10MyeemLFy9m1jC7kXHE/sejbtiwIazGdCcj4JRKwCHXH4OBNWvWYLeb/UlduHh8RDu/WkQisH37dkioh1Xw6s8//yxXrpxeL4mTjRs3Nl9ZHD16FO/a+ELaNcFsyq9E/TcgAVnLt6w/ytLaNSCxLl26UMuBAwdixYqVJUsWFSgd/tVXXwUEBMjZJh2lrU0dXLh4UkRfVuMDOz+umjlzprYi0NkvvviiYsWK+nQZYAxrQZiEAwMDOSsdqxRoX6pUKc0RYumoUaMKFy6sN16S+eGHHxIkSICPzaSQJk2amDFjmpfeZClZsqT5a64TJ07gCMimUIqL5wBuk+5UZEe0Y7UXPCS2/jbEz8/P/IM0t7ZOnTrmr2exzNGc+NWKYpNnzZrV+ZCMAEa1FLt4iDWePn16fXdtnlwwa5jdDosXL44RrvdnYNasWaVLl9abD6tFNplNwMVzAHcK2JHIjGjNasgm2vTo0cP5XGrGjBmtWrVSGGVbpkyZ4OBgwhLGijYPyUTXJUuWwFKpZcnAXq05JyrV/fnnn+PG640X6NatG6zWjqUkFihQQJ9qqUCBvCrNxfPB8+ztcK0rurOa4+7du9G9eqYFLly4gM9s9lEw23eKnKhfX19frUJBtXJvMOOhtPMvfvbt25chQwatIVcKJneePHn0YTZZrl+/jncNq/XfPV27djWfkVALWQgYkO7iuUGdb0fCE84VKc8crq7+D8azNv0VA1u2bKln3QD2YntrH3+LYv+pUqWK+XhT1tqIESPMBkkqoV69ekOHDlUKWQgsXrwYt1mzAFFKgNKA0rACUqdOffz4cdKtGmz97+KFQDfoOSBcTf1ozWpuIZ375ZdfXrlyRbdz/fr1hQsXNku+0aV6q6x7gGXu7+8vSXHvyJEj2NU7d+40Mu+//z5qWY+yJYPSpsyvv/6aMLh16xYmfYcOHeLHj583b17K1xTw3MaTiyiP6MtqUVp2tYCd7HwQvWvXrmLFiv3888/i2/nz53PkyCFykqJEo9gVZXbA9tZ2pUoBCJilLGDs2LFNmzbFkofVSZMmlakvw1sCLlz8TURrXS0uAQVGjhxZsWJF0gnDyZo1a+pPqolyRG9r1wROKWXdunXwXD62OIwlX7VqVacMUwM2vN54Abx39POBAweOHTuWOHHi2LFjawdihCXvwsXfhw8Kyg5GY8AoaJY7d269iwJz585Fb5sPa/bt24elrQ+eYSzASfbz83P+xc+JEyeyZct2+PBhkwLq16+v5WJk4ditWzdtHnz16tW0adPiWmuRuc66cPFM4HP9+nUNqWg+sNq2bWs2MNJ/dziXfKO3tVOKsdgnT56MfX7v3j3Tb5jZzg88waJFi/DDcaQVpUCKlW5nMs2ZMyesXrt2LVGKjeb97+IZwvOfmFIs0XlUce0w0Ow90qFDB/O+Gnz++ee+vr7avld9dfz48UyZMulLLKVs3LgRVY/vTVFiPmQuWLCgSCvUrl3bLCANCQlJliwZrNbmZ+QCOuXCxd+E7VdH8yHlvPytW7dmyZLFfNTx66+/5suXT3+FB4El2bJly8aNGyuFI4Y6DvmcOXMIG63bt29ffZgtBAUF6X+2FDVfbpl/wFUuF88H3DhzN6MeovXTMifEK/gZEBCgV01C7969S5QoYUcsbNq0CR9bewOKpeh5CKwhoiN+OG6z/uAe3Lx5s7hjT9I9e/akT58+duzYsFqr1lw8Z3BHzBLgqIb79/8/ZuJgJuWNk0AAAAAASUVORK5CYII="

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Formarea de nori cumulonimbus și, prin urmare, formarea de furtuni înainte de sosirea unui front este cel mai probabil cu")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "fronturi reci în ianuarie"))
_question.answers.append(Parag_Model_Answer(False, "fronturi calde în ianuarie."))
_question.answers.append(Parag_Model_Answer(True,  "fronturi reci în luna august"))
_question.answers.append(Parag_Model_Answer(False, "fronturi calde în luna august"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("O masă de aer cald și umed se află deasupra României. Prognoza prezice sosirea unei mase polare de aer rece din nord-vest în timpul zilei. La ce tip de vreme ne poatem aștepta pentru această zi?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Condiții foarte favorabile pentru zborurile termice și la distanță din cauza aerului rece încălzit rapid de sol"))
_question.answers.append(Parag_Model_Answer(False, "Aerul rece care va sosi va stabiliza atmosfera, făcând astfel zborurile termice imposibile pentru ceva timp"))
_question.answers.append(Parag_Model_Answer(True,  "Furtuni frontale care aduc grindină si vânturi puternice"))
_question.answers.append(Parag_Model_Answer(False, "Răcirea continuă a aerului umed și cald și începutul treptat al precipitațiilor"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("În ce perioadă a zilei sunt furtunile termice (locale) cele mai probabile?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Dimineața"))
_question.answers.append(Parag_Model_Answer(True,  "După-amiaza târziu"))
_question.answers.append(Parag_Model_Answer(False, "La scurt timp după amiază"))
_question.answers.append(Parag_Model_Answer(False, "Timpul zilei nu are nici o influență asupra furtunilor termice (locale)."))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("În ce moment al zilei sunt probabile furtunile frontale?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "10 am"))
_question.answers.append(Parag_Model_Answer(False, "15 pm"))
_question.answers.append(Parag_Model_Answer(False, "20 pm"))
_question.answers.append(Parag_Model_Answer(True,  "Timpul zilei nu are nici o influență asupra furtunilor frontale"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("În general, ce condiții cauzează o inversiune la nivelul solului?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Încălzirea aerului care coboară, cu rata adiabatului uscat, în fața și în centrul unei presiuni ridicate"))
_question.answers.append(Parag_Model_Answer(True,  "Radiația nocturnă a căldurii din sol atunci când există cer senin"))
_question.answers.append(Parag_Model_Answer(False, "Masele de aer continentale care se stratifică aproape de sol"))
_question.answers.append(Parag_Model_Answer(False, "Încălzirea straturilor de aer adiacente solui pe parcursul zilei"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce cauzează dispariția unei inversiuni de la nivelul solului? ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Încălzirea aerului cald care coboară în fața și în centrul unei presiuni ridicate"))
_question.answers.append(Parag_Model_Answer(True,  "Radiația nocturnă a căldurii de pe pământ atunci când există cer senin"))
_question.answers.append(Parag_Model_Answer(False, "Aerul cald intrat în straturile superioare de aer"))
_question.answers.append(Parag_Model_Answer(False, "Încălzirea straturilor de aer aproape de sol pe parcursul zilei"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care sunt cele mai bune condiții pentru crearea unor termici bune într-o anumită zonă?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Unghi mare de incidență al razelor solare, reflexie puternică"))
_question.answers.append(Parag_Model_Answer(True,  "Unghi mare de incidență a razelor solare, reflexie slabă"))
_question.answers.append(Parag_Model_Answer(False, "Unghi scăzut de incidență a razelor solare, reflexie slabă"))
_question.answers.append(Parag_Model_Answer(False, "Unghi scăzut de incidență a razelor solare, reflexie puternică"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care sunt cele mai bune condiții pentru crearea unor termici bune într-o anumită zonă? ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Zonă umedă și expusă vântului"))
_question.answers.append(Parag_Model_Answer(False, "Zonă uscată și expusă vântului"))
_question.answers.append(Parag_Model_Answer(False, "Zonă umedă și protejată de vânt"))
_question.answers.append(Parag_Model_Answer(True,  "Zonă uscată și protejată de vânt"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("În care din următoarele luni sunt cele mai pronunțate termici înzonele deluroase?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "ianuarie"))
_question.answers.append(Parag_Model_Answer(True,  "mai"))
_question.answers.append(Parag_Model_Answer(False, "august"))
_question.answers.append(Parag_Model_Answer(False, "octombrie"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("În care din următoarele luni ajung termicile din munți la cele mai mari altitudini? ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "ianuarie "))
_question.answers.append(Parag_Model_Answer(False, "mai"))
_question.answers.append(Parag_Model_Answer(True,  "august"))
_question.answers.append(Parag_Model_Answer(False, "octombrie"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Termenul 'termică de sub vânt' înseamnă")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Curentul descendent de pe partea protejată de vânt a unei mase de aer cald în urcare"))
_question.answers.append(Parag_Model_Answer(True,  "Aerul cald care se ridică de pe partea protejată de vânt a unui munte"))
_question.answers.append(Parag_Model_Answer(False, "Aerul cald creat de turbulența rotorului pe partea protejată de vânt a unui munte"))
_question.answers.append(Parag_Model_Answer(False, "Curent termic ascendent format în partea de sub vânt a altui curent termic ascendent"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Termicile de sub vânt sunt cel mai probabil întâlnite")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "pe pantele nordice în timp ce bate vântul din nord"))
_question.answers.append(Parag_Model_Answer(False, "pe pantele nordice în timp ce bate vântul din sud"))
_question.answers.append(Parag_Model_Answer(False, "pe pantele sudice în timp ce bate vântul din sud"))
_question.answers.append(Parag_Model_Answer(True,  "pe pantele sudice în timp ce bate vântul din nord"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Termenul 'termică albastră' înseamnă")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "aerul cald în urcare în care umiditatea este atât de mică încât nu permite dezvoltarea norilor cumulus"))
_question.answers.append(Parag_Model_Answer(False, "aerul cald în urcare în care umiditatea este atât de ridicată încât formează nori care generează precipitații"))
_question.answers.append(Parag_Model_Answer(False, "aerul cald în urcare de peste corpuri întinse de apă, pe timpul nopții"))
_question.answers.append(Parag_Model_Answer(False, "aerul cald în urcare, care este ridicat de o masă continentală de aer rece"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ar trebui să ne așteptăm la termici albastre când ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "termica nu provine de la sol, ci dintr-un strat de aer mai înalt"))
_question.answers.append(Parag_Model_Answer(True,  "diferența de temperatură - punct de rouă a masei de aer în urcare este atât de mare încât punctul de rouă nu este atins"))
_question.answers.append(Parag_Model_Answer(False, "solul se răcește atât de mult în timpul nopții încât este mai rece decât un corp de apă învecinat"))
_question.answers.append(Parag_Model_Answer(False, "stratificarea atmosferică este atât de stabilă încât curenții termici sunt suprimați"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Termenul 'ascendență de restituție' se referă la")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "masele de aer care coboară în timpul zilei deasupra suprafețelor reci, cum ar fi ghețarii și lacurile"))
_question.answers.append(Parag_Model_Answer(True,  "masele de aer în urcare din mijlocul văii, după apariția vântului de munte (catabatic)"))
_question.answers.append(Parag_Model_Answer(False, "masele de aer descendente din apropierea curenților termici"))
_question.answers.append(Parag_Model_Answer(False, "curentul descendent din cauza temperaturii"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Pe o hartă meteorologică, acest simbol definește")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "o izobară"))
_question.answers.append(Parag_Model_Answer(True,  "un front rece"))
_question.answers.append(Parag_Model_Answer(False, "un front cald"))
_question.answers.append(Parag_Model_Answer(False, "un front oclus"))
_question.image = ""

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Pe o hartă meteorologică, acest simbol definește")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "o izobară"))
_question.answers.append(Parag_Model_Answer(False, "un front rece. "))
_question.answers.append(Parag_Model_Answer(True,  "un front cald"))
_question.answers.append(Parag_Model_Answer(False, "un front oclus"))
_question.image = ""


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Pe o hartă meteorologică, acest simbol definește")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "o izobară"))
_question.answers.append(Parag_Model_Answer(False, "un front rece"))
_question.answers.append(Parag_Model_Answer(False, "un front cald"))
_question.answers.append(Parag_Model_Answer(False, "un front oclus"))
_question.image = ""


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Pe o hartă meteorologică, acest simbol definește")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "o izobară"))
_question.answers.append(Parag_Model_Answer(False, "un front rece"))
_question.answers.append(Parag_Model_Answer(False, "un front cald"))
_question.answers.append(Parag_Model_Answer(True,  "un front oclus"))
_question.image = ""


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Unde este centrul ciclonului?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "lângă Tunis"))
_question.answers.append(Parag_Model_Answer(False, "deasupra golfului Biscaya (Golf von Biskaya) "))
_question.answers.append(Parag_Model_Answer(False, "lângă Stockholm"))
_question.answers.append(Parag_Model_Answer(True,  "lângă Lulea"))
_question.image = ""


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Unde este centrul anticiclonului?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "lângă Tunis"))
_question.answers.append(Parag_Model_Answer(True,  "deasupra golfului Biscaya (Golf von Biskaya) "))
_question.answers.append(Parag_Model_Answer(False, "lângă Stockholm"))
_question.answers.append(Parag_Model_Answer(False, "lângă Lulea"))
_question.image = ""


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Unde este gradientul presiunii cel mai plat?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "lângă Tunis"))
_question.answers.append(Parag_Model_Answer(False, "deasupra golfului Biscaya (Golf von Biskaya)"))
_question.answers.append(Parag_Model_Answer(False, "lângă Stockholm"))
_question.answers.append(Parag_Model_Answer(False, "lângă Lulea"))
_question.image = ""


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Unde este gradientul presiunii cel mai abrupt?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "lângă Tunis"))
_question.answers.append(Parag_Model_Answer(False, "deasupra golfului Biscaya (Golf von Biskaya)"))
_question.answers.append(Parag_Model_Answer(True,  "lângă Stockholm"))
_question.answers.append(Parag_Model_Answer(False, "lângă Lulea"))
_question.image = ""


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Unde e cel mai puternic vânt?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "În nordul Africii"))
_question.answers.append(Parag_Model_Answer(False, "AAÎn ElvețiaAAA"))
_question.answers.append(Parag_Model_Answer(True,  "În sudul Scandinaviei"))
_question.answers.append(Parag_Model_Answer(False, "În Islanda"))
_question.image = ""


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Unde e cel mai slab vânt? ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "În nordul Africii"))
_question.answers.append(Parag_Model_Answer(False, "În Elveția"))
_question.answers.append(Parag_Model_Answer(False, "În sudul Scandinaviei"))
_question.answers.append(Parag_Model_Answer(False, "În Islanda"))
_question.image = ""


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care este direcția vântului în Alger?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "100 °"))
_question.answers.append(Parag_Model_Answer(False, "190 °"))
_question.answers.append(Parag_Model_Answer(True,  "280 °"))
_question.answers.append(Parag_Model_Answer(False, "320 °"))
_question.image = ""


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care este direcția vântului în Londra?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "130 °"))
_question.answers.append(Parag_Model_Answer(False, "190 °"))
_question.answers.append(Parag_Model_Answer(False, "270 °"))
_question.answers.append(Parag_Model_Answer(True,  "310 °"))
_question.image = ""


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care este direcția vântului în Atena?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "130 °"))
_question.answers.append(Parag_Model_Answer(False, "190 °"))
_question.answers.append(Parag_Model_Answer(False, "270 °"))
_question.answers.append(Parag_Model_Answer(False, "310 °"))
_question.image = ""


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care este direcția vântului în Zurich? ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "100 °"))
_question.answers.append(Parag_Model_Answer(True,  "210 °"))
_question.answers.append(Parag_Model_Answer(False, "280 °"))
_question.answers.append(Parag_Model_Answer(False, "30 °"))
_question.image = ""


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care este direcția vântului în Lisabona?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "100 °"))
_question.answers.append(Parag_Model_Answer(False, "190 °"))
_question.answers.append(Parag_Model_Answer(False, "250 °"))
_question.answers.append(Parag_Model_Answer(True,  "320 °"))
_question.image = ""


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care dintre următoarele orașe se află într-un sector cald?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Lulea și Sankt-Petersburg"))
_question.answers.append(Parag_Model_Answer(True,  "Zurich și Stockholm"))
_question.answers.append(Parag_Model_Answer(False, "Lisabona și Atena"))
_question.answers.append(Parag_Model_Answer(False, "Paris și Londra"))
_question.image = ""

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("În care dintre următoarele orașe sunt condiții meteo de după front?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Lulea și Sankt-Petersburg"))
_question.answers.append(Parag_Model_Answer(False, "Zurich și Stockholm"))
_question.answers.append(Parag_Model_Answer(False, "Lisabona și Atena "))
_question.answers.append(Parag_Model_Answer(True,  "Paris și Londra"))
_question.image = ""

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care dintre următoarele orașe sunt sub influența anticiclonului?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Lulea și Sankt-Petersburg"))
_question.answers.append(Parag_Model_Answer(False, "Zurich și Stockholm"))
_question.answers.append(Parag_Model_Answer(True,  "Lisabona și Atena "))
_question.answers.append(Parag_Model_Answer(False, "Paris și Londra"))
_question.image = ""

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care este distribuția de nori cea mai probabilă în Lulea?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "3/8 - 5/8 cumulus "))
_question.answers.append(Parag_Model_Answer(True,  "5/8 - 7/8 cirostratus "))
_question.answers.append(Parag_Model_Answer(False, "8/8 nimbostratus "))
_question.answers.append(Parag_Model_Answer(False, "5/8 - 7/8 cumulonimbus, lenticulari izolați în est"))
_question.image = ""

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care este distribuția de nori cea mai probabilă în Paris?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "3/8 - 5/8 cumulus "))
_question.answers.append(Parag_Model_Answer(False, "5/8 - 7/8 cirostratus "))
_question.answers.append(Parag_Model_Answer(False, "8/8 nimbostratus AAAA"))
_question.answers.append(Parag_Model_Answer(False, "5/8 - 7/8 cumulonimbus, lenticulari izolați în est"))
_question.image = ""

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care este distribuția de nori cea mai probabilă în nordvestul Elveției? ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "5/8 - 7/8 cirocumulus"))
_question.answers.append(Parag_Model_Answer(False, "5/8 - 7/8 cirostratus"))
_question.answers.append(Parag_Model_Answer(False, "8/8 nimbostratus "))
_question.answers.append(Parag_Model_Answer(True,  "5/8 - 7/8 cumulonimbus, lenticulari izolați în est"))
_question.image = ""

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care este distribuția de nori cea mai probabilă în St. Petersburg")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "3/8 - 5/8 cumulus "))
_question.answers.append(Parag_Model_Answer(False, "5/8 - 7/8 cirostratus "))
_question.answers.append(Parag_Model_Answer(True,  "8/8 nimbostratus "))
_question.answers.append(Parag_Model_Answer(False, "5/8 - 7/8 cumulonimbus, lenticulari izolați în est"))
_question.image = ""
