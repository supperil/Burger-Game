from pyscript import when#la utilizzo per segnalare quando un evento dovrà accadere
from js import document#mi serve per sfruttare il document.getElementById(id) ecc da python
import random as rand#mi serve a eseguire i numeri randomici
from pyweb import pydom#mi serve per creare elementi html da python
import threading#potevo utilizzare altre librerie per fare aspettare tot secondi ma ho preferito questa. Dal nome si intuisce si possa usare per sfruttare i thread su python
import js#la utilizzo per chiamare funzioni javascript dal mio python


culoSu=True#variabili del panino ordinato impostate a vere perché sempre presenti
culoGiu=True
#dizionario degli elementi del panino che viene ordinato (senza parti del pane poiché già presenti)
elementi_panino = [
    {
        "valore": 0,
        "filename": "carne",
        "title":"hamburger"
    },
    {
        "valore": 0,
        "filename": "polloP",
        "title":"pollo"
    },
    {
        "valore": 0,
        "filename": "baconP",
        "title":"bacon"
    },
    {
        "valore": 0,
        "filename": "pomodoroP",
        "title":"pomodoro"
    },
    {
        "valore": 0,
        "filename": "fogliaInsalata",
        "title":"insalata"
    },
    {
        "valore": 0,
        "filename": "avocadoP",
        "title":"avocado"
    },
    {
        "valore": 0,
        "filename": "ketchupP",
        "title":"ketchup"
    },
    {
        "valore": 0,
        "filename": "maioneseP",
        "title":"maionese"
    },
    {
        "valore": 0,
        "filename": "sBurgherP",
        "title":"salsa burgher"
    }
]
#dizionario del panino che viene composto,compreso il pane essendo che è l'utente che lo inserisce
elementi_panino2 = [
    {
        "valore":0,
        "filename":"culoSu"
    },
    {
        "valore":0,
        "filename":"culoGiu"
    },
    {
        "valore": 0,
        "filename": "carne"
    },
    {
        "valore": 0,
        "filename": "polloP"
    },
    {
        "valore": 0,
        "filename": "baconP"
    },
    {
        "valore": 0,
        "filename": "pomodoroP"
    },
    {
        "valore": 0,
        "filename": "fogliaInsalata"
    },
    {
        "valore": 0,
        "filename": "avocadoP"
    },
    {
        "valore": 0,
        "filename": "ketchupP"
    },
    {
        "valore": 0,
        "filename": "maioneseP"
    },
    {
        "valore": 0,
        "filename": "sBurgherP"
    }
]
frase='Salve vorrei un panino con:\n'#frase iniziale
risultatoGiusto=2#variabile per la prima scrematura di correzione, che è quella corretta (parte da due perché il pane è composto da due elementi)
risultatoControlla=0#variabile che tene conto degli elementi selezionati
precario = pydom['#precario'][0]#utiliziamo pydom per selezionare in quale div inserire gli elementi
b_riprova=pydom['#bottoni'][0]
tempConta = 100#utilizzato per il z-index
punteggio=0#abbastanza auto esplicativo è il punteggio


#questa funzione permette di cambiare pagina senza implementare una nuova pagina html
#inoltre inizia per la prima volta ad assegnare i valori casuali
@when("click", "#cambio_schermata")
def cambioSchermata(e):
    global risultatoGiusto, panino
    global frase
    document.getElementById('schermata_inizio').style.display='none'
    document.getElementById('cucina').style.display='block'
    js.inizio('')#sweetalert
    for i in elementi_panino:
        i['valore'] = rand.randrange(2)#assegna a tutti gli elementi dell'ordine(tranne il pane) valore casuale
    
    aggiornaPunteggio()#anche questo abbastanza auto esplicativa, verrà spiegata dopo

    panino = pydom['#ordine'][0]#permette di selezionare tramite pydom un div dove potremmo aggiungere elementi
    panino.append(buildPreset())#append serve per creali e "appenderli" in definitivo sulla pagina, inseriamo una funzione perché tutto ciò all'interno di essa verrà appesa


