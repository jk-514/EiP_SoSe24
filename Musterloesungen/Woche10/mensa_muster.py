def read_tsv(filename : str):
    dishes = []
    with open(filename, 'r') as file:
        dishes = [line.strip().split('\t') for line in file]
        dishes = [(dish[0], int(dish[1]), float(dish[2])) for dish in dishes]
    return dishes


dish_list = read_tsv('mensa.tsv')

# Hier kommt dein Code hin.
class Dish:
    def __init__(self, name, price, rating):
        self.name = name
        self.price = price
        self.rating = rating

    def __str__(self):
        return self.name + ' (' + str(self.price/100) + '€)' + ' [' + str(self.rating) + ']'
    
    def __eq__(self, other: 'Dish') -> bool:
        return self.name == other.name 
    
    def __hash__(self) -> int:
        return hash(self.name)
    
    

#a)
dish_list = [Dish(*dish) for dish in dish_list]
#c)
print(len([d for d in dish_list if d == Dish('Veggi Kraut Dog- XXL Hot Dog mit knackigem Kraut und Röstzwiebeln (1,2,Gl,Ei,So,Sl,Sf,We)',0,0)]))

d = {}
for dish in dish_list:
    if dish not in d:
        d[dish] = []

    d[dish] += [dish.rating]

for dish in d:
    print(dish.name + f' {sum(d[dish]) / len(d[dish])}, {len(d[dish])} Bewertungen')
