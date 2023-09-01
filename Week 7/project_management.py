import datetime
from project import Project

MENU = "(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new project" \
       "\n(U)pdate project\n(Q)uit"
FILENAME = "projects.txt"
projects = []


def main():
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "l":
            load_projects(FILENAME)
            # elif choice == "s":
            # elif choice == "d":
            # elif choice == "f":
            # elif choice == "a":
            # elif choice == "u":
            # else:
            print("Invalid input")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Read the file, load projects data, and store as a list."""
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            name, start_date, priority, cost_estimate, completion = line.strip().split("\t")
            start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
            project = Project(name, start_date, int(priority), float(cost_estimate), int(completion))
            projects.append(project)


main()
