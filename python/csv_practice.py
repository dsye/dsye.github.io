import csv
# with open('csvs/basic.csv', 'r') as csvfile:
#     our_reader = csv.reader(csvfile)
#     names = [row for row in our_reader]
# print(names)
# print(names[1])
# print(names [1][2])
# print(len(names))
#find length of each first names
# for row in names:
#    print(len(row[2]))

#find the longest first name
# longest = ""
# for row in names:
#     if len(row[2]) > len(longest):
#         longest = row[2]
# # print(longest)
# # construct a new list consisting of only the first names we have here
# first_names = [row[2] for row in names]
# first_names.reverse()
# # print(first_names)
# new_row = [2, 'wayne', 'graham', 'meh']
# names.append(new_row)
# #print(names)
# a_row = [3, 'fox', 'eliza', 'SO COOL']
# names.append(a_row)
# # print(names)
# with open('csvs/practice.csv', 'w', newline= '') as fout:
#     csvwriter = csv.writer(fout)
#     for i in range(0,100,10):
#         csvwriter.writerow([i, i + 5, i + 10, i + 15, i + 20, i +25, i +30])
# with open('csvs/practice.csv', 'r') as fin:
#     our_reader = csv.reader(fin)
#     data = [row for row in our_reader]
# # print(data)
# data[3][5] = 'Ethan'
# data[5][4] = 'Brandon'
# data[2][6] = 'Tony the Cat'
#
# with open('csvs/practice.csv', 'w', newline='') as fout:
#     csvwriter = csv.writer(fout)
#     for row in data:
#         csvwriter.writerow(row)
# data

groceries = []
with open('csvs/shopping.csv','r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader: groceries.append(row)

# print(groceries)
# print(groceries[2]['name'])
for item in groceries:
    print(item['name'])
tony = {'name': 'tony', 'nutritious': 'false', 'id': '5'}
groceries.append(tony)
with open('csvs/updated_groceries.csv', 'w', newline='') as fout:
    column_names = ['id', 'name', 'nutritious']
    dictwriter = csv.DictWriter(fout, fieldnames=column_names)
    dictwriter.writeheader()
    for row in groceries:
        dictwriter.writerow(row)
