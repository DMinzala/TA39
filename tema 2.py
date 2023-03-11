''''
        TEMA 2
        Tema 1 _ Operatori & Tipuri de Date
Exerciții Recomandate - grad de dificultate: Ușor
1. Revizualizeaza intalnirea 2 si ia notite in caz ca ti-a scapat ceva
2. Vizualizeaza video despre Operatori si Flow Control din 'Primii pasi in Programare'
(Daca nu ai facut-o deja)
3. Vizualizeaza video 3 despre Structuri de date din 'Primii pasi in Programare'. Astfel, la
intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele si sigur ti se vor intipari in
minte mai bine. Link catre video: https://www.itfactory.ro/8174437-intro-in-programare
'''

'''
Exerciții obligatorii - grad de dificultate: Ușor spre Mediu:
Pentru toate exercitiile se va folosi notiunea de if in rezolvare. Indirect veti exersa si operatorii in
cadrul conditiilor ramurilor din if
Variabila X specificata in exercitiile de mai jos poate fi initializata direct in cod sau citita de la
tastatura, dupa preferinte si va fi o variabila int
'''

#  1. Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else
# if/else - Evalueaza conditii si bifurca codul in functie de rezultat

#  2. Verifica si afiseaza daca x este numar natural sau nu (un numar se considera natural
#  daca este numar intreg mai mare ca 0)

# x = -1
# if x >= 0:
#     print('x este numar Natural')
# else:
#     print('x Nu este numar Natural')

# # sau >>>>varianta de la tastatura
# x = int(input('Introdu numarul x\n'))
# if x >= 0:
#     print('x este numar Natural')
# else:
#     print('x Nu este numar Natural')

#  3. Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru

# x = int(input('Introdu valoarea lui x\n'))
# if x < 0:
#     print('x este Numar negativ')
# elif x > 0:
#         print('x este Numar pozitiv')
# else:
#     print ('x este numar neutru pentru adunare')

#  4. Verifica si afiseaza daca x este intre -2 si 13 (incluzand captele de interval).

# x = int(input('Introdu valoarea lui x\n'))
# if x >= -2 and x <= 13:
#     print(' x se afla in intervalul [-2;13]')
# else:
#     print('x este in afara intervalului[-2;13]\n')

'''
SAU
x = int(input('Introdu numar: '))
if x in range(-2, 14):
    print('Se afla in numerotare')
else:
    print('Nu se afla in numerotare')
'''

#  5. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5 (diferenta inseamna
# cate numere sunt intre x si y, nu rezultatul diferentei intre x si y). Hint: Se va folosi functia
# abs

# x = int(input('Introdu valoarea lui x\n'))
# y = int(input('Introdu valoarea lui y\n'))
# z = abs(x) - abs(y)
# if z < 5:
#     print('suma numerelor dintre x si y este <5')
# else:
#     print('suma numerelor dintre x si y este >= 5')

# x = int(input('introdu un nr\n'))
# y = int(input('introdu un nr\n'))
# z = abs(x-y)
# if z <= abs(5):
#     print(f'diferenta este 5')
# else:
#     print(f'este mai mare')

# 6. Verifica daca x NU este intre 5 si 27, incluzand capetele de interval.
# (a se folosi ‘not’)

# x = int(input('Introdu valoarea lui x\n'))
# if not( x >= 5 and x <= 27):
#     print('x NU este in intervalul [5;27]\n')
# else:
#     print('x este in intervalul [5;27]\n')

#  7. Declara o noua variabila y de tip int si apoi verifica si afiseaza
#  daca x si y sunt egale, daca nu, afiseaza care din ele este mai mare

# x = int(input('Introdu valoarea lui x\n'))
# y = int(input('Introdu valoarea lui y\n'))
# if x == y:
#     print('x egal cu y')
# elif x < y:
#     print('x este mai mic decat y')
# else:
#     print('x este mai mare decat y')

