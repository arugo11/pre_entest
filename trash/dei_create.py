import csv
from os import terminal_size

path_word = "dic_o.csv"
path_id_ans = "n_dic.csv"
word_list = []
ans_list = []
ques = []

selects = []
with open(path_word) as f:
    s = f.read()
    ques = s.split("\n")
    for i in ques:
        find_blank = i.find(",")
        word_list.append(i[:find_blank-1])

with open(path_id_ans) as g:#ans
    s = g.read()
    b_list = s.split("\n")   
    for i in b_list:
        find_blank = i.find(" ")
        ans_list.append(str(i)[find_blank:])
    # print(ans_list)


with open("dic_f_1.csv" , "w") as h:
    writer = csv.writer(h)
    for i in range(1900):
        writer.writerow([i +1 , word_list[i] , ans_list[i][1:]])





for i in range(1900):
    one_find = ques[i].find("①") 
    two_find = ques[i].find("②")
    three_find = ques[i].find("③") 
    four_find = ques[i].find("④")
    # print(ques[i][one_find+2:two_find-1])
    selects.append(ques[i][one_find+2:two_find-1])
    selects.append(ques[i][two_find+2:three_find-1])
    selects.append(ques[i][three_find+2:four_find-1])
    selects.append(ques[i][four_find+2:-3])


selects = list(set(selects))

with open("dic_q.csv" , "w") as f:
    writer = csv.writer(f)
    for i in range(1900):
        writer.writerow([selects[i]])


#1 or 2 or 3 or 4をfindして次の単語を抽出
    