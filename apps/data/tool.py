import csv

file = open("./RegionalHospital.csv", 'r', encoding="utf-8")

reader = csv.reader(file)

address = []
department = []

for row in reader:
    address.append(row[4])
    department.append(row[8])
    # print(address)
print("=========================")

district = []
for index, context in enumerate(address):
    if context[0:2] == '新北':
        print(context)
        district.append(context[3:6])
        print(department[index].split(','))

print(district)
print(list(set(district)))
