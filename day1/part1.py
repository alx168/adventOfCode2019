def getFuel(mass):
    return (mass // 3) - 2

f = open("input.txt")
totalFuel = 0
for line in f:
    mass = int(line)
    totalFuel += getFuel(mass)

print(totalFuel)
