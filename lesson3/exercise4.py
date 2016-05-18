# Level 2
# forth exercise

import csv

data = []


def substitution(file, param):
    reader = csv.DictReader(file)

    for row in reader:
        try:
            if row[param] == 'critical':
                row[param] = 'high'
                data.append(row)
            elif row[param] == 'high':
                row[param] = 'medium'
                data.append(row)
            elif row[param] == 'medium':
                row[param] = 'low'
                data.append(row)
        except IndexError as e:
            print(e)
            pass


def rewrite(input_file, output_file):

    with open(input_file, 'r') as the_file:
        substitution(the_file, 'Priority')

        with open(output_file, 'w') as to_file:
            header = ['#', 'Description', 'Environment', 'Priority', 'Owner', 'Created At']
            writer = csv.DictWriter(to_file, fieldnames=header)

            writer.writeheader()
            writer.writerows(data)


def rows_amount(filename):
    with open(filename) as f:
        for i, line in enumerate(f, 1):
            pass
    print(i)

rewrite('Python for QA - bugs list - Sheet1.csv', 'new.csv')

rows_amount('new.csv')
rows_amount('Python for QA - bugs list - Sheet1.csv')

