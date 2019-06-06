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
_question.image = ""

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))


"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("AAAAA")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
_question.answers.append(Parag_Model_Answer(False, "AAAAA"))
