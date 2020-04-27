from parag_model.parag_model  import *

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_category        = Parag_Model_Category()
_category.name   = "cunoasterea aeronavei"
PARAG_CATEGORY_7 = _category

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Actionarea acceleratorului are ca efect:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "reducerea vitezei de zbor"))
_question.answers.append(Parag_Model_Answer(False, "dublarea vitezei de zbor"))
_question.answers.append(Parag_Model_Answer(True, "cresterea vitezei de zbor "))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("O parapanta omologata LTF – 1 respectiv EN – A este destinata:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "pilotilor de competitie"))
_question.answers.append(Parag_Model_Answer(True, "pilotilor incepatori"))
_question.answers.append(Parag_Model_Answer(False, "exclusiv pilotilor de acrobatie"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Riscul de twist este mai mare cand:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "chinga de piept este foarte stransa"))
_question.answers.append(Parag_Model_Answer(True, "folosim seleta este de tip cocoon"))
_question.answers.append(Parag_Model_Answer(False, "chinga de piept este foarte larga "))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Tensiunea in comenzi creste datorita:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "cresterii presiunii in voalura"))
_question.answers.append(Parag_Model_Answer(True, "cresterii unghiului de incidenta"))
_question.answers.append(Parag_Model_Answer(False, "cresterii vitezei de zbor"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("O parapanta omologata LTF 2 (EN –C) este destinata:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "exclusiv pilotilor incepatori"))
_question.answers.append(Parag_Model_Answer(False, "exclusiv zborului in tandem"))
_question.answers.append(Parag_Model_Answer(True, "exclusiv pilotilor cu nivel mediu/ridicat de pregatire"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Alungirea aripii este: ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "raportul dintre coarda medie si anvergura"))
_question.answers.append(Parag_Model_Answer(False, "raportul dintre profunzimea maxima a aripii si anvergura "))
_question.answers.append(Parag_Model_Answer(False, "raportul dintre grosimea maxima relativa a profilului si anvergura"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Aripa de parapanta prezinta torsiune geometrica: ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "da"))
_question.answers.append(Parag_Model_Answer(False, "nu "))
_question.answers.append(Parag_Model_Answer(False, "torsiunea geometrica nu are legatura cu aerodinamica"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Profilul aripii este dat de : ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "membranele intercheson "))
_question.answers.append(Parag_Model_Answer(False, "proiectia aripii pe un plan orizontal "))
_question.answers.append(Parag_Model_Answer(False, "suprafata aripii desfasurata"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Lungimea suspantelor poate influenta finetea parapantei: ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "da"))
_question.answers.append(Parag_Model_Answer(False, "nu"))
_question.answers.append(Parag_Model_Answer(False, "numai o data cu cresterea incarcarii alare. "))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Incarcarea alara se refera la : ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "raportul dintre greutatea totala in zbor si suprafata portanta "))
_question.answers.append(Parag_Model_Answer(False, "greutatea maxima in zbor "))
_question.answers.append(Parag_Model_Answer(False, "sarcina nimima si maxima a parapantei"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("La actionarea in jos a comenzilor unghiul de incidenta: ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "creste "))
_question.answers.append(Parag_Model_Answer(False, "scade "))
_question.answers.append(Parag_Model_Answer(False, "ramane constant"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Alegeti afirmatia falsa:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "parapanta are profil aerodinamic"))
_question.answers.append(Parag_Model_Answer(True, "parapanta nu are profil aerodinamic"))
_question.answers.append(Parag_Model_Answer(False, "profilul aerodinamic al parapantei poate fi identificat ca proiectia acesteia pe un plan orizontal"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Nodul pe o suspanta are drept efect:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "scade rezistenta la rupere a suspantei respective"))
_question.answers.append(Parag_Model_Answer(False, "creste rezistenta la rupere a suspantei respective"))
_question.answers.append(Parag_Model_Answer(False, "nu influenteaza rezistenta la rupere a suspantelor"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Alegeti afirmatia adevarata:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "comenzile actioneaza asupra stabilizatoarelor"))
_question.answers.append(Parag_Model_Answer(False, "comenzile actioneaza asupra liniei de suspante B"))
_question.answers.append(Parag_Model_Answer(True, "comenzile actioneaza asupra bordului de fuga"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Suspantele fac legatura dintre:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "cordul de atac, bordul de fuga si seleta"))
_question.answers.append(Parag_Model_Answer(True, "voalura si chingi portsuspante"))
_question.answers.append(Parag_Model_Answer(False, "voalura si carabinierele de acrosaj"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Bordul de fuga este:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "partea din fata a profilului "))
_question.answers.append(Parag_Model_Answer(False, "partea centrala a  aripii"))
_question.answers.append(Parag_Model_Answer(True, "partea din spate a aripii"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Alegeti afirmatia falsa:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "intradosul aripii este in partea inferioara a profilului"))
_question.answers.append(Parag_Model_Answer(False, "extradosul aripii este in partea superioara a profilului"))
_question.answers.append(Parag_Model_Answer(True, "intradosul este in partea superioara a profilului"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Alegeti afirmatia corecta:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "nodurile slabesc rezistenta la rupere a suspantelor"))
_question.answers.append(Parag_Model_Answer(True, "radiatia ultravioleta degradeaza kevlarul"))
_question.answers.append(Parag_Model_Answer(False, "suspantele din kevlar nu au nevoie de manta de protectie"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Tesatura din care este construita voalura trebuie sa fie:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "deformabila atat pe urzeala cat si pe batatura"))
_question.answers.append(Parag_Model_Answer(True, "nedeformabila pe urzeala si pe batatura"))
_question.answers.append(Parag_Model_Answer(False, "elastica pe orice directie"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Alegeti afirmatia corecta:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "distanta dintre punctele de acrosaj a seletei modifica comportamentul parapantei in zbor"))
_question.answers.append(Parag_Model_Answer(False, "distanta dintre punctele de acrosaj a seletei modifica nu comportamentul parapantei in zbor"))
_question.answers.append(Parag_Model_Answer(True, "distanta dintre punctele de acrosaj a seletei este importanta la testele de omologare"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Omolgarea parapantei arata:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "performantele parapantei: finete maxima, viteza minima de infundare, viteza maxima"))
_question.answers.append(Parag_Model_Answer(True, "nivelul de pilotaj necesar"))
_question.answers.append(Parag_Model_Answer(False, "factorul de sarcina admis"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Alegeti afirmatia corecta:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "comenzile actioneaza asupra bordului de atac"))
_question.answers.append(Parag_Model_Answer(True, "cu ajutorul comenzilor modificam unghiul de incidenta"))
_question.answers.append(Parag_Model_Answer(False, "manevra URECHI se face cu ajutorul comenzilor"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Stabilitatea pe directie a parapantei este asigurata de:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "bordul de fuga"))
_question.answers.append(Parag_Model_Answer(False, "efectul de pendul"))
_question.answers.append(Parag_Model_Answer(True, "stabilizatoare (capetele de plan)"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Membranele intercheson au rolul :")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "de a mentine presiunea dinamica in interiorul voalurii"))
_question.answers.append(Parag_Model_Answer(False, "de a prelua sarcina de pe intrados "))
_question.answers.append(Parag_Model_Answer(True, "de a materializa profilul aerodinamic al parapantei"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Caracteristicile si performantele de zbor ale parapantei sunt influentate de:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "gradul de uzura al voalurii"))
_question.answers.append(Parag_Model_Answer(True, "lungimea suspantelor"))
_question.answers.append(Parag_Model_Answer(True, "altitudinea de zbor"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Acceleratorul modifica:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "unghiul de incidenta"))
_question.answers.append(Parag_Model_Answer(False, "scheletul profilului"))
_question.answers.append(Parag_Model_Answer(False, "coarda profilului"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Omologarea parapantelor are drept scop: ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "verificarea performantelor de zbor "))
_question.answers.append(Parag_Model_Answer(True, "verificarea gradului de securitate"))
_question.answers.append(Parag_Model_Answer(False, "ambele de la pct a. si b."))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Alegeti afirmatia corecta:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "seletele tip cocoon au rezistenta la inaintare mai mica fata de seletele clasice"))
_question.answers.append(Parag_Model_Answer(False, "seletele tip cocoon au rezistenta la inaintare mai mare fata de seletele clasice"))
_question.answers.append(Parag_Model_Answer(False, "seletele tip cocoon au protectie la impact mai buna decat seletele clasice"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Alegeti afirmatia corecta:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "sistanta dintre punctele de acrosaj are influenta asupra comportamentului parapantei"))
_question.answers.append(Parag_Model_Answer(False, "sistanta dintre punctele de acrosaj are influenta doar asupra confortului pilotului"))
_question.answers.append(Parag_Model_Answer(True, "sistanta dintre punctele de acrosaj se regleaza intr-un domeniu strict"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Voalura este confectionata din material sintetic in carouri( Rip-Stop) pentru:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "a mentine mai bine presiunea in voalura"))
_question.answers.append(Parag_Model_Answer(True, "pentru a mari rezistenta materialului"))
_question.answers.append(Parag_Model_Answer(True, "a limita extinderea in caz de ruptura"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Seletele dotatate cu protector dorsal sunt recomandata:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "doar elevilor piloti in perioada de scolarizare"))
_question.answers.append(Parag_Model_Answer(True, "tuturor pilotilor indiferent de nivel"))
_question.answers.append(Parag_Model_Answer(False, "doar elevilor cu nivel superior de pregatire"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Suspantele parapantei sunt:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "elasice"))
_question.answers.append(Parag_Model_Answer(True, "statice"))
_question.answers.append(Parag_Model_Answer(False, "pe linia A si B sunt statice iar C si D elastice"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cate categorii de greutate regasim la parapante:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "fiecare producator are intervale de greutate proprii, conform omologarilor"))
_question.answers.append(Parag_Model_Answer(False, "sunt 3 nivele : S, M si L"))
_question.answers.append(Parag_Model_Answer(False, "sunt 4 nivele: S,M,L si XL"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Incarcarea peste limita superioara a parapantei are ca efect:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "cresterea tuturor vitezelor"))
_question.answers.append(Parag_Model_Answer(False, "scaderea vietezei la finete maxima"))
_question.answers.append(Parag_Model_Answer(False, "scaderea vitezei minime de infundare"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care este numarul standard de chingi portsuspante la parapante:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "nu exista un numar standard"))
_question.answers.append(Parag_Model_Answer(False, "4"))
_question.answers.append(Parag_Model_Answer(False, "5"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care sunt riscurile ce apar o data cu uzura voalurii:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "finetea maxima se obtine doar cu acceleratorul actionat la maximum"))
_question.answers.append(Parag_Model_Answer(True, "pericol de angajare prematura si deepstall"))
_question.answers.append(Parag_Model_Answer(False, "scade viteza minima de infundare"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Alegeti afirmatia corecta:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "modificarea configuratiei suspantelor altereaza gradul de securitate in zbor"))
_question.answers.append(Parag_Model_Answer(False, "modificarea configuratiei suspantelor altereaza doar performantele de zbor ale parapantei"))
_question.answers.append(Parag_Model_Answer(False, "modificarea configuratiei suspantelor nu este critica decat asupra maneabilitatii parapantei"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Alegeti afirmatia corecta:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "prelungirea suspantelor de comanda duce la marirea vitezei maxime de zbor"))
_question.answers.append(Parag_Model_Answer(False, "prelungirea suspantelor de comanda duce la marirea finetii in zbor"))
_question.answers.append(Parag_Model_Answer(True, "prelungirea suspantelor de comanda duce la marirea cursei comenzilor spre in jos"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Alegeti categoria cu care este posibil zborul de distanta (XC):")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "LTF 1 / EN-A"))
_question.answers.append(Parag_Model_Answer(True, "LTF 1-2 /  EN-B"))
_question.answers.append(Parag_Model_Answer(True, "LTF 2/ EN-C"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Pentru a zbura cu pasager este necesar:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "parapanta speciala pentru zborul cu pasager"))
_question.answers.append(Parag_Model_Answer(False, "parapanta omologata LTF 1 / EN A"))
_question.answers.append(Parag_Model_Answer(False, "parapanta omologata LTF 2-3 / EN-D"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Finetea parapantei este direct influentata de :")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "lungimea suspantelor"))
_question.answers.append(Parag_Model_Answer(True, "alungirea aripii"))
_question.answers.append(Parag_Model_Answer(False, "clasa de omologare"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Seleta tip cocoon  influenteaza:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "viteza minima de infundare"))
_question.answers.append(Parag_Model_Answer(True, "finetea parapantei"))
_question.answers.append(Parag_Model_Answer(False, "viteza minima de infundare"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce regim de zbor este potrivit la o aripa LTF1 / ENA pentru spiralarea in termica:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "regim de zbor la finete"))
_question.answers.append(Parag_Model_Answer(True, "regim de zbor la infundare minima"))
_question.answers.append(Parag_Model_Answer(False, "regim de zbor la viteza maxima"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cate regimuri de zbor prezinta parapanta:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "3"))
_question.answers.append(Parag_Model_Answer(False, "2"))
_question.answers.append(Parag_Model_Answer(False, "5"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care este zona de uzura maxima a voalurii de parapanta?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "extrados treimea anterioara, masurand de la bordul de atac"))
_question.answers.append(Parag_Model_Answer(False, "tot extradosul"))
_question.answers.append(Parag_Model_Answer(False, "tot intradosul"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Depasirea intervalului de greutate poate sa duca la:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "modificarea comportamentului parapantei"))
_question.answers.append(Parag_Model_Answer(True, "modificarea performantelor parapantei"))
_question.answers.append(Parag_Model_Answer(False, "modificarea formei parapantei"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Unghiul de incidenta se masoara:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "fata de orizontala"))
_question.answers.append(Parag_Model_Answer(False, "fata de directia de zbor"))
_question.answers.append(Parag_Model_Answer(True, "intre corda profilului si directia de curgere a fileurilor de aer"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Alegeti afirmatia corecta:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "toate suspantele sunt fixe"))
_question.answers.append(Parag_Model_Answer(True, "suspantele de comanda sunt mobile"))
_question.answers.append(Parag_Model_Answer(False, "toate suspantele sunt mobile"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Alegeti afirmatia corecta:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "orice parapanta poate fi lansata prin remorcaj la mosor"))
_question.answers.append(Parag_Model_Answer(False, "orice parapanta poate fi folosita la zbor cu motor"))
_question.answers.append(Parag_Model_Answer(True, "orice parapanta poate fi folosita la exercitii de gonflaj la sol"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Constructiv voalura se compune din:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "extrados, intrados, membrane intercheson"))
_question.answers.append(Parag_Model_Answer(False, "extrados, intrados, bord de atac, bord de fuga"))
_question.answers.append(Parag_Model_Answer(False, "extrados, intrados, stabilizatoare"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Alegeti elementele care duc la uzura prematura a volaurii:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "expunere la radiatie ultravioleta"))
_question.answers.append(Parag_Model_Answer(True, "zbor in atmosfera salina "))
_question.answers.append(Parag_Model_Answer(False, "remorcaj la mosor"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Scheletul profilului este materializat de:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "forma profilului aerodinamic"))
_question.answers.append(Parag_Model_Answer(False, "totalitatea elemntelor de ranforsare din interiorul aripii"))
_question.answers.append(Parag_Model_Answer(True, "nu este materializat "))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("O parapanta cu mai multe membrane intercheson va avea:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "finete mai mare"))
_question.answers.append(Parag_Model_Answer(False, "finete mai mica"))
_question.answers.append(Parag_Model_Answer(False, "viteza de angajare mai mica"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question(" La parapanta centrul de greutate este:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "la nivelul voalurii"))
_question.answers.append(Parag_Model_Answer(True, "la nivelul pilotului"))
_question.answers.append(Parag_Model_Answer(False, "deasupra voalurii"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Alegeti afirmatia corecta:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "profilul aerodinamic al parapantei se regaseste in proiectia voalurii pe un plan orizontal"))
_question.answers.append(Parag_Model_Answer(False, "parapanta nu are profil aerodinamic ci doar extrados, intrados, bord de atac si bord de fuga"))
_question.answers.append(Parag_Model_Answer(True, "profilul aerodinamic al parapantei este materializat de membranele intercheson"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Alegeti afirmatia corecta:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "polara se gaseste pe extrados"))
_question.answers.append(Parag_Model_Answer(False, "polara se gaseste pe intrados"))
_question.answers.append(Parag_Model_Answer(True, "polara este o forma sintetica de descriere a performantelor de zbor"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("In cazul aripii de parapanta regasim: ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "torsiune geometrica "))
_question.answers.append(Parag_Model_Answer(False, "numai torsiune transversala "))
_question.answers.append(Parag_Model_Answer(False, "numai torsiune aerodinamica"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("In zbor orizontal centrul de greutate este situat: ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "sub centrul de presiune "))
_question.answers.append(Parag_Model_Answer(False, "deasupra centrului de presiune "))
_question.answers.append(Parag_Model_Answer(False, "coincide cu centrul de presiune"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Alegeti afirmatia corecta:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "toate parapantele au profil reflex"))
_question.answers.append(Parag_Model_Answer(True, "toate parapantele au profil aerodinamic"))
_question.answers.append(Parag_Model_Answer(False, "parapantele nu au profil aerodinamic"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Alegeti afirmatia corecta:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "suspantele parapantei sunt elastice"))
_question.answers.append(Parag_Model_Answer(False, "toate suspantele parapantei sunt fixe"))
_question.answers.append(Parag_Model_Answer(True, "suspantele de comanda nu sunt fixe"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Alegeti afirmatia corecta:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "din polara putem deduce sarcina utila, viteza maxima si viteza minima a parapantei"))
_question.answers.append(Parag_Model_Answer(True, "din polara putem deduce regimurile de zbor ale parapantei"))
_question.answers.append(Parag_Model_Answer(False, "din polara putem deduce forma profilului parapantei"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Alegeti afirmatia corecta:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "aripile omologate LTF 2-3 / EN –D se folosesc la scolarizare"))
_question.answers.append(Parag_Model_Answer(False, "aripile omologate LTF 2-3 / EN –D se folosesc de regula de catre piloti cu minimum de experienta"))
_question.answers.append(Parag_Model_Answer(True, "aripile omologate LTF 2-3 / EN –D se folosec doar de piloti avansati"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question(" Alegeti categoria de omologare folosita pentru aripile de scoala:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "LTF 1 / EN-A"))
_question.answers.append(Parag_Model_Answer(False, "LTF 2 / EN-C"))
_question.answers.append(Parag_Model_Answer(False, "LTF 2-3 / EN-D"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Alegeti clasa de omologare cu nivelul de securitate cel mai ridicat:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "LTF 1 / EN-A"))
_question.answers.append(Parag_Model_Answer(False, "LTF 1-2 / EN-B"))
_question.answers.append(Parag_Model_Answer(False, "LTF 2  / EN-C"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("O aripa cu vechime de 15 ani, care a zburat in acest interval de timp, prezinta:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "uzura fizica"))
_question.answers.append(Parag_Model_Answer(False, "uzura morala"))
_question.answers.append(Parag_Model_Answer(True, "uzura fizica si morala"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Intervalul de greutate se refera la :")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "greutatea totala in zbor: pilot echipat+seleta+parasuta de rezerva+parapanta"))
_question.answers.append(Parag_Model_Answer(False, "greutatea suspendata: pilot echipat+seleta+parasuta de rezerva"))
_question.answers.append(Parag_Model_Answer(False, "greutatea pilotului complet echipat"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Alegeti afirmatia corecta:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "parapantele se comporta identic la nivelul marii sau la altitudini peste 6000m"))
_question.answers.append(Parag_Model_Answer(True, "performantele si comportamentul parapantei depind de densitatea aerului"))
_question.answers.append(Parag_Model_Answer(False, "performantele si comportamentul parapantei depind numai de greutatea totala in zbor"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Stabilizatoarele parapantei au rol de:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "stabilizeaza parapanta pe directie"))
_question.answers.append(Parag_Model_Answer(False, "stabilizeaza unghiul de incidenta al parapantei"))
_question.answers.append(Parag_Model_Answer(False, "stabilizeaza unghiul de panta al parapantei"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care dintre următoarele materiale sunt utilizate în construcția pânzei de parapantă?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Aramid (Kevlar)"))
_question.answers.append(Parag_Model_Answer(False, "Polietilenă (Dyneema)"))
_question.answers.append(Parag_Model_Answer(True, "Poliamidă (nailon)"))
_question.answers.append(Parag_Model_Answer(False, "Policlorură de vinil (PVC)"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question('Termenul de material "ripstop" înseamnă')
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "întărirea zonelor puternic încărcate ale parapantei."))
_question.answers.append(Parag_Model_Answer(False, "barierele de rupere care împiedică răspândirea rupturii de la un element al parapantei la altul."))
_question.answers.append(Parag_Model_Answer(True, "tehnica în care firel mai rezistente  se interconectează la intervale regulate în urzeala și bătătura țesăturii pentru a preveni continuarea rupturii."))
_question.answers.append(Parag_Model_Answer(False, "un strat special de protecție care mărește elasticitatea țesăturii și, prin urmare, îmbunătățește rezistența la rupere a țesăturii."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Rezistența la ruperea și deșirare a materialelor folosite la parapante este îmbunătățită prin")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "impregnarea pânzei cu un strat de protecție."))
_question.answers.append(Parag_Model_Answer(True, 'tehnica "ripstop" în țesătură.'))
_question.answers.append(Parag_Model_Answer(False, "interconectarea firelor cu o elasticitate mai mare."))
_question.answers.append(Parag_Model_Answer(False, "țeserea extrem de fină a materialului."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Când vorbim de parapante, ce înseamnă termenul de porozitate?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Rezistența la rupere a țesăturii."))
_question.answers.append(Parag_Model_Answer(False, "Rezistența țesăturii la încovoiere."))
_question.answers.append(Parag_Model_Answer(True, "Permeabilitatea la aer a unui material."))
_question.answers.append(Parag_Model_Answer(False, "Compoziția suprafeței superioare a aripii."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Porozitatea materialelor utilizate pentru parapante (la volaură)")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "ar trebui să fie cât mai mare posibil."))
_question.answers.append(Parag_Model_Answer(True, "ar trebui să fie cât mai mică posibil."))
_question.answers.append(Parag_Model_Answer(False, "nu trebuie să fie niciodată sub o valoare predeterminată, deoarece stratul limită devine prea laminar."))
_question.answers.append(Parag_Model_Answer(False, "nu este important, rezistența mecanică este cea care contează."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Țesăturile  folosite pentru parapante sunt impregnate cu diferiți lianți pentru a")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "crește elasticitatea și rezistența mecanică."))
_question.answers.append(Parag_Model_Answer(True, "micșora porozitatea și elasticitatea."))
_question.answers.append(Parag_Model_Answer(False, "crește porozitatea și rezistența mecanică."))
_question.answers.append(Parag_Model_Answer(False, "micșora elasticitatea și rezistența mecanică."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Materialele acoperite cu poliester (Mylar) sunt diferite de cele acoperite cu poliuretan sau silicon pentru că au")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "elasticitate diagonală mai mică."))
_question.answers.append(Parag_Model_Answer(False, 'o mai mare elasticitate pe  direcția de "bătătură" a țesăturii.'))
_question.answers.append(Parag_Model_Answer(False, "sensibilitate redusă la radațiile UV."))
_question.answers.append(Parag_Model_Answer(False, "porozitate mai mare."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Stratul de impregnare al țesăturilor folosite la parapante ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "crește sensibilitatea la radiațiile UV."))
_question.answers.append(Parag_Model_Answer(True, "reduce porozitatea."))
_question.answers.append(Parag_Model_Answer(False, "crește elasticitatea."))
_question.answers.append(Parag_Model_Answer(False, "reduce rezistența mecanică."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Stratul de impregnare al țesăturilor folosite la parapante ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "reduce sensibilitatea țesăturii la radiațiile UV."))
_question.answers.append(Parag_Model_Answer(False, "crește porozitatea țesăturii."))
_question.answers.append(Parag_Model_Answer(False, "crește elasticitatea țesăturii."))
_question.answers.append(Parag_Model_Answer(False, "reduce rezistența mecanică a țesăturii."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Stratul de impregnare al țesăturilor folosite la parapante ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "crește sensibilitatea țesăturii la radiațiile UV."))
_question.answers.append(Parag_Model_Answer(False, "crește porozitatea țesăturii."))
_question.answers.append(Parag_Model_Answer(True, "scade elasticitatea țesăturii."))
_question.answers.append(Parag_Model_Answer(False, "scade rezistența mecanică a țesăturii."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Stratul de impregnare al țesăturilor folosite la parapante ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "crește sensibilitatea țesăturii la radiațiile UV."))
_question.answers.append(Parag_Model_Answer(False, "crește porozitatea țesăturii."))
_question.answers.append(Parag_Model_Answer(False, "crește elasticitatea țesăturii."))
_question.answers.append(Parag_Model_Answer(True, "crește rezistența mecanică a țesăturii."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce efecte asupra performanței voalurii are stratul de impregnare vechi, deteriorat sau insuficient?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Parapanta este greu de manevrat și are tendință de instabilitate de-a lungul axei longitudinale."))
_question.answers.append(Parag_Model_Answer(False, "Întreaga gamă de viteză a parapantei crește, iar tendința de închidere crește."))
_question.answers.append(Parag_Model_Answer(False, "Întregul interval de viteză al parapantei se reduce și curba polară devine mai plată."))
_question.answers.append(Parag_Model_Answer(True, "Viteza de angajare este mai mare, precum si tendința de a intra in angajare parașutată."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Stratul de protecție a voalurii poate fi deteriorat considerabil de către")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "manevre extreme care duc la închideri ale voalurii."))
_question.answers.append(Parag_Model_Answer(True, "curățarea voalurii cu produse de curățare, agresive, de uz casnic."))
_question.answers.append(Parag_Model_Answer(False, "depozitarea regulată a parapantei într-un loc întunecat protejat de lumina soarelui."))
_question.answers.append(Parag_Model_Answer(False, "depozitarea parapantei cât mai uscate într-o încăpere rece."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Stratul de protecție a voalurii poate fi deteriorat considerabil de către")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "manevre extreme care duc la închideri ale voalurii."))
_question.answers.append(Parag_Model_Answer(False, "curățarea voalurii cu apă rece."))
_question.answers.append(Parag_Model_Answer(False, "depozitarea regulată a parapantei într-un loc întunecat protejat de lumina soarelui."))
_question.answers.append(Parag_Model_Answer(True, "depozitarea parapantei într-o încăpere umedă  și cu variații mari de temperatură."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Stratul de protecție a voalurii poate fi deteriorat considerabil de către")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "manevre extreme care duc la închideri ale voalurii."))
_question.answers.append(Parag_Model_Answer(False, "curățarea voalurii cu apă rece."))
_question.answers.append(Parag_Model_Answer(True, "depozitarea regulată a parapantei într-un loc luminos, expus luminii directe a soarelui."))
_question.answers.append(Parag_Model_Answer(False, "depozitarea parapantei într-o încăpere răcoroasă."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Stratul de protecție a voalurii poate fi deteriorat considerabil de către")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "frecarea de materiale abrazive cum ar fi stânci, nisip, sare etc."))
_question.answers.append(Parag_Model_Answer(False, "curățarea voalurii cu apă rece."))
_question.answers.append(Parag_Model_Answer(False, "depozitarea regulată a parapantei într-un loc întunecat protejat de lumina soarelui."))
_question.answers.append(Parag_Model_Answer(False, "depozitarea parapantei într-o încăpere răcoroasă."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("O parapantă care a intrat în contact cu apa de mare ar trebui să fie")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "uscată cât mai repede posibil prin gonflare în briza mării."))
_question.answers.append(Parag_Model_Answer(False, "uscată la umbră si apoi bine scuturată pentru a elimina sarea."))
_question.answers.append(Parag_Model_Answer(True, "clătită bine cu apă dulce și apoi uscată."))
_question.answers.append(Parag_Model_Answer(False, "testată porozitatea de un expert."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cea mai mare sarcină pe o aripă în timpul zborului este")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "pe extradosul aripii lângă bordul de atac."))
_question.answers.append(Parag_Model_Answer(False, "pe intradosul aripii lângă bordul de atac."))
_question.answers.append(Parag_Model_Answer(False, "pe extradosul aripii lângă bordul de fugă."))
_question.answers.append(Parag_Model_Answer(False, "pe intradosul aripii lângă bordul de fugă."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care sunt semnele îmbătrânirii la o parapantă?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "Porozitate crescută; angajarea la o viteză mai mare; o tendință mai pronunțată de a intra in angajare parașutată."))
_question.answers.append(Parag_Model_Answer(False, "Elasticitatea scăzută; presiunea internă redusă; planorul reacționează mai brusc la comenzi."))
_question.answers.append(Parag_Model_Answer(False, "Materialul se întinde din cauza încărcării continue; crește grosimea profilului; viteza se reduce pe întreagul interal al curbei polare."))
_question.answers.append(Parag_Model_Answer(False, "Materialul se contractă datorită expunerii UV constante; profilul devine mai plat; viteza crește pe întreagul interval al curbei polare."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care este scopul traveelor și întăriturilor diagonale dintr-o aripă?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "De a limita circulația aerului în interiorul parapantei și pentru a minimiza astfel porozitatea aripii."))
_question.answers.append(Parag_Model_Answer(True, "De a distribui încărcarea din suspante în mod uniform pe suprafața superioară a aripii."))
_question.answers.append(Parag_Model_Answer(False, "De a îmbunătăți rezistența structurală a aripii pe axa longitudinală și transversală."))
_question.answers.append(Parag_Model_Answer(False, "De a regla circulația aerului în interiorul aripii și, prin urmare, de a menține o presiune internă uniformă."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Sarcina pe travee este cea mai mare")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "în jumătatea din față a aripii unde sunt atașate suspantele."))
_question.answers.append(Parag_Model_Answer(False, "între punctele de legătură ale suspantelor de la jumătatea dinfață a aripii."))
_question.answers.append(Parag_Model_Answer(False, "la jumătatea din spate a aripii unde sunt atașate suspantele."))
_question.answers.append(Parag_Model_Answer(False, "între punctele de racordare a suspantelor la jumătatea din spate a aripii."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("În care din următoarele cazuri traveele au cea mai mare încărcare ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Într-o spirală."))
_question.answers.append(Parag_Model_Answer(False, "Într-o termică puternică."))
_question.answers.append(Parag_Model_Answer(False, 'În timp ce zburăm cu "urechi mari".'))
_question.answers.append(Parag_Model_Answer(True, "Într-o angajare cu  B-urile."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Producătorii reduc deformarea traveelor la care sunt atașate suspantele prin")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "aranjarea orificiilor din travee direct peste punctele de atașare ale suspantelor."))
_question.answers.append(Parag_Model_Answer(True, "răspândirea sarcinii pe o suprafață mai mare a traveelor folosind armături triunghiulare pe zonele cu cele mai mari incărcări."))
_question.answers.append(Parag_Model_Answer(False, "minimizarea numărului de puncte de atașare a suspantelor."))
_question.answers.append(Parag_Model_Answer(False, "alegerea unui profil de aripă relativ gros."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("De ce sunt adăugate întăriturile diagonale între travee, în construcția parapantelor?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Ajută la o redeschidere blândă și continuă a aripii după o închidere."))
_question.answers.append(Parag_Model_Answer(False, "Inhibă în special deformarea permanentă a aripii ca rezultat al întinderii lente a materialului."))
_question.answers.append(Parag_Model_Answer(False, "Inhibă epulzarea rapidă a aerului din celule individuale și, prin urmare, inhibă închiderile."))
_question.answers.append(Parag_Model_Answer(True, "Permit ca sarcina de pe extradosul aripii să fie susținută de un număr redus de suspantr, reducând astfel rezistența la înaintare."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Orificiile intercelulare (din travee)")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Fac posibilă o presiune egală între suprafața superioară și cea inferioară a aripii."))
_question.answers.append(Parag_Model_Answer(False, "Distribuie uniform încărcătura generată de portanță pe întregul perete al celulei."))
_question.answers.append(Parag_Model_Answer(True, "Ajută la umplerea celulelor cu aer, atunci când bordul de atac e închis sau celula nu are priză de aer."))
_question.answers.append(Parag_Model_Answer(False, "Permite o egalizare între presiunea statică din interior și presiunea dinamică din afara aripii."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Parapanta X are 18 celule, parapanta Y are 24 de celule. Ambele au o suprafață de 24m² și o anvergură de 10m. Ele sunt construite cu aceleași materiale și principii. Care din urmatoarele afirmații este adevarată?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "Y are un profil mai precis și un volum de împachetare mai mare decât X."))
_question.answers.append(Parag_Model_Answer(False, "Y are o alungire mai mare și un volum de împachetare mai mare decât X."))
_question.answers.append(Parag_Model_Answer(False, "X are un profil mai gros și un volum de împachetare mai mare decât Y."))
_question.answers.append(Parag_Model_Answer(False, "X are o alungire mai mică decât Y, dar ambele au același volum de împachetare."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("În ce direcție, poate încărcarea pe materialul ripstop pe o perioadă de timp, provoca cele mai multe deformări?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, 'Încărcări paralele cu direcția firului "bătătură"  (weft) în cârpă.'))
_question.answers.append(Parag_Model_Answer(False, 'Paralele cu direcția firului "urzeală" (warp) în cârpă.'))
_question.answers.append(Parag_Model_Answer(False, "Încărcări verticale (la 90 de grade) cu materialul."))
_question.answers.append(Parag_Model_Answer(True, "Încărcări diagonale în raport cu construcția materialului."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Dacă cusătura pe o voalură este prea apropiată")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "rezistența la rupere este mărită."))
_question.answers.append(Parag_Model_Answer(False, "cusătura se mulează mai bine pe forma pânzei / aripii."))
_question.answers.append(Parag_Model_Answer(True, "materialul este perforat și îsă pierde din rezistență."))
_question.answers.append(Parag_Model_Answer(False, "porozitatea este minimizată."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cum se grupeză suspantele unei parapante?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "prin culoarea lor; de exemplu galben, roșii."))
_question.answers.append(Parag_Model_Answer(False, "prin diametrul lor; de exemplu 0,9 mm, 1,3 mm, 1,5 mm."))
_question.answers.append(Parag_Model_Answer(False, "prin materialele lor; de exemplu poliester, dyneema, kevlar, poliamidă."))
_question.answers.append(Parag_Model_Answer(True, "prin punctul lor de atașare la voalură; de exemplu suapantele A, B, C, D."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Unde se atașează suspantele A de voalură? ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Pe bordul de fugă. "))
_question.answers.append(Parag_Model_Answer(False, "Pe stabilizatoare. "))
_question.answers.append(Parag_Model_Answer(False, "Pe axa longitudinală. "))
_question.answers.append(Parag_Model_Answer(True, "Pe bordul de atac."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce cerințe, printre altele, trebuie să îndeplinească suspantele moderne?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Elasticitate scăzută, capacitate redusă de încărcare cu un diametru minim."))
_question.answers.append(Parag_Model_Answer(False, "Elasticitate ridicată, capacitate redusă de încărcare cu un diametru minim."))
_question.answers.append(Parag_Model_Answer(True, "Elasticitate scăzută, capacitate ridicată de încărcare cu un diametru minim."))
_question.answers.append(Parag_Model_Answer(False, "Elasticitate ridicată, capacitate ridicată de încărcare cu un diametru minim."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("La o parapantă modernă, care este întinderea tolerată a unei suspante de 6 m, sub sarcină de 50 N (5 kg)?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Suspantele pentru parapantele moderne sunt realizate din materiale care nu se întind."))
_question.answers.append(Parag_Model_Answer(True, "aprox. 3cm."))
_question.answers.append(Parag_Model_Answer(False, "aprox. 6cm."))
_question.answers.append(Parag_Model_Answer(False, "aprox. 9cm."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce materiale sunt folosite la fabricarea suspantelor?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Poliester și polietilenă (Dyneema)."))
_question.answers.append(Parag_Model_Answer(False, "Poliester și poliamid (nailon)."))
_question.answers.append(Parag_Model_Answer(False, "Aramid (Kevlar) și Poliester."))
_question.answers.append(Parag_Model_Answer(True, "Polietilenă (Dyneema) și Aramid (Kevlar)."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Motivul construcției suspantei moderne, de obicei, dintr-un miez și o manta este")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "astfel încât capacitatea de încărcare a suspantei să fie mărită de manta."))
_question.answers.append(Parag_Model_Answer(True, "pentru a proteja miezul de efectele luminii și frecării."))
_question.answers.append(Parag_Model_Answer(False, "astfel încât acestea să poată fi colorate diferit și, prin urmare, să fie mai ușor deosebite."))
_question.answers.append(Parag_Model_Answer(False, "astfel încât, în caz de rupere a miezului, mantaua să poată prelua încărcarea pentru o perioadă scurtă de timp."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Dacă miezul este realizat dintr-un material cu elasticitate foarte mică,  pe termen lung ar trebui să ne așteptăm la schimbări în lungimea suspantelor? ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "Da, în special datorită faptului că mantaua suspantei tinde să se micșoreze și, prin urmare, să scurteze suspantele."))
_question.answers.append(Parag_Model_Answer(False, "Nu, suspantele realizate din materiale cu întindere minimă nu își modifică niciodată lungimea în mod semnificativ. "))
_question.answers.append(Parag_Model_Answer(False, "Da, deoarece toate materialele sub sarcină continuă își schimbă semnificativ lungimea. "))
_question.answers.append(Parag_Model_Answer(False, "Da, cu siguranță la temperaturi de peste 600 °C."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Tehnica utilizată pentru coaserea suspantelor")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "necesită o mare atenție în producție și nu reduce semnificativ rezistența."))
_question.answers.append(Parag_Model_Answer(False, "este singura metodă de producție care garantează permanent suficientă rezistență."))
_question.answers.append(Parag_Model_Answer(True, "poate, în special pentru liniile de Kevlar, să diminueze sarcina lor maximă cu până la 40%."))
_question.answers.append(Parag_Model_Answer(False, "ține numai de aspect."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce tehnică ne permite să asigurăm buclele în capetele liniilor de suspensie nemanalizate atunci când sunt fabricate din Kevlar fără a diminua în mod semnificativ puterea lor?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Nici una."))
_question.answers.append(Parag_Model_Answer(False, "Coasere."))
_question.answers.append(Parag_Model_Answer(False, "Lipire."))
_question.answers.append(Parag_Model_Answer(True, "Croșetare."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce poate cauza deteriorarea miezului suspantelor aramid (Kevlar) sau polietilenă (dyneema), slăbindu-le în mod semnificativ rezistența?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Zborul cu încărcare apropiată de, sau peste limita maximă permisă."))
_question.answers.append(Parag_Model_Answer(False, "Încărcarea mare a unei suspante sau grup de suspante în timpul manevrelor, cum ar fi închiderile frontale, închiderile asimetrice sau angajarea cu B-urile."))
_question.answers.append(Parag_Model_Answer(False, "Deteriorarea miezului este întotdeauna o eroare de productie si nu poate fi cauzata de folosirea parapantei."))
_question.answers.append(Parag_Model_Answer(True, "Când acestea sunt ude și se permiterea înghețarea lor."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Suspantele de 1 mm cu rezistență de 100 daN (10 kg) diferă de suspantele de 1,5 mm cu aceeași rezistență datorită faptului că au")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "rezistența la înaintare redusă și tendința redusă de înodare, în timpul pregătirii parapantei."))
_question.answers.append(Parag_Model_Answer(False, "rezistența la înaintare crescută și tendința crescută de înodare în timpul pregătirii parapantei."))
_question.answers.append(Parag_Model_Answer(False, "rezistența la înaintare crescută și tendința redusă de înodare în timpul pregătirii parapantei."))
_question.answers.append(Parag_Model_Answer(True, "rezistența la înaintare redusă și tendința crescută de înodare în timpul pregătirii parapantei."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce se poate spune despre încărcarea pe suspantele unei aripi stabile?")

_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "suspantele A și B au mai mult decât dublul încărcării suspantelor C și D."))
_question.answers.append(Parag_Model_Answer(False, "suspantele C și D au mai mult decât dublul încărcării suspantelor A și B."))
_question.answers.append(Parag_Model_Answer(False, "Încărcarea unei parapante moderne este distribuită în mod egal pe toate liniile principale."))
_question.answers.append(Parag_Model_Answer(False, "suspantele A și C poartă sarcina, în timp ce suspantele B și D creează în principal forma profilului."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care este avantajul suspantelor atașate prin sistemul buclă în buclă, față de de cusutul lor pe voalură?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Conexiunile cu buclă sunt mai bune deoarece suspanta nu este slăbită de cusătură."))
_question.answers.append(Parag_Model_Answer(True, "Întreținerea este mai ușoară, deoarece suspantele deteriorate pot fi ușor înlocuite."))
_question.answers.append(Parag_Model_Answer(False, "Conexiunile cu buclă sunt mai eficiente din punct de vedere aerodinamic și sunt, prin urmare, utilizate pe toate parapantele moderne de înaltă performanță."))
_question.answers.append(Parag_Model_Answer(False, "Nici una. Este o măsură ce ține strict de aspect."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Atunci când înlocuiți suspantele deteriorate, este important să vă asigurați că")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "datorită rezisteței la înaintare, suspantele noi au același diametru."))
_question.answers.append(Parag_Model_Answer(False, "în toate cazurile sunt folosite suspante al fel de rezistente sau mai rezistente."))
_question.answers.append(Parag_Model_Answer(False, "suspantele se conformează dimensional cu cele înlocuite."))
_question.answers.append(Parag_Model_Answer(True, "sunt utilizate numai suspantele originale furnizate de producător."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce circumstanțe pot provoca o modificare a lungimii inițiale a suspantelor?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Numai o încărcare foarte mare pe suspante individuale, de exemplu atunci când o suspantă este prinsă undeva în timpul lansării sau a aterizării."))
_question.answers.append(Parag_Model_Answer(False, "Numai utilizarea suspantelor de diferite tipuri sau dimensiuni."))
_question.answers.append(Parag_Model_Answer(False, "Suspantele moderne nu își schimbă niciodată permanent lungimea."))
_question.answers.append(Parag_Model_Answer(True, "Încărcarea diferită a suspantelor în timpul utilizării normale."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care sunt consecințele unei supraîncărcări mari pe anumite suspante, de exemplu atunci când o suspantă este prinsă undeva în timpul lansării sau a aterizării.")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "Suspantele pot fi întinse permanent și pot afecta comportamentul parapantei."))
_question.answers.append(Parag_Model_Answer(False, "Toate suspantele puternic supraîncărcate se vor rupe, ceea ce poate afecta comportamentul parapantei."))
_question.answers.append(Parag_Model_Answer(False, "Rezistența suspantei supraîncărcate va fi redusă critic."))
_question.answers.append(Parag_Model_Answer(False, "Suspantele moderne nu sunt afectate atât în ceea ce privește rezistența, cât și lungimea."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce ar putea cauza scurtarea permanentă a suspantelor?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Parapanta nu este folosită deloc într-o perioadă lungă de timp."))
_question.answers.append(Parag_Model_Answer(False, "Sortarea greșită a liniilor înainte de împachetarea parapantei."))
_question.answers.append(Parag_Model_Answer(True, "Expunerea suspantelor la umiditate și murdărie."))
_question.answers.append(Parag_Model_Answer(False, "Expunerea suspantelor la temperaturi scăzute."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care sunt consecințele unei alungiri permanente mai mari a suspantelor A în comparație cu celelalte?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "Unghiul de atac crește, iar profilul și manevrabilitatea parapantei se modifică."))
_question.answers.append(Parag_Model_Answer(False, "Unghiul de atac crește, profilul rămâne neschimbat și manevrabilitatea parapantei se modifică."))
_question.answers.append(Parag_Model_Answer(False, "Unghiul de atac rămâne neschimbat, iar profilul și manevrabilitatea parapantei se modifică."))
_question.answers.append(Parag_Model_Answer(False, "Unghiul de atac se reduce, iar profilul și manevrabilitatea parapantei se modifică."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care sunt consecințele scurtării suspantelor A?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Unghiul de atac crește, iar profilul și manevrabilitatea parapantei se modifică."))
_question.answers.append(Parag_Model_Answer(False, "Unghiul de atac crește, profilul rămâne neschimbat și manevrabilitatea parapantei se modifică."))
_question.answers.append(Parag_Model_Answer(False, "Unghiul de atac rămâne neschimbat, iar profilul și manevrabilitatea parapantei se modifică."))
_question.answers.append(Parag_Model_Answer(True, "Unghiul de atac se reduce, iar profilul și manevrabilitatea parapantei se modifică."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care sunt consecințele scurtării suspantelor B?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Unghiul de atac crește, iar profilul și manevrabilitatea parapantei se modifică."))
_question.answers.append(Parag_Model_Answer(False, "Unghiul de atac crește, profilul rămâne neschimbat și manevrabilitatea parapantei se modifică."))
_question.answers.append(Parag_Model_Answer(True, "Unghiul de atac rămâne neschimbat, iar profilul și manevrabilitatea parapantei se modifică."))
_question.answers.append(Parag_Model_Answer(False, "Unghiul de atac se reduce, iar profilul și manevrabilitatea parapantei se modifică."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care sunt consecințele alungirii suspantelor D?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Unghiul de atac crește, iar profilul și manevrabilitatea parapantei se modifică."))
_question.answers.append(Parag_Model_Answer(False, "Unghiul de atac crește, profilul rămâne neschimbat și manevrabilitatea parapantei se modifică."))
_question.answers.append(Parag_Model_Answer(False, "Unghiul de atac rămâne neschimbat, iar profilul și manevrabilitatea parapantei se modifică."))
_question.answers.append(Parag_Model_Answer(True, "Unghiul de atac se reduce, iar profilul și manevrabilitatea parapantei se modifică."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care sunt consecințele scurtării suspantelor D?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "Unghiul de atac crește, iar profilul și manevrabilitatea parapantei se modifică."))
_question.answers.append(Parag_Model_Answer(False, "Unghiul de atac crește, profilul rămâne neschimbat și manevrabilitatea parapantei se modifică."))
_question.answers.append(Parag_Model_Answer(False, "Unghiul de atac rămâne neschimbat, iar profilul și manevrabilitatea parapantei se modifică."))
_question.answers.append(Parag_Model_Answer(False, "Unghiul de atac se reduce, iar profilul și manevrabilitatea parapantei se modifică."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cum se schimbă comportamentul parapantei dacă suspantele A sunt prelungite sau întinse?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "Parapanta este mai dificil de gonflat, zboară mai lent datorită unghiului de atac crescut, este mai puțin predispusă la închideri frontale, dar este mai predispusă la angajare parașutată."))
_question.answers.append(Parag_Model_Answer(False, "Parapanta este mai dificil de gonflat, necesită comenzi mai ample dar mai puțin puternice din cauza centrului de greutate situat mai jos și transformă viteza în înălțime (filaj) mai bine la aterizare."))
_question.answers.append(Parag_Model_Answer(False, "Parapanta este mai ușor de gonflat, zboară mai lent datorită unghiului de atac scăzut, este mai puțin predispusă la închideri frontale, dar este mai predispusă la angajare parașutată."))
_question.answers.append(Parag_Model_Answer(False, "Parapanta este mai ușor de gonflat, zboară mai repede datorită scăderii unghiului de atac, este mai predispusă la închideri frontale, dar este mai puțin predispusă la angajare parașutată."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cum se schimbă comportamentul parapantei dacă suspantele D sunt prelungite sau întinse?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Parapanta este mai dificil de gonflat, zboară mai lent datorită unghiului de atac crescut, este mai puțin predispusă la închideri frontale, dar este mai predispusă la angajare parașutată."))
_question.answers.append(Parag_Model_Answer(False, "Parapanta este mai dificil de gonflat, necesită comenzi mai ample dar mai puțin puternice din cauza centrului de greutate situat mai jos și transformă viteza în înălțime (filaj) mai bine la aterizare."))
_question.answers.append(Parag_Model_Answer(False, "Parapanta este mai ușor de gonflat, zboară mai lent datorită unghiului de atac scăzut, este mai puțin predispusă la închideri frontale, dar este mai predispusă la angajare parașutată."))
_question.answers.append(Parag_Model_Answer(True, "Parapanta este mai ușor de gonflat, zboară mai repede datorită scăderii unghiului de atac, este mai predispusă la închideri frontale, dar este mai puțin predispusă la angajare parașutată."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cum se schimbă comportamentul parapantei dacă suspantele A se scurtează?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Parapanta este mai dificil de gonflat, zboară mai lent datorită unghiului de atac crescut, este mai puțin predispusă la închideri frontale, dar este mai predispusă la angajare parașutată."))
_question.answers.append(Parag_Model_Answer(False, "Parapanta este mai dificil de gonflat, necesită comenzi mai ample dar mai puțin puternice din cauza centrului de greutate situat mai jos și transformă viteza în înălțime (filaj) mai bine la aterizare."))
_question.answers.append(Parag_Model_Answer(False, "Parapanta este mai ușor de gonflat, zboară mai lent datorită unghiului de atac scăzut, este mai puțin predispusă la închideri frontale, dar este mai predispusă la angajare parașutată."))
_question.answers.append(Parag_Model_Answer(True, "Parapanta este mai ușor de gonflat, zboară mai repede datorită scăderii unghiului de atac, este mai predispusă la închideri frontale, dar este mai puțin predispusă la angajare parașutată."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cum se schimbă comportamentul parapantei dacă suspantele D se scurtează?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "Parapanta este mai dificil de gonflat, zboară mai lent datorită unghiului de atac crescut, este mai puțin predispusă la închideri frontale, dar este mai predispusă la angajare parașutată."))
_question.answers.append(Parag_Model_Answer(False, "Parapanta este mai dificil de gonflat, necesită comenzi mai ample dar mai puțin puternice din cauza centrului de greutate situat mai jos și transformă viteza în înălțime (filaj) mai bine la aterizare."))
_question.answers.append(Parag_Model_Answer(False, "Parapanta este mai ușor de gonflat, zboară mai lent datorită unghiului de atac scăzut, este mai puțin predispusă la închideri frontale, dar este mai predispusă la angajare parașutată."))
_question.answers.append(Parag_Model_Answer(False, "Parapanta este mai ușor de gonflat, zboară mai repede datorită scăderii unghiului de atac, este mai predispusă la închideri frontale, dar este mai puțin predispusă la angajare parașutată."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("La decolare un pilot observă că una dintre suspantele B ale parapanteii este ruptă. Ce ar trebui să facă pilotul?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Să scoată suspanta ruptă și să zbare fără ea."))
_question.answers.append(Parag_Model_Answer(False, "Să lege capetele cu un nod pescăresc."))
_question.answers.append(Parag_Model_Answer(False, 'Să reconecteze capetele cu o bucată scurtă de suspantă suplimentară, asigurându-se că suspanta "reparată" nu este mai scurtă sau mai lungă decât suspanta B învecinată.'))
_question.answers.append(Parag_Model_Answer(True, "Pilotul nu trebuie să zboare până când suspanta deteriorată este înlocuită."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Comparativ cu o parapantă cu suspante de 5m, una cu suspante de 7m are")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "centrul de greutate mai sus și pendulare mai mare atunci când se schimbă rapid direcția."))
_question.answers.append(Parag_Model_Answer(False, "centrul de greutate mai jos și pendulare mai mică atunci când se schimbă rapid direcția. "))
_question.answers.append(Parag_Model_Answer(True, "centrul de greutate mai jos și pendulare mai mare atunci când se schimbă rapid direcția. "))
_question.answers.append(Parag_Model_Answer(False, "centrul de greutate mai sus și pendulare mai mică atunci când se schimbă rapid direcția."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Comparativ cu o parapantă cu suspante de 7m, una cu suspante de 5m are")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "centrul de greutate mai sus și pendulare mai mare atunci când se schimbă rapid direcția."))
_question.answers.append(Parag_Model_Answer(False, "centrul de greutate mai jos și pendulare mai mică atunci când se schimbă rapid direcția. "))
_question.answers.append(Parag_Model_Answer(False, "centrul de greutate mai jos și pendulare mai mare atunci când se schimbă rapid direcția. "))
_question.answers.append(Parag_Model_Answer(True, "centrul de greutate mai sus și pendulare mai mică atunci când se schimbă rapid direcția."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("După 200 de zboruri cu aceeași parapantă, pilotul observă îndoirea materialului pe întrega anvergură, între atașamentele suspanelor B și C.")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Suspantele B și C trebuie să fie scurtate ușor."))
_question.answers.append(Parag_Model_Answer(False, "Suspantele A și B trebuie să fie scurtate ușor."))
_question.answers.append(Parag_Model_Answer(False, "Parapanta trebuie înlocuită deoarece materialul este prea uzat."))
_question.answers.append(Parag_Model_Answer(True, "Parapanta trebuie să fie verificată  și retrimată de producător."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("După aterizare,  parapanta ar trebui")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "să nu cadă niciodată pe o partea, deoarece încărcarea continuă pe o singură parte a suspantelor poate duce la întinderea asimetrică a acestora."))
_question.answers.append(Parag_Model_Answer(False, "să cadă pe sol înainte sau înapoi pentru a evita încurcarea suspantelor."))
_question.answers.append(Parag_Model_Answer(True, "să nu cadă niciodata în față pe sol, deoarece aerul nu poate scăpa din celule, mărind astfel presiunea internă și, prin urmare, riscul de rupere a traveelor."))
_question.answers.append(Parag_Model_Answer(False, "să fie coborâtă cât mai repede posibil pentru a evita căderea voalurii pe pilot și încurcarea acestuia în suspante."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Dacă un material este supus unei sarcini egale cu rezistența sa maximă, ar trebui să presupuneți următorul  lucru:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "Dimensiunile și forța fizică a materialului nu vor mai fi aceleași ca înaite."))
_question.answers.append(Parag_Model_Answer(False, "Dimensiunile și rezistența originale ale materialului rămân neschimbate, cu condiția ca sarcina maximă să nu fie depășită."))
_question.answers.append(Parag_Model_Answer(False, "Dimensiunile s-au schimbat într-o oarecare măsură, dar rezistența nu este diminuată."))
_question.answers.append(Parag_Model_Answer(False, "Parapanta trebuie retrimată într-o oarecare măsură, pentru a compensa pentru modificarea dimensiunilor."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Tipul de încărcare pe voalura parapantei este:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Presiunea."))
_question.answers.append(Parag_Model_Answer(True, "Tensiunea."))
_question.answers.append(Parag_Model_Answer(False, "Torsiunea"))
_question.answers.append(Parag_Model_Answer(False, "Îndoirea."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Legăturile dintre chingi și suspante sunt cunoscute sub numele de:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Carabinele seletei."))
_question.answers.append(Parag_Model_Answer(True, "Carabine rapide cu filet."))
_question.answers.append(Parag_Model_Answer(False, "Manșonul carabinei."))
_question.answers.append(Parag_Model_Answer(False, "Manșonul suspantei."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Carabinele rapide cu filet de pe chingile portasuspante trebuie să fie")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "strânse."))
_question.answers.append(Parag_Model_Answer(False, "strânes ușor cu mâna."))
_question.answers.append(Parag_Model_Answer(True, "strânse cu mâna, apoi un ¼ de tură cu o cheie."))
_question.answers.append(Parag_Model_Answer(False, "Strângeți cât mai bine posibil cu o cheie și apoi destrângeți un ¼ de tură."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("O parapantă are 4 rânduri de suspante, A, B, C și D. Care grupă de suspante are cea mai mică încărcare în zbor stabil?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "A"))
_question.answers.append(Parag_Model_Answer(False, "B"))
_question.answers.append(Parag_Model_Answer(False, "C"))
_question.answers.append(Parag_Model_Answer(True, "D"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Executarea continuă a manevrelor extreme pe o parapantă normală, certificată")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "nu va duce la o întindere apreciabilă a materialului voalurii."))
_question.answers.append(Parag_Model_Answer(False, "va încărca în diagonală stabilitatorii, rezultând un profil modificat în mijlocul parapantei."))
_question.answers.append(Parag_Model_Answer(True, "poate duce la întinderea diferitelor părți ale parapantei și, prin urmare, la modificarea caracteristicilor de zbor ale parapantei."))
_question.answers.append(Parag_Model_Answer(False, "poate duce la în fisuri în carabinele rapide datorită încărcării."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cum funcționează un accelerator de picior pe o parapantă modernă, de serie?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Prin întinderea picioarelor centrul de greutate se mișcă înainte, reducând unghiul de atac și rezultând accelerarea parapantei."))
_question.answers.append(Parag_Model_Answer(False, "Este atașat suspantelor A, permițând să fie trase în jos suspantele din față, scăzând unghiul de atac și accelerând parapanta."))
_question.answers.append(Parag_Model_Answer(False, "Este atașat la suspantele D, permițând astfel variația lungimii chingilor portsuspante D și, prin urmare, varioația unghiului de atac."))
_question.answers.append(Parag_Model_Answer(True, "Poate acționa chingile portsuspante A,  B și C care îi permit să schimbe lungimea liniilor A , B și C care modifică unghiul de atac și viteza aripii."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Dacă călcăm acceleratorul până la cursa maximă, pe o parapantă modernă, în aer calm,")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "finețea se îmbunătățește."))
_question.answers.append(Parag_Model_Answer(False, "viteza de înfundare scade."))
_question.answers.append(Parag_Model_Answer(True, "crește viteza de înaintare."))
_question.answers.append(Parag_Model_Answer(False, "nu se întâmplă / se schimbă nimic."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Dacă călcăm acceleratorul până la cursa maximă, pe o parapantă modernă, în vânt de față de 25 km/h")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "finețea se îmbunătățește."))
_question.answers.append(Parag_Model_Answer(False, "viteza de înfundare scade."))
_question.answers.append(Parag_Model_Answer(False, "finețea scade."))
_question.answers.append(Parag_Model_Answer(False, "nu se întâmplă / se schimbă nimic."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Trimerele modifică, în general, lungimea")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "chingilor portsuspante A."))
_question.answers.append(Parag_Model_Answer(False, "chingilor portsuspante B."))
_question.answers.append(Parag_Model_Answer(False, "chingilor portsuspante C."))
_question.answers.append(Parag_Model_Answer(True, "chingilor portsuspante D."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Trimerele")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "până la o lungime de 5 cm pot fi adăugate la toate parapantele de serie fără a afecta certificarea sau siguranța parapantei."))
_question.answers.append(Parag_Model_Answer(True, "modifică lungimea și, prin urmare, caracteristicile de zbor ale parapantei. O parapantă cu trimere poate fi garantată ca fiind certificată doar dacă a fost testată cu trimere."))
_question.answers.append(Parag_Model_Answer(False, "afectează comportamentul de zbor al fiecărei parapnte cu fiecare poziție a lor."))
_question.answers.append(Parag_Model_Answer(False, "nu afectează comportamentul de zbor al unei parapante, dar compromite rezistența chingilor."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Pentru zboruri rapide, trimerele sunt")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "eliberate pentru a reduce unghiul de atac și pentru a ridica profilul în spate."))
_question.answers.append(Parag_Model_Answer(False, "eliberate pentru a crește unghiul de atac și pentru a ridica profilul în spate."))
_question.answers.append(Parag_Model_Answer(False, "strânse pentru a reduce unghiul de atac și pentru a coborî profilul din spate."))
_question.answers.append(Parag_Model_Answer(False, "strânse pentru a crește unghiul de atac și pentru a ridica profilul în spate."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Eliberarea trimerelor în timpul unui zbor drept și stabil ")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "reduce șansele de închidere frontală și cursa comenzii necesară pentru controlul direcției devine mai scurtă."))
_question.answers.append(Parag_Model_Answer(True, "crește șansele de închidere frontală și cursa comenzii necesară pentru controlul direcției devine mai lungă."))
_question.answers.append(Parag_Model_Answer(False, "reduce șansele de închidere frontală și cursa comenzii necesară pentru controlul direcției devine mai lungă."))
_question.answers.append(Parag_Model_Answer(False, "crește șansele de închidere frontală și cursa comenzii necesară pentru controlul direcției devine mai scurtă."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Suspantele comezilor pot fi protejate împotriva uzurii prin")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "evitarea folosirii inutile a comenzii."))
_question.answers.append(Parag_Model_Answer(False, "tragerea comenzii din față în jos până la mijloc."))
_question.answers.append(Parag_Model_Answer(True, "folosirea unor scripeți pentru trecerea ghidarea suspantelor."))
_question.answers.append(Parag_Model_Answer(False, "aplicarea comenzilor într-o manieră foarte controlată."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Lungimea corectă a comenzilor")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "trebuie ajustată pentru a se potrivi poziției seletei și pilotului."))
_question.answers.append(Parag_Model_Answer(True, "este determinată de către producător și trebuie scurtată numai de către ei sau reprezentanții acestora."))
_question.answers.append(Parag_Model_Answer(False, "depinde de greutatea pilotului și de viteza de înaintare dorită."))
_question.answers.append(Parag_Model_Answer(False, "trebuie să fie ajustate pentru a se potrivi dimensiunii corpului, în special lungimii brațului pilotului."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Lungimea comenzilor este stabilită astfel încât")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "nu este niciodată necesar să înfășurați suspantele comenzii pe mâini la aterizare."))
_question.answers.append(Parag_Model_Answer(False, "parapanta zboară cu cea mai bună finețe cu comenzile trase la înălțimea umărului."))
_question.answers.append(Parag_Model_Answer(True, "este posibil să se atingă întreaga gamă de vitezeă a parapantei fără probleme."))
_question.answers.append(Parag_Model_Answer(False, "să fie cât mai scurte posibil pentru a evita încurcarea cu suspantele D."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("În timp ce zburăm cu comenzile frânate, suspantele D se detensionează formând un arc, ce putem concluziona?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "Comenzile preiau sarcina suspantelor D, ceea ce este normal când se zboară frânat."))
_question.answers.append(Parag_Model_Answer(False, "Suspantele D s-au întins treptat sub sarcină. Parapanta trebuie trimisă producătorului pentru verificare."))
_question.answers.append(Parag_Model_Answer(False, "Suspantele comenzilor au fost reglate prea scurt și, prin urmare, trebuie să fie prelungite."))
_question.answers.append(Parag_Model_Answer(False, "Parapanta a fost livrată cu suspantele D prea lungi. Acestea trebuie înlocuite."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce efect va avea o seletă cu chingi diagonale asupra pilotului?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Pilotul simte mai puțin turbulența și are capacitate mai mare de a controla parapanta prin deplasarea greutății."))
_question.answers.append(Parag_Model_Answer(False, "Pilotul simte mai mult turbulența și are capacitate mai mare de a controla parapanta prin deplasarea greutății."))
_question.answers.append(Parag_Model_Answer(False, "Pilotul simte mai mult turbulența și are capacitate mai mică de a controla parapanta prin deplasarea greutății."))
_question.answers.append(Parag_Model_Answer(True, "Pilotul simte mai puțin turbulența și are capacitate mai mică de a controla parapanta prin deplasarea greutății."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce efect va avea o seletă fără chingi diagonale asupra pilotului?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Pilotul simte mai puțin turbulența și are capacitate mai mare de a controla parapanta prin deplasarea greutății."))
_question.answers.append(Parag_Model_Answer(True, "Pilotul simte mai mult turbulența și are capacitate mai mare de a controla parapanta prin deplasarea greutății."))
_question.answers.append(Parag_Model_Answer(False, "Pilotul simte mai mult turbulența și are capacitate mai mică de a controla parapanta prin deplasarea greutății."))
_question.answers.append(Parag_Model_Answer(False, "Pilotul simte mai puțin turbulența și are capacitate mai mică de a controla parapanta prin deplasarea greutății."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Dacă se scurtează chinga de piept a seletei (se micșorează distanța dintre carabinele principale)")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "pilotul simte mai mult turbulența și crește pericolul unei răsuciri."))
_question.answers.append(Parag_Model_Answer(True, "pilotul simte mai puțin turbulența și crește pericolul unei răsuciri."))
_question.answers.append(Parag_Model_Answer(False, "pilotul simte mai mult turbulența și pericolul unei răsuciri este redus."))
_question.answers.append(Parag_Model_Answer(False, "pilotul simte mai puțin turbulența și pericolul unei răsuciri este redus."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Dacă se lungește chinga de piept a seletei (se mărește distanța dintre carabinele principale)")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "pilotul simte mai mult turbulența și crește pericolul unei răsuciri."))
_question.answers.append(Parag_Model_Answer(False, "pilotul simte mai puțin turbulența și crește pericolul unei răsuciri."))
_question.answers.append(Parag_Model_Answer(True, "pilotul simte mai mult turbulența și pericolul unei răsuciri este redus."))
_question.answers.append(Parag_Model_Answer(False, "pilotul simte mai puțin turbulența și pericolul unei răsuciri este redus."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce efect au seletele cu puncte înalte de atașare a carabinelor în timpul turbulențelor?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Pilotul simte mai puțin turbulența, dar îi este mai dificil a se apleca înainte când accelerează la decolare."))
_question.answers.append(Parag_Model_Answer(False, "Pilotul simte mai mult turbulența, dar îi este mai puțin dificil a se apleca înainte când accelerează la decolare."))
_question.answers.append(Parag_Model_Answer(False, "Pilotul simte mai puțin turbulența, dar îi este mai puțin dificil a se apleca înainte când accelerează la decolare."))
_question.answers.append(Parag_Model_Answer(False, "Pilotul simte mai mult turbulența, dar îi este mai dificil a se apleca înainte când accelerează la decolare."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce efect au seletele cu puncte joase de atașare a carabinelor în timpul turbulențelor?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "Pilotul simte mai puțin turbulența, dar îi este mai dificil a se apleca înainte când accelerează la decolare."))
_question.answers.append(Parag_Model_Answer(True, "Pilotul simte mai mult turbulența, dar îi este mai puțin dificil a se apleca înainte când accelerează la decolare."))
_question.answers.append(Parag_Model_Answer(False, "Pilotul simte mai puțin turbulența, dar îi este mai puțin dificil a se apleca înainte când accelerează la decolare."))
_question.answers.append(Parag_Model_Answer(False, "Pilotul simte mai mult turbulența, dar îi este mai dificil a se apleca înainte când accelerează la decolare."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("O seletă fără chingi diagonale pe o parapantă este înlocuită cu o seletă cu chingi transversale, acest fapt va avea, printre altele, o influență asupra")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "graficului polarei vitezelor a parapantei."))
_question.answers.append(Parag_Model_Answer(True, "comportamentului parapantei în situații extreme de zbor."))
_question.answers.append(Parag_Model_Answer(False, "profilului și, prin urmare, unghiului de atac al parapantei."))
_question.answers.append(Parag_Model_Answer(False, "torsiunii profilului parapantei."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Dacă o seletă este reglată astfel încât pilotul să fie într-o poziție foarte înclinată, avantajul este că")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "rezistența la înaintare este mai mică și finețea mai bună."))
_question.answers.append(Parag_Model_Answer(False, "riscul de răsucire într-o situație necontrolată este redus la minimum."))
_question.answers.append(Parag_Model_Answer(False, "parapanta este mai ușor de condus prin schimbarea de greutate."))
_question.answers.append(Parag_Model_Answer(False, "parapanta este mai ușor de gonflat."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Dacă o seletă este reglată astfel încât pilotul să fie într-o poziție foarte înclinată, dezavantajul este că")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "rezistența la înaintare este mai mare și finețea mai mică."))
_question.answers.append(Parag_Model_Answer(True, "riscul de răsucire este mărit într-o situație necontrolabilă."))
_question.answers.append(Parag_Model_Answer(False, "parapanta nu poate fi condusă prin schimbarea de greutate."))
_question.answers.append(Parag_Model_Answer(False, "parapanta este mai greu de gonflat."))