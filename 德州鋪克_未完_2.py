import copy
import random
from itertools import product
 
color=["♥", "♠", "♣", "♦"]
value=["2 ","3 ","4 ","5 ","6 ","7 ","8 ","9 ","10","J ","Q ","K ","A "]
pai = [co+va+"" for co,va in product(color,value)]
print(pai)
random.shuffle(pai)
def deal_cards(number,num):
    pais=copy.deepcopy(pai)
    random.shuffle(pais)  # 洗牌
    players=[list() for x in range(number)]
    for pl in range(len(players)):
        players[pl]=[" " for x in range(num)]
    for numb in range(number):#同一副牌
        n=0
        while n<num:
            players[numb][n]=pais.pop(random.randint(0,len(pais)-1))
            n+=1
    return players

def judge_card_type(value,Color_type):#value为一个玩家的牌值须按照从大到小排好序，color为对应的花色
    result=0
    num=0#牌值相同的个数
    if len(value)!=5:
        print("牌数不为五张或过多，无法判断！")
        sys.exit()
    for A in range(0, len(value)):#统计相等的个数 或者是否为顺子
        if value[A-1]- value[A]== 1:
            result += 1#如果为顺子，则resul=4
        elif value[A] == value[A - 1]:
            num += 1
 
    if Color_type=="true":#同花
        if value==[13,12,11,10,9]:#皇家同花顺
            return "0"
        elif result==4:#同花顺
            return "1"
        else:return "4"#同花
    if Color_type=="false":#非同花
        if num==3:#四条或葫芦
            if value[1]==value[2]==value[3]==value[4] or value[0]==value[1]==value[2]==value[3]:
                return "2"#四条
            else: return "3"#葫芦
        elif result==4:#顺子
            return "5"
        elif num==2:#三条或两队
            if value[0]==value[1]==value[2] or value[1]==value[2]==value[3] or value[2]==value[3]==value[4]:
                return "6"#三条
            else: return "7"#两队
        elif num==1:#一对
            return "8"
        else:return "9"#高牌

def compare_value(player_fir, play_sec, card_type_fir, card_type_sec): 
    if card_type_fir < card_type_sec:
        return 1 #first<second
    elif card_type_fir > card_type_sec:
        return -1 #first>second
    elif card_type_fir == card_type_sec:  #牌型相等 比較大小
        if card_type_fir in [9, 5, 4, 1, 0]: #高牌、順子、同花、同花順、皇家同花順  直接比大小
            for i in range(5):
                if player_fir[i] > play_sec[i]:
                    return 1
                elif player_fir[i] < play_sec[i]:
                    return -1
        elif card_type_fir in [2, 3, 6]: #四條、葫蘆、三條 比較中間的呢個牌值
            if player_fir[2] > play_sec[2]:
                return 1
            elif player_fir[2] < play_sec[2]:
                return -1
            else :#相等
                for i in range(5):
                    if player_fir[i] > play_sec[i]:
                        return 1
                    elif player_fir[i] < play_sec[i]:
                        return -1
        elif card_type_fir == 7: #兩對
            if player_fir[1] > play_sec[1]:
                return 1
            elif player_fir[1] < play_sec[1]:
                return -1
            else:
                if player_fir[3] > play_sec[3]:
                    return 1
                elif player_fir[3] < play_sec[3]:
                    return -1
                else:
                    for i in range(5):
                        if player_fir[i] > play_sec[i]:
                            return 1
                        elif player_fir[i] < play_sec[i]:
                            return -1
        elif card_type_fir == 8: #一對  先找到對子的位置，比較大小
            d1, d2 = 0, 0
            for i in range(4):
                if player_fir[i] == player_fir[i + 1]:
                    d1 = player_fir[i]
                if play_sec[i] == play_sec[i + 1]:
                    d2 = play_sec[i]
            if d1 > d2:
                return 1
            elif d1 < d2:
                return -1
            elif d1 == d2:
                for i in range(5):
                    if player_fir[i] > play_sec[i]:
                        return 1
                    if player_fir[i] < play_sec[i]:
                        return -1
        return 0