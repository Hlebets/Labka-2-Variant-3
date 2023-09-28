print("Лабораторна робота №2 Варіант 3")

print("Гліб Кобрин, ІКСМ-1, Навчальна Група №2")

user_input = input("Введіть довільне ціле число: ")

if user_input.isdigit():
    num = int(user_input)

    num_str = str(num)

    for digit in num_str:
        count = int(digit)
        histogram = "#" * count
        print(histogram)

else:
    print("Error: Введене значення не є цілим числом")
