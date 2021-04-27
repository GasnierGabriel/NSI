from math import ceil
import sys

def get_new_augmentation_var_values(width_augmentation_avancement : int, width_augmentation_moment : int, width_augmentation : int) -> tuple:
    width_augmentation_avancement = 0
    width_augmentation_moment += 2
    width_augmentation += 2
    return (width_augmentation_avancement, width_augmentation_moment, width_augmentation)


def get_width_last_mini_floor(n : int) -> int:  #calculate the width of the last mini floor of the pyramide
    width_floor, width_mini_floor, width_augmentation, width_augmentation_moment, width_augmentation_avancement = 3, 3, 6, 3, 1
    for i in range(n):
        for j in range(width_floor-1):
            width_mini_floor += 2
        if i == n-1:
            return width_mini_floor
        if width_augmentation_avancement == width_augmentation_moment:
            width_augmentation_avancement, width_augmentation_moment, width_augmentation = get_new_augmentation_var_values(width_augmentation_avancement, width_augmentation_moment, width_augmentation)
        width_mini_floor, width_floor, width_augmentation_avancement = (width_augmentation+ width_mini_floor, width_floor+1, width_augmentation_avancement+1)
    return width_mini_floor

def door_build(size_door, rank, size_floor, j, door):
    count = 0
    for i in range(size_door):
        if rank >= 5 and j == ceil(((size_floor - 2) / 2) + 1) and count == size_door-2:
            return door + '$|'
        door += '|'
        count += 1
    return door

def get_door_line(j, i, size_door, rank, size_floor) -> str:
    door = ""
    if j >= 2 and i == (rank - 1):
        door += door_build(size_door, rank, size_floor, j, door)
    else:
        door += size_door * "*"
    return door

def pyramide(n):
    if n <= 0:
        return print("(chaîne vide)")

    size_floor, size_mini_floor, size_door, door_augmentation_moment, door_augmentation_avancement, augmentation, augmentation_moment, augmentation_avancement = 3, 3, 1, 1, 1, 4, 3, 1
    for i in range(n):
        for j in range(size_floor):
            if i==0 and j ==0:
                print(int((get_width_last_mini_floor(n) - size_mini_floor + 2) / 2-1)* ' ' + '/*\\')
            else:
                size_mini_floor += 2
                print(int((get_width_last_mini_floor(n)-size_mini_floor+2)/2-1) * ' ' + '/' + int((size_mini_floor-size_door)/2-1)*"*" + get_door_line(j, i, size_door, n, size_floor) + int((size_mini_floor-size_door)/2-1)* "*" + '\\')
        if augmentation_avancement == augmentation_moment:
            augmentation_avancement, augmentation_moment, augmentation = 0, augmentation_moment+1, augmentation+2
        if door_augmentation_avancement == door_augmentation_moment:
            door_augmentation_avancement, door_augmentation_moment, size_door = 0, door_augmentation_moment+2, size_door+2
        augmentation_avancement, door_augmentation_avancement, size_mini_floor, size_floor = augmentation_avancement+1, door_augmentation_avancement+1, size_mini_floor+augmentation, size_floor+1

if len(sys.argv) == 1:
    print("Aucune valeun n'a été entrée")
else:
    pyramide(int(sys.argv[1]))
