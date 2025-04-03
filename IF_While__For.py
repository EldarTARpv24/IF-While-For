n = int(input("Сколько вы хотите ввести чисел?"))
biggest = 0
for numbs in range(n):
    numb = int(input("Введите число: "))
    if numbs > numb:
        biggest == numb
print(biggest)