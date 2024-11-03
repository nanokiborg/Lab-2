from csv import reader

while True:
    flag = 0
    search = input('Введите запрос: ')
    if search == '0':
        break
    with open('books.csv', 'r', encoding='windows-1251') as csvfile:
        table = reader(csvfile, delimiter=';')
        for row in table:
            lower_case = row[3].lower()
            index = lower_case.find(search.lower())
            if index != -1 and (row[6][6:][:4] == '2015' or row[6][6:][:4] == '2018'):
                print(f'{row[1]} | {row[3]}')
                flag += 1
                
        if flag == 0:
            print('Ничего не найдено.')
        else:
            print(f'Найдено {flag} результатов.')

