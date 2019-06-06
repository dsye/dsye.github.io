import csv
with open ('ripper.csv', 'r') as csvfile:
## step 2: prints out first row of csvfile
    our_reader = csv.reader(csvfile)
    rows = [row for row in our_reader]
#
# print(rows[0])
## step 3: stored report texts as new variable
#     all_texts = [row [4] for row in our_reader]
# print(all_texts)
# # step 4: find earliest publish date
#     dates = [row[3] for row in our_reader]
# print(min(dates))

# step 5: write a new CSV with same texts data but in lowercase
for row in rows:
    row[4] = row[4].lower()
with open ('ripper2.csv', 'w', newline= '') as fout:
    csvwriter=csv.writer(fout)
    for row in rows:
        csvwriter.writerow(row)
