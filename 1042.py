array = input().split()

for i in range(len(array)):
    array[i] = int(array[i])

orderedArray = array.copy()

for i in range(len(orderedArray) - 1):
    for j in range(i + 1, len(orderedArray)):
        if orderedArray[i] > orderedArray[j]:
            orderedArray[i], orderedArray[j] = orderedArray[j], orderedArray[i]

for i in range(len(orderedArray)):
    print(orderedArray[i])

print()

for i in range(len(array)):
    print(array[i])
