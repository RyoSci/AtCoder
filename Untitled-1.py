import random
# 定数
FIELD_H = 5
FIELD_W = 10
CHAR_OF_NONE = " "
CHAR_OF_POS = "p"
CHAR_OF_GOAL = "o"
CHAR_OF_WALL = "x"
MSG_GAME_START = "ゲームを開始します"
MSG_GAME_END = "ゲームを終了します"
MSG_GAME_COMMAND = "コマンドを入力してください(q:終了, h:左, j:下, k:上, l:右)" 
MSG_GAME_CLEAR = "GAME CLEAR!"
MSG_GAME_CONTINUE = "ゲームを続行しますか?(y:はい, n:いいえ)" 
MSG_GAME_INVALID_INPUT = "不正な入力です"
pos_w,pos_h=random.randint(1,5),random.randint(1,10)
o_1,o_2=random.randint(1,5),random.randint(1,10)
def show_field(field): 
    global pos_w,pos_h
    field=create_field()
    field[pos_w][pos_h]="p"
    field[o_1][o_2]="o"
    for i in range(7):
        print(field[i])

def create_field(): 
    field=[]

    for i in range(7):
        if i == 0 or i == 6:
            field.append(list("xxxxxxxxxxxx"))
        else:
            tmp=[]
            for j in range(12):
                if j == 0 or j == 11:
                    tmp.append("x")
                else:
                    tmp.append(" ")
            field.append(tmp)
    # p_1,p_2=random.randint(1,5),random.randint(1,10)
    # o_1,o_2=random.randint(1,5),random.randint(1,10)
    # field[p_1][p_2]="p"
    # field[o_1][o_2]="o"
    return field#,(p_1,p_2),(o_1,o_2)

def update_position(command, pos_h, pos_w): 
    if command == "h":
        pos_w=max(1,pos_w-1)
    elif command == "j":
        pos_h=min(5,pos_h+1)
    elif command == "k":
        pos_h=max(1,pos_h-1)
    elif command == "l":
        pos_w=min(10,pos_w+1)
    else:
        print(MSG_GAME_INVALID_INPUT)
    return pos_h,pos_w
        
    
def main():
    global pos_w,pos_h
    global o_1,o_2
    print(MSG_GAME_START)
    field = create_field()
    # pos_w,pos_h=random.randint(1,5),random.randint(1,10)
    # o_1,o_2=random.randint(1,5),random.randint(1,10)
    show_field(field)
    command=" "
    # print(field)
    while command != "q":
        print(MSG_GAME_COMMAND)
        command = input()
        pos_w, pos_h = update_position(command, pos_w, pos_h)
        if pos_w == o_1 and pos_h == o_2:
            print(MSG_GAME_CLEAR)
            print(MSG_GAME_CONTINUE)
            flag = ""
            while flag != "n" and flag != "y":
                flag = input()
                if flag == "y":
                    field= create_field()
                    pos_w,pos_h=random.randint(1,5),random.randint(1,10)
                    o_1,o_2=random.randint(1,5),random.randint(1,10)
                    # show_field(field)
                elif flag == "n":
                    print(MSG_GAME_END)
                    break
                else:
                    print(MSG_GAME_INVALID_INPUT)
        if flag=="n":
            break
        show_field(field)
if __name__== "__main__":
    main()