#questa funzione aggiorna il punteggio a video ogni volta che richiamata
def aggiornaPunteggio():
    document.getElementById('punteggio').innerHTML=f"Punteggio={punteggio}"

#questa funzione permette di creare tutte le volte l'ordine con tanto di panino e frase descrittiva
def buildPreset():
    global risultatoGiusto, risultatoControlla, punteggio#variabili globali utilizzati nella funzione
    global frase
    if punteggio!=4:#permette di personalizzare l'ultimo cliente
        frase="Salve vorrei un panino con:"
    else:
        frase="voglio il mio famosissimo PANINO ALLA SCIBETTA con:"
    div_el = pydom.create('div')#permette di creare un div che per comodità ho denominato div_el
    img_culo_su = js.document.createElement('img')#si tralascia il nome particolare, comunque essendo due elementi già presenti li creo
    img_culo_giu = js.document.createElement('img')#sottolineo che li sto solo creando e non ancora appendendo
    
    img_culo_giu.setAttribute('src', "risorse/culoGiu.png")#per permettere di avere una fonte per delle immagini tramite set attribute gli conferisco la risorsa
    img_culo_su.setAttribute('src', "risorse/culoSu.png")#ad entrambi
    
    img_culo_giu.setAttribute('title', 'sotto del panino')#per far si che sia specificato anche al passaggio del mouse
    img_culo_su.setAttribute('title', 'sopra del panino')
    img_culo_su.style.zIndex = "12"#utilizzato per z-index
    
    div_el.id = 'panino'#dò un id a questo div per poterlo sfruttare poi
    div_el.style.zIndex = "0"#così non sarà al di sopra di nulla
    div_el.append(img_culo_su)#inizio ad appendere la parte superiore del panino
    
    #tramite questo ciclo controllo il valore di ogni elemento del dizionario dell'ordine del cliente
    for index, el in enumerate(elementi_panino[::-1]):
        if not el['valore']: continue#se è vera entro nell'if
        risultatoGiusto+=1#così sarà possibile la prima scrematura di controllo
        img_el = js.document.createElement('img')#creo ogni volta un elemento immagine
        img_el.setAttribute('src', f"risorse/{el['filename']}.png")#che avrà come collegamento l'elemento filename giusto(è stato comodo farli tutti in png)
        frase+=el['title']+', '#si aggiunge ogni volta l'elemento title anch'esso presente nel dizionario per comporre la frase
        img_el.setAttribute('alt', el['filename'])#ad ognuno dò un alt in caso di problemi con le foto
        img_el.setAttribute('title', el['title'])#e ad ognuno dò il title sta volta come attributo dell'elemento stesso
        img_el.style.zIndex = str(len(elementi_panino) - index)#grazie a questa espressione riesco ad affibiare ad ogni elemento uno z index inferiore così che risultino uno sotto l'altro
        div_el.append(img_el)#finalmente appendo e quindi faccio visionare la foto
    
    frase=frase[:-2]#elimino due elementi che sarebbero ", "
    frase+='.'#per poi aggiungere il punto(è più ordinato)
    document.getElementById('frase').innerHTML=frase#inserisco la frase finalmente costruita a video
    div_el.append(img_culo_giu)#chiudo il meraviglioso panino con la parte sottostante
    js.errore(risultatoControlla)#funzione che ho usato per controllare le variabili, la troverà un po' ovunque
    
    return div_el#restituisco questo buon panino di un div che verrà appeso per intero
    
