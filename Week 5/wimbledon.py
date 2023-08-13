FILENAME = "wimbledon.csv"
CHAMPION_INDEX = 2
COUNTRY_INDEX = 1


def main():
    champion_to_count = {}
    countries = set()
    records = []
    count = 0
    process_file(records)
    extract_champion(champion_to_count, count, records)
    extract_country(countries, records)
    display_results(champion_to_count, countries)


def display_results(champion_to_count, countries):
    """Display champions and countries"""
    print("Wimbledon Champions:")
    for champion, count in champion_to_count.items():
        print(f"{champion} {count}")
    print()
    print(f"These {len(countries)} have won Wimbledon:\n{', '.join(sorted(countries))}")


def extract_country(countries, records):
    """Extract country from the records"""
    for record in records:
        countries.add(record[COUNTRY_INDEX])


def extract_champion(champion_to_count, count, records):
    """Extract champion from the records"""
    for record in records:
        champion_to_count[record[CHAMPION_INDEX]] = champion_to_count.get(record[CHAMPION_INDEX], count) + 1


def process_file(records):
    """Read the data from the file and store as a list"""
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for text in in_file:
            parts = text.strip().split(",")
            records.append(parts)


main()