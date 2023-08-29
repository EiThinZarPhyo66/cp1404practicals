from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    guitars = []
    with open(FILENAME, "r") as in_file:  # Read existing guitars from the file
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)

    guitars.sort()  # Sort the list of guitars by year
    in_file.close()

    for guitar in guitars:
        print(guitar)

    name = input("Name: ").title()
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(f"{guitar_to_add}, added.")
        name = input("Name: ").title()

    with open(FILENAME, "w") as out_file:
        for guitar in guitars:
            out_file.write(str(guitar) + "\n")


main()
