frogJump, platforms = input().split()
frogJump = int(frogJump)
platforms = int(platforms)

platformHeight = input().split()
for i in range(len(platformHeight)):
    platformHeight[i] = int(platformHeight[i])

gameWin = True

for i in range(platforms - 1):
    if abs(platformHeight[i] - platformHeight[i+1]) > frogJump:
        gameWin = False

if gameWin:
    print("YOU WIN")
else:
    print("GAME OVER")
