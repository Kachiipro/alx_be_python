# This script will prompt the user to enter a positive integer, then use nested loops to print a square pattern of that size made of asterisks (*).

pattern = int(input("Enter the size of the pattern:"))

count = 1

while count <= pattern:
    for i in range(0, pattern):
        print("*", end="")

    count += 1
    print()
