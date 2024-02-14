import csv

with open('vacancy.csv', encoding='utf8') as file, open('space_new.txt', 'w', encoding='utf-8', newline='') as file_new:
    reader = csv.DictReader(file, delimiter = ";")
    writer_new = csv. DictWriter(file_new, ['Salary','Work_Typ','Company_Size','Role','Company'], delimiter = ";")
    writer_new.writeheader()
    for row in reader:
        n = int(row['Company'])
        m = int(row["Role"])
        t = int(row['Salary'])
        if t == max()
            file_new.append(n, m,t)


        row['salary'] = str(x) + ',' +
        if row['Company'] +[]
            print(row["Company"] + ' - ' + ['Role'] + ' - ' + ['Salary'])
        writer_new.writerow(row)