'''
 8. Presupunand ca x, y, z (toate de tip int) - reprezinta laturile unui triunghi,
afiseaza daca triunghiul este isoscel (doua laturi sunt egale),
echilateral (toate laturile sunt egale) sau oarecare (nicio latura nu e egala cu alta).
'''
# x = int(input('Introdu valoarea lui x\n'))
# y = int(input('Introdu valoarea lui y\n'))
# z = int(input('Introdu valoarea lui z\n'))
# if x == y and x != z and y != z:
#     print('Triunghiul este isoscel')
# elif x == z and y == z and z == x:
#     print('Triunghiul este echilateral')
# else:
#     print('Triunghiul este oarecare')

# sau varianta Lidiei cu or
# x = int(input('introdu latura A\n'))
# y = int(input('introdu latura B\n'))
# z = int(input('introdu latura C\n'))
# if x == y == z:
#     print(f'Triunghiul este Echilateral')
# elif x == y or y == z or z == x :
#     print(f'Triunghiul este Isoscel')
# else:
#     print(f'Triunghiul este Oarecare')

#  9. Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu.
#  Atentie! Trebuie sa evaluati si cazurile uppercase si cazurile lowercase.

# !!!!!!!!!

# litera = str(input('Introdu o litera:\n'))
# if litera.upper == 'a' or litera.upper == 'e' or litera.upper == 'i' or litera.upper == 'u':
#     print('Litera este o vocala')
# elif litera.lower == 'a' or litera.lower == 'e' or litera.lower == 'i' or litera.lower == 'u':
#     print('Litera este o vocala')
# else:
#     print('Litera este o consoana')

# x = input('introdu o litera\n')
# if x.lower() in ('a', 'e', 'i', 'o', 'u'):
#     print(f'litera ESTE o Vocala')
# elif x.upper() in ('A', 'E', 'I', 'O', 'U'):
#     print(f'litera ESTE o Vocala')
# else:
#     print(f'litera NU este o Vocala')

'''
10. Transforma si printeaza notele din sistem românesc in sistem american dupa cum
urmeaza:
a. Peste 9 => A
b. Peste 8 => B
c. Peste 7 => C
d. Peste 6 => D
e. Peste 4 => E
f. 4 sau sub => F
'''
# nota = float(input('Introdu o nota\n'))
# if nota >= 9.00 and nota <=10:
#     print('Nota este A')
# elif nota >= 8.00 and nota <= 8.99:
#     print('Nota este B')
# elif nota >= 7.00 and nota <= 7.99:
#     print('Nota este C')
# elif nota >= 6.00 and nota <= 6.99:
#     print('Nota este D')
# elif nota >= 4.01 and nota <= 5.99:
#     print('Nota este E')
# elif nota >= 0.01 and nota <= 4.00:
#     print('Nota este F')
# else:
#     print('Nu este o nota')

'''
Exerciții Opționale - grad de dificultate: Mediu spre
greu (s-ar putea să ai nevoie de Google).
'''
#  1. Verifica daca x are minim 4 cifre (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
# x = input('scrie numarul\n')
# if len(x) >= 4:
#     print('Numarul are min patru cifre')
# else:
#     print('Numarul nu are 4 cifre')

#  2. Verifica daca x are exact 6 cifre

# x = input('scrie numarul\n')
# if len(x) == 6:
#     print('x are exact 6 cifre')
# else:
#     print(f'{x} Nu are exact 6 cifre')  # listeaza 123 in loc de x

#  3. Verifica daca x este numar par sau impar

# x = int(input('scrie numarul\n'))
# if x % 2 == 0:
#     print('Numarul este par')
# else:
#     print('Numarul este impar')

#  4. Avand trei variabile x, y, z (toate int) afiseaza in consola
#  care este cea mai mare dintre ele

# x = int(input('Introdu valoarea lui x\n'))
# y = int(input('Introdu valoarea lui y\n'))
# z = int(input('Introdu valoarea lui z\n'))
# if x > y and x > z:
#     print('x este cel mai mare dintre ele')
# elif y > z and y > x:
#     print('y este cel mai mare')
# elif z > x and z > y:
#     print('z este cel mai mare')
# else:
#     print('numerele sunt egale')

