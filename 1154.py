ageList = []

while True:
    age = int(input())
    if age < 0:
        break
    ageList.append(age)

ageTotalSum = 0
for i in range(0, len(ageList)):
    ageTotalSum += ageList[i]

median = ageTotalSum / len(ageList)

print("%.2f" % median)
