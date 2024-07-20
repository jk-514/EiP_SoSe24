import random

room = ['Curtain', [['Lamp'], 'Vacuum cleaner', 'Curtain', 'Laundry basket', 'Mouse', [['Printer'], 'Slippers', 'Air conditioner', ['Computer', [['Charger'], 'Vase', 'Broom', 'Mirror', 'Vacuum cleaner', 'Heater', [['Mop'], 'Dresser', [], 'Cleaning supplies', ['Candles'], ['Coat rack', ['Speakers'], [], 'Mirror', 'Television', 'Mouse', 'Side table', [[['Sheets'], ['Soap', 'Backpack'], ['Mouse', 'Printer'], 'Conditioner', 'Jewelry box', 'Vase', 'Newspaper', 'Handbag', 'Keyboard', 'Shower curtain', 'Towel', 'Candles', 'Comforter', 'Computer', 'Clock', 'Printer', [], 'Wardrobe', ['Speakers'], 'Chair', 'Remote control', ['Wardrobe'], 'Hairbrush', 'Sunglasses', [], 'Air conditioner', 'Dresser', 'Shoes', ['Light switch'], 'Mop', [], 'Clothes hanger', 'Conditioner', 'Remote control', 'Hat', [], 'Toilet', 'Cleaning supplies', 'Handbag', 'Lamp', 'Heater', 'Vase', [], [], [], [[['Pillow', 'Dresser', 'Plant'], 'Hat', ['Vacuum cleaner', 'Toilet'], ['Keyboard', 'Handbag', ['Soap dispenser'], 'Speakers', 'Keyboard', ['Dresser'], ['Makeup', [], 'Hat', [], 'Pillow', [], 'Gloves', 'Tissue box', ['Broom', 'Light switch'], 'Newspaper', 'Rug', [], 'Pillow', 'Soap dispenser', 'Paper', ['Alarm clock', [], 'Fan', 'Clothes hanger', [], 'Computer', 'Book', 'Laundry basket', 'Pillow', 'Charger', ['Speakers', 'Comb', 'Toothpaste'], 'Toothpaste', [[['Ironing board'], 'Coffee table', [], [[], [], [], 'Television', ['Picture frame'], 'Makeup', ['Wardrobe', 'Rug', 'DVDs', [['Coasters', 'Coat rack', [], 'Recycling bin', 'Game console', 'Closet', 'Sofa', 'Iron', 'Laundry basket', 'Mop', 'Fan', ['Umbrella'], 'Makeup', ['Coat rack', 'Sunglasses'], [], 'Paper', 'Alarm clock', 'Comb', 'Clothes hanger', 'Vacuum cleaner', 'Soap dispenser', ['Magazine', ['Comforter', 'Sofa'], ['DVD player'], 'Iron', 'Desk', 'Remote control', ['Vase'], 'DVD player', [[], 'Comb', 'Sink', 'Hairbrush', ['Sofa', 'Keyboard', 'Notebook'], 'Clock', 'Charger', 'Blinds', 'Coffee table', 'Remote control', 'Toothbrush', ['Hand sanitizer', [[[['Game console'], 'Medicine cabinet', 'Clock', 'Bucket', 'Side table', 'Ironing board', 'Soap', 'Cushion', 'Toilet', 'Medicine cabinet', 'Outlet', 'Mirror', ['Alarm clock', [], 'Wallet', ['Desk', 'Towel', [], 'Soap', 'Slippers', ['Backpack'], 'Computer', 'Toothpaste', 'Side table', ['Newspaper'], ['Mop', 'Slippers'], 'Charger', 'Broom', 'Candles', 'Light switch', ['Coat rack'], 'Outlet', ['Telephone'], 'Alarm clock', 'Tissue box', [['Tissue box', [[], 'Vase', [[['Wallet'], [[['Shampoo', [], [], 'Wallet', 'Monitor', 'Medicine cabinet']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], 'Slippers', 'Laundry basket', 'Air conditioner', 'Soap', 'Wallet', 'Comforter', 'Printer', []]

# with open('words.txt') as f:
#     words = f.readlines()
#     words = [word.strip() for word in words]



# def generate_room():
#     room = []
#     count = 0
#     level = 1
#     l = room
#     old_l = l
#     while count != 200:
#         c = random.choice([0,0,1,1,2])
#         if c == 1:
#             l.append(random.choice(words))
#             count += 1
#         elif c == 2:
#             l.append([])
#             old_l = l
#             l = l[-1]
#             level += 1
#         elif c == 0 and level > 1:
#             l = old_l
#             level -= 1
#
#     random.shuffle(room)
#     return room

   
def count_boxes(l):
    count = 0
    if isinstance(l, list):
        count += 1
        for a in l:
            count += count_boxes(a)
    return count

def count_items(l):
    count = 0
    if isinstance(l, list):
        for a in l:
            count += count_items(a)
    else:
        count += 1
    return count

def find_in_box(l, box):
    if isinstance(l, list):
        if all(item in l for item in box):
            return True
        found = False
        for a in l:
            found = found or find_in_box(a, box)
        return found
    return False

def unpack(l):
    if isinstance(l, list):
        #if len(l) == 1:
        #    return unpack(l[0])
        #f = flatten(l[0]) + flatten(l[1:])
        f = []
        for a in l:
            f += unpack(a)
        return f
    else:
        return [l]
    

func_count = count_boxes(room)
actual_count = str(room).count('[')
print(func_count)
print(actual_count) # sanity check
print(count_items(room))
print(find_in_box(room, ['Soap dispenser', 'Paper'])) # sanity check
print(find_in_box(room, ['DVDs', 'DVD player', 'Television']))
print(unpack(room))
