"""головний модуль додатку
виводить розрахункову таблицю
"""

from process_data import create_zajavka
from data_service import show_clients, show_orders
import os

MAIN_MENU = \
"""
~~~~~~~~~ ОБРОБКА ЗЯВОК НА ПРОДАЖ УСТАТКУВАННЯ ~~~~~~~~~~

1 - вивід заявок на екран
2 - запис заявок в файл
3 - вивід списка накладних
4 - вивід довідника клієнтів
0 - завершити роботу
-----------------------------
"""

TITLE = "ЗАЯВКИ НА ПРОДАЖ УСТАТКУВАННЯ ПО МАГАЗИНУ"
HEADER = \
'''
==========================================================================================
| Устаткування      |   Клієнт           |  Номер заказа  | Кількість |   Ціна   |  Сума |
==========================================================================================
'''
FOOTER = \
'''
==========================================================================================
'''

STOP_MESSAGE = "Нажміть будь-яку клавішу для продовження"

def show_zajavka(zajavka_list):
    """виводить сформовані заявки на екран у вигляді таблиці

    Args:
        zajavka_list ([type]): список заявок
    """
    
    print(f'\n\n{TITLE:^90}')
    print(HEADER)
    
    for zajavka in zajavka_list:
        print(f"{zajavka['oborud']:20}",
              f"{zajavka['client']:20}",
              f"{zajavka['zakaz']:^15}",
              f"{zajavka['kol']:>12}"
              f"{zajavka['price']:>10.2f}"
              f"{zajavka['total']:>11.2f}"
              )
    
    print(FOOTER)


def write_zajavka(zajavka_list):
    """пише список заявок у файл

    Args:
        zajavka_list ([type]): список заявок
    """
    
    with open('.\data\zajavki.txt', "w") as zajavka_file:
        for zajavka in zajavka_list:
            line = ','.join(list(zajavka.values()))
            zajavka_file.write(line)
    
    


while True:
    os.system('clear')
    print (MAIN_MENU)
    func_nomer = input('Введіть номер функції: ')

    if func_nomer == '0':
        print("\nПрограма завершила роботу")
        exit(0)
    elif func_nomer == '1':
        zajavka_list = create_zajavka()
        show_zajavka(zajavka_list)
        input(STOP_MESSAGE)
    elif func_nomer == '2':
        zajavka_list = create_zajavka()
        write_zajavka(zajavka_list)
        input(STOP_MESSAGE)

    
    
    
