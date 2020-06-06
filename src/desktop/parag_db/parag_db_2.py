from parag_model.parag_model  import *

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_category        = Parag_Model_Category()
_category.name   = "legislatie"
PARAG_CATEGORY_2 = _category

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care este principalul act normativ care reglementeza activitatea de zbor in Romania?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "OMTCT 630/2007"))
_question.answers.append(Parag_Model_Answer(True,  "Legea 399/2005"))
_question.answers.append(Parag_Model_Answer(False, "HG 912/2010"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("RACR-LPAN AUN stabileste cerintele specifice aplicabile pentru")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "obtinerea revalidarea, si reinoirea licentei de pilot aeronave ultrausoare"))
_question.answers.append(Parag_Model_Answer(True, "autorizarea ca examinatori a persoanelor care organizeaza si efectueaza examinarile teoretice si practice"))
_question.answers.append(Parag_Model_Answer(True, "obtinerea altor calificari specifice licentei de pilot aeronave ultrausoare"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Principala autoritate din Romania in domeniul aeronautic este")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AACR- Autoritatea Aeronautica Civila"))
_question.answers.append(Parag_Model_Answer(True,  "MTI – Ministerul Transporturilor si Infrastructurii"))
_question.answers.append(Parag_Model_Answer(False, "AZLR – Asociatia de Zbor Liber din Romania"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Zborurile in interes propriu reprezinta conform Codului Aerian")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "operatiuni de  aviatie generala, efectuate de persoane fizice sau juridice, cu aeronave civile proprii sau inchiriate, pentru si in sustinerea nevoilor proprii, fara perceperea de tarife"))
_question.answers.append(Parag_Model_Answer(False, "operatiuni de  aviatie generala, efectuate de catre detinatorii de aeronave civile, persoane fizice , exclusiv in scop necomercial"))
_question.answers.append(Parag_Model_Answer(False, "operatiuni de  aviatie generala organizate de persoane fizice sau juridice cu aeronave civile proprii in vederea pregatirii personalului aeronautic civil navigant, fara perceperea de tarife"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Pentru obtinerea  licentei de instructor AUN, o persoana trebuie sa indeplineasca urmatoarele conditii specifice")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "sa demonstreze ca a abolvit in ultimele 12 luni un program de pregatire teoretica si practica la sol si in zbor care cuprinde disciplina „ Metodologia zborului in tandem” cu un instructor autorizat"))
_question.answers.append(Parag_Model_Answer(True,  "sa detina  de cel putin 5 ani o licenta de pilot de aeronave ultrausoare nemotorizate din clasa pentru care solicita calificarea, in termen de valabilitate"))
_question.answers.append(Parag_Model_Answer(False, "sa aiba varsta de 21 ani impliniti, sa detina un certificat medical corespunzator"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Documentele necesare reinoirii licentei de pilot sunt urmatoarele")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "certificat medical corespunzator,  carnet de zbor care sa ateste activitatea de   zbor declaratie de responsabilitate, teste teoretice, proces verbal de examinare, cerere specifica"))
_question.answers.append(Parag_Model_Answer(False, "certificat medical corespunzator, teste teoretice, proces verbal de examinare, carnet de zbor, cerere de specifica"))
_question.answers.append(Parag_Model_Answer(True,  "certificat medical corespunzator, fisa de pregatire teoretica si practica, teste de  examinare, proces verbal de examinare, carnet de  zbor, cerere specifica"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Varsta minima de la care o persoana romana poate desfasura activitati  de zbor cu aeronave ultrausoare nemotorizate in calitate de pilot este conform OM630/2007")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "16 ani impliniti"))
_question.answers.append(Parag_Model_Answer(False, "18 ani impliniti"))
_question.answers.append(Parag_Model_Answer(False, "15 ani impliniti"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Eliberarea licentelor personalului aeronautic navigant , aeronave ultrausoare  nemotorizate se face conform legii:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "postal , detinatorului licentei"))
_question.answers.append(Parag_Model_Answer(True,  "doar titularului pe baza de semnatura sau unui imputernicit legal al acestuia"))
_question.answers.append(Parag_Model_Answer(False, "instructorului care a efectuat pregatirea sau a depus dosarul titularului"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Parapantele de tandem pentru a putea efectua zboruri cu alte persoane decat elevii piloti  e obligatoriu sa detina")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "certificat de identificare, sau certificat de omologare"))
_question.answers.append(Parag_Model_Answer(True,  "ştampila sau eticheta fabricantului sau orice alt document de omologare"))
_question.answers.append(Parag_Model_Answer(False, "nu este necesara nici un document"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Conform RACR-REAC, in categoria activitatilor ulterioare raportarii evenimentelor de aviatie civila obligatia agentului aeronautic civil este")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "sa desfasoare o cercetare/investigatie proprie interna interna imediata pentru orice eveniment care a afectat sau poate afecta siguranta in vederea stabilirii de masuri corective, necesare pentru prevenirea unor elemente similare"))
_question.answers.append(Parag_Model_Answer(False, "sa verifice daca masurile corective necesare  stabilite in urma cercetarii/investigatiei sunt implementate si efective"))
_question.answers.append(Parag_Model_Answer(False, "sa investigheze tehnic accidentele si incidentele grave conform legii"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Orice accident sau incident grav de aviatie civila se raporteaza telefonic imediat sau in scris in maxim 6 ore direct la ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "AACR, IavC"))
_question.answers.append(Parag_Model_Answer(False, "AACR, AZLR"))
_question.answers.append(Parag_Model_Answer(False, "AACR, AR"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("In conformitate cu OM630/2007, o aeronava AUN neomologata, poate fi folosita in procesul de instruire?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "pentru parapante si deltaplane nu este necesar ca aeronava sa fie omologata, nicaieri, in consecinta poate fi folosita in procesul de instruire"))
_question.answers.append(Parag_Model_Answer(True,  "poate fi folosita in procesul de instruire doar daca proprietarul acesteia este si persoana instruita"))
_question.answers.append(Parag_Model_Answer(False, "in procesul de instruire se folosesc doar aeronave omologate care poseda certificat de identificare, sau certificat de omologare"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Conform legislatiei aeronautice in vigoare cu privire la domeniul aeronavelor ultrausoare nemotorizate, continutul minim obligatoriu al programei de pregatire teoretica si practica la sol si in zbor a pilotilor din clasa parapanta este")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "50 ore teorie si 12 ore de zbor"))
_question.answers.append(Parag_Model_Answer(True,  "50 ore teorie si 10 ore de zbor"))
_question.answers.append(Parag_Model_Answer(False, "50 ore teorie si 15 ore de zbor"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Varsta minima de la care o persoana romana poate desfasura activitati  de zbor cu aeronave ultrausoare nemotorizate este conform OM630/2007")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "16 ani impliniti"))
_question.answers.append(Parag_Model_Answer(False, "18 ani impliniti"))
_question.answers.append(Parag_Model_Answer(True,  "15 ani impliniti"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("RACR-REAC, se aplica de catre persoanele fizice si juridice  implicate in activitati aeronautice ori de cate ori")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "un accident sau incident grav s-a produs pe teritoriul Romaniei indiferent de inmatriculare sau operator"))
_question.answers.append(Parag_Model_Answer(True,  "un incident s-a produs in afara teritoriului Romaniei si este in legatura cu o aeronava civila, inmatriculata in Romania, sau operata de un agent aeronautic civil"))
_question.answers.append(Parag_Model_Answer(False, "aceasta reglemetare se aplica doar de catre personalul civil aeronautic navigant"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Procesul verbal de examinare se intocmeste de catre")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "elevul pilot"))
_question.answers.append(Parag_Model_Answer(True,  "examinatorul autorizat"))
_question.answers.append(Parag_Model_Answer(False, "instructorul care a efectuat pregatirea"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Valabilitatea testelor teoretice si a testelor de indemanare  si competenta in zbor este")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "3 luni de la data sustinerii acestora"))
_question.answers.append(Parag_Model_Answer(True,  "6 luni de la data sustinerii acestora"))
_question.answers.append(Parag_Model_Answer(False, "12 luni de la data sustinerii acestora"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Revalidarea este")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "procedeu administrativ efectuat in interiorul perioadei de valabilitate a unei calificari sau autorizatii"))
_question.answers.append(Parag_Model_Answer(False, "procedeu administrativ efectuat dupa ce ce o calificare sau autorizatie a expirat"))
_question.answers.append(Parag_Model_Answer(False, "nici unul din raspunsurile enumerate mai sus"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Securitatea zborului este")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "capacitatea sistemului aeronautic de a indeplini in mod satisfacator functiunile sale la un moment dat sau intr-o perioada de timp data cand e folosit in anumite conditii"))
_question.answers.append(Parag_Model_Answer(True,  "capacitatea activitatii aeronautice constand in evitarea afectarii sanatatii sau pierderii de vieti omenesti, precum si a producerii de pagube materiale"))
_question.answers.append(Parag_Model_Answer(False, "un eveniment legat de utilizarea unei aeronave ca urmare a aparitiei intamplatoare a unor factori de natura sa puna in pericol activitatea de zbor"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Pentru a opera in conditiile legii o aeronava AUN, o persoana este necesar sa detina")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "licenta de pilot pe clasa de aeronave pe care opereaza"))
_question.answers.append(Parag_Model_Answer(True, "asigurare pentru pagube produse tertilor"))
_question.answers.append(Parag_Model_Answer(True, "informare de zbor sau dupa caz plan de zbor"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Timpul minim  de pregatire recomandat la disciplina proceduri operationale este")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "4 ore"))
_question.answers.append(Parag_Model_Answer(False, "2 ore"))
_question.answers.append(Parag_Model_Answer(False, "6 ore"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Pentru revalidarea licentei de pilot aeronave ultrausoare nemotorizate este necesar ca si conditie specifica ca solicitantul sa  demonstreze ca")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "a efectuat in ultimele 12 luni minimum 5 ore de zbor incluzand 10 decolari si 10 aterizari in calitate de pilot pe clasade aeronave pentru care se solicita revalidarea"))
_question.answers.append(Parag_Model_Answer(False, "a efectuat in ultimele 12 luni minimum 3 ore de zbor incluzand 5 decolari si 5 aterizari in calitate de pilot pe clasade aeronave pentru care se solicita revalidarea"))
_question.answers.append(Parag_Model_Answer(True,  "a efectuat in ultimele 12 luni minimum 2 ore de zbor incluzand 5 decolari si 5 aterizari in calitate de pilot pe clasade aeronave pentru care se solicita revalidarea"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Conform Codului Aerian al Romaniei, art.3.12 , autorizarea reprezinta")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "confirmarea oficiala data printr-un document eliberat, prin care se atesta capacitatea detinatorului de a desfasura activitatile aeronautice civile mentionate in acest document"))
_question.answers.append(Parag_Model_Answer(False, "recunoasterea faptului ca un serviciu, un produs, o piesa sau un echipament, o organizatie sau o persoana se conformeaza cerintelor aplicabile"))
_question.answers.append(Parag_Model_Answer(False, "document emis ca rezultat al certificarii, in conformitate cu reglementarile specifice aplicabile"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Conform Codului Aerian, cap XII scopul investigatiei tehnice in cazul incidentelor si accidentelor de aviatie il reprezinta")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "stabilirea faptelor, cauzelor si imprejurarilor care au condus la producerea incidentului sau a accidentului de aviatie civila, precum si identificarea masurilor preventive corespunzatoare"))
_question.answers.append(Parag_Model_Answer(False, "cresterea sigurantei zborurilor, prin emiterea de recomandari in vederea prevenirii producerii unor incidente sau accidente similare in aviatia civila"))
_question.answers.append(Parag_Model_Answer(False, "stabilirea responsabilitatilor, a persoanelor vinovate, a gradului de vinovatie, precum si aplicarea sanctiunilor"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Planul de zbor reprezinta")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "o ruta definita si proiectata astfel incat fluxul traficului aerian sa fie orientat in functie de necesitati"))
_question.answers.append(Parag_Model_Answer(False, "o metoda de navigatie care permite operarea unei aeronave pe orice traiectorie dorita, in limitele de acoperire a unor mijloace de navigatie"))
_question.answers.append(Parag_Model_Answer(True,  "ansamblu de informatii specifice furnizate serviciilor de trafic cu privire la zborul pe  care o aeronava urmeaza sa-l efectueze"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Constituie contraventii, conform Codului Aerian, daca nu au fost savarsite in astfel de conditii incat, potrivit legii, sa constituie infractiuni, urmatoarele fapte")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "refuzul comandantului unei aeronave civile de a prezenta persoanelor imputernicite, in conditiile legii, documentele obligatorii prevazute la art. 17 alin. (2), art. 36 alin. (2) si la art. 73 alin. (2)"))
_question.answers.append(Parag_Model_Answer(True, "neinformarea Ministerului Transporturilor, Constructiilor si Turismului cu privire la producerea incidentelor si accidentelor de aviatie civila, de catre cei care au aceasta obligatie in conformitate cu prevederile art. 90 alin. (2)"))
_question.answers.append(Parag_Model_Answer(True, "refuzul comandantului unei aeronave civile de a prezenta persoanelor imputernicite, in conditiile legii, documentele obligatorii prevazute la art. 17 alin. (2), art. 36 alin. (2) si la art. 73 alin. (2)."))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("NOTAM inseamna")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "publicatie emisa in numele statului roman sub autoritatea MTI, care contine informatii aeronautice de durata, esentiale pentru navigatia aeriana"))
_question.answers.append(Parag_Model_Answer(False, "ansamblu de informatii specifice furnizate unitatilor de trafic aerian cu privire la zborurile ce urmeaza a fi efectuate"))
_question.answers.append(Parag_Model_Answer(True,  "mesaj de notificare distribuit prin mijloace de telecomunicatii care contine informatii despre aparitia, starea, modificarea, oricarui mijloc serviciu, procedura sau hazard, informatii a caror cunoastere este esentiala pentru zbor"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("In cazul  reinnoirii licentei de pilot aeronave ultrausoare nemotorizate durata cursului de pregatire teoretica este")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "15 ore pentru o intrerupere mai mica de 5 ani"))
_question.answers.append(Parag_Model_Answer(True,  "10 ore pentru o intrerupere mai mica de 5 ani"))
_question.answers.append(Parag_Model_Answer(False, "25 ore pentru o intrerupere mai mica de 5 ani"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Dreptul  de a efectua activitatea de inspectie in teritoriu revine conform legii, inspectorilor autorizati de catre autoritatea de certificare")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "adevarat"))
_question.answers.append(Parag_Model_Answer(False, "fals"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("In cadrul procesului de examinare, inspectorul examinator, are obligatia sa verifice carnetul de zbor al persoanei  examinate")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "fals deoarece doar instructorul este cel care are acces la informatiile din carnetul de zbor"))
_question.answers.append(Parag_Model_Answer(False, "fals, deoarece fisa de pregatire este documentul care atesta orele de pregatire ale persoanei examinate"))
_question.answers.append(Parag_Model_Answer(True,  "adevarat"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Spatiu aerian restrictionat este  ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "portiunea de spatiu aerian in care zborul aeronavelor este interzis"))
_question.answers.append(Parag_Model_Answer(True,  "portiunea de spatiu aerian care se afla sub responsabilitatea unei autoritati"))
_question.answers.append(Parag_Model_Answer(True,  "portiunea de spatiu aerian in care in timpul unor perioade specificate se desfasoara activitati periculoase pentru zbor"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Zborul VFR al unei aeronave civile executat in intregime intr-o zona de spatiu aerian de clasa G se considera autorizat daca")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "aeronava este asigurata dupa caz cf legii pt daune produse tertilor"))
_question.answers.append(Parag_Model_Answer(False, "operatorul aeronavei a depus plan de zbor, sau a facut informare cf legii"))
_question.answers.append(Parag_Model_Answer(False, "in zona aeriana de clasa G nu este necesar nici un document"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Conform HG.912/2010, controlul utilizarii spatiului aerian se efectueaza de catre")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Ministerul Trasporturilor"))
_question.answers.append(Parag_Model_Answer(True,  "Ministerul Apararii"))
_question.answers.append(Parag_Model_Answer(False, "organele de trafic civile"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Examinarea practica pentru obtinerea/revalidarea si reinoirea calificarilor personalului aeronautic navigant se sustine intotdeauna dupa examinarea teoretica indiferent daca candidatul a obtinut 75% la aceasta")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "adevarat"))
_question.answers.append(Parag_Model_Answer(True,  "fals"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Operarea unei aeronave civile in spatiul aerian national pentru care nu s-a incheiat asigurare pentru pagube produse tertilor se pedepseste cu amenda de la")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "20000- 35000 lei"))
_question.answers.append(Parag_Model_Answer(False, "40000-50000 lei"))
_question.answers.append(Parag_Model_Answer(False, "50000 lei"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Inaltimea conform RACR-RA este definita ca")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "distanta verticala unui nivel punct sau obiect, considerat ca punct de la nivelul mediu al marii"))
_question.answers.append(Parag_Model_Answer(True,  "distanta verticala unui nivel punct sau obiect, considerat ca punct masurata de la un punct de referinta specificat"))
_question.answers.append(Parag_Model_Answer(False, "distanta verticala unui nivel punct sau obiect, considerat ca punct, masurat de la nivelul 0 al marii"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cererea de licentiere se intocmeste de catre")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "instructor"))
_question.answers.append(Parag_Model_Answer(False, "examinatorul autorizat"))
_question.answers.append(Parag_Model_Answer(True,  "elevul pilot"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Intreaga responsabilitate pentru actiunile desfasurate in timpul activitatii  de zbor revine conform legii")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "pilotului comandant"))
_question.answers.append(Parag_Model_Answer(False, "instructorilor aflati in zona"))
_question.answers.append(Parag_Model_Answer(False, "directorilor de concurs in cazul competitiilor sportive"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("In timpul procesului de pregatire, elevul pilot desfasoara activitate de zbor numai sub supravegherea instructorului")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "adevarat, deoarece instructorul este cel care stabileste temele de pregatire conform  programului de pregatire la sol si in zbor "))
_question.answers.append(Parag_Model_Answer(False, "fals, elevul poate efectua zboruri si in prezenta unor piloti avansati"))
_question.answers.append(Parag_Model_Answer(False, "adevarat deoarece instructorul este singura persoana abilitata sa supravegheze activitatea de pregatire la sol si in zbor"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Autoritatea de certificare poate retrage anula o calificare/autorizatie de aeronave ultrausoare nemotorizate")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "nu , deoarece o calificare odata obtinuta nu poate fi retrasa"))
_question.answers.append(Parag_Model_Answer(True,  "da, daca se constata ca titularul nu mai indeplineste conditiile minime specificate in reglementare"))
_question.answers.append(Parag_Model_Answer(True,  "da, daca titularul a fost implicat in actiuni de natura a afecta siguranta zborului "))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Zborurile VFR  se pot executa pentru desfasurarea de")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "operatiuni de transport aerian public"))
_question.answers.append(Parag_Model_Answer(True, "operatiuni de aviatie generala"))
_question.answers.append(Parag_Model_Answer(True, "operatiuni de lucru aerian"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Harta VFR AIP Romania cu indicativul LR-1 corespunde zonei")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Muntenia"))
_question.answers.append(Parag_Model_Answer(True,  "Transilvania"))
_question.answers.append(Parag_Model_Answer(False, "Moldova"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce cuprinde art.93 din Codul Aerian?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "contraventii"))
_question.answers.append(Parag_Model_Answer(False, "infractiuni"))
_question.answers.append(Parag_Model_Answer(False, "sanctiuni"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Harta VFR AIP Romania cu indicativul LR-1 corespunde zonei")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Muntenia"))
_question.answers.append(Parag_Model_Answer(True,  "Transilvania"))
_question.answers.append(Parag_Model_Answer(False, "Moldova"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Carnetul de zbor este obligatoriu in desfasurarea activitatilor de zbor cu aeronave ultrausoare  nemotorizate?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "da"))
_question.answers.append(Parag_Model_Answer(False, "nu"))
_question.answers.append(Parag_Model_Answer(False, "doar pe perioada de instruire"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Documentele necesare unui pilot strain pentru  a putea desfasura activitati de zbor pe teritoriul Romaniei sunt ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "licenta de pilot in termen de valabilitate"))
_question.answers.append(Parag_Model_Answer(True,  "IPPI Card"))
_question.answers.append(Parag_Model_Answer(False, "aviz din partea autoritatii de certificare"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Fisa de pregatire teoretica si practica la sol si in zbor se intocmeste de catre")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "inspectorul examinator"))
_question.answers.append(Parag_Model_Answer(True,  "instructorul sub supravegehrea caruia s-a finalizat pregatirea"))
_question.answers.append(Parag_Model_Answer(False, "elevul pilot, instructorul semneaza doar documentul"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Conform OM 630/2007 RACR-LPAN AUN 4010, testele grila in vederea examinarii sunt intocmite de catre")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "autoritatea de certificare"))
_question.answers.append(Parag_Model_Answer(True,  "autoritatea de certificare prin intermediul examinatorilor"))
_question.answers.append(Parag_Model_Answer(False, "autoritatea de certificare prin intermediul instructorilor"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Zborurile VFR  se executa ziua")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "intre rasaritul si apusul soarelui"))
_question.answers.append(Parag_Model_Answer(False, "cu 30 min dupa rasarit, si se incheie cu 30 min inainte de apus"))
_question.answers.append(Parag_Model_Answer(False, "dupa noua reglementare HG.912 nu mai exista regula"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Actul normativ care stabileste modul si conditiile de  certificare a personalului aeronautic in domeniul aeronavelor ultrausoare nemotorizate este")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Codul Aerian"))
_question.answers.append(Parag_Model_Answer(False, "RACR-RA"))
_question.answers.append(Parag_Model_Answer(True,  "OM 630/2007"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Asociatia de Zbor Liber din Romania este autoritate delegata de")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Directia Aviatiei Civile"))
_question.answers.append(Parag_Model_Answer(True,  "Autoritatea Aeronautica Civila"))
_question.answers.append(Parag_Model_Answer(False, "Ministerul Transporturilor"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Principala autoritate din Romania in domeniul aeronavelor ultrausoare nemotorizate este")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "AACR- Autoritatea Aeronautica Civila"))
_question.answers.append(Parag_Model_Answer(False, "MTI – Ministerul Transporturilor si Infrastructurii"))
_question.answers.append(Parag_Model_Answer(True,  "AZLR – Asociatia de Zbor Liber din Romania"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care este principalul act normativ care reglementeza activitatea de zbor cu aeronave ultrausoare in Romania?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "OMTCT 630/2007"))
_question.answers.append(Parag_Model_Answer(False, "Legea 399/2005"))
_question.answers.append(Parag_Model_Answer(False, "HG 912/2010"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Autoritatea de certificare, daca constata ca detinatorul unei licente nu mai indeplineste conditiile specificate in reglementari")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "poate suspenda licenta specifica"))
_question.answers.append(Parag_Model_Answer(True,  "poate retrage licenta specifica"))
_question.answers.append(Parag_Model_Answer(False, "odata o calificare dobandita ea nu mai poate fi retrasa"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Conform Codului Aerian în vigoare este considerat accident")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "rănirea gravă sau moartea atunci când persoana se află într-o aeronavă"))
_question.answers.append(Parag_Model_Answer(False, "producerea unui infarct miocardic în interiorul unei aeronave"))
_question.answers.append(Parag_Model_Answer(False, "rănirea unui pasager clandestin aflat în interiorul calei aeronavei"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Executarea de activiăţi de zbor cu aeronave ultrauşoare se face")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True,  "cu asumarea responsabilităţilor de către cei care zboară, în baza unei declaraţii tip"))
_question.answers.append(Parag_Model_Answer(True,  "cu respectarea reglementărilor aeronautice specifice şi generale din România"))
_question.answers.append(Parag_Model_Answer(False, "cu respectarea reglementărilor specifice, dar numai pentru cetăţenii români"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Pentru a putea zbura cu parapanta este necesar")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "să-ţi cumperi o parapantă"))
_question.answers.append(Parag_Model_Answer(True,  "să urmezi o şcoală zburând sub îndrumarea instructorului"))
_question.answers.append(Parag_Model_Answer(True,  "obţinerea licenţei de pilot pentru a putea zbura nesupravegheat de un instructor"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Zborul de şcoală este caracterizat ca fiind")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "zborul efectuat pentru pregătire în vederea participării la competiţii"))
_question.answers.append(Parag_Model_Answer(False, "zborul efectuat în vederea pregătirii pentru depăşirea unor recorduri"))
_question.answers.append(Parag_Model_Answer(True,  "zborul efectuat pentru iniţiere sau instruire"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Spaţiul aerian naţional reprezintă coloana de aer situatã deasupra teritoriului de suveranitate al României, până la:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "10.000 AGL"))
_question.answers.append(Parag_Model_Answer(False, "12.000 ASL"))
_question.answers.append(Parag_Model_Answer(True,  "limita inferioară a spaţiului extraatmosferic"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Executarea instruirii cu parapanta se face de către")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "orice pilot avansat"))
_question.answers.append(Parag_Model_Answer(False, "operatorul radio"))
_question.answers.append(Parag_Model_Answer(True,  "instructorul licenţiat"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Pentru obtinerea licentei de pilot aeronave ultrusoare clasa parapanta elevul pilot trebuie sa parcurga un program de pregatire teoretica ce include un numar total de ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "48 ore "))
_question.answers.append(Parag_Model_Answer(True,  "50 ore "))
_question.answers.append(Parag_Model_Answer(False, "48 ore fara  dicipina telefonie"))
