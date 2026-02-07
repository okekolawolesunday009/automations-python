# with open('data.csv', 'r') as file:
#     content = file.read()
#     print(content)

with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)