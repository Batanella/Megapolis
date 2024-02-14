import csv
import string
import random


def take_init(s: string) -> str:
    """
    Функция позволяет добыть инициалы из ScientistName - полностью фамилию и первую букву из имени и отчества
    :param s: берётся фамилия, имя и отчество из файла, определяет по столбцу ScientistName
    :return: полностью фамилия и первую букву из имени и отчества
    """
    ScientistName = s.split()
    return f'{ScientistName[0]}_{ScientistName[1][0]}{ScientistName[2][0]}'


def gen_password() -> str:
    """
    Функция генерирует пароль из алфавита, который состоит из английского алфавита(26 строчных и 26 заглавных) и десятичные цифры
    :return: пароль
    """
    alphabet = string.ascii_letters + string.digits
    password = ''.join(random.choice(alphabet) for _ in range(10))
    return password


scientist_password = []
with open('scientist.txt', encoding='utf8') as file:
    reader = list(csv.DictReader(file, delimiter="#", quotechar="'"))
    for row in reader:
        row['login'] = take_init(row['ScientistName'])
        row['password'] = gen_password()
        scientist_password.append(row)

with open('scientist_password.csv', 'w', encoding='utf8', newline='') as file:
    w = csv.DictWriter(file, ['ScientistName', 'preparation', 'date', 'components', 'login', 'password'], delimiter="#")
    w.writeheader()
    w.writerows(scientist_password)
