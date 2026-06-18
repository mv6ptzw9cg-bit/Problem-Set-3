grocery = {}

while True:
    try:
        item = input("Item: ").upper()

        if item in grocery:
            grocery[item] = grocery[item] + 1
        else:
            grocery[item] = 1

    except EOFError:
        print()
        break

for item in sorted(grocery):
    print(grocery[item], item)
