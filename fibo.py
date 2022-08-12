num = int(input("Enter number:"))
a = 0
b = 1
for i in range(num+1):
    print(a)
    sumab = a + b
    a = b
    b = sumab
