'''Tema 5 - Funcții
Exerciții Recomandate - grad de dificultate: Ușor
1. Revizualizează întâlnirea 5 și ia notițe în caz că ți-a scăpat ceva.
2. Vizualizează din ‘Primii pași în Programare’ video.
- OOP;
Astfel, la întâlnirea LIVE deja va fi a 2-a oară când vei auzi conceptele și sigur ți
se vor întipări în minte mai bine.
Link: https://www.itfactory.ro/8174437-intro-in-programare/
Pentru toate exercițiile. Apelați funcția de cel puțin 2 ori cu valori diferite
pentru a testa. Daca functia are return, printati raspunsul
Te rog să scrii pe canalul de comunicare scrisă unde întâmpini dificultăți și te
ajut.
Dacă stai blocat > 30 min, cere indiciu.

'''
# Exerciții obligatorii - grad de dificultate: Usor spre Mediu

#1.Funcție care să calculeze și să returneze suma a două numere
# def suma():
#     a = int(input('Introduceti a:\n'))
#     b = int(input('Introduceti b:\n'))
#     return a + b
#
#
# print(suma())


# 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
# a = int(input('introdu un numar\n'))
# def par_impar(a):
#     if a % 2 == 0:
#         return 'TRUE'
#     if a % 2 != 0:
#         return 'FALSE'
#
#
# print(par_impar(a))

'''
3. Funcție care returnează numărul total de caractere din numele tău complet.
(nume, prenume, nume_mijlociu)
'''
#
# def lungime_nume_complet(nume, initiala, prenume):
#     nume_complet = nume + initiala + prenume
#     return nume + prenume + initiala
#
#
# print(len(lungime_nume_complet('Minzala', 'Daniela', 'GH')))

# 4. Funcție care returnează aria dreptunghiului
#
# def aria_dreptunghiului():
#     lungimea = int(input('lungimea:\n'))
#     latimea = int(input('latimea:\n'))
#     aria_dreptunghiului = lungimea * latimea
#     return aria_dreptunghiului
#
#
# print(aria_dreptunghiului())

# 5. Funcție care returnează aria cerculu
# import math
# def aria_cercului():
#     r = int(input('Introdu raza r:\n'))
#     aria = math.pi * r**2
#     return aria
#
#
# print(aria_cercului())

# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
# și False dacă nu găsește.
# def se_gaseste_caracterul(x,text):
#     if x in text:
#         return True
#     else:
#         return False
# print(se_gaseste_caracterul('a','Ana are mere'))

# 7. Funcție fără return, primește un string și printează pe ecran:
# ● Nr de caractere lower case este x
# ● Nr de caractere upper case exte y

# def afisare_caractere(cale_text):
#     nr_lowercase = 0
#     nr_uppercase = 0
#     for caracter in cale_text:
#         if caracter.islower():
#             nr_lowercase += 1
#         elif caracter.isupper():
#             nr_uppercase += 1
#         print('Numar caractere lowercase este', nr_lowercase)
#         print('Numar caractere uppercase este', nr_uppercase)
#
# afisare_caractere('Marina Comerciala')


# 8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
# numerele pozitive

# def Lista_numere_pozitive():
#     Lista_numere = [-5, -3, 0, 1, 3, 5]
#     Lista_numere_pozitive = []
#     for x in range(len(Lista_numere)):
#         if Lista_numere[x] <= 0:
#             continue
#         else:
#             Lista_numere_pozitive.append(Lista_numere[x])
#     print(f'Lista_numere_pozitive, {Lista_numere_pozitive}')
#
#
# Lista_numere_pozitive()

# 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# ● Primul număr x este mai mare decat al doilea nr y
# ● Al doilea nr y este mai mare decat primul nr x
# ● Numerele sunt egale.

# def relatia_numerelor(x,y):
#     if x > y:
#         print('Primul numar', x, 'este mai mare decat al doilea nr', y)
#     elif x < y:
#         print('Primul numa', y, 'este mai mare decat al doilea nr', x)
#     else:
#         print('Numerele', x, 'si', y, 'sunt egale')
#
#
# relatia_numerelor(2,4)

# 10. Funcție care primește un număr și un set de numere.
# ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
# ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
# returnează Fals

# def adauga_in_set(numar, set_numere):
#     numar_nou = int(input('Introdu numarul nou\n'))
#     if numar_nou in set_numere:
#         print('Nu am adaugat numarul in set. Acesta exista deja.', False)
#         return False
#     else:
#         print('Am adaugat nr-ul in set.', True)
#         return True
#
#
# adauga_in_set(4, {2, 3, 5})

#  Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google.

# 1. Funcție care primește o lună din an și returnează câte zile are acea luna

# from calendar import monthrange
# def zile_ale_lunii(an, luna):
#     return monthrange(an, luna)[1]
#
#
# print(zile_ale_lunii(2016, 2))

