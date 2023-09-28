print("Лабораторна робота №2 Варіант 3")

print("Гліб Кобрин, ІКСМ-1, Навчальна Група №2")

num = int(input("Введіть довільне ціле число: "))

num_str = str(num)

for digit in num_str:
    count = int(digit)
    histogram = "#" * count
    print(histogram)
