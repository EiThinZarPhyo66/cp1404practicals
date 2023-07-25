name = input("Name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

in_file = open("name.txt", "r")
in_file.close()
print("Your name is")

with open("numbers.txt", "r") as in_file:
print("Your name is")

