print("Лабораторна робота №2 Варіант 3")

print("Гліб Кобрин, ІКСМ-1, Навчальна Група №2")

while True:
    user_input = input("Введіть довільне ціле число: ")

    if user_input.isdigit():
        num = int(user_input)

        num_str = str(num)

        for digit in user_input:
            count = int(digit)
            histogram = "#" * count

            print(histogram)

        explanation_title = "\nПояснення:"

        print(explanation_title)

        for index, digit in enumerate(user_input, start=1):
            count = int(digit)
            explanation = f"Розряд {index}: "

            if count == 1:
                explanation += f"{count} символ"
            elif 1 < count < 5:
                explanation += f"{count} символи"
            else:
                explanation += f"{count} символів"

            print(explanation)

        break

    else:
        print("Error: Введене значення не є цілим числом.")
