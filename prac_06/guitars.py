from prac_06.guitar import Guitar


def sort_by_year(guitar):
    return guitar.year


def main():
    """Guitar program, using Guitar class."""
    guitars = []

    print("My guitars!")
    name = input("Name: ").title()
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(f"{guitar_to_add}, added.")
        name = input("Name: ").title()

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    guitars.sort(key=sort_by_year)  # Sort the list of guitars using the custom sorting function

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        print(f"Guitar {i}:  {guitar.name:>20} ({guitar.year}), worth $ {guitar.cost:10,.2f} {vintage_string}")


main()
