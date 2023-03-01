from datetime import date

from helper import Scoala, TableIt
from helper import Cerc
from helper import Dreptunghi
from helper import Angajat
from helper import ContBancar

# Functie care sa returneze daca un nume este nume de fata sau de baiat
# def gen_nume():
#     nume = input('Scrie numele:\n')
#     if nume[-1] == 'a' and nume != 'Mircea' and nume != 'Luca':
#         print('Acesta este un nume de fata')
#     elif nume == 'Mircea' or nume == 'Luca':
#         print('Acesta este un nume de baiat')
#     elif nume == 'Carmen' or nume == 'Beatrice':
#         print('Acesta este un nume de fata')
#     else:
#         print('Acesta este un nume de baiat')
#
#
# gen_nume()

# Sau dupa Matei
# def gen_nume():
#     lista_exceptii_fete = ['Carmen', 'Beatrice']
#     lista_exceptii_baieti = ['Mircea', 'Luca']
#     nume = input('Scrie numele:\n')
#     if nume in lista_exceptii_fete:
#         print("Nume de fata")
#     elif nume in lista_exceptii_baieti:
#         print("Nume de baiat")
#     elif nume[-1] == 'a' and nume not in lista_exceptii_fete:
#         print("Nume de fata")
#     else:
#         print("Nume de baiat")
#
#
# gen_nume()


''' CLASA, OBIECT, CONSTRUCTOR, CLASA IMPORTATA DIN ALT FISIER
Intalnirea 6 -Ce este o CLASA?
● O clasă este o rețetă (blueprint) pentru crearea obiectelor
● Ea conține elemente descriptive: atribute/fields
(practic niste variabile)
● Conține acțiuni posibile: metode (practic niște funcții)
● Self - este instanță clasei, ajută funcția să aibă acces
la atributele clasei
● Deci o clasă este doar un concept, cum ar fi o rețetă pentru
paste carbonara. Faptul că există rețetă nu înseamnă că
există și pastele.
● Dar aceeași rețetă o putem folosi ca să facem 1, 2, 100
de porții carbonara.
'''

# class Car:
#     # fields / attributes ( caracteristicile pe care poate sa le aiba clasa Car)
#     make = 'Dacia'
#     model = None
#     year = 2023
#     color = 'alb'

# contructorul se defineste dupa atribute si inainte de metode
# def __init__(self, model, color):
#     self.model = model
#     self.color = color

# METODE (methods) - actiunile pe care poate sa le faca sau sa le suporte clasa noastra
# def accelerate(self):  # def startup(self): functia de deschidere
#     print('Masina accelereaza: Vrrrum, vrum')
'''  Pe scurt un test case apare asa:
#   def startup(self): functia de deschidere
#      se executa pasii test case-urile
#      pas 1
#      pas 2
#      pas 3
#    def teardown(self): functia de inchidere care sterge tot
'''
#      def rezervor(self):
#        print(f'Rezervorul are capacitatea de {}, litri')
#
#
# def change_color(self, color):  # color este unparametru care devine argument
#     self.color = color
# exemplu pt change color:
# car1 = Car()
# car1.color = 'red'
# print(car1.color)

#
# def model_masina(self, model):
#     self.model = model
#
#
# def stop(self):  # teardown(self): functia de inchidere care sterge tot
#      print('Masina s-a oprit')

'''  Ce este un OBIECT?
● Obiect = instanță a clasei
● Toate obiectele de tip Car vor avea același comportament

○ Aceleași atribute
○ Aceleași metode
○ Atributele pot suferi modificări după inițializarea obiectului
○ Ex: o mașină se poate vopsi într-o culoare nouă

● Putem crea oricâte obiecte de tip Car dorim
● Acesta e și avantajul OOP: write once, use n times
'''
# obiecte de tipul Car() -ne creem masinile pe care vrem sa le vedem /folosim/testam
# fiecare dintre obiecte are acces la toate atributele si metodele clasei

