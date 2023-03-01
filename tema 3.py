'''Tema 3 _ Structuri de date
I.
Exerciții Recomandate - grad de dificultate: Ușor
1. Revizualizeaza intalnirea 3 si ia notite in caz ca ti-a scapat ceva
2. Vizualizeaza video despre Structuri de date din 'Primii pasi in Programare' (Daca nu ai
facut-o deja)
3. Vizualizeaza video 4 despre Flow Control din 'Primii pasi in Programare'. Astfel, la
intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele si sigur ti se vor intipari in
minte mai bine. Link video: https://www.itfactory.ro/8174437-intro-in-programare/
'''
'''
II.
Exerciții obligatorii - grad de dificultate: Ușor spre
Mediu:

1. Declara o lista note_muzicale in care sa pui do re mi etc pana la do
a. Afiseaz-o
b. Inversează ordinea folosind slicing si suprascrie aceasta lista, apoi printeaza
varianta actuala (inversata)
c. Pe aceasta lista, aplica o metoda care banuiesti ca face același lucru, adica sa ii
inverseze ordinea (Nu trebuie sa o suprascrii în acest caz, deoarece metoda face
asta automat) si apoi printeaza varianta actuala a listei. Practic ai ajuns înapoi la
varianta inițială
Concluzii: slicing e temporar, dacă vrei sa pastrezi noua varianta va trebuie sa
suprascrii lista sau sa o salvezi intr-o listă nouă. Metoda gasita de tine face
suprascrierea automat și permanentizeaza aceste modificări. Ambele variante își
găsesc utilitatea în funcție de ce ne dorim in acel moment.
'''
# # 1a
# note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si']
# print(note_muzicale)
# # 1b
# note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si']
# print(note_muzicale[::-1])
# note_muzicale.reverse()
# print(note_muzicale)

# # 2. De cate ori apare do?
# note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# # note_muzicale.count('do')  # sintaxa de numarare element
# print(note_muzicale.count('do'))
#
# # 3. Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]
# # Gasiti 2 variante sa le uniti intr-o singura lista.
# list1 = [3, 1, 0, 2]
# list2 = [6, 5, 4]
# list3 = list1 + list2
# print(list3)
# for x in list2:
#     list1.append(x)
# print(list1)
#
# # 4. Sortati si afisati lista generata la ex anterior
# # Stergeti numarul 0 folosind o functie
# # Afisati iar lista
# lista3 = [3, 1, 0, 2, 6, 5, 4]
# lista3.sort()
# print(lista3)
# lista3.remove(0)
# print(lista3)

# 5. Folosind un if verificati lista generata la ex3 si afisati
# Lista este goala (IF)
# Lista nu este goala (ELSE)
# lista3 = [3, 1, 0, 2, 6, 5, 4]
'''if lista3 == [3, 1, 0, 2, 6, 5, 4]:
    print('Lista nu este goala')
else:
    print('Lista este goala')
lista3.clear()
print('Lista este goala')
'''
# # Rezolvare trainer
# lista3 = [3, 1, 0, 2, 6, 5, 4]
# if len(lista3) > 0:
#     print('lista3 nu este goala')
# else:
#     print('Lista3 este goala')

#
# # 6. Foloseste o functie care sa goleasca lista de la exercitiul 3
# lista3 = [3, 1, 0, 2, 6, 5, 4]
# lista3.clear()
# print(lista3)

# # 7. Rescrie if-ul de la exercitiul 5 si verifica inca o data rezultatul.
# Acum ar trebui sa se afiseze ca lista e goala
# lista3 = [3, 1, 0, 2, 6, 5, 4]
'''# if lista3 == [3, 1, 0, 2, 6, 5, 4]:
#     print('Lista nu este goala')
# lista3.clear()
# print('lista este goala')
'''
# Rezolvare corectata
# if len(lista3) > 0:
#     print('Lista3 nu este goala')
# lista3.clear()
# print('lista3 este goala')

