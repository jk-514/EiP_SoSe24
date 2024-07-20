import random

nums = list(range(1, 76))

fields = [random.sample(nums, 25) for _ in range(4)]

gerda = random.sample(nums, 75)

'''
with open('sheet05/bingo.txt', 'w') as f:
    for field in fields:
        for i in range(5):
            s = [str(x) if i*5+j != 12 else 'x' for j,x in enumerate(field[i*5:i*5+5])]
            f.write(' '.join(s))
            f.write('\n')
        f.write('\n')
    
    f.write(' '.join([str(x) for x in gerda]))
'''
# Ich habe das Lesen mal weggelassen

def mark_cell(field, num):
    for i in range(5):
        if num in field[i*5:i*5+5]:
            field[i*5:i*5+5] = [x if x != num else 'x' for x in field[i*5:i*5+5]]

def check_bingo(field):
    for i in range(5):
        if all([x == 'x' for x in field[i*5:i*5+5]]):
            return True
        if all([x == 'x' for x in field[i::5]]):
            return True
    if all([field[i*5+i] == 'x' for i in range(5)]):
        return True
    if all([field[4*i] == 'x' for i in range(1,6)]):
        return True
    return False

for g in gerda:
    for i, field in enumerate(fields):
        mark_cell(field, g)
        if check_bingo(field):
            print(f'Bingo! Player {i} won!')
            exit(0)
