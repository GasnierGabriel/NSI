from math import *
import sys

def add(times, symbole):
    out = ""
    for i in range(int(times)):
        out += str(symbole)
    return out

def calc_last_mini_floor(n):
    size_floor, size_mini_floor, augmentation, augmentation_moment, augmentation_avancement = 3, 3, 6, 3, 0
    for i in range(n):
        for j in range(size_floor-1):
            size_mini_floor += 2
        if i == n-1:
            return size_mini_floor
        augmentation_avancement += 1
        if augmentation_avancement == augmentation_moment:
            augmentation_avancement = 0
            augmentation_moment += 1
            augmentation += 2
        size_mini_floor += augmentation
        size_floor += 1
    return size_mini_floor

def pyramide(n):
    if n <= 0:
        return print("(chaîne vide)")
    size_floor, size_mini_floor, size_door, door_augmentation_moment, door_augmentation_avancement, augmentation, augmentation_moment, augmentation_avancement = 3, 3, 1, 1, 1, 4, 3, 0

    for i in range(n):
        for j in range(size_floor):
            if i==0 and j ==0:
                mini_floor = add((calc_last_mini_floor(n) - size_mini_floor + 2) / 2-1, ' ') + '/*\\'
                print(mini_floor)
            else:
                size_mini_floor += 2
                mini_floor = add((calc_last_mini_floor(n)-size_mini_floor+2)/2-1, ' ') + '/' + add(((size_mini_floor-size_door)/2)-1, "*")
                if j >=2 and i==(n-1):
                    count = 0
                    for p in range(size_door):
                        if n >= 5:
                            if j == ceil(((size_floor-2)/2)+1):
                                if count == size_door-2:
                                    mini_floor += '$'
                                    count = 0
                                else:
                                    mini_floor += "|"
                                    count += 1
                            else:
                                mini_floor += "|"
                        else:
                            mini_floor += '|'
                else:
                    mini_floor += add(size_door, '*')
                mini_floor += add((size_mini_floor-size_door)/2-1, "*") + '\\'
                print(mini_floor)
        augmentation_avancement += 1
        if augmentation_avancement == augmentation_moment:
            augmentation_avancement, augmentation_moment, augmentation = 0, augmentation_moment+1, augmentation+2
        if door_augmentation_avancement == door_augmentation_moment:
            door_augmentation_avancement, door_augmentation_moment, size_door = 0, door_augmentation_moment+2, size_door+2
        door_augmentation_avancement += 1
        size_mini_floor += augmentation
        size_floor += 1

if len(sys.argv) == 1:
    print("Aucune valeun n'a été entrée")
else:
    pyramide(int(sys.argv[1]))
