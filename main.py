from function import *



def main():
    if check_record():
        record_on = True
    else:
        record_on = False
    print("0:Setting 1:range 2:got wrong last time ")
    if record_on:
        now = "有効"
    else:
        now = "無効"
    print("記録モードは{}です".format(now))

    mode = input()

    if mode == "0":
        print("What setting?")
        print("--------------------------------")
        print("0:exit , 1:record , 2,reset_data")
        what = input()
        if what == "0":
            main()
        elif what == "1":
            record_switch()
            main()
        elif what == "2":
            reset_data()
            main()
            
    elif mode == "1":
        
        print("Please specify a range.")
        start = int(input("start No? :"))
        finish = int(input("finish No? :"))

        No = 1
        history = []
        recent_wrong = []
        for i in range(start , finish + 1):

            ans = quiz(i,No ,record_on)

            history.append(ans)
            if not ans:#間違えたものリストへ
                recent_wrong.append(i)
            No += 1
        have_False = False in history 
        review(have_False , recent_wrong)

        main()



    elif mode == "2":
        if recommend(0,True) == 0:
            print("There's no mistake from last time.")
        print("Displays the questions you got wrong last time.")
        print("Up to {} can be displayed.".format(recommend(0,True)))

        for i in recommend(int(input("How many quizzes do you give? :")),False):
            answer(i,record_on)


        main()
    elif mode == "exit":
        exit()






if __name__ == "__main__":
    main()



"""
#タイムキー

#途中:問題数の表示
エンター面倒
色変える
エラー間違え

"""

