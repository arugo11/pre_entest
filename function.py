from os import O_CREAT, replace, waitpid
import random
import datetime as dt
import csv


path_f = "entest/data/dic_f.csv"
path_q = "entest/data/dic_q.csv"
path_r = "entest/data/record.csv"
path_s = "entest/data/settings.csv"
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
    ans_pos = int(random.randint(0,3))
    for i in range(0,4):
        if i == ans_pos:
            temp = str(ans_pos+1) +  ":" + str(word_list[id][2])
            choice.insert(i, temp)#答えの挿入 
        else:
            temp = str(i+1) + ":" +questions[random.randint(0,1898)]
            choice.insert(i,temp)
    return [choice , ans_pos]#choice :

def quiz(id , num , switch):#問題を表示→正誤のみ返す
    #問題番号 , 何問目　, 記録するかしないか
    #問題文の表示
    temp_select = select(id)#selects[0]→選択肢(str) , 答えNo
    print("({})".format(num) + str(word_list[id][1]))#英単語
    print(" ".join(temp_select[0]))#選択肢
    #入力の例外処理
    try:
        ans = input()
    except ValueError:
        print("数値を入力してください")
        quiz(id ,num , True)

    if ans == "0":
        if switch:
            record(id , False)
        print("")
        print(color((str(word_list[id][1]) + " : " + word_list[id][2]),"under_line"))
        print(color("","reset"))
        return False

    elif int(ans) == temp_select[1] + 1:#True
        print(color("True!!" , "red"))
        if switch:
            record(id , True)


        return True
    elif ans == "?":#中断
        print(color("中断" , "red"))
        exit()

    else:
        print(color("False(´・ω・｀)" , "blue"))
        if switch:
            record(id , False)
        print("")
        print(color((str(word_list[id][1]) + " : " + word_list[id][2]),"under_line"))
        print(color("","reset"))


        return False

def record(id , judge):
    with open(path_r) as f:
        reader = csv.reader(f)
        l = [row for row in reader]

    with open(path_r , "w") as g:
        id = int(id) - 1
        count = int(l[id][1]) + 1
        wrong_count = int(l[id][2])
        #数字加算
    
        if  judge:
            wrong_count -= 1
            last_time = 0
        else:
            wrong_count += 1
            last_time = 1
            


        result = [id + 1, count , wrong_count,last_time]
        up_to_date = l[id][4:]#すべての日付
        up_to_date = [int(i) for i in up_to_date]

#日付処理
        today = int((str(dt.date.today())).replace("-" , ""))
        if judge:
            pass
        else:
            up_to_date.append(today)
        
        result += up_to_date

        l[id]  = result

        writer = csv.writer(g)
        writer.writerows(l)
        
def recommend(num,mode):
    with open(path_r) as f:
        reader = csv.reader(f)
        l = [row for row in reader]
        last_wrong = []

        for i in range(1900):
            if l[i][3] == "1":
                last_wrong.append(int(l[i][0]))
            Lr = random.sample(last_wrong,len(last_wrong))
        if mode:
            return len(Lr)#for文の中にreturnを入れてはいけませんって言ったでしょ！！！！！！！
        Lr = Lr[:num]
        return Lr#for文の中にreturnを入れてはいけません(約束)

def review(history , wrongs ):
    print(color("REVIEW" , "green"))


    if history:
        print("1:exit , 2:review(record)  , 3:review(not record)" )
        choice = input()
        if choice == "1":#exit
            exit()
        elif choice == "2":#review(record)
            No = 1
            history = []
            recent_wrong = []
            for i in wrongs:
                i = int(i)
                ans = quiz(i , No ,True)
                history.append(ans)
                if not ans:
                    recent_wrong.append(i)
                No += 1
        elif choice == "3":
            No = 1
            history = []
            recent_wrong = []
            for i in wrongs:
                i = int(i)
                ans = quiz(i , No ,True)
                history.append(ans)
                if not ans:
                    recent_wrong.append(i)
                No += 1
        else:
            review(history,wrongs)
        if False in history:
            review(history,recent_wrong)
        else:
            print("all questions answered correctly!!!")
            
    else:
        print("all questions answered correctly!!!")

    
def color(letter , kind):
    if kind == "red":
        return '\033[31m'+str(letter)+'\033[0m'
    elif kind == "blue":
        return '\033[34m'+str(letter)+'\033[0m'
    elif kind == "green":
        return '\033[32m'+str(letter)+'\033[0m'
    elif kind == "under_line":
        return '\033[4m' + str(letter) + '\033[4m'
    elif kind == "reset":
        return '\033[0m' + str(letter) + '\033[0m'

def answer(id,record_on):
    No = 1
    history = []
    recent_wrong = []
    ans = quiz(id,No,record_on)
    history.append(ans)
    if not ans:
        recent_wrong.append(id)
    No += 1
    have_False = False in history
    review(have_False , recent_wrong)

def reset_data():

    with open("data/record.csv" , "w") as f:
        for i in range (1 , 1901):
            writer = csv.writer(f)
            rand = "2021" + str(random.randint(1,12)) + str(random.randint(1,12))
            writer.writerow([i , 0 , 0 ,0 ])#リセット条件
    print("reset done")

def record_switch():
    with open(path_s,) as f:
        reader = csv.reader(f)
        l = [row for row in reader]


    print("record? y/n")
    judge = input()
    if judge == "y":
        ans = 1
    elif judge == "n":
        ans = 0
    else: record_switch()

    l[0][1] = ans

    with open(path_s , "w") as f:
        writer = csv.writer(f)
        writer.writerows(l)

    if l[0][1] == 1:
        return True
    elif l[0][1] == 0:
        return False

def check_record():
    with open("entest/data/settings.csv") as f:
        reader = csv.reader(f)
        l = [row for row in reader]

        if l[0][1] == "1":
            return True
        else:
            return False

    