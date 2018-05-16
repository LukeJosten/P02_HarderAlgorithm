import random

def main():
    f = open("testing_input.txt", "w+")
    t = 19
    f.write(str(t) + "\n")
    for i in range(t):
        n = random.randrange(1, 100, 1)
        f.write(str(n) + "\n")
        for i in range(n):
            health = random.randrange(1, 200, 1)
            ammo = random.randrange(0, 200, 1)
            f.write(str(health) + " " + str(ammo) + "\n")
    f.close()

main()