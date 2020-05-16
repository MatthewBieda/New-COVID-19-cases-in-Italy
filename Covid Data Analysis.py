from matplotlib import pyplot as plt

FILE_NAME = "C:\\Users\Matt\Desktop\italy.txt"

list_of_cases = []
counter = 0

for x in open(FILE_NAME, "r"):
    list_of_cases.append(x)

for i in range(0, len(list_of_cases)):
    list_of_cases[i] = int(list_of_cases[i])

new_cases = []

for i in range(len(list_of_cases) - 1):
    if list_of_cases[i] != 0:
        new_cases.append(list_of_cases[i + 1] - list_of_cases[i])

plt.plot(new_cases)
plt.show()
