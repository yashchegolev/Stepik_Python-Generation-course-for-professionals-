total_en = 0
total_ru = 0
for _ in range(3):
    s = input()
    if s in "AaBCcEeHKMOoPpTXxy":
        total_en += 1
    elif s in "АаВСсЕеНКМОоРрТХху":
        total_ru += 1    
if total_en == 3:
    print('en')
elif total_ru == 3:
    print('ru')
else:
    print('mix')
