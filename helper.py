from datetime import date


def suma(a, b):
    return a + b


def print_hi(nume):
    print(f'Hi{nume}')


class Scoala:
    profil_real = 'mate_info'
    profil_uman = 'romana_engleza'
    profil_stiintele_naturii = 'bio_chimie'
    nr_elevi = 1000
    tip = 'Liceu teoretic'

    def __init__(self, tip, profil_real):
        self.tip = tip
        self.profil_real = profil_real

    def inscriere(self):
        print(f'Te-ai inscris la profilul{self.profil_real}')


class Cerc:
    raza = 5
    culoare = 'rosu'
    # aria = 3.14 * raza ** 2
    # diametru = 2 * raza
    # lungime = 2 * 3.14 * raza

    def __init__(self, culoare, raza):
        self.raza = raza
        self.culoare = culoare

    def descriere_cerc(self):
        print(f'Cercul are culoarea {self.culoare} si raza {self.raza}')

    def aria_cerc(self):
        return 3.14 * (self.raza ** 2)

    def diametru_cerc(self):
        return self.raza * 2

    def lungime_cerc(self):
        return 2 * 3.14 * self.raza

    def cerc_definit(self):
        print('Acesta este cercul definit')


class Dreptunghi:
    lungime = 5
    latime = 3
    culoare = 'orange'

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descriere_dreptunghi(self):
        print(f'Dreptunghiul are lungimea de: ', 5, 'latime de:', 3, 'si culoarea: ', self.culoare)

    def aria_dreptunghi(self):
        return self.lungime * self.latime

    def perimetrul_dreptunghi(self):
        return 2 * self.lungime + 2 * self.latime

    def schimba_culoarea(self, alta_culoare):
        self.culoare = alta_culoare


class Angajat:
    nume = 'nume'
    prenume = 'prenume'
    salariu = 5000

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descriere_Angajat(self):
        print(f'Angajatul:', self.nume, self.prenume, 'are salariul de:', 5000)

    def nume_complet(self):
        return self.nume + self.prenume

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        return self.salariu * 12

    def marire_salariu(self):
        return self.salariu + self.salariu * 5 / 100

class ContBancar:
    # iban = 'iban'
    # titular_cont = 'titular_cont'
    # sold = 1500
    # suma = 500

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = int(sold)

    def afisare_sold(self):
        print(f'Titularul: {self.titular_cont} are in contul {self.iban} suma de {self.sold}')

    def debitare_cont(self, suma):
        if int(suma) > self.sold:
            print(f'Fonduri insuficiente in contul {self.iban}')
        else:
            self.sold -= int(suma)
            print(f'S-a debitat suma de {int(suma)} lei din contul {self.iban} Soldul curent este {self.sold} lei.')
            return self.sold

    def creditare_cont(self, suma):
        self.sold += int(suma)
        print(f'S-a creditat suma de {int(suma)}lei in contul {self.iban} Soldul curent este {self.sold} lei.')


class TableIt:
    @classmethod
    def printTable(cls, factura_mea, useFieldNames):
        pass

#
# class Factura:
#     today = date.today().strftime('%d/%m/%y')
#     serie = "F2023"  # serie constanta
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
#     def schimba_nume_produs(self, nume):
#         self.nume_produs = nume
#         print(f'Noul nume al produsului este {nume}')
#
#     def genereaza_factura(self):
#         factura = Factura
#         print(f'FACTURA: {factura.serie} \nNumar: {self.numar}')
#         print(f'Data: {factura.today}')
#         factura_emisa = [
#             ['Produs', 'Cantitate', 'Pret Bucata', 'Total'],
#             [self.nume_produs, self.cantitate, self.pret_buc, self.cantitate * self.pret_buc],
#         ]
#         TableIt.printTable(factura_emisa, useFieldNames=True)

        # print(f'Data: {factura.today}')
        # total = self.cantitate * self.pret_buc

        # print(f'FACTURA {Factura.serie} - {self.numar}')
        # print(f"Produs: {self.nume_produs}")
        # print(f"Cantitate: {self.cantitate}")
        # print(f"Pret/buc: {self.pret_buc}")
        # print(f"Total: {total}")