# # 8. Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5},
# # foloseste o functie ca sa afisezi Elevii (cheile)
# dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
# x = dict1.keys()
# print(x)
#
# # 9. Printeaza cei 3 elevi din dictionarul de mai sus si respectiv notele lor
# # Ex: ‘Ana a luat nota {x}’.
# # Doar nota o vei lua folosindu-te de cheie
# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# print('Ana a luat nota:', dict1['Ana'])
# print('Gigel a luat nota:', dict1['Gigel'])
# print('Dorel a luat nota:', dict1['Dorel'])

# rezolvare trainer cu get
# x = dict1.get('Ana')
# y = dict1.get('Gigel')
# z = dict1.get('Dorel')
# print(f'Ana a luat nota {x}')
# print(f'Gigel a luat nota {y}')
# print(f'Dorel a luat nota {z}')

# varianta Lidia + Petre
# dict1 = {
#     'Ana': 8,
#     'Gigel': 10,
#     'Dorel': 5# }
# x = dict1.get('Ana')
# y = dict1.get('Gigel')
# z = dict1.get('Dorel')
# # x = dict1['Ana']
# # y = dict1['Gigel']
# # z = dict1['Dorel']
# print(f'Ana a luat nota {x}.')
# print(f'Gigel a luat nota {y}.')
# print(f'Dorel a luat nota {z}.')

# # 10. Imagineaza-ti ca Dorel a facut contestatie si a primit nota 6.
# # - Modifica nota lui Dorel in 6
# # - Printeaza nota lui dupa modificare
# dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
# dict1['Dorel'] = 6
# print('Dorel a luat nota:', dict1['Dorel'])

# sau rezolvare trainer cu get
# dict1.update({"Dorel": 8})
# z = dict1.get('Dorel')
# print(f'Dorel a luat nota {z}')
#
# # 11. Imagineaza-ti ca Gigel se transfera din clasa.
# # - Cauta o functie care sa il stearga
# # Vine un coleg nou.
# # - Adaugati-l in lista pe Ionica, cu nota 9
# # - Printati dictionarul cu noii elevi
# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# dict1.pop('Gigel')
# print(dict1)
# dict1['Ionica'] = 9
# print(dict1)

# sau varianta trainer cu get:
# dict1.pop('Gigel')
# dict1.update({'Ionica':8})
# print(dict1)

# 12. Ai urmatoarele seturi:
# zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend = {'sambata', 'duminica'}
# - Incearca sa adaugi in setul zilele_sapt ziua de ‘luni’ si observa ce se intampla.
# - Afiseaza setul zile_sapt si constata rezultatul adaugarii anterioare.
# zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend = {'sambata', 'duminica'}
# zile_sapt.add('luni')
# print(zile_sapt)  # returneaza 'luni' o singura data

# 13. Foloseste un if si verifica daca:
# - Weekend este un subset al zilelor din sapt (adica daca elementele din
# setul weekend se regasesc intre elementele din setul zile_sapt)
# -Else Weekend nu este un subset al zilelor din sapt
# Hint: Va puteti folosi fie de operatorul de comparatie fie de o functie.
# Rezultatul fiecarui punct de mai sus va fi un boolean
# zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend = {'sambata', 'duminica'}
# !!!!!!
# if weekend < zile_sapt:
#     print(weekend in zile_sapt)  # returneaza False
# if weekend > zile_sapt:
#     print('Weekend este un subset al zile_sapt')

# Rezolvare trainer cu subset si superset corectat
# if weekend.issubset(zile_sapt):
#     print('True')
# else:
#     print('False')
# # versus:
# if weekend.issuperset(zile_sapt):
#     print('True')
# else:
#     print('False')

# Varianta Lidia + Petre
# 13
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
# if weekend < zile_sapt:
# __________<<< de ce operatorul asta?
#     print(True)
# else:
#     print(False)
# if weekend.issubset(zile_sapt):
#     print(True)
# else:
#     print(False)


# # 14. Afiseaza diferentele dintre aceste 2 seturi (adica elementele care
# sunt in zile_sapt si nu sunt in weekend si invers)
# print(zile_sapt - weekend)
# print(weekend - zile_sapt)
#
# 15. Afiseaza intersectia elementelor din aceste 2 seturi (adica elementele
# care exista in ambele seturi). Hint:Va puteti folosi de o functie
#
# y = zile_sapt - weekend
# print(weekend - y)

