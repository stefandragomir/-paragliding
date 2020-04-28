from parag_model.parag_model  import *

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_category        = Parag_Model_Category()
_category.name   = "performante de zbor"
PARAG_CATEGORY_8 = _category

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Durata tipului de zbor: Deal Vale - DV  in conditii de vant anabatic comparativ cu vant catabatic este:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "mai lunga pe anabatic"))
_question.answers.append(Parag_Model_Answer(True, "mai scurta pe catabatic "))
_question.answers.append(Parag_Model_Answer(False, "la fel"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce reguli de zbor se aplică categoriei de aeronave din care face parte parapanta:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "reguli de zbor IFR"))
_question.answers.append(Parag_Model_Answer(True, "reguli de zbor VFR "))
_question.answers.append(Parag_Model_Answer(False, "VFR si IFR"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("La efectuarea informarii de zbor VFR in spaţiul clasa G:  ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "se comunica: locatia, inaltimea, persoana de contact, ora de incepere                                      "))
_question.answers.append(Parag_Model_Answer(True, "aveţi obligaţia de a respecta cerinţele, limitările şi restricţiile aplicabile publicate"))
_question.answers.append(Parag_Model_Answer(False, "in spatiul aerian de clasa G nu este necesar autorizarea zborurilor"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Creşterea vitezei fata de sol duce la: ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "creşterea rezistenţei la înaintare    "))
_question.answers.append(Parag_Model_Answer(True, "cresterea finetei "))
_question.answers.append(Parag_Model_Answer(False, "solicitarea mai mare a structurii aripii"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("La decolare este indicat să se planifice o distanţă de rezervă pentru alergare?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "da, daca vantul este slab  "))
_question.answers.append(Parag_Model_Answer(True, "da, daca incarcarea aripii este mai mare"))
_question.answers.append(Parag_Model_Answer(False, "nu, daca terenul are o inclinatie mica"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Vântul influenţează distanţa de aterizare astfel:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "vântul de faţă reduce distanţa   "))
_question.answers.append(Parag_Model_Answer(False, "vântul de faţă măreşte distanţa"))
_question.answers.append(Parag_Model_Answer(False, "vântul de spate reduce distanţa"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Aeronavele nemotorizate care zboară în spaţiul aerian necontrolat sunt obligate să respecte înălţimile minime de siguranţa publicate în:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AIP Romania"))
_question.answers.append(Parag_Model_Answer(True, "RACR-RA"))
_question.answers.append(Parag_Model_Answer(False, "Zborurile VFR nu sunt supuse restrictilor referitoare la inaltimi minime."))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care sunt clasele de spaţiu aerian în care  sunt obligatorii comunicaţiile radio pentru zborurile VFR:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "A"))
_question.answers.append(Parag_Model_Answer(True, "C"))
_question.answers.append(Parag_Model_Answer(False, "G"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question(" Cand nu este recomandat de a zbura in afara intervalului de greutate stabilit de producator:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "sub limita inferioara"))
_question.answers.append(Parag_Model_Answer(False, "peste limita  superioara"))
_question.answers.append(Parag_Model_Answer(True, "niciodata"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question(" Care sunt riscurile daca se zboara cu aripa uda")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "nici un risc, umezeala nu afecteaza performantele"))
_question.answers.append(Parag_Model_Answer(True, "aripa se poate angaja"))
_question.answers.append(Parag_Model_Answer(True, "aripa nu-si mai revine din eventualele evolutii"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Prin efectuarea manevrei urechi mari este posibil sa:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "creasca unghiul de incidenta pana la unghiul critic de angajare"))
_question.answers.append(Parag_Model_Answer(False, "scada unghiul de incidenta si aripa va zbura mai rapid"))
_question.answers.append(Parag_Model_Answer(False, "nu afecteze unghiul de incidenta"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Prin actionarea acceleratorului se muta: ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "centrul de greutate"))
_question.answers.append(Parag_Model_Answer(True, "centrul de presiune"))
_question.answers.append(Parag_Model_Answer(False, "centrul geometric"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question(" Cand nu este recomandat a zbura cu aripa incarcata la limitele inferioare")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "pe vant cu intensitate ridicata"))
_question.answers.append(Parag_Model_Answer(False, "pe conditii cu turbulente accentuate"))
_question.answers.append(Parag_Model_Answer(True, "pe nici una din conditiile de mai sus "))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Daca forta portanta (Fz) este egală cu greutatea (G). ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "se obtine zborul orizontal"))
_question.answers.append(Parag_Model_Answer(False, "se obtine viteza maxima"))
_question.answers.append(Parag_Model_Answer(True, "se obtine finetea maxima fata de sol"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Viteza vantului este egal cu viteaza de trim a aripii")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "la decolare aripa va decola in verticala"))
_question.answers.append(Parag_Model_Answer(True, "la aterizare va cobori in verticala"))
_question.answers.append(Parag_Model_Answer(True, "cu vant de spate vom obtine viteza dubla"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question(" Finetea maxima obtinem fata de sol")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "cu vant de fata"))
_question.answers.append(Parag_Model_Answer(True, "cu vant de spate"))
_question.answers.append(Parag_Model_Answer(False, "prin incarcarea maxima a aripii"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care sunt factorii prin care se pot obtine performante mai bune de zbor          ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "parapanta"))
_question.answers.append(Parag_Model_Answer(True, "conditia meteo"))
_question.answers.append(Parag_Model_Answer(True, "pilotul"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question(" De unde obtinem urmatoarea informatie: la ce viteaza si infundare se atinge finetea maxima fata de fileele de aer")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "din polara aripii"))
_question.answers.append(Parag_Model_Answer(False, "din gps cu datele masurate fata de sol"))
_question.answers.append(Parag_Model_Answer(False, "din manualul aripii"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care dintre urmatoarele factori influenteaza decolarea aeronavei:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "greutatea totala in zbor"))
_question.answers.append(Parag_Model_Answer(True, "directia si intensitatea vantului"))
_question.answers.append(Parag_Model_Answer(True, "panta decolarii"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Distante maxime in zbor pot fi atinse:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "cu vant de spate"))
_question.answers.append(Parag_Model_Answer(False, "cu vant de fata"))
_question.answers.append(Parag_Model_Answer(False, "cu vant nul"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("O aripa incarcata spre limita maxima va avea distanta:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "mai mare de alergare la aterizare pe vant nul "))
_question.answers.append(Parag_Model_Answer(False, "mai mare de alergare pe vant de fata"))
_question.answers.append(Parag_Model_Answer(True, "mai mare de alergare pe vant de spate"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question(" Cazul in care intensitatea vantului este mare, priza de aterizare se face:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "mai aproape de punctul fix si cu vant de fata"))
_question.answers.append(Parag_Model_Answer(False, "de mai departe si cu vant de fata"))
_question.answers.append(Parag_Model_Answer(False, "de mai aproape si cu vant de spate"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question(" Elementele planificarii zborului sunt:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "verificarea disponibilitatii spatiului aerian, eventualele restrictii"))
_question.answers.append(Parag_Model_Answer(True, "informare de zbor "))
_question.answers.append(Parag_Model_Answer(True, "conditiile meteo, alegerea locului de zbor"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Pentru selectarea rutei zborului se va tine cont de:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "performantele aripii, "))
_question.answers.append(Parag_Model_Answer(True, "meteo, relieful "))
_question.answers.append(Parag_Model_Answer(True, "spatiul aerian"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("In spatiul aerian de clasa G, Autorizarea ATC:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "este obligatorie pentru zborurile VFR"))
_question.answers.append(Parag_Model_Answer(True, "nu este obligatorie pentru zborurile VFR"))
_question.answers.append(Parag_Model_Answer(False, "este obligatorie pentru zborurile IFR"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("In Spatiul aerian de clasa G")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "este obligatoriu comunicare radio pentru zborurile VFR"))
_question.answers.append(Parag_Model_Answer(False, ") nu este obligatorie comunicatiile radio pentru zborurile VFR"))
_question.answers.append(Parag_Model_Answer(False, "zborurile IFR nu sunt permise"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Aeronavele ultrausoare clasa parapanta fara comunicare radio pot zbura in spatiul aerian de clasa")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "G"))
_question.answers.append(Parag_Model_Answer(False, "C"))
_question.answers.append(Parag_Model_Answer(False, "A"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question(" Informatiile necesare pentru a efectua o informare de zbor sunt:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "nume, prenume, ora inceperii, nr de parapante, locatia, inaltimea, nr de telefon, "))
_question.answers.append(Parag_Model_Answer(False, "nume, prenume, nr de parapante, locatia, inaltimea, nr de telefon, "))
_question.answers.append(Parag_Model_Answer(False, "nume, prenume, ora inceperii, locatia, inaltimea, nr de telefon, "))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Planificarea, respectiv efectuarea zborului este influentata de:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "ploaie"))
_question.answers.append(Parag_Model_Answer(True, "ceata"))
_question.answers.append(Parag_Model_Answer(True, "turbulenta puternica "))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Pentru decolare se va alege o pantă care să îndeplinească urmatoarele condiții:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "vântul să fie de față"))
_question.answers.append(Parag_Model_Answer(False, "între locul de decolare și aterizare să nu fie obstacole "))
_question.answers.append(Parag_Model_Answer(False, "de la locul de decolare să se vadă locul de aterizare"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("La intrarea în termică:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "parapanta va avea unghi de incidență mic"))
_question.answers.append(Parag_Model_Answer(False, "se va frîna parapanta cât mai mult"))
_question.answers.append(Parag_Model_Answer(True, "aripa rămîne în spatele pilotului"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Manevra de spirala poate fi periculoasa deoarece:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "datorita fortei centrifuge mari parapanta se poate rupe"))
_question.answers.append(Parag_Model_Answer(True, "pilotul poate să leșine"))
_question.answers.append(Parag_Model_Answer(False, "parapanta se poate angaja"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("În cazul în care două aparate de zbor se întâlnesc se vor ocoli:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "prin stânga"))
_question.answers.append(Parag_Model_Answer(True, "prin dreapta"))
_question.answers.append(Parag_Model_Answer(False, "ambii piloți vor reduce viteza"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Aterizarea pe o pantă cu înclinație mare in situația în care vîntul bate perfect de față se va face:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "în contrapantă "))
_question.answers.append(Parag_Model_Answer(False, "paralel cu panta"))
_question.answers.append(Parag_Model_Answer(True, "cu vânt de față"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Aripile care sunt recomandate unui elev pilot fără experiență de zbor cu parapanta sunt cele care au omologarea:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "LTF 1"))
_question.answers.append(Parag_Model_Answer(False, "LTF 2"))
_question.answers.append(Parag_Model_Answer(False, "LTF 3"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Când calculăm încărcarea voalurii luăm în calcul:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "greutatea parapantei"))
_question.answers.append(Parag_Model_Answer(True, "greutatea pilotului"))
_question.answers.append(Parag_Model_Answer(True, "greutatea seletei"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Zborul cu parapanta în nor:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "este permis doar dacă norii nu au dezvoltare pe verticală"))
_question.answers.append(Parag_Model_Answer(True, "nu este permis"))
_question.answers.append(Parag_Model_Answer(False, "este permis în cazul norilor de tip cumulus"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Modificarea unghiului de incidență la o parapantă se poate face prin:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "prin sistemul de speed"))
_question.answers.append(Parag_Model_Answer(False, "nu este posibil "))
_question.answers.append(Parag_Model_Answer(True, "prin trimere"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Viteza maximă de zbor a unei parapante poate fi influențată de:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "forma și mărimea seletei"))
_question.answers.append(Parag_Model_Answer(True, "greutatea pilotului"))
_question.answers.append(Parag_Model_Answer(False, "nu poate fi influențat"))