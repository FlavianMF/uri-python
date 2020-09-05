measures = int(input())

heights = input().split()
for i in range(measures):
    heights[i] = int(heights[i])

Nlogonia = True

if measures == 0 or measures == 1:
    Nlogonia = False
elif measures == 2 and heights[0] == heights[1]:
    Nlogonia = False
else:
    lastDiference = heights[0] - heights[1]

for i in range(1, measures-1):
    diference = heights[i] - heights[i + 1]
    if lastDiference > 0 and diference >= 0:
        Nlogonia = False
        break
    elif lastDiference < 0 and diference <= 0:
        Nlogonia = False
        break
    lastDiference = diference

if Nlogonia:
    print(1)
else:
    print(0)
