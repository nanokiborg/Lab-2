from csv import reader

while True:
    flag = 0
    with open('books.csv', 'r', encoding='windows-1251') as csvfile:
        table = reader(csvfile, delimiter=';')
        for row in table:
            lower_case = row[1].lower()
            if len(lower_case) >= 30:
                flag += 1

        print(f'Найдено {flag} книг')
    break

