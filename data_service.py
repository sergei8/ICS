""" модуль для отримання даних про постачання та вивід їх на екран
"""


def get_clients():
    """ повертає вміст файла 'clients.txt` у вигляді списка

    Returns:
        'from_file' - список рядків файла
    """

    with open('./data/clients.txt') as clients_file:
        from_file = clients_file.readlines()

    # накопичувач клієнтів
    clients_list = []

    for line in from_file:
        line_list = line.split(';')
        line_list[2] = line_list[2][:-1]  # вилучити `\n` в кінці
        clients_list.append((line_list))

    return clients_list

def get_orders():

        from_file = [
        "35;202;ARTLINE Gaming X51 ;2;5200",
        "39;203;Everest Home 4070 ;1;12000",
        "44;205;Asus ROG Strix;2;17000",
        "45;207;MacBook Pro 15”;2;30000",
        "47;211;Everest Home 4070 ;1;12000",
        "50;204;MacBook Pro 15”;1;30000",
        "54;206;Asus ROG Strix;2;17000",
        "67;212;MacBook Pro 13”;2;26000"
    ]

def show_clients(clients):
    """виводить список клієнтів

    Args:
        clients (list): список клієнтів
    """

    # задати інтервал виводу
    client_code_from = input("З якого кода клієнта? ")
    client_code_to   = input("По який код клієнта? ")
    
    # накопичує кількість виведених рядків
    kol_lines = 0

    for client in clients:
        if  client_code_from  <= client[0] <= client_code_to:
            print("код: {:3} назва: {:16} адреса: {:20}".format(client[0], client[1], client[2]))
            kol_lines += 1

    # перевірити чи був вивід хоча б одного рядка
    if kol_lines == 0:
        print("По вашому запиту клієнтів не знайдено!")
    

clients = get_clients()
show_clients(clients)
