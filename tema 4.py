import random
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
# ● ‘Mașina mea preferată este x’- FOR
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for masina in range(len(masini)):
#     print(f'Masina mea preferata este {masini[masina]}')

# sau varianta finala trainer:
# masini1 = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for i in range(len(masini1)):
#      print(f'masina mea preferata este FOR {masini1[i]}')
# # FOR simplu foloseste range

# ● Fă același lucru cu un FOR EACH.
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for name in masini:
#     print(f'Masina mea preferata este', name)

# sau varianta finala trainer:
# masini1 = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for masina in masini1:
#     print(f'Masina mea preferata este FOR EACH {masina}')
# FOR EACH folosit ca atare

# # ● Fă același lucru cu un while.
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# i = 0
# while i >= 0 < len(masini):
#     print(f'Masina mea preferata este', {masini[i]})
#     i = i + 1

# sau varianta finala trainer
# masini1 = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# i = 0
# while i < len(masini1):
#     print(f'Masina mea preferata este', {masini1[i]})
#     i = i + 1

'''2. Aceeași listă:
Folosește un for else
În for
- Modifică elementele din listă astfel încât să fie scrise cu majuscule,
exceptând primul și ultimul.
În else:
- Printează lista.
'''
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# pentru prima si ultima litera a fiecarei masini -lower
# for name in masini:
#     prim = name[0]
#     intre = name[1:-1]
#     ultim = name[-1]
#     print(f'{prim.lower()}{intre.upper()}{ultim}')
# else:
#     print(masini)

# pentru prima si ultima masina - lower, restul upper
# prima = masini[0]
# print(prima)
# ultima = masini[-1]
# print(ultima)
# intre = masini[1:-1]
# print(intre)
# for i in range(1, len(masini)-1):
#     masini[i] = masini[i].upper()
# else:
#     print(masini)

# sau varanta trainer:
# masini2 = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# prima_masina = masini2[0]
# print(prima_masina)
# ultima_masina = masini2[len(masini2)-1]
# print(ultima_masina)
# for masina in range(1, len(masini2)-1):
#     masini2[masina] = masini2[masina].upper()
# else:
#     print(masini2)

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
#     if masina == 'Trabant' or masina == 'Lastun':
#         continue
#     else:
#         print(f'S-ar putea să vă placă {masina}')

# sau varianta trainer:
# for masina in masini:
#     if masina == 'Trabant':
#         continue
#     elif masina == 'Lastun':
#         continue
#     else:
#         print(f'S-ar putea să vă placă {masina}')

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

 # sau varianta trainer:
# masini1 = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# masini_vechi = []
# masina1 = 'Lastun'
# masina2 = 'Trabant'
# masina3 = 'Tesla'
# for i in range(0, len(masini1)):
#     if masini1[i] == masina1 or masini1[i] == masina2:
#      masini_vechi.append(masini1[i])
#      masini1[i] =masina3
# print(f'Modele noi{masini1}')
# print(f'Modele vechi {masini_vechi}')

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
# # # # ● Itereaza prin dict.items() și accesează mașina și prețul.
# for x, y in pret_masini.items():
#     if y <= 15000:
#        print(x, y)
# # # # ● Printează Pentru un buget de sub 15000 euro puteți alege mașină
# # xLastun
# for x, y in pret_masini.items():
#     if y <= 500:
#         print(f'Pentru un buget de sub 15000 euro puteți alege mașină {x}')

# sau varianta trainer:
# buget = 15000
# itemi = pret_masini.items()  # afiseaza itemii din dictionar
# print(itemi)
# for item in itemi:
#     pret_masina = item[1]
#     if buget >= pret_masina:
#         print(f'Pentru bugetul de: {buget} puteti cumpara {item[0]} care costa {item[1]}')
# else:
#     print(f'{item[0]} e pre scump pt bugetul dv {buget} pt ca are pretul de {item[1]}')
# print(pret_masini['Dacia'])

# 7. Având lista:
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# ● Iterează prin ea.
# ● Afișează de câte ori apare 3 (nu ai voie să folosești count).
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# ● Iterează prin ea.
# for x in numere:
#     print(x)
# # ● Afișează de câte ori apare 3 (nu ai voie să folosești count).
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# nr_3 = []
# for x in numere:
#     if x == 3:
#         nr_3.append(x)
#         print(nr_3)

# sau varianta trainer:
# y = 0  # unde y este count
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3, 3, 3, 3, 3, 0]
# for i in numere:
#     if i == 3:
#         y = y + 1  # folosim count ca si numerotare
# print(f'numarul apare de {y} ori')


#  altfel, de la Lidia:
# i = 3
# if i in numere:
#     print(sum(i == 3 for i in numere))  # syntaxa pe un sing rand

#
# # 8. Aceeași listă:
# # ● Iterează prin ea
# # ● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# print(numere)
# suma = 0
# for x in numere:
#     suma = suma + x
# print(f'Suma este {suma}')

''' 9. Aceeași listă:
● Iterează prin ea.
● Afișază cel mai mare număr (nu ai voie să folosești max)
'''
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# maxim = 0
# for i in numere:
#     if i > maxim:
#         maxim = i  # practic suprascriu mereu cel mai mare numar gasit cu urmatorul mai mare
# print(f'Numarul maxim este {maxim}')

