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