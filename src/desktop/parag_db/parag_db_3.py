from parag_model.parag_model  import *

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_category        = Parag_Model_Category()
_category.name   = "navigatie"
PARAG_CATEGORY_3 = _category

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce este navigatia aeriana? ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "o informare"))
_question.answers.append(Parag_Model_Answer(False, "un sistem de deplasare al aeronavelor"))
_question.answers.append(Parag_Model_Answer(True, "o stiinta"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care este metoda de navigatie pentru zborul in VFR?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "observata"))
_question.answers.append(Parag_Model_Answer(False, "estimata"))
_question.answers.append(Parag_Model_Answer(False, "izobarica"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cum sunt numerotate meridianele?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "de la est la vest"))
_question.answers.append(Parag_Model_Answer(False, "de la vest la est "))
_question.answers.append(Parag_Model_Answer(True, "in ambele sensuri"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cum sunt numerotate paralelele?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "de la nord la sud"))
_question.answers.append(Parag_Model_Answer(False, "de la ecuator spre sud"))
_question.answers.append(Parag_Model_Answer(True, "de la ecuator spre nord si sud  "))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce reprezinta nivelmentul?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "totalitatea formelor de relief"))
_question.answers.append(Parag_Model_Answer(False, "forme de relief specifice hartilor"))
_question.answers.append(Parag_Model_Answer(False, "reprezinta planeitatea terenului"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care sunt directiile principale?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "N , NV ,  E, SE"))
_question.answers.append(Parag_Model_Answer(True, "N , S , E , V"))
_question.answers.append(Parag_Model_Answer(False, "E, SE, V, NV"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("1.	Care sunt Nordurile folosite in navigatie?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "a)	Nordul adevarat"))
_question.answers.append(Parag_Model_Answer(True, "b)	Nordul magnetic"))
_question.answers.append(Parag_Model_Answer(False, "c)	Nordul izobaric"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce este declinatia magnetica?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "directia compas"))
_question.answers.append(Parag_Model_Answer(False, "unghiul dintre aeronava si Nord"))
_question.answers.append(Parag_Model_Answer(True, "unghiul dintre Nordul magnetic si Nordul adevarat"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce este distanta?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "spatiul dintre doua puncte"))
_question.answers.append(Parag_Model_Answer(False, "lungimea liniei care le uneste"))
_question.answers.append(Parag_Model_Answer(False, "unitatea de masura"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce unitate de masura este folosit pentru inaltime in normele OACI?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "yardul"))
_question.answers.append(Parag_Model_Answer(True, "foot"))
_question.answers.append(Parag_Model_Answer(False, "inch-ul"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care este scara hartii pentru zborul in VFR?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "1: 200 000"))
_question.answers.append(Parag_Model_Answer(False, "1: 50 000"))
_question.answers.append(Parag_Model_Answer(True, "1: 500 000 "))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cum se numeste meridianul prim?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Pascal "))
_question.answers.append(Parag_Model_Answer(True, "Greenwich"))
_question.answers.append(Parag_Model_Answer(False, "Hecto"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cum se numeste traseul de la decolare pana la aterizare?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "itinerar"))
_question.answers.append(Parag_Model_Answer(True, "traiect"))
_question.answers.append(Parag_Model_Answer(False, "ruta"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Pentru un zbor in VFR este nevoie de o harta ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "informativa"))
_question.answers.append(Parag_Model_Answer(False, "operativa"))
_question.answers.append(Parag_Model_Answer(False, "de ruta"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care sunt reperele liniare pe o harta ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "orase, lacuri, terenuri"))
_question.answers.append(Parag_Model_Answer(True, "caii ferate , sosele, rauri"))
_question.answers.append(Parag_Model_Answer(False, "poduri mari, fabrici izolate, silozuri"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("La o rotatie de 24 de ore a pamantului corespund ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "180 grade longitudine"))
_question.answers.append(Parag_Model_Answer(False, "230 grade longitudine"))
_question.answers.append(Parag_Model_Answer(True, "360 grade longitudine"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("In ce se masoara viteza vantului ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "m/s"))
_question.answers.append(Parag_Model_Answer(True, "noduri"))
_question.answers.append(Parag_Model_Answer(True, "km/h"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce este UTC ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "timpul local "))
_question.answers.append(Parag_Model_Answer(False, "ora actuala"))
_question.answers.append(Parag_Model_Answer(True, "timpul universal coordonat"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care sunt etapele planificarii zborului ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "alegerea hartilor"))
_question.answers.append(Parag_Model_Answer(True, "estimarea meteo"))
_question.answers.append(Parag_Model_Answer(True, "trasarea traiectului"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce este GPS ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "sistem de navigatie"))
_question.answers.append(Parag_Model_Answer(False, "sistem de control"))
_question.answers.append(Parag_Model_Answer(True, "sistem de pozitie"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Pozitionarea in sistem GPS se face prin")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "sistem radio"))
_question.answers.append(Parag_Model_Answer(True, "triangulatie"))
_question.answers.append(Parag_Model_Answer(False, "balize"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cate surse minim foloseste sistemul GPS pentru stabilirea pozitiei si altitudinii?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "3"))
_question.answers.append(Parag_Model_Answer(False, "5"))
_question.answers.append(Parag_Model_Answer(True, "4"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cate surse minim foloseste sistemul GPS pentru stabilirea pozitiei?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "3"))
_question.answers.append(Parag_Model_Answer(False, "12"))
_question.answers.append(Parag_Model_Answer(False, "9"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce este o altitudine barometrica?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "o inaltime de la nivelul marii"))
_question.answers.append(Parag_Model_Answer(False, "o inaltime care corespunde presiunii standard"))
_question.answers.append(Parag_Model_Answer(False, "o inaltime dintr-un punct de referinta"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Din ce directie bate vantul la 135 grade")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "NE"))
_question.answers.append(Parag_Model_Answer(False, "E"))
_question.answers.append(Parag_Model_Answer(True, "SE"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Din ce directie bate vantul la 270 grade")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "N"))
_question.answers.append(Parag_Model_Answer(True, "W"))
_question.answers.append(Parag_Model_Answer(False, "SW"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Din ce directie bate vantul la 0 grade")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "N"))
_question.answers.append(Parag_Model_Answer(False, "NE"))
_question.answers.append(Parag_Model_Answer(False, "NW"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care este inaltimea minima a unui obstacol pentru a fi reprezentat pe o harta de navigatie")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "50m"))
_question.answers.append(Parag_Model_Answer(True, "100m"))
_question.answers.append(Parag_Model_Answer(False, "300m"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Inaltimea unui punct este distanta dintre acel punct si")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "nivelul mediu al marii"))
_question.answers.append(Parag_Model_Answer(False, "izobara de 1013mb"))
_question.answers.append(Parag_Model_Answer(True, "terenul survolat"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care sunt coordonatele geografice")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "latitudine"))
_question.answers.append(Parag_Model_Answer(False, "altitudine"))
_question.answers.append(Parag_Model_Answer(True, "longitudine"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cate secunde are 1 grad de latitudine sau longitudine?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "60"))
_question.answers.append(Parag_Model_Answer(True, "3600"))
_question.answers.append(Parag_Model_Answer(False, "600"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("O mila nautica (1NM) este echivalenta cu")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "1 minut de longitudine in orice punct de pe pamant"))
_question.answers.append(Parag_Model_Answer(True, "1 minut de latitudine in orice punct de pe pamant"))
_question.answers.append(Parag_Model_Answer(False, "1 grad de latitudine in orice punct de pe pamant"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cati kilometri are 1 mila nautica (NM) ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "1.8"))
_question.answers.append(Parag_Model_Answer(False, "1.5"))
_question.answers.append(Parag_Model_Answer(False, "2.2"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cate minute au 0.25 grade")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "45 minute"))
_question.answers.append(Parag_Model_Answer(True, "15 minute"))
_question.answers.append(Parag_Model_Answer(False, "25 minute"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce este o zona interzisa")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "un spatiu definit unde zborul nu este permis"))
_question.answers.append(Parag_Model_Answer(False, "un spatiu definit unde zborul se face dupa reguli stricte"))
_question.answers.append(Parag_Model_Answer(False, "un spatiu definit ca fiind temporar restrictionat"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce este o zona restrictionata")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "un spatiu definit unde este restrictionat zborul"))
_question.answers.append(Parag_Model_Answer(True, "un spatiu definit unde zborul se face in conditii specificate"))
_question.answers.append(Parag_Model_Answer(False, "un spatiu definit unde au loc activiati periculoase zborului"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Deplasarea aeronavei fata de sol este compusa din")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "viteza aeronavei fata de aer"))
_question.answers.append(Parag_Model_Answer(False, "viteza aeronavei fata de vant"))
_question.answers.append(Parag_Model_Answer(True, "viteza aerului fata de sol"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Viteza vantului se descompune in")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "componenta verticala"))
_question.answers.append(Parag_Model_Answer(True, "componenta laterala"))
_question.answers.append(Parag_Model_Answer(True, "componenta longitudinala"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce este deriva ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "unghiul dintre directia vantului si directia de deplasare fata de sol "))
_question.answers.append(Parag_Model_Answer(False, "unghiul dintre directia de orientare si directia de deplasare fata de aer"))
_question.answers.append(Parag_Model_Answer(True, "unghiul dintre directia de orientare si directia de deplasare fata de sol"))
"""*****************************a)	adevarat********************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Acul busolei se va alinia cu Nordul")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "adevarat"))
_question.answers.append(Parag_Model_Answer(True, "magnetic"))
_question.answers.append(Parag_Model_Answer(False, "izobaric"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("FL50 observat pe o harta reprezinta cu aproximatie")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "5000m"))
_question.answers.append(Parag_Model_Answer(True, "5000ft"))
_question.answers.append(Parag_Model_Answer(False, "500m"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("In conditii de vant calm directia de deplasare a aeronavei este")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "perpendiculara pe directia vantului"))
_question.answers.append(Parag_Model_Answer(False, "paralela cu directia vantului"))
_question.answers.append(Parag_Model_Answer(True, "neinfluentata de vant"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cu vant din spate viteza aeronavei fata de aer este")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "mai mare"))
_question.answers.append(Parag_Model_Answer(False, "mai mica"))
_question.answers.append(Parag_Model_Answer(True, "nu difera"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cum afiseaza sistemul GPS coordonatele geografice")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "grade, minute, secunde"))
_question.answers.append(Parag_Model_Answer(True, "grade, minute"))
_question.answers.append(Parag_Model_Answer(False, "grade, secunde"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Hartile trebuie sa fie")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "digitale"))
_question.answers.append(Parag_Model_Answer(True, "cu scara constanta"))
_question.answers.append(Parag_Model_Answer(True, "conforme (sa respecte unghiurile reale)"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Scara unei harti poate fi reprezentata ca")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "fractie reprezentativa (1:500.000)"))
_question.answers.append(Parag_Model_Answer(True, "linie gradata"))
_question.answers.append(Parag_Model_Answer(True, "text descriptiv (1cm egal 5km)"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce ii trebuie unui sistem GPS pentru determinarea pozitiei")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "cer senin"))
_question.answers.append(Parag_Model_Answer(True, "spatiu neacoperit"))
_question.answers.append(Parag_Model_Answer(False, "conexiune la Internet"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("O viteza a vantului de 20 de noduri (20kts) reprezinta")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "15m/s"))
_question.answers.append(Parag_Model_Answer(False, "10km/h"))
_question.answers.append(Parag_Model_Answer(True, "10m/s"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Vantul este din sector sud vestic (SW). Va asteptati ca directia sa fie din")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "000deg - 045deg"))
_question.answers.append(Parag_Model_Answer(False, "225deg - 315deg"))
_question.answers.append(Parag_Model_Answer(True, "180deg - 270deg"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Linia care uneste pe o harta punctele cu aceeasi altitudine se numeste")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "ortodroma"))
_question.answers.append(Parag_Model_Answer(True, "curba de nivel"))
_question.answers.append(Parag_Model_Answer(False, "izoclina"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cota este:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "înălţimea obstacolului măsurată faţă de nivelul mediu al mării;"))
_question.answers.append(Parag_Model_Answer(False, "înălţimea obstacolului fata de un nivel de referinta."))
_question.answers.append(Parag_Model_Answer(False, "distanţa obstacolului măsurată faţă de nivelul mării;"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("În cazul navigației estimate:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "determinarea poziției aeronavei nu este exactă"))
_question.answers.append(Parag_Model_Answer(True, "determinarea poziției aeronavei se face după instrumente de la bord"))
_question.answers.append(Parag_Model_Answer(False, "nu se folosește la determinarea poziției aeronavei"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Metoda navigației observate")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "este utilizat la zborurile IFR"))
_question.answers.append(Parag_Model_Answer(False, "nu poate fi utilizat de către piloții de parapantă"))
_question.answers.append(Parag_Model_Answer(True, "implică folosirea unei hărți"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Reperele folosite in navigatie pot fi:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "repere fixe sau repere mobile"))
_question.answers.append(Parag_Model_Answer(True, "repere punctiforme sau repere lineare"))
_question.answers.append(Parag_Model_Answer(False, "repere statice sau dinamice"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Reperele de suprafață pot fi:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "orașe, lacuri"))
_question.answers.append(Parag_Model_Answer(False, "căi ferate, șosele, râuri"))
_question.answers.append(Parag_Model_Answer(False, "poduri, fabrici, ferme"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Vizibilitatea scăzută:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "nu influențeaza zborurile VFR"))
_question.answers.append(Parag_Model_Answer(False, "reprezintă distanța pe verticală de la care se pot observa reperele de la sol"))
_question.answers.append(Parag_Model_Answer(True, "poate fi cauzat de fum, ceață, ploaie"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Meridianul Greenwich se află la:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "longitudinea 0"))
_question.answers.append(Parag_Model_Answer(False, "longitudinea 45 si latitudinea 45"))
_question.answers.append(Parag_Model_Answer(False, "latitudinea 90"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Directia vest corespunde cu:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "90 grade"))
_question.answers.append(Parag_Model_Answer(False, "180 grade"))
_question.answers.append(Parag_Model_Answer(True, "270 grade"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Documentul de bază pentru informarea tuturor operatorilor în vederea efectuării activității de zbor pe teritoriul României este:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "F.I.R."))
_question.answers.append(Parag_Model_Answer(True, "A.I.P"))
_question.answers.append(Parag_Model_Answer(False, "N.A.V."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Alegeți afirmația adevărată cu privire la viteza indicata a unei aeronave IAS (viteza indicată de vitezometru aflat la bordul aeronavei bazat pe capsula manometrică):")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "în cazul în care viteza vântul WS este 0, va fi întotdeauna egal cu viteza aeronavei față de sol GS"))
_question.answers.append(Parag_Model_Answer(True, "este influențat de densitatea aerului"))
_question.answers.append(Parag_Model_Answer(False, "nu depinde de înălțimea de zbor"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ora universala coordinata UTC este:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "ora locală la meridianul 0 "))
_question.answers.append(Parag_Model_Answer(False, "ora locală de la aerodromul de plecare"))
_question.answers.append(Parag_Model_Answer(False, "este ora de la miezul nopții"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Diferența între LMT și UTC este aceeași :")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "de a lungul aceluiași meridian de longitudine"))
_question.answers.append(Parag_Model_Answer(False, "indiferent de poziția pe glob"))
_question.answers.append(Parag_Model_Answer(False, "de a lungul aceluiași meridian de latitudine"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ora apusului și răsăritului la o anumită dată:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "nu depinde de latitudine"))
_question.answers.append(Parag_Model_Answer(False, "nu depinde de longitudine"))
_question.answers.append(Parag_Model_Answer(True, "depinde atât de latitudine cît și de longitudine"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ora apusului și răsăritului: ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "se schimbă în cursul anului"))
_question.answers.append(Parag_Model_Answer(False, "nu se schimbă față de UTC"))
_question.answers.append(Parag_Model_Answer(False, "diferă în funcție de condițiile meteorologice"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Următoarea caracteristică a unei hărți ne ajută la calcularea directă a distanței prin măsurare pe hartă:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "nivelmentul"))
_question.answers.append(Parag_Model_Answer(False, "planimetria"))
_question.answers.append(Parag_Model_Answer(True, "scara hărții"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Daca o harta are scala 1:50.000 două puncte aflate la o distanță de 32 cm vor fi în realitate la:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "50 km"))
_question.answers.append(Parag_Model_Answer(True, "16 km"))
_question.answers.append(Parag_Model_Answer(False, "32 km"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Conditiile de vizibilitate minimă pentru zborurile VFR sunt stabilite prin:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "RACR LPAS"))
_question.answers.append(Parag_Model_Answer(False, "RACR AUN"))
_question.answers.append(Parag_Model_Answer(True, "RACR RA"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Pentru efectuarea cu parapanta unui zbor de 300 de km:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "se va alege o hartă de navigție la scara de 1:500000 în care sunt marcate mai multe detalii necesare desfășurării zborului"))
_question.answers.append(Parag_Model_Answer(False, "se va alege harta lumii unde exista posibilitatea marcării ortodromei în vederea determinării elementelor de zbor"))
_question.answers.append(Parag_Model_Answer(False, "nu este necesară folosirea unei hărți deoarece cu parapanta se zboară la vedere"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Paralelele de latitudine sunt:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "paralele cu meridianul Greenwich"))
_question.answers.append(Parag_Model_Answer(False, "paralele cu loxodroma"))
_question.answers.append(Parag_Model_Answer(True, "paralele cu ecuatorul"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Prescurtarea AWY semnifică:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "pistă de decolare/aterizare"))
_question.answers.append(Parag_Model_Answer(False, "regiune de control aerodrom"))
_question.answers.append(Parag_Model_Answer(True, "cale aeriană"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Regiunile terminale de control:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "sunt spații aeriene rezervate"))
_question.answers.append(Parag_Model_Answer(True, "sunt spații aeriene controlate"))
_question.answers.append(Parag_Model_Answer(False, "sunt spații aeriene necontrolate"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Zonele de control de aerodrom sunt spații aeriene cu dimensiuni stabilite pe verticală:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "de la o anumită altitudine/înălțime pînă la o anumită altitudine/înălțime"))
_question.answers.append(Parag_Model_Answer(True, "de la nivelul solului pînă la o anumită altitudine/înălțime"))
_question.answers.append(Parag_Model_Answer(False, "nu are limite stabilite pe verticală, doar pe orizontală"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Alegeți care clasă de spațiu aerian se regăsește în FIR București:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "clasa B"))
_question.answers.append(Parag_Model_Answer(True, "clasa C"))
_question.answers.append(Parag_Model_Answer(False, "clasa D"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("În spațiul aerian de clasa C sunt permise:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "numai zboruri IFR"))
_question.answers.append(Parag_Model_Answer(False, "numai zboruri VFR"))
_question.answers.append(Parag_Model_Answer(False, "zboruri VFR și IFR"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Pentru efectuarea unui zbor în spațiu aerian de clasa C este obligatorie:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "efectuarea unei informări de trafic VFR"))
_question.answers.append(Parag_Model_Answer(True, "depunerea unui plan de zbor"))
_question.answers.append(Parag_Model_Answer(False, "obținerea autorizației de survol"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Comunicațiile radio bilaterale în cazul zborurilor VFR:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "sunt obligatorii în spațiul aerian de clasă C"))
_question.answers.append(Parag_Model_Answer(False, "sunt obligatorii în spațiul aerian de clasă G"))
_question.answers.append(Parag_Model_Answer(False, "în spațiile aeriene din FIR București nu sunt obligatorii"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Spațiu aerian de clasă G are limita superioară la maxim:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "FL195"))
_question.answers.append(Parag_Model_Answer(False, "4000 metrii ASL"))
_question.answers.append(Parag_Model_Answer(True, "FL100"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("În ce condiții un zbor VFR efectuat în întregime în spațiu aerian de clasa G se consideră autorizat:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "s-a obținut o autorizație de survol"))
_question.answers.append(Parag_Model_Answer(True, "s-a depus un plan de zbor sau o informare de trafic"))
_question.answers.append(Parag_Model_Answer(False, "s-a obținut avizul Ministerului Apărării Naționale"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Zonele de control de aerodrom pe hărțile de navigație sunt prescurtate:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "ZCA"))
_question.answers.append(Parag_Model_Answer(True, "CTR"))
_question.answers.append(Parag_Model_Answer(False, "TRA"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("În FIR București spațiile aeriene de tip TMA pot fi:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "clasa C si clasa G"))
_question.answers.append(Parag_Model_Answer(False, "clasa A și clasa B"))
_question.answers.append(Parag_Model_Answer(True, "clasa A și clasa C"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Conform RACR RA un zbor VFR (cu excepția: decolării, aterizării sau  autorizării corespunzătoare acordate de autoritatea competentă) nu va fi efectuat:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "la o înălțime mai mare de 2000 de metrii AGL"))
_question.answers.append(Parag_Model_Answer(False, "la o înălțime mai mare de 2000 de metrii AGL"))
_question.answers.append(Parag_Model_Answer(True, "la o înălțimea mai mică de 150 de metrii AGL"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("În cazul în care planul de zbor se depune de la sol acesta va fi depus înaintea decolării cu cel puțin:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "10 minute"))
_question.answers.append(Parag_Model_Answer(False, "24 ore"))
_question.answers.append(Parag_Model_Answer(True, "o oră"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Conform HG 912/2017 decolarea și aterizarea parapantelor se poate face:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "numai de pe aerodromuri certificate"))
_question.answers.append(Parag_Model_Answer(False, "de pe aerodromuri certificate și de pe terenuri extravilane cu acordul Primăriei"))
_question.answers.append(Parag_Model_Answer(True, "de pe orice teren cu acordul proprietarului"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Pentru a efectua un zbor în spațiu aerian de clasă G pilotul este obligat să se informeze cu privire la limitările și restricțiile aplicabile zborului respectiv din următoarele surse:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "AIP"))
_question.answers.append(Parag_Model_Answer(True, "circularele aeronautice"))
_question.answers.append(Parag_Model_Answer(True, "mesajele de tip Notam"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Pentru a zbura în spațiu aerian rezervat, segregat sau restricționat un pilot trebuie obligatoriu să aibă:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "transponder"))
_question.answers.append(Parag_Model_Answer(True, "autorizarea unității de trafic sau a entității care a făcut rezervarea, respectiv a cerut utilizarea exclusiva a zonei respective"))
_question.answers.append(Parag_Model_Answer(False, "plan de zbor și statie radio în bandă de aviație pentru a realiza comunicații radio bilaterale"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Radiofarul nondirectional NDB este:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "un mijloc de radio comunicație"))
_question.answers.append(Parag_Model_Answer(False, "sistem de localizare a aeronavelor aflate în pericol"))
_question.answers.append(Parag_Model_Answer(True, "un mijloc de radionavigație"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Echipamentul DME asociat unei stații terestre VOR:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "înbunătățește semnalul VHF transmis de stația terestră VOR"))
_question.answers.append(Parag_Model_Answer(True, "este un echipament de măsurare a distanței "))
_question.answers.append(Parag_Model_Answer(False, "nu se folosește la noi în țară"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care din următoarele tipuri de spațiu aerian aflate în FIR București este de clasă A:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "CTR Otopeni"))
_question.answers.append(Parag_Model_Answer(True, "TMA București"))
_question.answers.append(Parag_Model_Answer(False, "AWY Cluj Napoca – Budapesta"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce clasă de spațiu aerian sunt rutele ATS din FIR București:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "clasa A"))
_question.answers.append(Parag_Model_Answer(True, "clasa C"))
_question.answers.append(Parag_Model_Answer(False, "clasa G"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce clasă de spațiu aerian este TMA NAPOC")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "clasa A"))
_question.answers.append(Parag_Model_Answer(False, "clasa B"))
_question.answers.append(Parag_Model_Answer(True, "clasa C"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Peste nivelul FL105 în FIR București putem avea spațiu aerian de clasa:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "A și C"))
_question.answers.append(Parag_Model_Answer(False, "A, C și G"))
_question.answers.append(Parag_Model_Answer(False, "A, B și C"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Pe o hartă aeronautică prescurtarea LR P semnifică o zonă restricționată de tip:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "restricționat"))
_question.answers.append(Parag_Model_Answer(False, "periculos"))
_question.answers.append(Parag_Model_Answer(True, "interzis"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("În interiorul unei zone notate cu LR D:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "se pot desfășura activități periculoase pentru zborul aeronavelor"))
_question.answers.append(Parag_Model_Answer(False, "zborul aeronavelor este interzis"))
_question.answers.append(Parag_Model_Answer(False, "nu sunt activități care să restricționeze zborul aeronavelor "))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("În zonele de tip TRA:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "se poate zbura dacă s-a obținut o autorizare ATC "))
_question.answers.append(Parag_Model_Answer(False, "nu se poate zbura zona fiind segregată pentru utilizare exclusivă"))
_question.answers.append(Parag_Model_Answer(False, "se poate zbura dacă s-a făcut o informare de trafic"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("În zonele de tip TSA:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "se poate zbura dacă s-a obținut o autorizare ATC "))
_question.answers.append(Parag_Model_Answer(True, "nu se poate zbura zona fiind segregată pentru utilizare exclusivă"))
_question.answers.append(Parag_Model_Answer(False, "se poate zbura dacă s-a făcut o informare de trafic"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Pentru definirea pe verticală a unei zone de tip TMA avem:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "numai limită inferioară"))
_question.answers.append(Parag_Model_Answer(True, "limită inferioară și superioară"))
_question.answers.append(Parag_Model_Answer(False, "numai limită superioară"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Pentru definirea pe verticală a unei zone de tip CTR avem:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "numai limită inferioară"))
_question.answers.append(Parag_Model_Answer(False, "limită inferioară și superioară"))
_question.answers.append(Parag_Model_Answer(True, "numai limită superioară"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("În FIR București între nivelul FL105 și nivelul FL190 putem avea următoarele clase de spațiu aerian:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "A, C, G"))
_question.answers.append(Parag_Model_Answer(False, "numai A"))
_question.answers.append(Parag_Model_Answer(True, "A și C"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("În FIR București spațiu aerian de clasă G cuprinde:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "toate zonele de control ale aviației utilitare și sportive"))
_question.answers.append(Parag_Model_Answer(True, "întregul spațiu aerian din FIR București care nu este desemnat ca având o altă clasă"))
_question.answers.append(Parag_Model_Answer(True, "zonele restricționate"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("În FIR București zonele de tip CTR sunt spații aeriene de:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "clasă A"))
_question.answers.append(Parag_Model_Answer(True, "clasă C"))
_question.answers.append(Parag_Model_Answer(False, "clasă G"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("În spațiu aerian de clasă A")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "sunt numai zboruri IFR"))
_question.answers.append(Parag_Model_Answer(False, "sunt zboruri VFR și IFR"))
_question.answers.append(Parag_Model_Answer(False, "sunt numai zboruri VFR"))