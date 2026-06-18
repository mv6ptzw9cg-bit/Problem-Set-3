while True:
    try:
        fraction = input("Fraction: ")

        x, y = fraction.split("/")

        x = int(x)
        y = int(y)

        if x > y:
            continue

        percentage = round((x / y) * 100)

        if percentage <= 1:
            print("E")
        elif percentage >= 99:
            print("F")
        else:
            print(f"{percentage}%")

        break

    except (ValueError, ZeroDivisionError):
        pass 
