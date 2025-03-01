file = open("students.txt", "r")

print("Reading Student Information:")
print()

lines = file.readlines()

for line in lines:
    print(line.strip())

file.close()