# car1 = Car()  # car1 = obiect de tip Car()
# car2 = Car()
# print(car1.make)
# print(car2.make)
# car1.color = 'albastru'
# car1.model = 'Duster'
# car2.color = 'galben'
# car2.model = 'Logan'
# print(car1.color)
# print(car1.model)
# print(car1.accelerate())
# print(car1.stop())
# print(car2.color)
# print(car2.model)
# print(car2.accelerate())
# print(car2.stop())


'''Ce este un constructor?
● Constructor se asigură că la crearea obiectelor setăm
niște date fără de care obiectul nu are sens să existe

● Practic atribuie valori atributelor
● Dacă ne gândim la un formular, ar fi acele field-uri cu *

care sunt OBLIGATORII / sau permanetizam

● Dacă prin constructor suntem obligați să dăm model și
color, nu am putea să instanțiem obiecte de tip
Car fără să dăm aceste valori obligatorii
'''

# vezi contructorul care se defineste dupa atribute si inainte de metode

# class Car:
#     make = 'Dacia'
#     model = None
#     year = 2023
#     color = 'alb'
#
# # contructorul se defineste dupa atribute si inainte de metode
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color
#
#     def accelerate(self):  # def startup(self): functia de deschidere
#         print('Masina accelerate: Vrrrum, vrum')
#
#     def change_color(self, color):  # color este unparametru care devine argument
#         self.color = color
#
#     def model_masina(self, model):
#         self.model = model
#
#     def stop(self):  # teardown(self): functia de inchidere care sterge tot
#         print('Masina s-a oprit')
#
#
# car1 = Car('Duster', 'albastru')  # car1 va trebui sa aiba argumentele'model' si 'culoare' din cauza constructorului
# car2 = Car('Logan', 'galben')  # similar car1 va avea acceasi obligativitate de argumente: 'model' si 'culoare'
# print(car1.make)
# print(car2.make)
# car1.color = 'albastru'
# car1.model = 'Duster'
# car2.color = 'galben'
# car2.model = 'Logan'
# print(car1.color)
# print(car1.model)
# print(car1.accelerate())
# print(car1.stop())
# print(car2.color)
# print(car2.model)
# print(car2.accelerate())
# print(car2.stop())

'''
Cum importăm clase din alte fișiere?
● from folder.folder.fișier import nume_clasă
'''
# Am definit in helper -> class Scoala:
# scoala1 = Scoala('tip_seral', 'profil_mate-info')
# print(scoala1.profil_real)
# print(scoala1.tip)
# print(scoala1.nr_elevi)
#
# scoala2 = Scoala('tip_liceu_teoretic', 'profil_uman')
# print(scoala2.profil_real)
# print(scoala2.tip)
# print(scoala2.nr_elevi)

'''Tema 6 - OOP _ Clase & Obiecte
Exerciții Recomandate - grad de dificultate: Ușor
1. Revizualizează întâlnirea 6 și ia notițe în caz că ți-a scăpat ceva.
Pentru toate clasele, creați cel puțin 2 obiecte cu valori diferite și apelați toate
metodele clasei.
'''
# Exercitii obligatorii - grad de dificultate: Usor spre Mediu

''' 1.Clasa Cerc
    
    Atribute: raza, culoare
    Constructor pentru ambele atribute
    Metode:
    ● descrie_cerc() - va PRINTA culoarea și raza
    ● aria() - va RETURNA aria
    ● diametru()
    ● circumferinta()
'''

#
# class Cerc:
#     raza = 5
#     culoare = 'rosu'
#
#     # aria = 3.14 * raza ** 2
#     # diametru = 2 * raza
#     # lungime = 2 * 3.14 * raza
#
#     def __init__(self, culoare, raza):
#         self.raza = raza
#         self.culoare = culoare
#
#     def descriere_cerc(self):
#         print(f'Cercul are culoarea {self.culoare} si raza {self.raza}')
#
#     def aria_cerc(self):
#         return 3.14 * (self.raza ** 2)
#
#     def diametru_cerc(self):
#         return self.raza * 2
#
#     def lungime_cerc(self):
#         return 2 * 3.14 * self.raza
#
#     def cerc_definit(self):
#         print('Acesta este cercul definit')
#
# cerc1 = Cerc('albastru', 5)
# print(cerc1.descriere_cerc())
# print('Aria cercului este', cerc1.aria_cerc())
# print('Diametrul cercului este', cerc1.diametru_cerc())
# print('Circumferinta cercului este', cerc1.lungime_cerc())

