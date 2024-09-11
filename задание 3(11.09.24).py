a=int(input("Введите длину отрезка:"))
b=int(input("Введите длину отрезка:"))
c=int(input("Введите длину отрезка:"))
if a+b>c and b+c>a and a+c>b:
    print("YES")
else:
    print("NO")