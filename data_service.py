"""модуль для роботи з файлами первинних даних
- зчитування та вивід на екран
"""


def get_clients():
    """ повертає список клієнтів який отримує з файлу 'clients.txt`

    Returns:
        client_list: список клієнтів 
    """    

    with open("./data/clients.txt") as clients_file:
        from_file = clients_file.readlines()

    # накопічувач клієнтів
    clients_list = []

    for line in from_file:
        
        # відрізати '\n' в кінці рядка
        line = line[:-2]
        
        line_list = line.split(';')
        clients_list.append(line_list)
    
    return clients_list

def show_clients(clients):
    """виводить на екран список клієнтів заданого діапазона

    Args:
        clients ([list]): список клієнтів
    """

    client_code_from = input("З якого кода? ")
    client_code_to   = input("По який код? ") 

    kol_lines = 0

    for client in clients:
        if  client_code_from <= client[0] <= client_code_to:
            print("код: {:4} назва: {:17} адреса: {:20}".format(client[0], client[1], client[2]))
            kol_lines += 1

    if kol_lines == 0:
        print("Код не знайден")

clients = get_clients()
show_clients(clients)
