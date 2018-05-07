#!/usr/bin/env python
import sys


numEnemies = int(sys.stdin.readline())
lines = sys.stdin.read().splitlines()
enemyList = []
for line in lines:
    line = line.split()
    enemyList.append(map(int,line))

minAmmo = 0
ammo = enemyList[0][0]

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


findMinAmmo()

print(minAmmo)
















