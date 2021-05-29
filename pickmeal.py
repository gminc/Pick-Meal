meals = []
with open('meal.txt', 'r', encoding = 'utf-8') as f:
    for line in f:
        name = line.strip()
        meals.append(name)            

while True:
    ans = input('想幹嘛? 1. 新增吃的 2. 刪除吃的 3. 挑要吃的 4. 沒事掰 → ')
    if ans == '1' or ans == '1.':
        while True:        
            name = input('想加啥: (不想加就輸入 q or Q) ')
            if name == 'q' or name == 'Q':
                break
            meals.append(name)

    if ans == '2' or ans == '2.':
        while True:
            for i in range(0,len(meals)):
                print(i+1, meals[i])
            r = input('不要哪個? 填編號ㄏㄚˋ (不想刪就輸入 q or Q) ')
            if r == 'q' or r == 'Q':
                break
            try:
                if 0 < int(r) <= len(meals):
                    meals.pop(int(r)-1)
                for i in range(0,len(meals)):
                    print(i+1, meals[i])
            except ValueError:
                print('只能輸入整數!!!')

    if ans == '3' or ans == '3.':
        import random
        print('去吃:', random.choice(meals))
    
    if ans == '4' or ans == '4.':
        print('不吃就不吃')
        break

    try:
        if int(ans) < 1 or int(ans) > 4:
            print('只有四個選項可以選喔')
    except ValueError:
        print('只有四個選項可以選喔')

with open('meal.txt', 'w', encoding = 'utf-8') as f:
    for line in meals:
        name = line.strip()
        f.write(name + '\n')
