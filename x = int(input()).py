x = int(input())
kol = 0
while x > 0:
    print(x%10)
    kol = kol+1

    x=x//10
print('Vsego cyfr:', kol)
