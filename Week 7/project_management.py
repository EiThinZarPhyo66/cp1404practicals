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
        if choice =="l":
        elif choice == "s":
        elif choice == "d":
        elif choice == "f":
        elif choice == "a":
        elif choice == "u":
        else:
            print("Invalid input")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")