'''
5. Presupunand ca x, y, z - reprezinta unghiurile unui triunghi, verifica si afiseaza daca
triunghiul este valid sau nu (un triunghi este valid daca suma tuturor unghiurilor este de
180 de grade sau daca suma lungimilor a oricare doua laturi este mai mare decat
lungimea celei de-a treia laturi)
'''
# x = int(input('scrie masura unghiului x\n'))
# y = int(input('scrie masura unghiului y\n'))
# z = int(input('scrie masura unghiului z\n'))
# if (x + y + z) == 180:
#     print('Triunghiul este valid')
# else:
#     print('Triunghiul nu este valid')

'''
6. Avand stringul: 'Coral is either the stupidest animal or the smartest rock' citește de
la tastatura un număr x de tip int și afișează stringul fără ultimele x caractere. ex: dacă
ați ales 7 se va afisa urmatorul string: 'Coral is either the stupidest animal or the
smarte'
'''
# narativ = 'Coral is either the stupidest animal or the smartest rock'
# n = int(input('numarul de litere lipsa\n'))
# print(narativ[0:-n])
#  sau mai complicat
# last_index = len(narativ) - n
# print(narativ[last_index])
# if last_index == len(narativ) - n:
#      print(narativ[0:last_index])


#  7. Folosindu-te de același string de la exercițiul 6,
#  declara un string nou care sa fie format din primele 5 caractere + ultimele 5

# narativ = 'Coral is either the stupidest animal or the smartest rock'
# lungime_narativ = len(narativ)
# print(lungime_narativ)
# firsts_index = narativ[0:5]
# lasts_narativ = narativ[52:57]
# print(f'{firsts_index} {lasts_narativ}')

# Sau
# x = str('Coral is either the stupidest animal or the smartest rock')
# y = x[0:5]+x[-5:]
# print(y)

'''
8. Folosindu-te de același string de la exercițiul 6, salvează într-o variabila și afiseaza
indexul de start al cuvântului rock - adică poziția in string la care începe cuvântul rock
(hint: este o funcție care te ajuta sa faci asta). Folosind aceasta variabila + slicing,
afișează tot stringul pana la acest cuvant. Output asteptat: 'Coral is either the stupidest
animal or the smartest '
'''

# narativ = 'Coral is either the stupidest animal or the smartest rock'
# start_index = len(narativ) - 4
# print(start_index)
# narativ_afisat = narativ[0:start_index]
# print(f'Narativul afisat este: {narativ_afisat}')

#  sau

# x = str('Coral is either the stupidest animal or the smartest rock')
# word = 'rock'
# cautare = x.find(word)
# print(x[0:cautare])

#  sau

# x = 'Coral is either the stupidest animal or the smartest rock'
# y = len(x) - 4
# z = x[y:]
# print(x[:y])


'''
9. Citeste de la tastatura un string si verifica daca primul și ultimul caracter sunt la fel. 
Se va folosi un assert. Atentie: se dorește ca programul sa fie case insensitive,
 adica 'apA' e acceptat ca un string in care primul si ultimul caracter este la fel (hint, 
 te poti folosi de o functie pentru a face string-ul case insensitive)
'''
#  !!!!!!!
# text = input('Scrie textul\n').upper()
# first_index = text[0]
# last_index = text[-1]
# assert first_index == last_index
# print(f'{first_index} {last_index}')

# sau

# x = input('Scrie un cuvant: ').upper()
# assert x[0] == x[-1]
# print('okay')

#  10. Avand stringul '0123456789' afiseaza doar numerele pare si apoi doar numerele impare
# (hint: foloseste slicing si controleaza afisarea in slicing cu slicing step)

# stringul = '0123456789'
# print(stringul[2:10:2])
# print(stringul[1:10:2])

