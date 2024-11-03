from csv import reader


output = open('result.txt', 'w')

while True:
    flag = 0
    
    with open('books.csv', 'r', encoding='windows-1251') as csvfile:
        table = reader(csvfile, delimiter=';')
        for row in table:
            output.write(f'{row[3]}. {row[1][1:]} - {row[6][6:][:4]}\n')
            flag += 1
            if flag == 20:
                print("Done")
                break
    if flag == 20:
        break

output.close()