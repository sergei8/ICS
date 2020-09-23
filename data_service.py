# Модуль роботи з вхідними даними:
# містить функції роботи (читання-вивід) з:
# довідника ....
# файла оперативної інформ.
# -------------------------------------

enterprises = [
    "1010; Універмаг;  1704",
    "1020; Дружба ЛТД; 972",
    "1030; Радунь;     500"
    ]


indicators = [

]


def get_clients():
    enterprises_list = []
    for enterprise in enterprises:
        enterprises_list.append(enterprise.split(";"))

    print(enterprises_list)
    pass
 


# get_clients()