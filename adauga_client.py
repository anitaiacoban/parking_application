file_path = "files/clients.txt"


def verifica_client_id_unic(file_path, client_id):
    """
    Verifica daca client id-ul introdus este unic sau nu.
    :param file_path: cale fisier clients.txt
    :param client_id: id-ul unic al fiecarui client
    :return: True or False
    """
    with open(file_path, "r") as file:
        for line in file:
            date_clienti = line.strip().split(",")
            id_existent = date_clienti[0]
            if str(client_id) == id_existent.strip():
                return False
    return True


def adauga_client(client_id, prenume, nume, telefon, oras, paria=False):
    """
    Adauga un client nou in fisierul clients.txt
    :param client_id: id-ul unic al fiecarui client
    :param prenume: prenumele clientului
    :param : nume: numele clientului
    :param : telefon: nr de telefon al clientului
    :param : oras: orasul clientului
    :param : paria: daca e sau nu paria
    :return: True or False
    """
    if verifica_client_id_unic(file_path, client_id):
        with open(file_path, "a") as file:
            client_nou = str(client_id) + ", " + prenume + ", " + nume + ", " + str(
                telefon) + ", " + oras + ", " + str(paria)
            file.write(client_nou.strip() + "\n")
        return True
    else:
        print("Nu s-a adaugat un client nou. Client id-ul introdus nu este unic.")
        return False