''' 2. Clasa Dreptunghi

Atribute: lungime, latime, culoare
Constructor pentru toate atributele
Metode:
● descrie()
● aria()
● perimetrul()
● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
'''

# class Dreptunghi:
#     lungime = 5
#     latime = 3
#     culoare = 'orange'
#
#     def __init__(self, lungime, latime, culoare):
#         self.lungime = lungime
#         self.latime = latime
#         self.culoare = culoare
#
#     def descriere_dreptunghi(self):
#         print(f'Dreptunghiul are lungimea de: ', 5, 'latime de:', 3, 'si culoarea: ', self.culoare)
#
#     def aria_dreptunghi(self):
#         return self.lungime * self.latime
#
#     def perimetrul_dreptunghi(self):
#         return 2 * self.lungime + 2 * self.latime
#
#     def schimba_culoarea(self, alta_culoare):
#         self.culoare = alta_culoare
#
#
# dreptunghi1 = Dreptunghi(5, 3, 'orange')
# print(dreptunghi1.descriere_dreptunghi())
# print(f'Aria dreptunghiului este:', dreptunghi1.aria_dreptunghi())
# print(f'Perimetrul dreptunghiului este:', dreptunghi1.perimetrul_dreptunghi())
# dreptunghi1.schimba_culoarea('rosu')
# print(dreptunghi1.descriere_dreptunghi())

''' 3.Clasa Angajat

Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
descrie()
nume_complet()
salariu_lunar()
salariu_anual()
marire_salariu(procent)
'''

# class Angajat:
#     nume = 'nume'
#     prenume = 'prenume'
#     salariu = 5000
#
#     def __init__(self, nume, prenume, salariu):
#         self.nume = nume
#         self.prenume = prenume
#         self.salariu = salariu
#
#     def descriere_Angajat(self):
#         print(f'Angajatul:', self.nume, self.prenume, 'are salariul de:', 5000)
#
#     def nume_complet(self):
#         return self.nume + self.prenume
#
#     def salariu_lunar(self):
#         return self.salariu
#
#     def salariu_anual(self):
#         return self.salariu * 12
#
#     def marire_salariu(self):
#         return self.salariu + self.salariu * 5 / 100
#
#
# angajat1 = Angajat('Ionescu', 'Marcel', 5000)
# print(angajat1.descriere_Angajat())
# print('Numele complet al angajatului1 este:', angajat1.nume_complet())
# print('Angajatul are salariul lunar de', angajat1.salariu_lunar())
# print('Angajatul are salariul anual de', angajat1.salariu_anual())
# print('Angajatul are o marire de salariul de', angajat1.marire_salariu())

'''4.Clasa Cont

Atribute: iban, titular_cont, sold
Constructor pentru toate
Metode:
afisare_sold() - Titularul x are in contul y suma de n lei
debitare_cont(suma)
creditare_cont(suma)
'''

# class ContBancar:
#     # iban = 'iban'
#     # titular_cont = 'titular_cont'
#     # sold = 1500
#     # suma = 500
#
#     def __init__(self, iban, titular_cont, sold):
#         self.iban = iban
#         self.titular_cont = titular_cont
#         self.sold = int(sold)
#
#     def afisare_sold(self):
#         print(f'Titularul: {self.titular_cont} are in contul {self.iban} suma de {self.sold}')
#
#     def debitare_cont(self, suma):
#         if int(suma) > self.sold:
#             print(f'Fonduri insuficiente in contul {self.iban}')
#         else:
#             self.sold -= int(suma)
#             print(f'S-a debitat suma de {int(suma)} lei din contul {self.iban} Soldul curent este {self.sold} lei.')
#             return self.sold
#
#     def creditare_cont(self, suma):
#         self.sold += int(suma)
#         print(f'S-a creditat suma de {int(suma)}lei in contul {self.iban} Soldul curent este {self.sold} lei.')
#
#
# cont = ContBancar('RO 72BREL', 'Popescu', '1500')
# cont.afisare_sold()
# cont.debitare_cont('200')
# cont.creditare_cont('500')