#tramite questa funzione costruisco il panino che l'utente seleziona
def bild_panino(chiave):
    global precario, tempConta#variabili globali utilizzate
    
    for index, el in enumerate(elementi_panino2[::-1]):#ciclo per scorrere gli elementi del secondo dizionario(panino utente)
        if el['filename']==chiave:#chiave è una stringa che le funzioni sottostanti passeranno che serve per capire quale elemento è stato selezionato
            if el['valore']:#controllo il valore dell'elemento per verificare se è stato selezionato o deselezionato
                #se è stato selezionato:
                img_el = js.document.createElement('img')#come prima creo l'elemento immagine
                img_el.setAttribute('src', f"risorse/{el['filename']}.png")#lo collego all'annesso file
                img_el.style.zIndex = tempConta#sistemo lo z-index
                tempConta -= 1#idem qui
                img_el.setAttribute('id', f"{el['filename']}{index}")#come prima dò un attributo
                precario.append(img_el)#si appente il tutto dentro precario inizializzato con pydom nelle prime righe
            else:#se è stato deselezionato
                el_da_rimuovere = document.getElementById(f"{el['filename']}{index}")#prendo l'elemento dal id
                el_da_rimuovere.parentNode.removeChild(el_da_rimuovere)#lo rimuovo
                tempConta += 1#sistemo lo z-index

#PUNTO DI RIPETIZIONE 1
#qui abbiamo la funzione when per ogni elemento che può comporre il panino composto da
#un ciclo che cerca il filename corretto
#inverte il valore dell'elemento nel dizionario del panino dell'utente(così si attiverà o disattiverà)
#inoltre se stai mettendo la salsa o il condimento si sentira il suono invece se lo si sta levando se ne sentirà un'altro
#variabile globale del risultato da controllare per poi eseguire la scrematura di errore, se esso viene attivato e quindi abbiamo 1 aumenta senno diminuisce di 1
#infine richiamo la funzione bild_panino e gli ripasso il nome del file
#avrei potuto fare tutto insieme ma ho preferito così
@when("click", "#ketchup")
def kt(e):
    global risultatoControlla
    for index, el in enumerate(elementi_panino2[::-1]):
        if el['filename']=='ketchupP':
            el['valore']= not (el['valore'])
            if el['valore']==1:
                risultatoControlla+=1
                js.squeesound()
            else:
                risultatoControlla-=1
                js.removeSound()
    bild_panino("ketchupP")
    js.errore(risultatoControlla)#sempre per controllare

#PUNTO DI RIPETIZIONE 1
@when("click", "#maionese")
def ms(e):
    global risultatoControlla
    for index, el in enumerate(elementi_panino2[::-1]):
        if el['filename']=='maioneseP':
            el['valore']= not (el['valore'])
            if el['valore']==1:
                risultatoControlla+=1
                js.squeesound()
            else:
                risultatoControlla-=1
                js.removeSound()
    bild_panino("maioneseP")
    js.errore(risultatoControlla)

#PUNTO DI RIPETIZIONE 1
@when("click", "#sburger")
def sb(e):
    global risultatoControlla
    for index, el in enumerate(elementi_panino2[::-1]):
        if el['filename']=='sBurgherP':
            el['valore']= not (el['valore'])
            if el['valore']==1:
                risultatoControlla+=1
                js.squeesound()
            else:
                risultatoControlla-=1
                js.removeSound()
    bild_panino("sBurgherP")
    js.errore(risultatoControlla)

#PUNTO DI RIPETIZIONE 1
@when("click", "#insalata")
def ins(e):
    global risultatoControlla
    for index, el in enumerate(elementi_panino2[::-1]):
        if el['filename']=='fogliaInsalata':
            el['valore']= not (el['valore'])
            if el['valore']==1:
                risultatoControlla+=1
                js.foodSound()
            else:
                risultatoControlla-=1
                js.removeSound()
    bild_panino("fogliaInsalata")
    js.errore(risultatoControlla)

