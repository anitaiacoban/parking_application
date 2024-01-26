file_path = "files/clients.txt"


def schimba_paria(lista_clienti_id_depasit):
    """
    Schimba valoarea atributului 'paria' din fisierul clients.txt in True pentru clientii care se gasesc in lista_clienti_id_depasit
    :param lista_clienti_id_depasit: o lista ce contine client_id clientilor care au depasit o anumite perioada
    :return:
    """
    linii_modificate = []

    with open(file_path, "r") as file:
        for line in file:
            date_clienti = line.strip().split(",")
            client_id = date_clienti[0]
            if client_id in lista_clienti_id_depasit:
                date_clienti[5] = "True"
                linie_modificata = ",".join(date_clienti)
                linii_modificate.append(linie_modificata + "\n")
            else:
                linii_modificate.append(line)

    with open(file_path, "w") as file:
        file.writelines(linii_modificate)