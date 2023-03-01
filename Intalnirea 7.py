from abc import abstractmethod, ABC

'''  Obiective Întâlnire 7

● Să știm ce e o excepție și cum o ‘tratăm’
● Să înțelegem cei 4 piloni ai OOP
○ Encapsulare
○ Moștenire
○ Abstractizare
○ Polimorfism

'''

import rez as rez

'''

Excepții

● Situații când codul nu poate executa instrucțiunile
● În acest caz codul ‘aruncă’ o excepție
● Programatorii se pot aștepta la ea, pot să o ‘prindă’ și să o ‘trateze’
● În acest sens putem anticipa erori și evităm să ‘crape’ aplicația
● Se folosește sintaxa try/except
● Uneori dorim să ‘ridicăm’ o excepție intenționat

'''
# print('Before')
#
# try:  # in try punem codul 'periculos
#     lista = [1, 2, 3]
#     lista[6]
# except IndexError as e:  #tratam Index Error exception
#     print(e)
#
# print('After')


#   Daca nu pun try except
# print('Before')
#
# lista = [1, 2, 3]
# lista[6]  # returneaza eroare: IndexError: list index out of range
#
# print('After')

#  A doua metoda  -- fortezi o exceptie
# x = 'str'
# if type(x) is int:
#     print('Ai folosit un tip de date valid')
# else:
#     raise TypeError('Folositi doar tipul int')

# Exemple

# try:
#     x = 10
#     rez = x / 0
#     print(rez)
# except ZeroDivisionError:
#     print('Eroare tip')

# try:
#     # x = 'salut'
#     print(x)
# except TypeError as e: # e este o variabila in care se salveaza eroarea generata de exceptiile redefinite (NameError, IndexError, TypeError)
#     print(e)
#
# try:
#     # x = 'salut'
#     print(x)
# except:
#     print('An excetion occurred')
#
# finally:
#     print('Am ajuns la final')

''' INHERITANCE (Mostenire)

● O clasă părinte poate fi moștenită de oricâte clase copil
● Aceste clase copil vor avea acces la toate atributele și metodele clasei părinte
'''

# class Chef:  # clasa parinte
#     tava = 'Tava masa1'
#
#     def make_salad(self):
#         print('Pot sa gatesc salata')
#
#     def make_soup(self):
#         print('Pot sa gatesc supa')
#
#     def make_fries(self):
#         print('fries')
#
#
# class Chef2:  # clasa copil care mosteneste clasa Chef (se trece intre paranteze numele clasei parinte)
#     tava2 = 'Tava masa2'
#
#     def make_salad2(self):
#         print('Pot sa gatesc salata2')
#
#     def make_soup2(self):
#         print('Pot sa gatesc supa2')
#
#
# class JapaneseChef(Chef, Chef2):  # poate mosteni de la doi parinti
#     def make_sushi(self):
#         print('Pot sa gatesc sushi')
#
#
# class ItalianChef(Chef, Chef2):
#     def make_pizza(self):
#         print('Pot sa gatesc pizza')
#
#
# obiect_jap = JapaneseChef()
# obiect_jap.make_salad()
# obiect_jap.make_soup()
# obiect_jap.make_sushi()
# print(obiect_jap.tava)
#
# std_it = ItalianChef()
# std_it.make_salad()
# std_it.make_soup()
# std_it.make_pizza()
# print(std_it.tava2)
# Std_it = obiecte definite: japonez

''' POLYMORPHISM

● Când există 2 funcții cu același nume dar au comportament diferit
Ca si exemplu de functie polimorfa, predefinita in python este functia: print
'''
# Exemple:
# 1.


# class Romania():
#     def language(self):
#         print('Romania')


# class USA():
#     def language(self):
#         print('English')
#
#
# obj_ro = Romania()
# obj_usa = USA()
# for country in (obj_ro, obj_usa):  # aici country este obiect
#     country.language()  # aici language este aceeasi metoda; in amandoua class-ele ai metoda language

