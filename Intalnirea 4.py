#   Intalnirea 4 - CICLURI REPETITIVE

'''   while / while else
● Se execută un bloc de cod atât timp cât o condiție e adevărată.
● Opțional: la final se poate pune else, această zonă se execută o dată, la final.
'''

# i = 0
# while i < 3:
#   print(i)
#   i += 1
# # obtional putem avea si else:
# else:
#     print('Am terminat ciclul')
#
# i = 6
# while i > 0 < 6:
#   print(i)
#   i -= 1

'''  Continue
● Cuvântul cheie ‘continue’ va sări peste iterația actuală.
● E un fel de skip.
● Se va sări peste blocul de cod de după skip, care ține de for/ while.
'''

# i = 0
# while i < 6:
#   i += 1
#   if i == 2:
#     continue
#   print(i)   # sare peste 3 la printare, adica excludem din rezultate

# i = 0
# while i < 89888888:
#   i += 900
#   i += 1232131
#   i += 1
#   if i == 2:  # dau debug si vad la ce rezultat am ajuns
#     continue
#   print(i)

# # Exemplu pt citit de la coada la cap:
#
# n = input('Type a string:\n')
# list = list(n)
# print(list)
# reverse = list[::-1]
# count = ''
# for i in reverse:
#   count += i
#   if len(count) ==len(n):
#     print(count)
#   else:
#     pass  # nu o sa ajunga niciodata la else in acest caz


# # sau def o FUNCTIE() apoi apelez o functie:
# i = 0
# while i < 6:
#     i += 1
#     if i == 2:
#      continue
#     print(i)

# functie()->>> cu zece obiecte cap - la - cap obtii un test case

'''break  - practic opreste iteratia
● Cuvântul cheie ‘break’ va opri iterația.
● Practic se iese automat din loop.
● Nu se mai execută codul de după break, din cadrul unui for/ while.
'''
# folosim de obicei atunci cand cautam dupa un element exact

# i = 1
# while i < 6:  # cand avem elemente pe care nu le stim exact
#   print(i)
#   if i == 3:
#     break
#   i += 1
#
# # Exemplu pt break:
# contacts = [
#     ('James', 42),
#     ('Amy', 24),
#     ('John', 31),
#     ('Amanda', 63),
#     ('Bob', 18)
# ]
# name = input('Enter name\n')
# for contact in contacts:  # for folosim cand stim exact elementele
#     if name == contact[0]:
#         print(name, "is", contact[1])
#         break
# else:
#     print('Not Found')


'''FOR/ FOR ELSE
● Se execută un bloc de cod pentru fiecare valoare din range.
● Range seamănă cu slicing. Ne spune:
○ De unde începem? Default e 0.
○ Până unde iterăm?
○ Opțional: pasul.
● Opțional: la final se poate pune else.
○ această zonă se execută o dată, la final.
'''
# for i in range(4):
#   print(i)

# sau ...este ca si la slicing cu index de inceput, sfarsit si pas
# for i in range(100, 0, -5):  # parcurgere inversa (descrescatoare) trebuie pus minus la pas
#   print(i)
# else:
#   print('Am ajuns la final') # La fel, else nu este obligatoriu sau esential
# for i in range(0, 101, 5):
#   print(i)

# for i in range(0, 101, 5):  # parcurgere crescatoare
#   print(i)

'''
Folosim si aici CONTINIU
'''

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue  # excludem item din lista
#   print(x)

'''
 Folosim si aici BREAK
'''
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#   if fruit == "cherry":
#     break
#   print(fruit)

''' FOR EACH
● Se parcurge o colecție și se salvează fiecare element într-o variabilă.
● La fiecare iterație, variabila se va suprascrie cu valoarea actuală.
● Rând pe rând, se vor parcurge toate elementele dintr-o colecție.
'''
# masini1 = ['Audi', 'Volvo', 'Mercedes']
# for masina in masini
#     print(f'<asina mea preferata este FOR EACH {masina}')

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
#
# for x in adj:
#   for y in fruits:
#     print(x, y)

# # daca vrem sa schimbam una dintre valorile din lista de mai sus accesam indexul respectiv
# culori = ['rosu', 'albastru', 'verde', 'galben']
# for culoare in culori:
#     print(f'Culoarea mea preferata este {culoare}')

# fruits = ["apple", "banana", "cherry"]
# print(f'Lista initiala = {fruits}')
# for i in range(len(fruits)):
#   if fruits[i] == 'cherry':
#     fruits[i] = 'kiwi'
# print(fruits)

# # Exercitii
#
# # 1 Acceleram pana nu mai avem benzina
#
# benzina = 10
# consum = 1
# while benzina > 0:
#     print('Acceleram')
#     benzina = benzina-consum
#     if benzina < 3:
#         print('Alimenteaza')
#     print(f'Mai ai {benzina} litri de benzina')
# else:
#     print('Ai ramas fara benzina')

# 2  Afiseaza doar numerele pozitive dintr-o lista.

