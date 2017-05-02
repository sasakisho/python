import random

#str = {"","グー","チョキ","パー"}
while True:
    com = random.randint(1,3)
    ply = int(input("グー:1、チョキ:2、パー:3 "))


    print("com=",com," ply=",ply)
    if(ply == 1):
        if(com == 1):
            print("あいこ")
            continue
        elif(com==2):
            print("勝ち")
        else:
            print("負け")
    elif(ply == 2):
        if(com == 2):
            print("あいこ")
            continue
        elif(com==3):
            print("勝ち")
        else:
            print("負け")
    elif(ply == 3):
        if(com == 3):
            print("あいこ")
            continue
        elif(com==1):
            print("勝ち")
        else:
            print("負け")
    else:
        print("入力が不正です")
        continue

    ret = input("続けますか y/n ")

    if(ret == "n"):
        break
    else:
        continue
