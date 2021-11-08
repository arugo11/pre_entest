import csv

with open("data/record.csv" , "w") as f:
    for i in range (1 , 1901):
        writer = csv.writer(f)
        writer.writerow([i , 0 , 0 , ""])#リセット条件

 

print("process done")







