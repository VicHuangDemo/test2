import random

card_color=['♠','♥','♦','♣']   #牌的花色陣列
card_number=['A','K','Q','J','10','9','8','7','6','5','4','3','2']  #牌的數字陣列
card=[]  #存放撲克牌的陣列

for i in card_color:
    for j in card_number:
        #加牌的花色及數字加到撲克牌的陣列(兩種寫法擇一)
        #card.append(i + j)
        card += [ i + j ]
             
total = 52  #總共要發幾張牌


for i in range(total):

    n = random.randint(0, total-1)  #隨機產生抽牌的位置
    print(card[n], end="  ")  # 印出抽到的牌
    del card[n]  #從card陣列刪掉抽到的牌
    total -= 1   #將牌的張數減一

    if (i+1) % 13 == 0:   #每發13張
         print()          #換行