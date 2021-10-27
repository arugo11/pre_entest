from os import O_CREAT, waitpid
import random
import datetime
import csv


path_f = "data/dic_f.csv"
path_q = "data/dic_q.csv"
path_r = "data/record.csv"
word_list = []
questions = []
records = []

with open(path_f) as f:
    temp = f.read()
    ques = temp.split("\n")#path_fの１行ずつ
    
    for i in range(1900):
        temp = ques[i].split(",")
        word_list.insert(i,temp)
with open(path_q) as g:
    temp = g.read()
    questions = temp.split("\n")
    del questions[0]

def select(id):
    # print(word_list[id][2])
    choice = []
    ans_pos = random.randint(1,4)
    for i in range(1,5):
        if i == ans_pos:
            choice.insert(i, str(ans_pos) +  ":" + str(word_list[id][2]))#答えの挿入 
        else:
            choice.insert(i,str(i) + ":" +questions[random.randint(0,1898)])
    return [choice , ans_pos]

def quiz(id):#問題を表示→正誤のみ返す
    #問題文の表示
    temp_select = select(id)#selects[0]→選択肢(str) , 答えNo
    print(word_list[id][1])
    print(" ".join(temp_select[0]))
    #入力の例外処理
    try:
        ans = int(input())
    except ValueError:
        print("数値を入力してください")
        quiz(id)
    if ans == temp_select[1]:#True
        print("True!!")
        return True
    else:
        print("False(´・ω・｀)")
        return False
    
def record(id , judge):

        with open(path_r) as g:
            reader = csv.reader(g)
            l = [row for row in reader]#前回までの記録の参照完了
            count = int(l[id][1])
            w_count = int(l[id][2])
            day = list(l[id][3])

        with open(path_r , "w") as f:
            count += 1
            if not judge:w_count += 1
            today = str(datetime.date.today())
            day.append(str(today))
            for i in l:
                writer = csv.writer(f)
                if i == id:
                    writer.writerow(i+1 , count , w_count , day)
                writer.writerow([l])
            

record(1 , False)

            




            
                
