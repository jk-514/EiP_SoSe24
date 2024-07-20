a = float(input("Preis a: "))
b = float(input("Preis b: "))
c = float(input("Preis c: "))

# Finde Minimum

if a <= b and a <= c:
    min_ = a
elif b <= a and b <= c:
    min_ = b
else:
    min_ = c

# Finde Mitte

if (b >= a >= c) or (b <= a <= c):
    mid = a
elif (a >= b >= c) or (a <= b <= c):
    mid = b
else:
    mid = c

# Berechne Durchschnitt

avg = (a + b + c) / 3

print("Am günstigsten: ", min_)
print("Am zweitgünstigsten: ", mid)
print("Durchschnitt: ", avg)