'''BONUS: (daca aveti timp si doriti sa lucrati suplimentar)

   5.Clasa Factura

Atribute: seria (va fi constanta, nu trebuie constructor, toate facturile vor avea aceeasi serie), numar, nume_produs, cantitate, pret_buc

Constructor: toate atributele, fara serie

Metode:
schimba_cantitatea(cantitate)
schimba_pretul(pret)
schimba_nume_produs(nume)
genereaza_factura() - va printa tabelar daca reusiti

Factura seria x numar y
Data: generati automat data de azi
Produs | cantitate | pret bucata | Total 
Telefon |      7       |       700       | 49000     

Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/
'''

# class Factura:
#     today = date.today().strftime('%d/%m/%Y')
#     serie = 'ITF 2023'
#
#     def __init__(self, numar, nume_produs, cantitate, pret_buc):
#         self.numar = numar
#         self.nume_produs = nume_produs
#         self.cantitate = cantitate
#         self.pret_buc = pret_buc
#
#     def schimba_cantitatea(self, cantitate):
#         self.cantitate = cantitate
#         print(f'Cantitatea s-a schimbat in {cantitate}')
#
#     def schimba_pretul(self, pret):
#         self.pret_buc = pret
#         print(f'Pretul este acum de {pret} RON')
#
#     def schimba_nume_prodsului(self, nume):
#         self.nume_produs = nume
#         print(f'Noul nume al produsului este {nume}')
#
#     def genereaza_factura(self):
#         factura = Factura
#         total = self.cantitate * self.pret_buc
#         print(f'Factura seria: {factura.serie} \nNumar: {self.numar}')
#         print(f'Data: {factura.today}')
#         print(f'Produs |  cantitate | pret bucata | TOTAL ')
#         print(f'{self.nume_produs} | {self.cantitate} | {self.pret_buc} | {total}')
#         # factura_mea = [
#         #     ['Produs', 'Cantitate', 'Pret Bucata', 'Total'],
#         #     [self.nume_produs, self.cantitate, self.pret_buc, self.cantitate * self.pret_buc],
#         # ]
#         # TableIt.printTable(factura_mea, useFieldNames=True)
#
#
# factura1 = Factura(1, 'Telefon', 8, 800)
# factura1.schimba_cantitatea(9)
# factura1.schimba_pretul(900)
# factura1.schimba_nume_prodsului('Smartphone')
# factura1.genereaza_factura()
# print('________________________________________________________________________________')
# factura2 = Factura(2, 'Laptop', 10, 2500)
# factura2.schimba_cantitatea(15)
# factura2.schimba_pretul(2000)
# factura2.schimba_nume_prodsului('Laptop Gaming')
# factura2.genereaza_factura()
'''
6.
Clasa Masina

Atribute: marca, model, viteza maxima, viteza_actuala, culoare, culori_disponibile (set), inmatriculata (bool)
Culoare = gri - toate masinile cand ies din fabrica sunt gri
Viteza_actuala = 0 - toate masinile stau pe loc cand ies din fabrica
Culori disponibile = alegeti voi 5-7 culori
Marca = alegeti voi - fabrica produce o singura marca dar mai multe modele
Inmatriculata = False

Constructor: model, viteza_maxima

Metode:
descrie() (se vor printa toate atributele, inafara de culori_disponibile)
inmatriculare() - va schimba atributul inmatriculata in True
vopseste(culoare) - se va vopsi masina in noua culoare DOAR daca noua culoare e in optiunea de culori displonibile, altfel afisati o eroare
accelereaza(viteza) - se va accelera la o anumiota viteza, daca viteza e negativa-eroare, daca viteza e mai mare decat viteza_max - masina va accelera pana la viteza maxima
franeaza() - masina se va opri si va avea viteza 0

'''

