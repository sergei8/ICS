"""модуль для роботи з файлами первинних даних
- зчитування та вивід на екран
"""


def get_clients():
    """ повертає список клієнтів який отримує ззовні

    Returns:
        client_list: список клієнтів 
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

    # накопічувач клієнтів
    clients_list = []

    for line in from_file:
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
