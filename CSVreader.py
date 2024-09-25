
import csv

# with open('names.csv', 'r') as csv_file, open('new_names.csv', 'w') as new_file:
#     csv_reader = csv.reader(csv_file)
#     csv_writer = csv.writer(new_file, delimiter='-')
    
#     for row in csv_reader:
#         csv_writer.writerow(row)


with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        print(line)
        print(line['email'])