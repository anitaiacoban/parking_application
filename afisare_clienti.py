file_path = "files/clients.txt"


def afisare_clienti(lista_clienti_id_depasit):
    """
    Afiseaza doar anumiti cienti din fisierul clients.txt daca avem valori in lista lista_clienti_id_depasit sau toti
    clientii din fisier daca nu exista valori in lista.
    :param lista_clienti_id_depasit: lista cu clientii care au depasit un anumit interval de timp
    :return: Continutul fisierului clients.txt pentru toti sau anumiti clienti
    """
    with open(file_path, 'r') as file:
        if lista_clienti_id_depasit:
            for line in file:
                date_clienti = line.strip().split(",")
                client_id = date_clienti[0]
                if str(client_id) in lista_clienti_id_depasit:
                    print(line.strip())
        else:
            print(file.read())