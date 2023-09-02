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
        elif choice == "s":
            save_projects(FILENAME)
        elif choice == "d":
            display_projects()
        elif choice == "f":
            filter_projects()
        # elif choice == "a":
        # elif choice == "u":
        else:
            print("Invalid input")
        print(MENU)
        choice = input(">>> ").lower()
    print("Thank you for using custom-built project management software.")


def filter_projects():
    """Filter and display projects that start after the input date."""
    filtered_date = input("Show projects that start after date (dd/mm/yy): ")
    filtered_date = datetime.datetime.strptime(filtered_date, "%d/%m/%Y").date()
    filtered_projects = []
    for project in projects:
        if project.start_date >= filtered_date:
            filtered_projects.append(project)
    filtered_projects.sort()
    for filtered_project in filtered_projects:
        print(filtered_project)


def display_projects():
    """Display sorted incompleted projects and completed projects nicely"""
    incompleted_projects = [project for project in projects if int(project.completion_percentage) < 100]
    incompleted_projects.sort()
    print("Incomplete projects: ")
    for incompleted_project in incompleted_projects:
        print(f"  {incompleted_project}")
    completed_projects = [project for project in projects if int(project.completion_percentage) == 100]
    completed_projects.sort()
    print("Complete projects: ")
    for completed_project in completed_projects:
        print(f"  {completed_project}")


def save_projects(filename):
    """Save update projects into projects.txt"""
    with open(filename, "w") as out_file:
        out_file.write("Name\tStart Date\tPriority\tEstimate\tCompletion\n")
        for project in projects:
            out_file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}"
                           f"\t{project.cost_estimate:.2f}\t{project.completion_percentage}\n")


def load_projects(filename):
    """Read the file, load projects data, and store as a list."""
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            name, start_date, priority, cost_estimate, completion = line.strip().split("\t")
            start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
            projects.append(Project(name, start_date, int(priority), float(cost_estimate), int(completion)))


main()