# 2.
#
#
# def adunare(x, y=0, z=0):  # atribute in momentul in care apelam functia; daca toate sunt =0 atunci pot sa las ()goala
#     print(x)
#     print(y)
#     print(z)
#
#     return x + y + z
#
#
# print('Adunarea zero', adunare(2, 3))
# print('Prima adunare', adunare(4, 67, 5))  # argument in momentul in care apelex fct
# print('A doua adunare', adunare(4, 67, 5))

# 3 Exemplu de polimorphism + mostenire

# class Pasari:
#     def descriere(self):
#         print('Exista mai multe specii de pasari')
#
#     def zboara(sef):
#         print('Majoritatea pasarilor pot sa zboare')
#
#     def metoda_test(self):
#         print('Test')
#
#
# class Bufnita(Pasari):
#
#     def descriere(self):
#         print('Bufnitele sunt pasari nocturne')
#
#     def zboara(self):
#         print('Bufnitele pot zbura')
#
#     def metoda_test(self):
#         print('Altceva')
#
#
# class Pinguin(Pasari):
#     def descriere(self):
#         print('Pinguinii traiesc la polul Sud')
#
#     def zboara(self):
#         print('Pinguinii nu pot zbura')
#
# # functia aceeasi: zboara dar rezultate diferite - polimorfism
# # bufnita+pinguin - inheritance
#
#
# x_pasari = Pasari()
# x_bufnita = Bufnita()
# x_pinguin = Pinguin()
# x_pasari.descriere()
# x_pasari.zboara()
# print('')
# x_bufnita.descriere()
# x_bufnita.zboara()
# x_bufnita.metoda_test()
# print('')
# x_pinguin.descriere()
# x_pinguin.zboara()

# def metoda_test(self):
#  print('Test')

''' ABSTRACTION - 

● O clasă abstractă conține metode fără corp dar și metode cu logică definită
● O Interfață conține doar metode abstracte
● Aceste clase vor fi moștenite de clasele copil care vor trebui să scrie logica metodelor
● “Dog() class implements the Animal() Inteface”
● Clasa părinte e că o rețetă ce trebuie implementată exact așa de către toți moștenitorii
'''

#
# class Animal(ABC):
#
#     @abstractmethod  # se numeste DECORATOR si are logica definita
#     def sound(self):
#         raise NotImplementedError
#
#     @abstractmethod
#     def sleep(self):
#         raise NotImplementedError
#
#
# class Dog(Animal):
#     def sound(self):
#         print('Ham Ham')
#
#     def sleep(self):
#         print('zzzzzz')
#
#
# class Cat(Animal):
#     def sound(self):
#         print('Miau Miau')
#
#     def sleep(self):
#         print('prrrr')
#
#
# dog = Dog()
# dog.sound()
# dog.sleep()
# cat = Cat()
# cat.sound()
# cat.sleep()


# Exemplu: Ferrari


# class Car(ABC):
#     @abstractmethod  # se numeste DECORATOR si are logica definita
#     def accelereaza(self):
#         raise NotImplementedError
#
#     @classmethod
#     def stop(self):
#         print('Stop')
#
#
# class Ferrari(Car):
#     def accelereaza(self):
#         print('Atinge 100km/h in 2.8 secunde')
#
#
# class Lastun(Car):
#     def accelereaza(self):
#         print('Atinge 100km/h in 14 secunde')
#
#
# car1 = Ferrari()
# car1.accelereaza()
# car1.stop()
# car2 = Lastun()
# car2.accelereaza()
# car2.stop()


''' ENCAPSULATION
Cand ascunde atributele si folosim getter, setter, deleter
● În general, că să nu aglomerăm opțiunile utilizatorului, atributele se ascund
● În loc să vadă toate fields și methods va vedea doar metodele
● Păstrăm codul clean/curat
● Și metodele care nu se doresc a fi expuse pot fi ascunse
● Se folosește sintaxa __fieldName sau __methodName
'''