#  2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
# împărțirea a două numere.
# În final vei putea face:
# a, b, c, d = calculator(10, 2)
# ● print("Suma: ", a)
# ● print("Diferenta: ", b)
# ● print("Inmultirea: ", c)
# ● print("Impartirea: ", d)

# def calculator(x, y):
#     suma = x + y
#     diferenta = x - y
#     inmultirea = x * y
#     impartirea = x / y
#     return suma, diferenta, inmultirea, impartirea
#
# a, b, c, d = calculator (10, 2)
# print('Suma:', a)
# print('Diferenta', b)
# print('inmultirea', c)
# print('impartirea', d)

#3. Funcție care primește o lista de cifre (adică doar 0-9)
# Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returnează un DICT care ne spune de câte ori apare fiecare cifră
# => dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0
# 9: 1
# }
# def functia():
#     new_list = [1, 3, 1, 5, 9, 7, 7, 5, 5]
#     for i in range(len(new_list)):


# functia()
# import json
# lista_cifre = [1, 3, 1, 5, 9, 7, 7, 5, 5]
# def numar_cifre(*lista_cifre):
#     dict_cifre = {i: 0 for i in range(10)}  # initializam dictionarul cu toate cifrele ca si cheie si valoare zero
#     for cifra in lista_cifre:
#         dict_cifre[cifra] = dict_cifre[cifra] + 1
#         return dict_cifre
#
#
# print(json.dumps(numar_cifre(1, 3, 1, 5, 9, 7, 7, 5, 5), indent= 4))

# 4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele
# def valoare_max(numar1, numar2, numar3):
#     return max(numar1, numar2, numar3)
#
#
# val_max = valoare_max(5, 9, 2)
# print(val_max)

# # sau:
# def maximul(x, y, z):
#     if x > y and x > z:
#         return x
#     elif y > x and y > z:
#         return y
#     else:
#         return z
#
#
# print(maximul(1, 4, 3))
# print(maximul(10, 2, 4))
# print(maximul(1, 32, 425))

# 5. Funcție care să primească un număr și să returneze suma tuturor numerelor
# de la 0 la acel număr
# Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)

# def suma_numerelor_pana_la(numar):
#     return sum(range(numar + 1))
#
#
# suma = suma_numerelor_pana_la(5)
# print(suma)

# sau
# def suma(n):
#     rezultat = 0
#     for i in range(1, n+1):
#         rezultat = rezultat + i
#     print(rezultat)
#
# suma(6)

'''  Exerciții Opționale - Bonus
1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați
numerele comune
Exemplu:
list1 = [1, 1, 2, 3]
list2 = [1, 1, 2, 3]
Răspuns: {2, 3}
'''
# def numere_comune(lista1, lista2):
#     set1 = set(lista1)
#     set2 = set(lista2)
#     return list(set1.intersection(set2))
#
#
# lista1 = [1, 1, 2, 3]
# lista2 = [2, 2, 2, 3]
# comune = numere_comune(lista1, lista2)
# print(comune)

'''
2.. Funcție care să aplice o reducere de preț
Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90
Tratați cazurile în care reducerea e invalida.
De exemplu o reducere de 110% e invalidă.
'''

# def aplicare_reducere(pret_initial, reducere):
#     if reducere <= 0 or reducere >= 100:
#         print("Reducerea trebuie sa fie intre 0 si 100%")
#         return pret_initial
#     pret_final = pret_initial * (100 - reducere) / 100
#     return pret_final
#
# pret_initial = 100
# reducere = 25
# pret_final = aplicare_reducere(pret_initial, reducere)
# print(pret_final)

# 3. Funcție care să afișeze data și ora curentă din ro
# (bonus: afișați și data și ora curentă din China)
# import datetime
# import pytz
#
# def display_current_time():
#     timezone_ro = pytz.timezone('Europe/Bucharest')
#     now_ro = datetime.datetime.now(timezone_ro)
#     print(f'Ora curenta in Romania: {now_ro.strftime("%Y-%m-%d %H:%M:%S")}') # string format time
#
#     timezone_cn = pytz.timezone('Asia/Shanghai')
#     now_cn = datetime.datetime.now(timezone_cn)
#     print(f'Ora curenta in China: {now_cn.strftime("%Y-%m-%d %H:%M:%S")}') # string format time
#
#
# display_current_time()

# 4. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la
# Crăciun dacă nu vrei să ne zici cand e ziua ta :)
#
# import datetime
#
# def zile_pana_la_craciun():
#     an_curent = datetime.datetime.now().year
#     data_craciun = datetime.datetime(an_curent, 12, 25)
#     diferenta = data_craciun - datetime.datetime.now()
#     return diferenta.days
#
# zile_ramase = zile_pana_la_craciun()
# print("Mai sunt", zile_ramase, "zile pana la Craciun!")