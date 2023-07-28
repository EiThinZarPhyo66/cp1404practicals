# 1
name = input("What is your name? ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# 2
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print("Your name is", name)

# 3
in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
print(number1+number2)

# 4.
total = 0
in_file = open("numbers.txt", "r")
for line in in_file:
    total += int(line)
in_file.close()
print(total)