# class Car:
#     __color = 'gray'  # ascunde atributele
#
#     def get_color(self):
#         return self.__color  # folosim getter ca sa afisam culoarea
#
#     def set_color(self, culoarea_dorita):  # folosim setter ca sa setam o alta culoare
#         self.__color = culoarea_dorita
#
#     def delete_color(self):
#         self.__color = None
#
#     def __hiden(self):
#         pass
#
#
# volvo = Car()
# print(volvo.get_color())
# volvo.set_color('albastru')
# print(volvo.get_color())

''' Encapsulation (optional)

● Decoratorul @property ne ajută să folosim getter, setter, deleter într-un mod ‘Pythonic’
'''

#
# class CarPy:
#     def __init__(self, color):
#         self.__color = color
#
#     @property  # decoratorul
#     def color(self):  # color reprezinta obiectul care are in spate metodele
#         return self.__color
#
#     @color.getter
#     def color(self):
#         print(f'Getter: Culoarea este {self.__color}')
#         return self.__color
#
#     @color.setter
#     def color(self, color):
#         print(f'Setter: Noua culoare este {color}')
#
#     @color.deleter
#     def color(self):
#         print(f'Deleter: Am sters culoarea')
#         self.__color = None
#
#
# car2 = CarPy('alb')
# car2.color
# car2.color = 'galben'
# # del car2.color

'''Tema 7 - OOP _ Cei 4 Piloni

Exerciții Recomandate - grad de dificultate: Ușor
1. Revizualizează întâlnirea 7 și ia notițe în caz că ți-a scăpat ceva.
1.Git setup
'''

'''
Exerciții obligatorii - grad de dificultate: Usor spre Mediu
1. Creează-ți cont de github și încarcă într-un repo nou tot ce am facut până
acum la ore.
Curs git/github https://bit.ly/3yfFvqL
VIDEOS 1, 2 si 3
'''
'''
2. Rezolvă exercițiul după ce ai urcat proiectul (tot ce am facut până acum
împreună).
ABSTRACTION
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
probabil am colturi
'''


class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        pass

    # def descriere(self):
    #     print('Cel mai probabil am colturi.')

    # def descrie(self):
    #     print('Eu nu am colturi')


    #  INHERITANCE
    # Clasa Pătrat - moștenește FormaGeometrica
    # constructor pentru latură


class Patrat(FormaGeometrica, ABC):
    def __init__(self, latura):
        self.__latura = latura

    @property
    def latura(self):
        return self.__latura

    def descriere(self):
        print('Cel mai probabil am colturi.')


    #   ENCAPSULATION
    # latura este proprietate privată
    # Implementează getter, setter, deleter pentru latură
    # Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
    # implementezi metoda abstractă aria)

    @latura.getter
    def latura(self):
        return self.__latura

    @latura.setter
    def latura(self, value):
        print(f'latura are dimensiunea de {value}')
        self.__latura = value

    @latura.deleter
    def latura(self):
        print(f'Deleter: Am sters valoarea {self.__latura}')
        del self.__latura

    def aria(self):
        return self.latura ** 2


class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self._raza = raza

    @property
    def raza(self):
        return self._raza

    def descriere_cerc(self):
        print('Eu nu am colturi')

    @raza.getter
    def raza(self):
        return self._raza

    @raza.setter
    def raza(self, value):
        print(f'raza are dimensiunea de {value}')
        self._raza = value

    @raza.deleter
    def raza(self):
        print(f'Deleter: Am sters valoarea {self._raza}')
        del self._raza

    def aria(self):
        return self.PI * self.raza ** 2


    #   POLYMORPHISM
    # Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
    # Creează un obiect de tip Patrat și joacă-te cu metodele lui
    # Creează un obiect de tip Cerc și joacă-te cu metodele lui


patrat = Patrat(5)
print(f'Latura patratului este', int(patrat.latura))
print(f'Aria patratului este', patrat.aria())
patrat.descriere()
del patrat.latura


cerc = Cerc(7)
print(f'Raza cercului este', int(cerc.raza))
print(f'Aria cercului este', cerc.aria())
cerc.descriere_cerc()
del cerc._raza