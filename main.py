from function import *

def main():
    try:
        print("0:設定 1:範囲指定")
        mode = int(input())
        if mode == 1:
            print("範囲を指定してください")
            start = int(input("開始No"))
            finish = int(input("終了No"))
            for i in range(start , finish):
                quiz(i)
            

    except ValueError:
        print("数値を入力してください")
        main(id)


if __name__ == "__main__":
    main()
