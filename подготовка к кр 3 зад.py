print("Введите первую координату")
x1 = float(input("x:"))
y1 = float(input("y:"))
print("Введите вторую координату")
x2 = float(input("x:"))
y2 = float(input("y:"))
print("Введите третью координату")
x3 = float(input("x:"))
y3 = float(input("y:"))
a = ((x2-x1)**2+(y2-y1)**2)**(1/2)
b = ((x3-x2)**2+(y3-y2)**2)**(1/2)
c = ((x1-x3)**2+(y1-y3)**2)**(1/2)
if a+b>c and b+c>a and a+c>b:
    print("Треугольник существует.")
    if a==b and b==c and a==c:
        print("Треугольник равносторонний")
    elif a==b or b==c or a==c:
        print("Треугольник равнобедренный")
    elif a!=b and b!=c or a!=c:
        print("Треугольник разносторонний")
else:
    print("Такого треугольника не существует")