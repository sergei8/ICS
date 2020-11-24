""" формування заявок на устаткування по магазину
"""

from data_service import get_clients, get_orders


# структура рядка вихідних даних
zajavka = {
    
    'oborud_name'  : '',     # назва устаткування
    'client_name'  : '',     # назва клієнта
    'order_number' : '',     # номер заказа
    'kol'          : 0,      # кількість
    'price'        : 0.0,    # ціна
    'total'        : 0.0     # сума
}

clients = get_clients()
orders = get_orders()


def create_zajavka_list():  
    """ накопичує та повертає список заявок
    """
    
    def get_client_name(client_code):
        """повертає назву клієнта по його коду

        Args:
            client_code ([type]): код клієнта

        Returns:
            [type]: назва клієнта
        """
        for client in clients:
            if client_code == client[0]:
                return client[1]
            
        return "*** назва не знайдена"
     
    # накопичувач заявок
    zajavka_list = []

    for order in orders:
        
        # створити робочу копію
        zajavka_work = zajavka.copy()
        
        zajavka_work['oborud_name']     = order[2]
        zajavka_work['order_number']    = order[1]
        zajavka_work['kol']             = order[3]
        zajavka_work['price']           = order[4]
        zajavka_work['total']           = zajavka_work['kol'] * zajavka_work['price']
        zajavka_work['client_name']     = get_client_name(order[0])
        
        zajavka_list.append(zajavka_work)
        
    return zajavka_list
    