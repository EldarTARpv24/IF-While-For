n = int(input("Сколько вы хотите ввести чисел?"))
biggest = 0
for numbs in range(n):
    try:
        numb = int(input("Введите число: "))
        if biggest < numb:
            biggest = numb
        else:
            biggest = biggest
    except ValueError:
print(biggest)

n = int(input("Сколько вы хотите ввести чисел?"))
for numbs in range(n):
    try:
        numb = int(input("Введите число: "))
        if numb == 13:
            print(f"13")
        else:
            print(f"{numb}")
    except ValueError:

try:
    first_day = 10
    rate = 1.1
    summ = 0
    for numb in range(1, 7):
        summ += first_day * (rate ** numb)
    x = round(summ, 2)
    print(x)
except ValueError:
    print("Ошибка ввода данных")

try:
    n = int(input("Сколько метров ткани?"))
    while n > 0:
        m = int(input("Сколько метров ткани нужно?"))
        if m <= n:
            print("ткань есть")
            n -= m
            print(f"Отрезан кусок длиной {m} метров. Остаток ткани: {n} метров.")
        else:
            print(f"Материала недостаточно для куска длиной {n} метров.")
            buy = input("Вы хотите выкупить остаток ткани? (да/нет): ")
            if buy == "да":
                print(f"Остаток ткани продан, последний кусок был длиной {n} метров.")
                break
            else:
                print("Переходим к следующему покупателю.")
except ValueError:
    print("Ошибка ввода данных")

while True:
    try: 
        b =int(input("Введите длину основания: "))
        d = int(input("Введите длину другого основания: "))
        h= int(input("Введите высоту: "))
        S = 0.5 * (b + d) * h
        print(f"Площадь трапеции: {S}")
        answer = int(input("Хотите перестать считать? Введите 1 для выхода, 0 для продолжения: "))

        if answer == 1:
            print("Выход из программы")
            break
        elif answer == 0:
                print(f"{S} площадь") 
                continue
        else:
            print("Ошибка ввода данных. Введите 0 или 1")
    except ValueError:
        print("Ошибка ввода данных. Пожалуйста, введите числа.")

try:
    numb = int(input("Введите число: "))
    if numb % 3 == 0:
        print("Число делится на 3")
    else:
        print("Число не делится на 3")
except ValueError:
    print("Ошибка ввода данных. Пожалуйста, введите число.")