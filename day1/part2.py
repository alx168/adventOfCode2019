def getFuel(mass):
    return (mass // 3) - 2

f = open("input.txt")
totalFuel = 0
for line in f:
    mass = int(line)
    test = 0
    while mass > 0: 
        fuel = getFuel(mass)
        if fuel > 0:
            totalFuel += fuel 
            test += fuel 
        mass = fuel

print(totalFuel)