# numere = [1, 0, 2, 5, 9, 10, -5, -25]
# numere_pozitive = []
# for numar in numere:
#     if numar > 0:
#         numere_pozitive.append(numar)
# print(numere_pozitive)
# # sau
# for numar in numere:
#     if numar <= 0:
#         continue
#     print(numar)
# # sau
# for i in range(len(numere)):
#     if numere[i] > 0:
#         numere_pozitive.append(numere[i])
# print(numere_pozitive)

# Notiunea de CONSTANTA - ar trebui scrise cu litere majuscule si nu se suprascriu decat daca e abs necesar


'''    TEMA 4  FUNCTII
Exerciții obligatorii - grad de dificultate: Usor spre Mediu .

1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']
Folosește un for că să iterezi prin toată lista și să afișezi;
● ‘Mașina mea preferată este x’.
● Fă același lucru cu un for each.
● Fă același lucru cu un while.
'''
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for name in masini:
#     print(f'Masina mea preferata este', name)
# masini1 = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for i in masini1:
#     print(f'Masina mea preferata este FOR {i}')
# # # ● Fă același lucru cu un for each.
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# print(f'Lista initiala = {masini}')
# for i in range(len(masini)):
#     print(f'masina mea preferata este', i)

# # ● Fă același lucru cu un while.
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# i = 0
# while i < len(masini):
#     i >= 0 < 9
#     print(f'Masina mea preferata este', masini[i])
#     break

'''2. Aceeași listă:
Folosește un for else
În for
- Modifică elementele din listă astfel încât să fie scrise cu majuscule,
exceptând primul și ultimul.
În else:
- Printează lista.
'''
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for name in masini:
#     prim = name[0]
#     intre = name[1:-1]
#     ultim = name[-1]
#     print(f'{prim.lower()}{intre.upper()}{ultim}')
# else:
#     print(masini)

'''3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Itereaza prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
Printează ‘am găsit mașina dorită de dvs’
Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
Printează ‘Am găsit mașina X. Mai căutam‘
'''
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# alege_masina = input('introdu marca\n')
# for masina in masini:
#     if alege_masina == 'Mercedes':
#         print('Am gasit masina dorita de dv')
#         break
#     else:
#         print('Nu am gasit cautata. Mai cautam')
#         break

'''4. Aceași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
excepția Trabant și Lăstun.
- Dacă mașina e Trabant sau Lăstun:
Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
else).
- Printează S-ar putea să vă placă mașina x.
'''
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for masina in masini:
#     if masina == 'Trabant' or 'Lastun':
#         continue
# print('S-ar putea să vă placă masina x')

'''5. Modernizează parcul de mașini:
● Crează o listă goală, masini_vechi.
● Itereaza prin mașini.
● Când găsesti Lăstun sau Trabant:
- Salvează aceste mașini în masini_vechi.
- Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).

● Printează Modele vechi: x.
● Modele noi: x.
'''
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# masini_vechi = []
#
# for masina in masini:
#     if masina == 'Trabant':
#         masini_vechi.append('Trabant')
#         masini.remove('Trabant')
#         masini.append('Tesla')
#     print(masini_vechi)
#     if masina == 'Lastun':
#         masini_vechi.append('Lastun')
#         masini.remove('Lastun')
#         masini.append('Tesla')
# print(f'Modele vechi', masini_vechi)
# print(f'Modele noi', masini)

'''6. Având dict:
pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
Vine un client cu un buget de 15000 euro.
● Prezintă doar mașinile care se încadrează în acest buget.
● Itereaza prin dict.items() și accesează mașina și prețul.
● Printează Pentru un buget de sub 15000 euro puteți alege mașină
xLastun
● Iterează prin listă.
'''
# pret_masini = {
# 'Dacia': 6800,
# 'Lăstun': 500,
# 'Opel': 1100,
# 'Audi': 19000,
# 'BMW': 23000
# }
# # ● Prezintă doar mașinile care se încadrează în acest buget.
# for x, y in pret_masini.items():
#     if y <= 15000:
#        print(x)
# # # ● Itereaza prin dict.items() și accesează mașina și prețul.
# for x, y in pret_masini.items():
#     if y <= 15000:
#        print(x, y)
# # # ● Printează Pentru un buget de sub 15000 euro puteți alege mașină
# xLastun
# for x, y in pret_masini.items():
#     if y <= 500:
#         print(f'Pentru un buget de sub 15000 euro puteți alege mașină {x}')

# 7. Având lista:
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# ● Iterează prin ea.
# ● Afișează de câte ori apare 3 (nu ai voie să folosești count).
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# # ● Iterează prin ea.
# for x in numere:
#     print(x)
# # ● Afișează de câte ori apare 3 (nu ai voie să folosești count).
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# nr_3 = []
# for x in numere:
#     if x != 3:
#         nr_3.append(x)
#         print(nr_3)
#         numere.remove(x)
# print(numere)
#  altfel, de la Lidia:
# i = 3
# if i in numere:
#     print(sum(i == 3 for i in numere))

#
# # 8. Aceeași listă:
# # ● Iterează prin ea
# # ● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# print(numere)
# suma = 0
# for x in numere:
#     suma = x + suma
#     print(suma)