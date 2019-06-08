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
_question.image = "iVBORw0KGgoAAAANSUhEUgAAAUMAAABbCAIAAABmo3ASAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAE++SURBVHhe7d1nsF3VeTdwTz5lEqc7mYydfEg8ZhLbMxibamOaRJcQEpIoKkgCJBDI9CpCk0QzECCiSEQ4KIjeDaEYjGiiFyFRDKJIVGNMM2Cw88L7O/t/tNicc+69Eva9tm/0n9Getdd+1lpPX886Z9+jz/3v//7vRx999PEqrMIq/EHh/1Vo3nz88eeE8Ycffvjyyy8///zzL7zwwrJ+jeeee+6VV1556aWXCNvs6r9YunTpq6++Gss2u/ovyEhSxv0/YlmS/vrXv/5UJPt33XXXbb755rvvvvvkyZP36NfYc889t9hii8GDB2s0u/opmHKvvfYaOHDgiBEj+r2wQNhBgwZttdVWGs2u/gvGFbA33nij4C0FdSOSzz333OOOO06I25z7DFm+ND744IP09yrIeMIJJ5xzzjl9IOyvfvWrNCIgpJ0iqA/kJeOhhx565ZVX9o1lSeSkFkk19BRh+wBkPOOMM0466aS+ETYgcuTVdo3UfQAyzpgx47//+78t2hrJp556au77DK+99toTTzyh8fTTTyt609kHOO200+bOndu86U0Utybg//zP/6j6tB977LGf/vSnGsUAvYojjjgimbu3UcS544475s+fn/aiRYveeeedtPsA3FgwN296GUVeBmVfjYcffrgEdh9AzkokFzQi+Qc/+MG///u/5773QHhlfVQgdP/1X/912LBh2rNnz95www1/+ctfepSnvQqS/td//VfzpjcRu86ZM+cf//EfCfvlL3954cKF06dPV+6GoA+E/bd/+zdJpHnTmyCLvUIZ//nPf/5LX/rSpEmT3O62227qQE+VJyHrVfznf/7nf/zHfzRvehPcOGnaefVv//ZvR48era22P/HEE/MUGnS9ie9///u/s0iGSHjTTTd98Ytf/NznPjdy5Ei3L7/88he+8IVLL720Iul19E0kV0npI1WQY/nUqVO59T/8wz9MnDjRzvynf/qnCxYsQNMH9u6bSI6wb7/9thLg9ttv52R/9Ed/9Morr1x//fV/8zd/s2TJEk+bpL2JvolkspRqSwxz47Fjx2qffvrp//zP//zGG29o9/9IjkUVt47lm2222eDBg9O/zTbbSGlp9zb6JpLZUhgzeXZmAfznf/7ntK+97rrrTpkyRaMP/LtvIjlixn3vu+++P/uzP/ve976nrbT+yle+csopp1RUvY4+i+QYTi05ZMiQ9dZbLxsSE//FX/zF5Zdfrt3/I7mOTTfddKuttkp7jz32+Kd/+qe+qcH6JpIhwazx7LPPKrCdIN566y23W2655cCBAyuSXkefRTLEv3/2s585rArgW265xa1jhRq7oup19E0kJ0oXLVq0wQYbKDdsSDkuvfvuu3/yJ38ybdo07aiiV/F7FMkDBgwokczYjpF9kMmgbyKZLTm3hrMDby6Sgnp7k002ad70MvomkhmOsKrr00477aWXXtLjBHHIIYdo/Mu//Es/i+REKek+//nPM6XrX/3VXzlT0IBInj59uqf/t/bkb3/72xtvvHHaO+64I+fug0wGfRPJbBlzqjMdpUSUc9Sdd96pRy6fMGFCRdXr6JtIDmxKDg7f+ta3DjzwwD/+4z++6667lCSrrbZanLsPjNtnezI8+eSTF1988bx58/7+7//+a1/72tKlS19//fW//Mu/PP/885t0vYwuI7nPDjMFxx9//EknnaTxxhtvfPGLX5w1a1b6ext9tie7cmXJe9SoUTvssMPWW2/NzK+++qosfsMNN4SstyGSr7vuuuZNr4GwkXfZsmUyl9Pjtdde6/a2227767/+64ULF4amQdqb6ONzcnDssceeffbZGuedd96XvvQlJVj6exudI/ncc8/t+z25QGKTyPvsuzgVYJ8lznbko77mTe/DfnjTTTc1b/ockyZNksWaN72Pvvw+uR3yl7zZvOl92HpbXotoRLKuww477Lnnnnvqqaee7is8U2HJkiUiGZ599lmdbvO0l0DGqVOnnnDCCRrNrl5GkSgCzpkz55prriE4Vfe2tq04ZcoU/q3RZ5aNXIrPn/zkJ2eeeeaPfvSjCOu2SdE7IKPtUSz1mWWDyLV48WKhdffdd0d8yNPegMmff/55td4FF1wgeEuB0IjkSy65ZL311uv7t3MnT55s0X333Xf//ffX3m233ZoPeg2W+853vuNMrmHFZm8vIwtFvfvttx9h++YVdyuuueaagwYN6stXke3DpAONAw44QLGdzjztPRB24403Xn/99aPnvkFdLmaVN5s3vQwyCtirrroqMRw0q+u+f1uzHfXjR+9Bde1I07zp7zjyyCOvv/765k1/xw9+8IPfYXUd8OF80tnbOPnkk1sOic1PvDqekxtH+yq6lBBXXHHFlVdeeeutt+aRxg9/+MNf/OIXuX3ooYcQ/PznP9eOJK4Z/uvqb6/ymgSksxr0CQpx874NefTiiy++9tpr2q+88gpmrr766htvvDE8hEAbV2gaYz7++J577sHV7bffntvQkLQ9kjFWDECWyy67zPyGu8W5YFAlaoRgwYIF1157bd4oDue5RrpKykYjE2qXmQOPQuba7Po0Qq+CevPNN0OzaNEiddPrr7+uHX1qEJMG3n33XW1kxLz88svvuusut+lxVW12H8lqUandPAQ0xGxEu+222zyyirUcs+GDDz7wVI9rGNAoPYWYUNWsnyBPe4SKsegTOBLxy8yuv/zlL1lWZ4P6448feeQRwv74xz+OUbKuk8vMmTOr559Cg9Fqqscff5xl4xLpvOWWW+jH5J5iwBLmrAY1RrWIE94Cj7J0Afq8EOFpetqBxtWBK7p66aWXaJ6n0fD777+fGQznxvp/9rOfZdSdd95J2DvuuCO3mX8l3rs2bxa2xvDhww888EDHy3zCPG3aNPv74Ycfroj68MMPDd95552POOKI0aNHxwARtZqmFXlUlxZ9eiJGs7cNb7zxxoYbbkjX2vvss8+YMWPsruQhcMVpY1GHh2233VYxySqceLvttrMpqd7xWcK7/bPrjA3DcsRmm2121FFHTZ8+XfDwYFWTaRWKgPK4445T3hDWWYDD6enowYF+QqFp3i/3hqwIzd42OFtusMEG999/v7bTprVIwQrLli3LbEJOfT506FBivv3224rY7bffPnZhKa4QMk/bv4XK6ho4ZzLq+v73v3/WWWfJFBTFrCaZMWMGAoI7Dhx88MF777133J1EdXEKdJrNtPWn2rFsrs3eNhBzo402Wrp0afP+44+33nprGtYoo5yBWXbChAksazsiOD5ZZNdddy066eqz61iHlow69NBDubEi1MyWIN1hhx3GnWwSdDh16lTaYH0TApqObytFIsi6gbYej7rxB+DA3BiNNm3vsssuDthA+VnRI7bGKq7wjD12P/roo5mAXeJyxq7E98mZVyMfnNigHn30UbcyiuVjV7qYN28eFeTDd6GVpIgbwx9++GG5RCxdc801N9xww0EHHWS787RdBa733nsv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"

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
