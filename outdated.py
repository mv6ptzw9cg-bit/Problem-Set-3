months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ").strip()

        if "/" in date:
            month, day, year = date.split("/")

            month = int(month)
            day = int(day)
            year = int(year)

        else:
            month_name, rest = date.split(" ", 1)

            if month_name not in months:
                continue

            day, year = rest.split(",")

            day = int(day.strip())
            year = int(year.strip())
            month = months.index(month_name) + 1

        if month < 1 or month > 12:
            continue

        if day < 1 or day > 31:
            continue

        print(f"{year:04}-{month:02}-{day:02}")
        break

    except (ValueError, IndexError):
        pass