'''
Exerciții Opționale - grad de dificultate: Mediu spre
greu (s-ar putea să ai nevoie de Google).

1. Ne imaginam o echipa de fotbal in timpul meciului. Sunt permise maxim 3 schimbari.
- Declara o lista cu 5 jucatori: lista_jucatori_teren
- Declara o lista cu 5 jucatori de rezerva: lista_jucatori_rezerva
- Declara o lista goala cu jucatori scosi din teren: lista_jucatori_scosi
- Schimbari_efectuate = joaca-te cu valori diferite ca sa vezi cum trec datele prin cod
- SCHIMBARI_MAX va fi o constanta cu valoarea 3
Daca Jucatorul x e in teren si mai avem schimbari la dispozitie atunci:
- Efectuam schimbarea daca jucatorul e in lista de rezerve si nu exista in jucatorii de pe
teren
- Stergem jucatorul scos din lista de teren si il adaugam in lista de jucatori scosi
- Adaugam jucatorul intrat in lista de jucatori de pe teren si il scoatem din lista de jucatori
de rezerva
- Afisam pe ecran: a intrat x, a iesit y. Mai aveti z schimbari (inlocuiti x, y si z cu numele
variabilelor voastre)
Daca jucatorul pe care vrem sa il schimbam nu e in teren:
- Afisati ‘nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
Altfel, afisati ecran: ‘mai aveti z schimbari’
Google search hint: “how to check if item is in list python”
'''
#
# lista_jucatori_teren = ['portar', 'fundas', 'libero', 'atacant', 'varf']
# lista_jucatori_rezerva = ['r_portar', 'r_fundas', 'r_libero', 'r_atacant', 'r_varf']
# lista_jucatori_scosi = []
# schimbari_max = 3
#
# x = 'fundas'
# if x in lista_jucatori_teren:
#     print('fundas este in teren')
# lista_jucatori_teren[1] = 'r_fundas'
# lista_jucatori_scosi.append('fundas')
# print(lista_jucatori_teren)
# print(lista_jucatori_scosi)
# if x not in lista_jucatori_teren:
#     print('Nu se poate efectua schimbarea, fundas nu este in teren')
# schimbari_max = int(schimbari_max -1)
# print('A intrat', lista_jucatori_teren[1], ',' 'a iesit:', lista_jucatori_scosi[0], 'si mai aveti:', int(schimbari_max), 'schimbari')

# rezolvare trainer + Petre

# lista_jucatori_teren = ['Marius', 'Adi', 'Dan', 'Alex', 'Bubu']
# lista_jucatori_rezerva = ['Vlad', 'Gigi', 'Mihai', 'Dorin', 'Alin']
# lista_jucatori_scosi = []
# schimbari_efectuate = 0
# schimbari_efectuate_cu_succes = 0
# SCHIMBARI_MAX = 3
# while SCHIMBARI_MAX > 0:
#     x = str(input('Iese de pe teren: \n'))
#     y = str(input('Intra pe teren: \n'))
#     if x in lista_jucatori_teren and y in lista_jucatori_rezerva and schimbari_efectuate <= SCHIMBARI_MAX:
#         lista_jucatori_teren.remove(x)
#         lista_jucatori_rezerva.remove(y)
#         lista_jucatori_scosi.append(x)
#         lista_jucatori_teren.append(y)
#         schimbari_efectuate_cu_succes += 1
#         SCHIMBARI_MAX -= 1
#         z = SCHIMBARI_MAX
#         print(f'A intrat {y}, a iesit {x}, mai aveti {z} schimari.')
#         print(f'Jucatori pe teren: {lista_jucatori_teren}')
#         print(f'Jucatori in rezerva: {lista_jucatori_rezerva}')
#         print(f'Jucatori scosi: {lista_jucatori_scosi}')
#     elif x not in lista_jucatori_teren:
#         print(f'Nu se poate efectua schimbarea deoarece jucatorul {x} nu este pe teren.')
#         schimbari_efectuate = schimbari_efectuate_cu_succes
#     elif y not in lista_jucatori_rezerva:
#         print(f'Nu se poate efectua schimbarea deoarece jucatorul {y} nu este rezerva.')
# else:
#     print(f'Limita de schimbari a fost atinsa')