#PUNTO DI RIPETIZIONE 1
@when("click", "#pomodoro")
def pom(e):
    global risultatoControlla
    for index, el in enumerate(elementi_panino2[::-1]):
        if el['filename']=='pomodoroP':
            el['valore']= not (el['valore'])
            if el['valore']==1:
                risultatoControlla+=1
                js.foodSound()
            else:
                risultatoControlla-=1
                js.removeSound()
    bild_panino("pomodoroP")
    js.errore(risultatoControlla)

#PUNTO DI RIPETIZIONE 1
@when("click", "#avocado")
def avoc(e):
    global risultatoControlla
    for index, el in enumerate(elementi_panino2[::-1]):
        if el['filename']=='avocadoP':
            el['valore']= not (el['valore'])
            if el['valore']==1:
                risultatoControlla+=1
                js.foodSound()
            else:
                risultatoControlla-=1
                js.removeSound()
    bild_panino("avocadoP")
    js.errore(risultatoControlla)

#PUNTO DI RIPETIZIONE 1
@when("click", "#paninoSu")
def ps(e):
    global risultatoControlla
    for index, el in enumerate(elementi_panino2[::-1]):
        if el['filename']=='culoSu':
            el['valore']= not (el['valore'])
            if el['valore']==1:
                risultatoControlla+=1
                js.foodSound()
            else:
                risultatoControlla-=1
                js.removeSound()
    bild_panino("culoSu")
    js.errore(risultatoControlla)

#PUNTO DI RIPETIZIONE 1
@when("click", "#paninoGiu")
def pg(e):
    global risultatoControlla
    for index, el in enumerate(elementi_panino2[::-1]):
        if el['filename']=='culoGiu':
            el['valore']= not (el['valore'])
            if el['valore']==1:
                risultatoControlla+=1
                js.foodSound()
            else:
                risultatoControlla-=1
                js.removeSound()
    bild_panino("culoGiu")
    js.errore(risultatoControlla)

#PUNTO DI RIPETIZIONE 1
@when("click", "#carne")
def carne(e):
    global risultatoControlla
    for index, el in enumerate(elementi_panino2[::-1]):
        if el['filename']=='carne':
            el['valore']= not (el['valore'])
            if el['valore']==1:
                risultatoControlla+=1
                js.foodSound()
            else:
                risultatoControlla-=1
                js.removeSound()
    bild_panino("carne")
    js.errore(risultatoControlla)

#PUNTO DI RIPETIZIONE 1
@when("click", "#pollo")
def pl(e):
    global risultatoControlla
    for index, el in enumerate(elementi_panino2[::-1]):
        if el['filename']=='polloP':
            el['valore']= not (el['valore'])
            if el['valore']==1:
                risultatoControlla+=1
                js.foodSound()
            else:
                risultatoControlla-=1
                js.removeSound()
    bild_panino("polloP")
    js.errore(risultatoControlla)

#PUNTO DI RIPETIZIONE 1
@when("click", "#bacon")
def bc(e):
    global risultatoControlla
    for index, el in enumerate(elementi_panino2[::-1]):
        if el['filename']=='baconP':
            el['valore']= not (el['valore'])
            if el['valore']==1:
                risultatoControlla+=1
                js.foodSound()
            else:
                risultatoControlla-=1
                js.removeSound()
    bild_panino("baconP")
    js.errore(risultatoControlla)

#questo viene avviato quando si cliccano tre bottoni che però appaiono in momenti differenti del gioco
#essenzialmente elimina gli elementi del vassoio
@when("click","#prosegui")
@when("click","#riprova")
@when("click","#elimina")
def elPrecario(e):
    global risultatoControlla#variabile globale usata
    js.removeSound()#suono per eliminare
    js.elimina(e)#ho usato una funzione javascript non presente su python che crea un vettore con le immagini presenti in un div e poi le ho eliminate una ad una
    for index, i in enumerate(elementi_panino2):#ho ovviamente azzerato i valori nel dizionario del panino utente così da poi poter riusare i condimenti in modo corretto
        i['valore']=0
    risultatoControlla=0#azzero anche il numero del controllo panino utente
    document.getElementById("frase").style.display='block'#per sicurezza levo e metto alcuni elementi che potrebbero essere stato modificati
    document.getElementById("elimina").style.display="block"
    document.getElementById("consegna").style.display="block"
    document.getElementById("problemi").style.display="none"
    document.getElementById("riprova").style.display='none'
    js.errore(risultatoControlla)#sempre la funzione di controllo variabile

