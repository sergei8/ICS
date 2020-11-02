"""модуль зчитує первинні файли для обробки
"""

def get_clients():
    """повертає список клієнтів з файла 'clients.txt` та фороматує значення

    Returns:
        clients_list: список клієнтів
    """

    with open("./data/clients.txt") as clients_file:
        from_file = clients_file.readlines() 

    # накопичувач клієнтів
    clients_list = []

    # блок виділяє окремі реквізити з кожного рядка
    for line in from_file:
        line = line[:-2]
        line_list = line.split(';')
        clients_list.append(line_list)

    return clients_list

def get_orders():
    """повертає список накладних з файла 'orders.txt`

    Returns:
        from_file: список накладних
    """

    with open("./data/orders.txt") as orders_file:
        from_file = orders_file.readlines() 

    # список-накопичувач
    orders_list = []    
    
    # розбити строку на реквізити та перетворити формати (при потребі)
    for line in from_file:
        line_list = line.split(';')
        line_list[3] = int(line_list[3])
        line_list[4] = int(line_list[4])
        orders_list.append(line_list)

    return orders_list

def show_clients(clients):
    """ виводить список клітєнтів за деякою умовою

    Args:
        clients ([list]): список клітєнтів
    """

    client_code_from = input("З якого коду клієнта? ")
    client_code_to   = input("По який код клієнта? ")
    
    kol_lines = 0

    for client in clients:
        if  client_code_from  <= client[0] <= client_code_to:
            print("код: {:4} назва: {:16} адреса: {:20}".format(client[0], client[1], client[2]))
            kol_lines = kol_lines + 1

    if kol_lines == 0:
        print("Записів з кодом {} не знайдено".format(client_code_from))

def show_orders(orders):
    """ виводить список накладних за деякою умовою

    Args:
        orders ([list]): список накладних
    """
    
    for order in orders:
        print("код: {:4} номер: {:4} товар: {:20} кільк: {:2} ціна: {:6}"
          .format(order[0], order[1], order[2], order[3], order[4]))


# clients = get_clients()
# show_clients(clients)

orders = get_orders()
show_orders(orders)