# sau
# x = '0123456789'
# print(x[2::2], x[1::2]) # se scoate conditionarea lungimii stringului : 10
'''
Exerciții Bonus
1. Vrem sa cream o aplicatie pentru achizitionare bilete de avion care sa primeasca drept
inputuri urmatoarele informatii:
a. Varsta
b. Insotit de mama
c. Insotit de tata
d. Pasaport
e. Act permisiune mama
f. Act permisiune tata
Conditii de imbarcare:
1. Daca pers are varsta peste 18 ani si are pasaport
2. Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti
3. Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte
si are permisiune in scris de la celalat parinte

Scrie codul care implementeaza conditiile de imbarcare de mai sus si testeaza-l cu toate
variantele care crezi ca ar trebui testate. Genereaza scenarii de testare cu expected results si
apoi ruleaza codul pentru a verifica daca expected results sunt egale cu actual results.

Exemple:
1. Varsta 19 ani, nu am pasaport => Nu ma pot imbarca
2. Varsta 17 ani, am pasaport, ambii parinti => Ma pot imbarca
'''

a = int(input('introdu varsta:\n'))
b = input('insotit de mama\n')
c = input('insotit de tata\n')
d = input('are pasaport\n')
e = input('Act permisiune mama\n')
f = input('Act permisiune tata\n')

if a >= 18 and d == 'da':
    print(f'Varsta {a} ani, am pasaport => Ma pot imbarca')
elif a < 18 and d == 'da' and c == 'da' and b == 'da':
    print(f'Varsta {a} ani, am pasaport, ambii parinti, fara acte de permisiune => Ma pot imbarca')
elif a < 18 and d == 'da' and (b == 'da' and f == 'da') or (c == 'da' and e == 'da'):
    print(f'Varsta {a} ani, am pasaport, cel putin un parinte si actul de permisune al celuilalt => Ma pot imbarca')
else:
    print('Nu ma pot imbarca fie din lipsa pasaportului, a unui parinte sau a unui act de permisiune in cazul in care sunt minor/a')

# sau varianta lui Petre:

# 1 (bonus)
# a = int(input('Varsta: '))
# b = input('Insotit de mama? (da/nu) ')
# c = input('Insotit de tata? (da/nu) ')
# d = input('Pasaport (da/nu) ')
# e = input('Act permisiune mama? (da/nu) ')
# f = input('Act permisiune tata? (da/nu) ')
# if a >= 18 and d == 'da':
#     print(f'Varsta {a} ani, am pasaport => Ma pot imbarca')
# elif a < 18 and d == 'da' and c == 'da' and b == 'da':
#     print(f'Varsta {a} ani, am pasaport, ambii parinti, fara acte de permisiune => Ma pot imbarca')
# elif a < 18 and d == 'da' and (b == 'da' and f == 'da') or (c == 'da' and e == 'da'):
#     print(f'Varsta {a} ani, am pasaport, cel putin un parinte si actul de permisune al celuilalt => Ma pot imbarca')
# else:
#     print('Nu ma pot imbarca fie din lipsa pasaportului, a unui parinte sau a unui act de permisiune in cazul in care sunt minor/a')

'''
2. Joc de noroc
- Cauta pe net si vezi cum se genereaza un numar random
- Imagineaza-ti ca dai cu zarul si salvezi acest numar intr-o variabila numita dice_roll.
Numarul salvat va fi generat random cu metoda gasita in online
- Introdu un numar de la tastatura care sa reprezinte numarul ales de la utilizator
- Verifica si afiseaza daca utilizatorul a ghicit numarul
- Vor exista 3 optiuni care vor trebui tratate:
● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
● Ai ghicit. Felicitari? Ai ales x si zarul a fost y
'''

# import random
# dice_roll = (random.randint(1, 6))  # ia numere aleatoriu intre 1 si 6
# # print(dice_roll)
# x = int(input('Alege un numar:'))
# if x == dice_roll:
#     print(f'Ai ghicit. Felicitari? Ai ales {x} si zarul a fost {dice_roll}')
# elif x > dice_roll and x <= 6:
#     print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {x} dar a fost {dice_roll}')
# elif x < dice_roll and  x >= 1:
#     print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {x} dar a fost {dice_roll}')
# else:
print('Alege una dintre cele 6 fete ale zarului ')