# class Masina:
#     marca = 'Dacia'
#     viteza_actuala = 0
#     culoare = 'gri'
#     culori_disponibile = {'rosu', 'verde', 'galben', 'albastru', 'mov'}
#     inmatriculare = False
#
#     def __init__(self, model, viteza_maxima):
#         self.model = model
#         self.viteza_maxima = viteza_maxima
#
#     def descrie(self):
#         print(f'Marca masinii este {self.marca}')
#         print(f'Viteza actuala este {self.viteza_actuala}')
#         print(f'Culoarea standard este {self.culoare}')
#         print(f'Este inmatriculata? {self.inmatriculare}')
#
#     def inmatriculare_masina(self):
#         self.inmatriculare = True
#         print(f'Am inmatriculat masina {self.model} {self.inmatriculare}')
#
#     def vopeste_masina(self, culoare):
#         self.culoare = culoare
#         if culoare in self.culori_disponibile:
#             self.culoare = culoare
#             print(f'Culoarea a fost inlocuita cu {culoare}')
#         else:
#             print('Culoarea aleasa nu este disponibila')
#
#     def accelereaza(self, viteza):
#         self.viteza = viteza
#         if self.viteza < 0:
#             print('Masina nu poate accelera!')
#         elif self.viteza > self.viteza_maxima:
#             print(f'Masina poate acelera doar pana la {self.viteza_maxima}')
#         else:
#             print(f'Masina accelereaza la {self.viteza} km/h')
#
#     def franeaza(self):
#         self.viteza = 0
#         print(f'Masina s-a oprit iar viteza este acum {self.viteza} km/h')
#
#
# masina1 = Masina('Logan', 200)
# masina1.descrie()
# masina1.inmatriculare_masina()
# masina1.vopeste_masina('rosu')
# masina1.accelereaza(150)
# masina1.franeaza()
# print('_________________')
# masina2 = Masina('Sandero', 180)
# masina2.descrie()
# masina2.inmatriculare_masina()
# masina2.vopeste_masina('violet')
# masina2.accelereaza(200)
# masina2.franeaza()


'''
7. Clasa TodoList
 
Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La inceput nu avem taskuri, dict e gol si nu avem nevoie de constructor

Metode:
adauga_task(nume, descriere) - se va adauga in dict
finalizeaza_task(nume) - se va sterge din dict
afiseaza_todo_list() - doar cheile
afiseaza_detalii_suplimentare(nume_task) - in f de numele taskului, printam detalii suplimentare
daca taskul nu e in todo list, intrebam utilizatorul daca vrea sa il adauge.
Daca acesta raspunde nu - la revedere
daca raspunde da - il cerem detalii task si salvam nume+detalii in dict

# '''

# import json
#
#
# class ToDoList:
#     todo = {}
#
#     def adauga_task(self, nume, descriere):
#         self.nume = nume
#         self.descriere = descriere
#         self.todo[nume] = descriere
#
#     def afiseaza_todo_list_complet(self):
#         print(json.dumps(self.todo, indent=4))
#
#     def finalizeaza_task(self, nume):
#         self.nume = nume
#         self.todo.pop(nume)
#         print(json.dumps(self.todo, indent=4))
#
#     def afiseaza_todo_list_keys(self):
#         for keys, value in self.todo.items():
#             print(keys)
#
#     def afiseaza_detalii_suplimentare(self, nume_task):
#         self.nume_task = nume_task
#         if nume_task not in self.todo:
#             raspuns = input('Task-ul nu este in lista ToDo, vrei sa il adaugi? \n')
#             if raspuns == 'da':
#                 detalii_task = input('Va rugam alegeti o descriere: \n')
#                 self.todo[nume_task] = detalii_task
#                 print(json.dumps(self.todo, indent=4))
#             elif raspuns == 'nu':
#                 print('La revedere')
#         else:
#             print('Task-ul este deja in lista')
#
#
# lista1 = ToDoList()
# lista1.adauga_task('Sa spal vase', 'Cu mult detergent')
# lista1.adauga_task('Sa alerg', 'Repede')
# lista1.afiseaza_todo_list_complet()
# lista1.afiseaza_todo_list_keys()
# lista1.afiseaza_detalii_suplimentare('Trebuie')
# lista1.finalizeaza_task('Sa spal vase')
