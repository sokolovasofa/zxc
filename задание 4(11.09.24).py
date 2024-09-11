a=int(input("Введите время в часах:"))
if a>=5 and a<=11:
    print("Утро")
elif a>=12 and a<=17:
    print("День")
elif a>=18 and a<=22:
    print("Вечер")
elif a>=23 and a<=4:
    print("Ночь")
else:
    print("Ошибка")