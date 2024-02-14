import csv
spis = []
with open('vacancy.csv', encoding = 'UTF8') as file:
    reader = csv.DictReader(file, delimiter = ";")
    for row in reader:
        spis.append(row['Company_Size'])
N = len(spis)
i = 0
while i < N - 1:
    m = i
    j = i + 1
    while j < N:
        if spis[j]  < spis[m]:
            m = j
        j += 1
        spis[i], spis[m] = spis[m], spis[i]
        i += 1
for i in range(10):
    print(spis[i])

