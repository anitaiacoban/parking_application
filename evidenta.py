file_path = "files/db.txt"
clienti_file_path = "files/clients.txt"
raport_file_path = "files/raport.txt"

from afisare_clienti import afisare_clienti
from schimba_paria import schimba_paria


def afisare_clienti_care_au_depasit(perioada):
    """
    Returneaza clientii care au depasit o anumite periaoda.
    :param perioada: este un string care poate sa fie "2 ore" sau "3 zile"
    :return:
    """
    lista_clienti_id_depasit = []

    with open(file_path, 'r') as file:
        for line in file:
            date_timp = line.strip().split(",")
            client_id = date_timp[0]
            timp_intrare = int(date_timp[1])
            timp_iesire = int(date_timp[2])
            diferenta = timp_iesire - timp_intrare
            nr_de_secunde_per_zi = 24 * 60 * 60
            diferenta_in_ore = int(diferenta / 3600)
            diferenta_in_zile = int(diferenta / nr_de_secunde_per_zi)

            if perioada == "2 ore":
                if diferenta_in_ore >= 2:
                    lista_clienti_id_depasit.append(client_id)
            elif perioada == "3 zile":
                if diferenta_in_zile >= 3:
                    lista_clienti_id_depasit.append(client_id)

    if perioada == "2 ore" and lista_clienti_id_depasit:
        print("Clientii sunt: ")
        afisare_clienti(lista_clienti_id_depasit)
    elif perioada == "3 zile" and lista_clienti_id_depasit:
        schimba_paria(lista_clienti_id_depasit)
        afisare_clienti(lista_clienti_id_depasit)
    else:
        print("Nu sunt clienti.")


def afisare_raport():
    """
    Afiseaza ce se afla in fisierul raport.txt
    :return: Continutul fisierului raport.txt
    """
    with open(raport_file_path, 'r') as file:
        print("Raportul este: " + "\n")
        print(file.read())

def raport():
    """
    Creeaza un raport cu toti clientii care au setat paria pe False. Acest raport combina toate detaliile clientilor din fisierle clients.txt si db.txt
    :return:
    """
    clienti_id = []
    detalii_clienti = {}
    with open(clienti_file_path, 'r') as file:
        for line in file:
            date_clienti = line.strip().split(",")
            client_id = date_clienti[0]
            paria = date_clienti[5]
            if paria.strip() == 'False':
                clienti_id.append(client_id)
                detalii_clienti[client_id] = date_clienti

    detalii_timpi_parcare_clienti = {}
    with open(file_path, 'r') as file:
        for line in file:
            date_clienti = line.strip().split(",")
            client_id = date_clienti[0]
            if client_id in clienti_id:
                detalii_timpi_parcare_clienti[client_id] = date_clienti

    with open(raport_file_path, 'w') as file:
        for client_id in detalii_clienti:
            if client_id in detalii_timpi_parcare_clienti:
                clienti = detalii_clienti[client_id]

                for i in range(1, len(detalii_timpi_parcare_clienti[client_id])):
                    clienti.append(detalii_timpi_parcare_clienti[client_id][i])

                file.write(','.join(clienti) + '\n')

    afisare_raport()