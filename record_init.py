import csv
import random

with open("data/record.csv" , "w") as f:
    for i in range (1 , 1901):
        writer = csv.writer(f)
        rand = "2021" + str(random.randint(1,12)) + str(random.randint(1,12))
        writer.writerow([i , 0 , 0 ,0])#リセット条件

 

print("process done")







