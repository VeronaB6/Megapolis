import csv
write_user = ''
while write_user != 'None':
    with open('vacancy.csv', encoding = 'UTF8') as file:
        reader = csv.DictReader(file)
        write_user = input()
        flag = True
        for row in reader:
            if write_user == row['Company']:
                flag = False
                print("В" + row['Company'] + "найдена вакансия: " + ['Role'] + ". З/п составит: " + ["Salary"])
        if flag:
            print("К сожалению, ничего не удалось найти")
        file.closed