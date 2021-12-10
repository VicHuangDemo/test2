import random

lottery=[]  #存放彩球的陣列
total = 39  #彩球的數量
num = 5       #要抽的彩球數

for i in range(1, total+1):
       #將數字加入彩球陣列 (兩種寫法擇一)
        #lottery.append(i)
        lottery += [i]
             

for i in range(num):

    n = random.randint(0, total-1)  #隨機產生抽出彩球的位置
    print(lottery[n], end=" ")  # 印出抽到的牌
    del lottery[n]  #從彩球陣列刪掉抽到的球
    total -= 1   #將彩球數減一