#questa funzione serve quando il pulsante di consegna è cliccato
#presenta due casi quasi identici, uno è per l'ultimo cliente e l'altro è per gli altri 4
@when("click", "#consegna")
def controllo():
    global punteggio, risultatoControlla, risultatoGiusto#variabili usate
    test=True#test per il controllo validità panino
    document.getElementById("problemi").style.display="block"#metto a schermo alcuni elementi che servono
    document.getElementById("elimina").style.display="block"
    document.getElementById("consegna").style.display="block"
    document.getElementById("frase").style.display="none"
    if punteggio!=4:#if per il controllo cliente 
        #RIPETIZIONE 2 PER TUTTI GLI ELEMENTI DI QUESTI IF
        #altro if per il controllo validità panino con controllo del numero di elementi, controllo presenza del pane(sia sopra che sotto) e verifica tramite una funzione js che controlla(tramite la stessa funzione di prima in js) se si trovano nei punti esatti
        if risultatoControlla == risultatoGiusto and elementi_panino2[0]['valore']==1 and elementi_panino2[1]['valore']==1 and (js.mangiabilita(0))==True :
            document.getElementById("problemi").innerHTML="adesso controllo.."
            #frase di verifica cliente
            for el1, el2 in zip(elementi_panino, elementi_panino2[2:]):#if di controllo di tutti gli elementi 
                if el1['valore']!=el2['valore'] :#controllo se sono presenti elementi che sono diversi
                    test=False#in caso il test è falso ed è sbagliato
                    break
            if(test):#se è giusto
                document.getElementById("frase").style.display='block'
                document.getElementById("problemi").style.display='none'#si rimettono le giuste frasi
                punteggio+=1#si aumenta il punteggio e aggiorna
                aggiornaPunteggio()
                threading.Event().wait(1)#si aspetta un attimo
                js.lvl_superato('')#sweetalert
                document.getElementById("frase").innerHTML=f"MHM buonissimo!\nDai, solo {5-punteggio} da servire ancora e avrai finito!"
                document.getElementById("prosegui").style.display='block'
                document.getElementById("elimina").style.display='none'
                document.getElementById("consegna").style.display='none'#prossimo cliente
            #gli altri else specificano il panino sbagliato, con gradi di errore più o meno grave
            else:#meno grave
                document.getElementById("problemi").style.display="block"
                document.getElementById("problemi").innerHTML="non è quello che ho ordinato. Riprova"
                document.getElementById("riprova").style.display='block'
                document.getElementById("elimina").style.display='none'
                document.getElementById("consegna").style.display='none'
                js.attenzione()
        else:#più grave
            document.getElementById("problemi").innerHTML="qualcosa è sbagliato..riprova, questa cosa non è mangiabile"
            document.getElementById("riprova").style.display='block'
            document.getElementById("elimina").style.display='none'
            document.getElementById("consegna").style.display='none'
            js.attenzione()
    else:#ultimo cliente
        #RIPETIZIONE 2
        if risultatoControlla == risultatoGiusto and elementi_panino2[0]['valore']==1 and elementi_panino2[1]['valore']==1 and (js.mangiabilita(0))==True :
            document.getElementById("problemi").innerHTML="Sembra quasi giusto..adesso controllo."
            document.getElementById("frase").style.display="none"
            for el1, el2 in zip(elementi_panino, elementi_panino2[2:]):
                if el1['valore']!=el2['valore'] :
                    test=False
                    break
            if(test):
                document.getElementById("frase").style.display='block'
                document.getElementById("problemi").style.display='none'
                punteggio+=1
                aggiornaPunteggio()
                threading.Event().wait(1)
                document.getElementById("frase").innerHTML=f"HAI FATTO ALLA PERFEZIONE IL MIO PANINO ALLA SCIBETTA, 10!"
                js.vinto('')#se tutto è giusto si ha vinto(sweetalert)
                document.getElementById("prosegui").style.display='block'#da qui poi si tornerà all'inizio
                document.getElementById("elimina").style.display='none'
                document.getElementById("consegna").style.display='none'#obbligo di schiacciare il pulsante prosegui
            else:
                #l'ultimo cliente si arrabierà molto se il numero degli elementi è lo stesso ma sono sbagliati quelli inseriti
                document.getElementById("problemi").style.display="block"
                document.getElementById("problemi").innerHTML="Volevi fregarmi eh? questo non è il mio fantastico panino, 1!"
                punteggio=1#ti farà tornare al 2 cliente
                aggiornaPunteggio()
                js.declassato('')#sweetalert
                document.getElementById("prosegui").style.display='block'
                document.getElementById("elimina").style.display='none'
                document.getElementById("consegna").style.display='none'
        else:
            #in questo caso di errore si arrabierà di meno
            document.getElementById("problemi").innerHTML="Cos'è questo?? non è il mio panino, 2!"
            punteggio=2#ti farà iniziare dal 3 cliente
            aggiornaPunteggio()
            js.declassato('')#sweetalert
            document.getElementById("prosegui").style.display='block'
            document.getElementById("elimina").style.display='none'
            document.getElementById("consegna").style.display='none'
            
