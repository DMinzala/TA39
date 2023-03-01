'''
         TEMA 1  Exerciții obligatorii - grad de dificultate: Ușor spre Mediu:
'''

# 1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
# O variabila este un tip de date stocata in memoria unui computer,
# careia ii dam o valoare si o initializam

'''
2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de
variabilă :
- string
- int
- float
- bool
Observație: Valorile vor fi alese de tine după preferințe.
'''
# nume = 'Daniela'
# varsta = 53
# inaltime = 1.69
# satena = True
# print('Ma numesc ' + nume + ' am varsta de ' + str(varsta) + ' inaltimea de ' + str(inaltime) + ' si sunt ' + str(satena))
# print(f'{nume} \n{varsta} \n{inaltime} \n{satena}')

# sau rezolvare trainer:
# a = str(2)
# b = int(233)
# c = float(3.233)
# d = True

# 3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
# nume = str('Daniela')
# print(type(nume))
# varsta = int('53')
# print(type(varsta))
# inaltime = float(1.69)
# print(type(inaltime))
# satena = bool(True)
# print(type(satena))

# sau rezolvare trainer:
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))


'''
4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare
 în aceeași variabilă (suprascriere):
- Verifică tipul acesteia.
'''
# inaltime = float(1.69)
# print(round(inaltime, 1))
# inaltime = float(1.7)
# print(type(inaltime))
#
# # sau rezolvare trainer:
# c = float(3.233)
# c = round(c)
# print(type(c))

'''
5. Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.
Rezolvă nepotrivirile de tip prin ce modalitate dorești.
'''
# nume = 'Daniela'
# varsta = 53
# inaltime = 1.69
# satena = True
# print('Numele meu este ' + nume)
# print('Am varsta de ' + str(varsta) + ' de ani')
# print('Inaltimea mea este de ' + str(inaltime))
# print('Culoarea parului meu este satena = ' + str(satena))
#
# # sau rezolvare trainer:
# a = str(2)
# b = int(233)
# c = float(3.233)
# d = True
# print(f'Omul are {a} picioare')
# print(f'Am facut {b} de puncte la un joc')
# print(f'Afara sunt {c} grade')
# print(f'{d} tradus in romana este Adevarat')


# '''
# 6. Citește de la tastatură:
# - numele;
# - prenumele.
# Afișează: 'Numele complet are x caractere'.
# '''
# numele: input('Introdu numele: \n')
# prenumele: input('Introdu prenumele: \n')
# Numele_complet = str('nume' + 'prenume')
# print(f'Numele complet are', len('Numele_complet'))

# sau rezolvare trainer:
# nume = input('Introdu numele\n')
# prenume = input('Introdu prenumele\n')
# lung_nume= len(nume) + len(prenume)
# print(f'Numele complet are {len(nume) + len(prenume)} caractere')

'''
7. Citește de la tastatură:
- lungimea;
- lățimea.
Afișează: 'Aria dreptunghiului este x'.
'''
# lungimea = int(input('Introdu lungimea\n'))
# latimea = int(input('Introdu latimea\n'))
# aria = lungimea * latimea
# print('Aria dreptunghiului este', aria)

# sau rezolvare trainer:
# latime = input('Latimea este egala cu\n')
# lungime = input('Lungimea este egala cu\n')
# print(f'Aria dreptunghiului este egala cu {int(latime) * int(lungime)} cm2')

'''
8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
- afișează de câte ori apare cuvântul 'the';
'''
# narativ = 'Coral is either the stupidest animal or the smartest rock'
# print(narativ.count('the'))
'''
9. Același string.
● Inlocuieste cuvantul 'the' cu 'THE' in stringul dat;
● Printează rezultatul.
'''
# narativ = 'Coral is either the stupidest animal or the smartest rock'
# narativ.replace(' the', ' THE')
# print(narativ.replace(' the', ' THE'))
'''
# 10. Același string.
# ● Folosiți un assert ca să verificați dacă acest string conține doar numere.
# '''
# narativ = 'Coral is either the stupidest animal or the smartest rock'
# print(type(narativ))
# assert narativ == str('Coral is either the stupidest animal or the smartest rock')
# print('narativul este un string')
# assert narativ == int('Coral is either the stupidest animal or the smartest rock')
# print('narativul contine doar numere')

