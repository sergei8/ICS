""" головний модуль задачі
- виводить розрахункову таблицю на екран та в файл
- виводить первинні данні на екран
"""

import os
from process_data import create_zajavka
from data_service import show_clients, show_orders, get_clients, get_orders

MAIN_MENU = \
"""
~~~~~~~  ОБРОБКА ЗАЯВОК НА ПРОДАЖ УСТАТКУВАННЯ ~~~~~~~

1 - вивід заявок на екран
2 - запис заявок в файл
3 - вивід списка накладних
4 - вивід списка клієнтів
0 - завершення роботи
----------------------------
"""

TITLE = "ЗАЯВКА НА ПРОДАЖ УСТАТКУВАННЯ ПО МАГАЗИНУ"

HEADER = \
"""
==========================================================================================
  Устаткування       |   Клієнт         | Номер заказа | Кількість | Ціна    |    Сума
==========================================================================================
"""

FOOTER = \
'''
==========================================================================================

'''

STOP_MESSAGE = 'Для продовження натисніть <Enter>'

def show_zajavka(zajavka_list):
    """виводиить таблицю заявок 

    Args:
        zajavka_list ([type]): список заявок
    """
    print(f"\n\n{TITLE:^91}")
    print(HEADER)

    for zajavka in zajavka_list:
        print(f"{zajavka['oborud_name']:20}",
              f"{zajavka['client_name']:20}",
              f"{zajavka['order_number']:^16}",
              f"{zajavka['kol']:>6}",
              f"{zajavka['price']:>11.2f}",
              f"{zajavka['total']:>11.2f}"
              )

    print(FOOTER)

def write_zajavka(zajavka_list):
    """записує список заявок у текстовий файл

    Args:
        zajavka_list ([type]): список заявок
    """

    with open('./data/zajavka.txt', 'w') as zajavka_file:
        for zajavka in zajavka_list:
            line = \
               zajavka['oborud_name'] + ';' +       \
               zajavka['client_name'] + ';' +       \
               zajavka['order_number'] + ';' +      \
               str(zajavka['kol']) + ';' +          \
               str(zajavka['price']) + ';' +        \
               str(zajavka['total'])  + '\n' 
               
            zajavka_file.write(line)  
            
    print('Файл успішно записано ...')             
                   

while True:
    
    # вивід головного меню
    os.system('clear')   
    print(MAIN_MENU)
    command_number = input("Введіть номер команди: ")
    
    # обробка команд користувача
    if command_number == '0':
        print('\nПрограма завершила роботу')
        exit(0)
        
    elif command_number == '1':
        zajavka_list = create_zajavka()
        show_zajavka(zajavka_list)
        input(STOP_MESSAGE)
        
    elif command_number == '2':
        zajavka_list = create_zajavka()
        write_zajavka(zajavka_list)
        input(STOP_MESSAGE)
        
    elif command_number == '3':
        orders = get_orders()
        show_orders(orders)
        input(STOP_MESSAGE)
        
    elif command_number == '4':
        clients = get_clients()
        show_clients(clients)
        input(STOP_MESSAGE)

        
    
    
    