# sau varianta trainer:
# numere = [1, 1, 3, 1, 3, 3, 1, 11, -4, 99]
# maxim = 2
# for i in numere:
#     if i > maxim:
#         maxim = i
# print(f'Maxim este {maxim}')

'''
10. Aceeași listă:
● Iterează prin ea.
● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
● Afișază noua listă.
'''
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# for i in numere:
#     if numere[i] > 0:
#         numere[i] = -abs(numere[i])
#         print(numere)

#sau varianta trainer:
# numere = [5, 7, 3, 9, 3, 3, 1, 11, -4, 3]
# for i in range(len(numere)):
#     if int(numere[i]) > 0:
#         numere[i] = - numere[i]
# print(numere)
#
# for x in numere:
#     print(-x)

'''
Exerciții Opționale - grad de dificultate: Mediu spre greu: may need
Google.
1.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Itereaza prin listă alte_numere
Populează corect celelalte liste
Afișeaza cele 4 liste la final
'''
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# for i in alte_numere:
#     if i % 2 == 0:
#         numere_pare.append(i)
#     if i % 2 != 0:
#         numere_impare.append(i)
#     if i > 0:
#         numere_pozitive.append(i)
#     if i < 0:
#         numere_negative.append(i)
# print(numere_pare)
# print(numere_impare)
# print(numere_pozitive)
# print(numere_negative)

# sau varianta trainer:
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# for i in alte_numere:
#     if i % 2 == 0:
#         numere_pare.append(i)
#     else:
#         numere_impare.append(i)
#     if i > 0:
#         numere_pozitive.append(i)
#     else:
#         numere_negative.append(i)
# print(numere_pare)
# print(numere_impare)
# print(numere_pozitive)
# print(numere_negative)

'''
2. Aceeași listă:
Ordonează crescător lista fară să folosești sort.
Te poți inspira vizual de aici.
https://www.youtube.com/watch?v=lyZQPjUT5B4
'''
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# alte_numere.sort()
# print(alte_numere)


# Varianta Cosmin
# for i in range(len(alte_numere)):
#     for j in range(i+1, len(alte_numere)):
#         if alte_numere[i] > alte_numere[j]:
#              alte_numere[i], alte_numere[j] = alte_numere[j], alte_numere[i]
# print(alte_numere)

# Varianta Petre
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_ordonate = []
# while alte_numere: # aici while va rula pana lista se goleste
#     minimum = alte_numere[0]
#     for numar in alte_numere:
#         if numar < minimum:
#             minimum = numar
#     numere_ordonate.append(minimum)
#     alte_numere.remove(minimum)
# print(numere_ordonate)

'''
3. Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while
User alege un număr
Programul îi spune:
● Nr secret e mai mare
● Nr secret e mai mic
● Felicitări! Ai ghicit!
'''
# Varianta Cosmin
# numar_secret = random.randint(0,30)
# # print(numar_secret)
# numar_ghicit = int(input('alege un numar'))
# while numar_secret:
#     if numar_ghicit < numar_secret:
#         print('Numarul secret este mai mare')
#         break
#     elif numar_ghicit > numar_secret:
#         print('Numarul secret este mai mic')
#         break
#     elif numar_ghicit == numar_secret:# numar_ghicit==numar_secret:
#         print('Ai ghicit numarul')
#         break

# Varianta Petre
# import random
# numar_secret = random.randrange(1, 30)
# numar_ghicit = int(input("Alege numar: "))
# while numar_secret != numar_ghicit:
#     if numar_secret > numar_ghicit:
#         print("Numarul secret este mai mare")
#         numar_ghicit = int(input("Alege alt numar: "))  # input-ul este adaugat aici pentru a continua ciclul
#     elif numar_secret < numar_ghicit:
#         print("Numarul secret este mai mic")
#         numar_ghicit = int(input("Alege alt numar: "))  # input-ul este adaugat aici pentru a continua ciclul
#     else:
#         break
# print("Felicitari! Ai ghicit!")

'''
4. Alege un număr de la tastatură
Ex: 7
Scrie un program care să genereze în consolă următoarea piramidă
1
22
333
4444
55555
666666
7777777
Ex:3
1
22
333
'''
# Varianta Cosmin:
# numar = int(input('Alege numarul:'))
# i = 1
# j = 0
# while i <= numar:
#     while j < i:
#         print(i, end='')
#         j += 1
#     print('')
#     j = 0
#     i += 1
# Varianta Petre:
# x = int(input("Alege un numar: "))
# for i in range(x + 1):
#     for j in range(i):
#         print(i, end='') # end='' este folosit pentru a afisa un caracterele iterate una langa cealalta in loc de una sub cealalta
#     print('')

'''
5.
tastatura_telefon = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]
Iterează prin listă 2d
Printează ‘Cifra curentă este x’
(hint: nested for - adică for în for)
'''
# Varianta Petre:
# tastatura_telefon = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]
# for i in range(len(tastatura_telefon)):  # index i folosit pentru a itera prin prima lista
#     for j in range(len(tastatura_telefon[i])):  # index j folosit pentru a itera prin fiecare din subliste
#         print(f"Cifra curenta este {tastatura_telefon[i][j]}") # printeaza fiecare element din fiecare lista, pe rand si pe orizontal
# ________________ sau??? ________________
# for x in tastatura_telefon:
#     for y in x:
#         print(f'Cifra curenta este {y}')
