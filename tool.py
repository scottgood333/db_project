import csv

file = open("data/RegionalHospital.csv", 'r', encoding="utf-8")

reader = csv.reader(file)

address = []

for row in reader:
    address.append(row[4])
    # print(address)
print("=========================")

district = []
for i in address:
    if i[0:2] == '臺東':
        print(i)
        district.append(i[3:6])

print(district)
print(list(set(district)))
