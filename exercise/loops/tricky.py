num1 = 0
num2 = 0

for x in range(5): # wehn loops ends, x is 4 (last value assigned)
    num1 = x
    for y in range(14): # wen loops ends, x is 13 (last value assigned)
        num2 = y + 3

print(num1 + num2)