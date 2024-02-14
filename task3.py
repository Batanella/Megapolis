import csv

with open('scientist.txt', encoding='utf8') as file:
    reader = csv.DictReader(file, delimiter="#", quotechar="'")
    data = sorted(reader, key=lambda x: x['date'])

da_ta = input()
while da_ta != 'эксперимент':
    dd, mm, yyyy = da_ta.split('.')
    check_data = str(f'{yyyy}-{mm}-{dd}')
    for el in data:
        if el['date'] == check_data:
            lastname, name, patronymic = el['ScientistName'].split()
            print(f'Ученый {lastname} {name[0]}.{patronymic[0]}. создал препарат: {el['preparation']} - {el['date']}')
            break
    else:
        print('В этот день ученые отдыхали')
    da_ta = input()
