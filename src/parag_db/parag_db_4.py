from parag_model.parag_model  import *

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_category        = Parag_Model_Category()
_category.name   = "performante umane"
PARAG_CATEGORY_4 = _category

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("De ce se aplica un badaj de tifon pe o rana?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "pentru a opri hemoragia"))
_question.answers.append(Parag_Model_Answer(True, "pentru calmarea durerilor"))
_question.answers.append(Parag_Model_Answer(True, "pentru a impiedica infectarea ranii"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("In cazul unui singur salvator, manevrele de resuscitare se fac continuu:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "pana la sosirea unei ambulantei"))
_question.answers.append(Parag_Model_Answer(True, "pana la extenuarea fizica a salvatorului"))
_question.answers.append(Parag_Model_Answer(True, "pana la extenuarea fizica a salvatorului"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Secventele resuscitarii unui pacient inconstient care nu respira normal sunt urmatoarele:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "cautam eventuale leziuni"))
_question.answers.append(Parag_Model_Answer(True, "deschidem caile aeriene si verificam respiratia si circulatia"))
_question.answers.append(Parag_Model_Answer(False, "il punem in pozitie laterala de siguranta"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Semne de certitudine ale unei fracturi de sunt:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "nu se tranmite miscarea desi e os continuu"))
_question.answers.append(Parag_Model_Answer(True, "desi nu este o articulatie la locul fracturii se misca anormal"))
_question.answers.append(Parag_Model_Answer(True, "se aude si se simte frecarea capetelor osului"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Hematomul este:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "escoriatie la nivel superficial fara a ajunge la vasele de sange"))
_question.answers.append(Parag_Model_Answer(True, "infiltrare de sange sub piele unde se rup micile vase de sange"))
_question.answers.append(Parag_Model_Answer(True, "colectie de sange care apare prin ruperea unui vas mare de sange"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Masajul cardiac se efectuează la adult în cazul BLS de către 1 persoană în raport de :")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "5 / 1"))
_question.answers.append(Parag_Model_Answer(False, "5 / 2"))
_question.answers.append(Parag_Model_Answer(True, "30 / 2"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("In cazul in care exista o sangerare masiva externa este indicata")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "presiune directa pe plaga cu un pansament"))
_question.answers.append(Parag_Model_Answer(False, "dacă plaga este produsă de un corp contondent, care se află încă în plagă, se scoate pentru a face compresie pe plaga cat mai repede şi se transportă victima de urgenţă la spital."))
_question.answers.append(Parag_Model_Answer(False, "aplicarea garoului"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Verificarea respiratiei la un pacient se face prin:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "privirea miscarilor toracelui"))
_question.answers.append(Parag_Model_Answer(True, "ascultarea la nivelul gurii a zgomotelor respiratorii"))
_question.answers.append(Parag_Model_Answer(True, "simtirea pe obraz a aerului expirat"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("In cazul imposibilitatii practicarii respiratiei gura la gura se:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "asteapta ajutor calificat,"))
_question.answers.append(Parag_Model_Answer(True, "se face respiratie gura la nas,"))
_question.answers.append(Parag_Model_Answer(False, "se transporta cat mai urgent la spital"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce este luxatia?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "leziune inchisa a unei articulatii, care a fost fortata sa faca o miscare / deplasare exagerata, dupa care suprafetele articulare ale oaselor si-au revenit la pozitia normala"))
_question.answers.append(Parag_Model_Answer(True, "leziune a unei articulatii, la care suprafetele articulare ale oaselor sunt deplasate permanent din pozitia normala"))
_question.answers.append(Parag_Model_Answer(False, "intreruperea totala sau partiala a continuitatii unui os"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce este o entorsa?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "leziune inchisa a unei articulatii, care a fost fortata sa faca o miscare /deplasare exagerata, dupa care suprafetele articulare ale oaselor si-au revenit la pozitia normala"))
_question.answers.append(Parag_Model_Answer(False, "leziune a unei articulatii, la care suprafetele articulare ale oaselor sunt deplasate permanent din pozitia normala"))
_question.answers.append(Parag_Model_Answer(False, "intreruperea totala sau partiala a continuitatii unui os"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Simptomele oboselii includ:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "greşeli mari, un slab raţionament, decizii slabe sau indecizia"))
_question.answers.append(Parag_Model_Answer(False, "concentrare marita"))
_question.answers.append(Parag_Model_Answer(True, "reacţii încetinite, slaba coordonare ochi-mână"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cu ce se recomanda transportarea persoanelor accidentate, care prezinta fracturi de coloana?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "cu un autoturism, deoarece asigura ranitului confort"))
_question.answers.append(Parag_Model_Answer(False, "cu orice mijloc de transport"))
_question.answers.append(Parag_Model_Answer(True, "cu un mijloc de transport cu platforma"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care este prima masura pe care trebuie sa o luati cand o persoana, ce a fost implicata intr-un accident, are o rana cu hemoragie?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "sa pansati rana"))
_question.answers.append(Parag_Model_Answer(True, "sa opriti hemoragia"))
_question.answers.append(Parag_Model_Answer(False, "sa curatati rana"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cum se face oprirea hemoragiei ?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "prin legarea stransa a bratului deasupra rani"))
_question.answers.append(Parag_Model_Answer(False, "prin legarea lejera a bratului deasupra ranii"))
_question.answers.append(Parag_Model_Answer(False, "prin legarea stransa a bratului in dreptul ranii"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce trebuie sa faceti, in primul rand, pentru a salva o persoana implicata intr-un accident?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "sa-i eliberati si sa-i degajati caile respiratorii"))
_question.answers.append(Parag_Model_Answer(False, "sa-i indreptati membrele fracturate"))
_question.answers.append(Parag_Model_Answer(False, "sa-i curatati ranile"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cum trebuie asezat un ranit care prezinta leziuni ale coloanei vertebrale?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "in aceasta situatie este recomandabil sa nu fie miscat pana la sosirea ambulantei"))
_question.answers.append(Parag_Model_Answer(False, "in pozitie sezanda"))
_question.answers.append(Parag_Model_Answer(False, "orizontal, cu fata in sus"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce trebuie sa aveti in vedere inaintea transportarii unei victime?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "ca autovehiculul cu care o veti transporta sa fie confortabil"))
_question.answers.append(Parag_Model_Answer(True, "ca functiile respiratorii si circulatorii sa fie asigurate"))
_question.answers.append(Parag_Model_Answer(False, "ca victima sa fie asistata, in timpul transportului, de o persoana competenta"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Pentru ce se folosesc substantele antiseptice?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "pentru oprirea hemoragiei"))
_question.answers.append(Parag_Model_Answer(True, "pentru dezinfectia plagilor"))
_question.answers.append(Parag_Model_Answer(False, "pentru calmarea durerilor"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce se aplica pe plaga, intr-un pansament?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "o compresa oarecare"))
_question.answers.append(Parag_Model_Answer(False, "o compresa de vata sterila"))
_question.answers.append(Parag_Model_Answer(True, "o compresa de tifon steril"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cum trebuie asezata o victima care a pierdut mult sange?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "in pozitie sezanda"))
_question.answers.append(Parag_Model_Answer(False, "culcata pe o parte"))
_question.answers.append(Parag_Model_Answer(True, "cu picioarele situate mai sus decat nivelul corpului"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce se impune pentru tratamentul de urgenta al unor plagi?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "curatarea, dezinfectia si pansarea plagilor"))
_question.answers.append(Parag_Model_Answer(False, "punerea tijelor de lemn pe zona ranita"))
_question.answers.append(Parag_Model_Answer(False, "pansarea plagilor"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce trebuie sa faceti pentru a evita complicatiile in cazul unei fracturi?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "sa curatati si sa dezinfectati zona"))
_question.answers.append(Parag_Model_Answer(False, "sa pansati zona fracturata"))
_question.answers.append(Parag_Model_Answer(True, "sa imobilizati zona fracturata"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cum se apreciaza gravitatea unei hemoragii?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "in functie de culoarea sangelui pierdut"))
_question.answers.append(Parag_Model_Answer(False, "in functie de fluiditatea sangelui pierdut"))
_question.answers.append(Parag_Model_Answer(True, "in functie de cantitatea sangelui pierdut"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cand se transporta persoanele accidentate ce prezinta hemoragii externe?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "imediat dupa oprirea hemoragiei"))
_question.answers.append(Parag_Model_Answer(False, "imediat dupa ce o persoana calificata i-a acordat asistenta medicala"))
_question.answers.append(Parag_Model_Answer(False, "imediat dupa sosirea unui mijloc de transport dotat cu platforma"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cum se pot opri hemoragiile la trunchi si la cap?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "prin aplicarea compreselor sterile si a pansamentului compresiv"))
_question.answers.append(Parag_Model_Answer(False, "prin aplicarea garoului"))
_question.answers.append(Parag_Model_Answer(False, "prin aplicarea atelelor"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cu ce se dezinfecteaza plagile inainte de a fi pansate?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "acid sulfuric"))
_question.answers.append(Parag_Model_Answer(True, "cu apa oxigenata"))
_question.answers.append(Parag_Model_Answer(True, "cu iod"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cum trebuie asezata o persoana ranita care prezinta leziuni ale coloanei vertebrale?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "orizontal, cu fata in sus"))
_question.answers.append(Parag_Model_Answer(False, "in pozitie sezanda"))
_question.answers.append(Parag_Model_Answer(True, "in situatia aceasta nu trebuie sa fie miscat pana la sosirea salvarii"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cum trebuie sa stea o persoana, ce a suferit leziuni intr-un accident, pana la transportarea la spital?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "intr-o pozitie cat mai comoda"))
_question.answers.append(Parag_Model_Answer(False, "obligatoriu cu fata in sus"))
_question.answers.append(Parag_Model_Answer(True, "intr-o pozitie care sa permita o buna respiratie"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cum se poate face respiratia artificiala in cazul in care gura ranitului a ramas inclestata?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "prin narile victimei"))
_question.answers.append(Parag_Model_Answer(False, "in cazul acesta nu se face respiratie artificiala"))
_question.answers.append(Parag_Model_Answer(False, "in acest ca  se face o incizie in obrazul victimei, pe unde apoi se face respiratia artificiala"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cum trebuie sa fie atelele pentru imobilizarea unei fracturi?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "sa nu fie foarte grele"))
_question.answers.append(Parag_Model_Answer(False, "foarte flexibile"))
_question.answers.append(Parag_Model_Answer(True, "sa fie suficient de lungi pentru a acoperi in intregime atat zona de deasupra, cat si cea de sub fractura"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("De ce se aplica un bandaj de tifon pe o rana deschisa?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "pentru a opri hemoragia"))
_question.answers.append(Parag_Model_Answer(True, "pentru calmarea durerilor"))
_question.answers.append(Parag_Model_Answer(True, "pentru a impiedica infectarea ranii"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce simptome prezinta o victima a unui accident care a suferit stop cardiac?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "aparitia hemoragiei pe gura"))
_question.answers.append(Parag_Model_Answer(True, "lipsa pulsului"))
_question.answers.append(Parag_Model_Answer(False, "innegrirea fetei si inrosirea ochilor"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care poate fi cauza stopului respirator in cazul persoanelor ce au fost implicate intrun accident?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "pierderea unei cantitati mari de sange"))
_question.answers.append(Parag_Model_Answer(False, "o leziune puternica in zona lombara"))
_question.answers.append(Parag_Model_Answer(True, "blocarea cailor respiratorii"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cum sa executati masajul cardiac unei persoane care a fost implicata intr-un accident, in urma caruia i s-au oprit bataile inimii?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "prin lovirea usoara cu palmele a obrajilor victimei"))
_question.answers.append(Parag_Model_Answer(True, "prin apasarea ritmica cu podul palmelor suprapuse a toracelui victimei, in dreptul inimii"))
_question.answers.append(Parag_Model_Answer(False, "numai o persoana calificata trebuie sa faca masajul cardiac"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cum se face imobilizarea membrului inferior ce a fost fracturat intr-un accident?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "cu ajutorul atelelor"))
_question.answers.append(Parag_Model_Answer(False, "legand strans garoul in jurul membrului"))
_question.answers.append(Parag_Model_Answer(False, "prin bandajarea locului fracturii"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Cum va fi ridicata o persoana grav ranita intr-un accident?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "cu atentie, de maini si de picioare de catre doua persoane"))
_question.answers.append(Parag_Model_Answer(True, "cu atentie, mentinandu-se in acelasi plan capul, gatul si toracele"))
_question.answers.append(Parag_Model_Answer(False, "mentinand picioarele in sus si capul ceva mai jos decat trunchiul, pentru o mai buna circulatie a sangelui in organism"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Caile respiratorii se pot astupa din cauza ca:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "victima a suferit un atac de panica"))
_question.answers.append(Parag_Model_Answer(True, "victimei i-au intrat corpuri straine pe caile respiratorii"))
_question.answers.append(Parag_Model_Answer(False, "victima sufera de scolioza"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Atunci când condiţiile meteo nu sunt tocmai favorabile cel mai mult contează:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "pregătirea teoretică a pilotului"))
_question.answers.append(Parag_Model_Answer(False, "nivelul tehnic al pilotului"))
_question.answers.append(Parag_Model_Answer(True, "atitudinea pilotului"))

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Hipoxia apare datorita :")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "deshidratarii"))
_question.answers.append(Parag_Model_Answer(True, "lipsei oxigenului"))
_question.answers.append(Parag_Model_Answer(False, "stresului"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Echiparea cu parasuta este obligatorie:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "in zborurile de antrenament"))
_question.answers.append(Parag_Model_Answer(True, "indiferent de inaltime"))
_question.answers.append(Parag_Model_Answer(False, "nu este obligatorie, ramane la hotararea comandantului de aeronava"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Vârsta până la care se poate practica parapantismul este:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "40 de ani"))
_question.answers.append(Parag_Model_Answer(False, "45 de ani"))
_question.answers.append(Parag_Model_Answer(True, "nu există limite dacă starea de sănătate permite"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce masuri sunt recomandate inaintea zborului pentru prevenirea raului de zbor ?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "somul suficient de noapte, de minim 8 ore"))
_question.answers.append(Parag_Model_Answer(True, "o alimentatie adecvata"))
_question.answers.append(Parag_Model_Answer(False, "o echipare corespunzatoare"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce efect asupra organismului poate avea o succesiune de viraje cu inclinare mare ?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "tulburare de vedere"))
_question.answers.append(Parag_Model_Answer(False, "respiratie dificila pe nas"))
_question.answers.append(Parag_Model_Answer(True, "pierderea cunostintei"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Este important ca un elev pilot să fie odihnit înainte de a veni la cursuri de parapantism?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "să se simtă bine, asta e important"))
_question.answers.append(Parag_Model_Answer(True, "întotdeauna este bine ca un pilot să fie odihnit înainte de decolare."))
_question.answers.append(Parag_Model_Answer(False, "chiar dacă nu s-a dormit o noapte, dacă este obişnuit poate face cîteva zboruri."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Care sunt cele mai importante decizii de luat cînd se decolează pe condiţii periculoase ?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "menţinerea aripii deasupra capului şi conducerea aripi cu multă atenţie."))
_question.answers.append(Parag_Model_Answer(False, "deschiderea paraşutei de rezerve dacă avem un incident grav."))
_question.answers.append(Parag_Model_Answer(True, "nu se decolează niciodată în condiţii periculoase."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Ce se poate întâmpla din cauza suprasarcinilor produse la manevrele de acrobaţie ?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "pilotul îşi poate pierde cunoştinţa."))
_question.answers.append(Parag_Model_Answer(False, "fara o pregătire fizică şi psihică bună nu se execută manevre de acrobaţie."))
_question.answers.append(Parag_Model_Answer(True, "suprasolicitarea poate duce la deteriorarea ariipi daca acesta este uzată."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("Este foarte cald, e bine să ne suprasolicităm ca să facem cit mai multe zboruri profitînd de vremea bună ?")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "întodeauna se decolează pentru a profita de condiţiile meteo cît mai mult."))
_question.answers.append(Parag_Model_Answer(False, "numai dacă se transpiră din greu se obţin rezultate foarte rapid."))
_question.answers.append(Parag_Model_Answer(True, "întotdeauna trebuie să ne cunoaştem limitele şi să nu ne suprasolicităm înainte de decolare."))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("PLS reprezintă:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(True, "pozitia prin care se previne aspiratia vomismentelor"))
_question.answers.append(Parag_Model_Answer(False, "pozitia laterala de siguranta a salvatorului"))
_question.answers.append(Parag_Model_Answer(True, "pozitia in care se aseaza pacientii inconstienti, dar care respiră"))
"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
_question       = Parag_Model_Question("In tratamentul hipotermiei este recomandat sa:")
_category.questions.append(_question)
_question.answers.append(Parag_Model_Answer(False, "se maseze zonele degerate"))
_question.answers.append(Parag_Model_Answer(False, "se adminstreze bauturi alcoolice victimei"))
_question.answers.append(Parag_Model_Answer(True, "se realizeze incalzirea victimei gradual"))
