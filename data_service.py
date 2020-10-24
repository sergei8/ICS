"""модуль для роботи з файлами первинних даних
- зчитування та вивід на екран
"""

"""модуль зчитує первинні файли для обробки
"""

def get_clients():
    """повертає список клієнтів

    Returns:
        clients_list: список клієнтів
    """

    from_file = [
        "35;ЕЛЕКС МАРКЕТИНГ;пр.Перемоги 11",
        "39;ПРАГМА;вул.Кіото 19",
        "44;ЕКСИМЕР;пр.Бандери 42",
        "45;ТЕМП;вул.Глибочицька 3",
        "47;КАМІ;вул.В.Вал 18",
        "50;ЛАНИТ;вул.Хрещатик 13",
        "54;ХІТОН;пр.ак.Глушкова 16",
        "67;ЕЛЬДОРАДО;вул.Васильківська 5"
        ]

    clients_list = []
    for line in from_file:
        line_list = line.split(';')
        clients_list.append(line_list)


    return clients_list


def get_orders():
    """повертає список накладних

    Returns:
        from_file: список накладних
    """


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

    
    # розбити строку на реквізити та перетворити формати (при потребі)
    orders_list = []    # список-накопичувач
    for line in from_file:
        line_list = line.split(';')
        line_list[3] = int(line_list[3])
        line_list[4] = int(line_list[4])
        orders_list.append(line_list)

    return orders_list


def show_clients(clients):
    """виводить список клієнтів по заданому інтервалу кодів

    Args:
        clients (list): список клієнтів
    """

    client_code_from = input("З якого кода клієнта? ")
    client_code_to   = input("По який кода клієнта? ")

    for client in clients:
        if client_code_from <= client[0] <= client_code_to:
            print ("код: {:5} назва: {:15} адреса: {:25}".format(*client)) 


clients = get_clients()
show_clients(clients)

# print("---------------------")

# orders = get_orders()
# for order in orders:
#     print(order)

