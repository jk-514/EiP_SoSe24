import random

# a)
def rob(houses):
    if len(houses) == 0:
        return 0
    return max(houses[0] + rob(houses[2:]), rob(houses[1:]))

# b)
def rob_dynamic(houses):
    last, now = 0, 0
    for house in houses:
        last, now = now, max(last + house, now)
    return now


random.seed(0)
houses = random.choices(range(10,30), k = 10)

# print(rob_dynamic(houses))
print(rob(houses))
