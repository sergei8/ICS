"""модуль зчитує первинні файли для обробки
"""

def get_clients():
    """повертає список клієнтів та фороматує значення

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

    # накопичувач клієнтів
    clients_list = []

    # блок виділяє окремі реквізити з кожного рядка
    for line in from_file:
        line_list = line.split(';')
        clients_list.append(line_list)

    return clients_list


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


clients = get_clients()
show_clients(clients)