#da qui l'algoritmo è autono e ricomincerà fino al 5 cliente che sarà con un panino personalizzato
#abbiamo anche gli altri 3 clienti(ovviamente il primo è fatto all'inizio), potevano essere di più ma sarebbe durato troppo
@when("click", "#prosegui")
def continua():
    global punteggio, panino, risultatoGiusto#variabili globali usate
    document.getElementById("elimina").style.display='block'
    document.getElementById("consegna").style.display='block'#rimettiamo i bottoni normali
    risultatoGiusto=2#rifacciamo iniziare il conto del panino oridnato da 2
    frase=document.getElementById("frase")#reimpostiamo la frase
    frase.innerHTML=" "
    js.eliminaDiv("panino")#eliminiamo l'intero div ordinato così da poi poterlo ricreare
    document.getElementById("prosegui").style.display='none'#così non lo si può cliccare
    if punteggio==4 :#se è l'ultimo cliente
            for i in elementi_panino:
                i['valore'] = 0#si azzerano i valori panino
            document.getElementById("scibetta").style.display='block'#arrivo dell'ultimo cliente
            document.getElementById(f"cliente{punteggio}").style.display='none'#si leva il cliente precedente
            elementi_panino[1]["valore"]=1#aggiunta valori del panino personalizzato
            elementi_panino[3]["valore"]=1
            elementi_panino[4]["valore"]=1
            elementi_panino[8]["valore"]=1
    elif punteggio==5:
        js.riavvia('')#se si ha vinto la pagina si riavvia
    else:
        #se è un normale cliente
        for i in elementi_panino:
            i['valore'] = rand.randrange(2)#si randomizzano tutti gli elementi
        document.getElementById(f"cliente{punteggio}").style.display='none'#si fa sparire il cliente precedente
        document.getElementById(f"cliente{punteggio+1}").style.display='block'#si fa apparire il cliente successivo
    panino.append(buildPreset())#si manda il tutto dinuovo in construzione dalla funzione precedente


@when("click", "#home")#funzione per tornare alla home durante il gioco
def riavvia():
    js.riavvia('')#viente richiamata la funzione js per farlo
