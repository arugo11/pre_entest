import csv


with open("record.csv" , "w") as f:
    for i in range (1 , 1901):
        writer = csv.writer(f)
        writer.writerow([i])


