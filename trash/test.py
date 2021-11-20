import csv
import datetime



with open("data/record.csv") as g:
    reader = csv.reader(g)
    l = [row for row in reader]
    # print(int(l[0][0]) + 1)
    day = list(l[0][3])
    today = datetime.date.today()
    day.append(str(today))
    print(day)