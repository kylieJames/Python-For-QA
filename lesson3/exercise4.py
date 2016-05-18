# Level 2
# forth exercise

import csv


data = []
with open('Python for QA - bugs list - Sheet1.csv', 'r') as the_file:
    reader = csv.DictReader(the_file)
    for row in reader:
        try:
            if row['Priority'] == 'critical':
                row['Priority'] = 'high'
                data.append(row)
            elif row['Priority'] == 'high':
                row['Priority'] = 'medium'
                data.append(row)
            elif row['Priority'] == 'medium':
                row['Priority'] = 'low'
                data.append(row)
        except IndexError as e:
            print(e)
            pass

    with open('new.csv', 'w') as to_file:
        header = ['#', 'Description', 'Environment', 'Priority', 'Owner', 'Created At']
        writer = csv.DictWriter(to_file, fieldnames=header)

        writer.writeheader()
        writer.writerows(data)


def rows_amount(filename):
    with open(filename) as f:
        for i, line in enumerate(f, 1):
            pass
    print(i)

rows_amount('new.csv')
rows_amount('Python for QA - bugs list - Sheet1.csv')

