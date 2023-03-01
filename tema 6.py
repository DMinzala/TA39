'''Tema 6 - OOP _ Clase & Obiecte
Exerciții Recomandate - grad de dificultate: Ușor
1. Revizualizează întâlnirea 6 și ia notițe în caz că ți-a scăpat ceva.
Pentru toate clasele, creați cel puțin 2 obiecte cu valori diferite și apelați toate
metodele clasei.
'''
from datetime import date

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


'''6. Clasa Masina
 
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

'''
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