# sau rezolvare trainer - este despre altceva :(
# my_str = 12313231
# assert my_str < 12313232
# assert type(my_str) == int
# print('Assert passed')
# print("Avem eroare la assert-ul de comparare numere")
# # assert my_str.isdigit() is True, 'Propozitia nu contine doar cifre'


''''
       Exerciții Opționale - grad de dificultate: Mediu spre greu
         (s-ar putea să ai nevoie de Google).
'''
'''1. Exercițiu:
- citește de la tastatură un string de dimensiune impară;
- afișează caracterul din mijloc.
 '''
# cuvant = input('Introdu cuvantul\n')
# lungime_cuvant = len(cuvant)
# print(lungime_cuvant)
# print(cuvant[lungime_cuvant // 2])

# sau rezolvare trainer:
'''paranteze = {x[(len(x)//2)]} sintaxa pt litera din mijloc
 {} - reprezinta "integrarea" cu f'{}'
[] - reprezinta indexul din x care vreau sa il afisez, aka x[2]
() - reprezinta integrarea functiei len() in indexul care vrem sa il afisam x[(len(x))]
'''
# x = input('Introdu string\n')
# print(f'Caracterul din mijloc este ->>>>> [ {x[(len(x)//2)]} ]')
# y = len(x)
# print(f'Sirul are {y} caractere')
# mij = y / 2
# print(f'Mijlocul sirului reprezinta {mij}')
# mij2 = int(mij)
# print(f'Partea intreaga din caracterul din mijloc reprezinta {mij2}')
# print(f'Caracterul din mijloc este ->>>>> {x[mij2]}')

# # 2. Folosind assert, verifică dacă un string este palindrom.
# x = input('palindrom \n')
# assert x == x[::-1]
# print('este un palindrom')

'''
3. Folosind o singură linie de cod :
- citește un string de la tastatură (ex: 'alabala portocala');
- salvează fiecare cuvânt într-o variabilă;
- printează ambele variabile pentru verificare.
'''
# glasul_copilariei = input('Introdu\n')
# print(glasul_copilariei)
# glasul = input('Primul cuvant\n')
# copilariei = input('Al doilea cuvant\n')
# print(glasul)
# print(copilariei)
# print(glasul + ' ' + copilariei)

# sau rezolvare trainer: este despre altceva :(
# str = 'alabala portocala'
# x, y = str.split()
# print(f'Primul cuvant este {x}')
# print(f'Al doilea cuvant este {y}')

'''
4. Exercițiu:
- citește un string de la tastatură (ex: alabala portocala);
- salvează primul caracter într-o variabilă - indiferent care este el, încearcă
cu 2 stringuri diferite;
- capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
caracter => alAbAlA portocAla.
'''
# myStr = input('Introdu cuvintele: \n')
# primul_caracter = myStr[0]
# print(myStr[0])
# s = myStr[1:17].replace('a', 'A')
# print(f'{myStr[0]}{s}{myStr[17]}')  # cu ajutorul Alinei

# sau rezolvare trainer: - ce complicatenie !!!
# str = 'alabala portocala'
# st_prim = str[0]
# st_ultim = str[-1]
# st_dintre = str[1:-1]
# print(st_prim)
# print(st_ultim)
# print(st_dintre)
# print(f'Stringul modificat este {st_prim}{st_dintre.upper()}{st_ultim}')
# print(f'Stringul modificat este {st_prim}{st_dintre.replace(st_prim, st_prim.upper())}{st_ultim}')  # fara count
# print(f'Stringul modificat este {st_prim}{st_dintre.replace(st_prim, st_prim.upper(), 2)}{st_ultim}')  # folosind count

'''
5.Exercițiu:
- citește un user de la tastatură;
- citește o parolă;
- afișează: 'Parola pt user x este ***** și are x caractere';
- ***** se va calcula dinamic, indiferent de dimensiunea parolei,
 trebuie să afișeze corect.
eg: parola abc => ***
parola abcd => ****
'''
# User= input("User:")
# Parola = input("Parola:")
# Lungime_parola=len(Parola)
# print(f'Parola pentru Userul {User} este {Lungime_parola * "*"}  si are {len(Parola)} caractere')
# # cu ajutorul lui Cosmin

# sau rezolvare trainer:
# user = input('Introdu user\n')
# parola = input('Introdu parola\n')
# obf = len(parola) * '*'
# print(f'Parola pentru userul {user} este {obf} si are {len(obf)} caractere')
# # print(f'Parola pentru userul {user} este {len(parola) * "*"} si are {len(parola)} caractere')