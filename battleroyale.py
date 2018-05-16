#!/usr/bin/env python
import sys

def findMinAmmo():
    global ammo, ammoList, minAmmo
    ammoList =[ammo]
    for enemy in enemyList:
        ammoRemaining = ammo - enemy[0]
        if ammoRemaining >= 0:
            if len(ammoList) < len(enemyList)+1:
                ammo = ammoRemaining + enemy[1]
                ammoList.append(ammo)
            else:
                minAmmo = ammoList[0]
                break
        else:
            ammo = ammoList.pop(0) + (enemy[0] - ammoList.pop(len(ammoList) - 1))
            findMinAmmo()

numTests = int(sys.stdin.readline())
lines = sys.stdin.readlines()
testIndex = 0

for i in range(numTests):
    totalEnemies = int(lines[testIndex])

    enemyList = []
    for j in range(1, totalEnemies + 1):
        enemy = lines[testIndex + j].split(" ")
        enemyList.append([int(enemy[0]), int(enemy[1])])

    minAmmo = 0
    ammo = enemyList[0][0]
    ammoCopy = ammo

    findMinAmmo()
    if minAmmo == 0:
        print(ammoCopy)
    else:
        print(minAmmo)
    testIndex += totalEnemies + 1
















