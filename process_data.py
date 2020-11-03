"""модуль розрахунку вихідних даних у вигляді словника
"""

from data_service import get_clients 
from data_service import get_orders

# структура запису вихідних даних
request_blank = {
    "tovar_name": '',         # назва товара (order.txt)
    "client_name": '',        # назва клієнта (client.txt)
    "order_number": '',       # номер накладної (order.txt)
    "qty": 0,                 # кількість (order.txt)
    "price": 0.0,             # ціна (order.txt)
    "total": 0.0              # сума (розрахункове)
}


def get_client_name_by_code(client_code):
    """повертає з масива клієнтів ім'я клієнта по його коду 
    або "*** not found" якщо не знайдено

    Args:
        client_code (str): код клієнта

    Returns:
        [str]: ім'я клієнта
    """

    for client in clients:
        if client_code == client[0]:
            return client[1]

    return "*** not found"

def process():
    """проходить по всім рядкам `orders` та формує розрахункові рядки `request`
    та накопичує їх в масиві requests_list

    Returns:
        list: спсисок виходних рядків
    """
    
    # накопичувач розрахункових даних
    requests_list = []

    for order in orders:
        
        # створити незалежний об'єкт `request` по зразку
        request = request_blank.copy()

        request["tovar_name"]   = order[2]
        request["client_name"]  = get_client_name_by_code(order[0])
        request["order_number"] = order[1]
        request["qty"]          = order[3]
        request["price"]        = order[4]
        request["total"]        = request["qty"] * request["price"]

        # накопичити вихідний рядок
        requests_list.append(request)

    return requests_list


if __name__ == "__main__":
    
    # отримати вхідні дані
    orders = get_orders()
    clients = get_clients()

    requests = process()
    
    import os
    os.system('clear')
    for r in requests:
        print("{} {} {} {} \n".format(**r))
