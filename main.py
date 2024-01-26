from adauga_client import adauga_client
from afisare_clienti import afisare_clienti
from evidenta import afisare_clienti_care_au_depasit, raport


if __name__ == "__main__":
    while True:
        print("----Parking Application----\n")
        print("1. Afisare clienti existenti")
        print("2. Adauga client")
        print("3. Afisare clienti care au depasit 2h de la ultima parcare")
        print("4. Afiseaza si verifica daca clientii au depasit 3 zile")
        print("5. Raport clienti care au atributul paria pe False")
        print("0. Iesire")

        optiune = input("Introdu optiune: ")

        if optiune == '1':
            print("Clientii sunt: \n")
            afisare_clienti(lista_clienti_id_depasit=[])
        elif optiune == '2':
            print("Adauga detaliile clientului. \n")
            client_id = input("Client id: \n")
            prenume = input("Prenume: \n")
            nume = input("Nume: \n")
            telefon = input("Nr telefon: \n")
            oras = input("Oras: \n")
            adauga_client(client_id, prenume, nume, telefon, oras, False)
        elif optiune == '3':
            afisare_clienti_care_au_depasit(perioada="2 ore")
        elif optiune == '4':
            afisare_clienti_care_au_depasit(perioada="3 zile")
        elif optiune == '5':
            raport()
        elif optiune == '0':
            print("Iesire din aplicatie.")
            break
        else:
            print("Te rog sa incerci din nou.")