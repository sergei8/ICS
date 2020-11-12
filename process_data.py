""" розрахунок заявок на товари по магазину
"""
from data_service import get_clients, get_orders


# словник в якому будуть накоплюватись результати розрахунків
zajavka = {
    'oborud' : "",     # назва устаткування
    'client' : "",     # назва клієнта
    'zakaz'  : "",     # номер заказа
    'kol'    : 0,      # кількість товару
    'price'  : 0.0,    # ціна
    'total'  : 0.0     # сума
}


print(get_orders())
print(get_clients())