lottory = input("Enter your lottory : ")

prize_1st = ['046750'] # รางวัลที่ 1
first_3num = ['666','421'] # เลขหน้า 3 ตัว
last_3num = ['160','335'] # เลขท้าย 3 ตัว
last_2num = ['23'] # เลขท้าย 2 ตัว
almost_prize = ['046749', '046751'] # รางวัลใกล้เคียง
last2_2num = ['688916','774867','222907','903009','607877'] # รางวัลที่ 2

if lottory in prize_1st:
    print('คุณถูกรางวัลที่ 1')
if lottory[:3] in first_3num:
    print('คุณถูกรางวัล เลขหน้า 3 ตัว')
if lottory[3:] in last_3num:
    print('คุณถูกรางวัล เลขท้าย 3 ตัว')
if lottory[4:] in last_2num:
    print('คุณถูกรางวัล เลขท้าย 2 ตัว')
if lottory in almost_prize:
    print('คุณถูกรางวัล รางวัลใกล้เคียง')
if lottory in last2_2num:
    print('คุณถูกรางวัลที่ 2')