from abc import abstractmethod, ABC
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


class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self._latura = latura

    @property
    def latura(self):
        return self._latura

    def descriere(self):
        print('Cel mai probabil am colturi.')


    #   ENCAPSULATION
    # latura este proprietate privată
    # Implementează getter, setter, deleter pentru latură
    # Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
    # implementezi metoda abstractă aria)

    @latura.getter
    def latura(self):
        return self._latura

    @latura.setter
    def latura(self, value):
        print(f'latura are dimensiunea de {value}')
        self._latura = value

    @latura.deleter
    def latura(self):
        print(f'Deleter: Am sters valoarea {self._latura}')
        del self._latura

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

cerc = Cerc(7)
print(f'Raza cercului este', int(cerc.raza))
print(f'Aria cercului este', cerc.aria())
cerc.descriere_cerc()
