import math

VOLUME_OF_CAN = 1.25
WINDOW_WIDTH = 0.9
DOOR_WIDTH = 0.9
WINDOW_HEIGHT = 1
DOOR_HEIGHT = 2
LIMIT_OF_WINDOWS = 3
LIMIT_OF_DOORS = 2

def input_f(prompt):
    while True:
        try:
            user_input = float(input(prompt).replace(',', '.'))
            return user_input
        except ValueError:
            print("Podaj poprawną liczbę.")

def calculate_paint_needed(a, b, c, z):
    room_area = 2 * (a * b + a * c + b * c)
    from_1_bucket = z * VOLUME_OF_CAN

    doors_amount = 0
    windows_amount = 0

    if c >= 2:
        for i in range(1, 6):
            if i == 1 and (0.3 * a >= DOOR_WIDTH or 0.3 * b >= DOOR_WIDTH) and doors_amount < LIMIT_OF_DOORS:
                doors_amount += 1
            elif i in [2, 3, 4] and windows_amount < LIMIT_OF_WINDOWS:
                if doors_amount == 1 and i == 2:
                    windows_amount += 1
                elif (0.3 * a) - (doors_amount * DOOR_WIDTH) >= WINDOW_WIDTH:
                    windows_amount += 1
                elif (0.3 * b) - (doors_amount * DOOR_WIDTH) >= WINDOW_WIDTH:
                    windows_amount += 1
            elif i == 5 and (0.3 * a) - (doors_amount * DOOR_WIDTH) - (windows_amount * WINDOW_WIDTH) >= DOOR_WIDTH and doors_amount < LIMIT_OF_DOORS:
                doors_amount += 1
    else:
        print('Too low to make doors')

    doors_and_windows_area = windows_amount * WINDOW_WIDTH + doors_amount * DOOR_WIDTH
    needed_amount_of_paint = (room_area / from_1_bucket - doors_and_windows_area) + WINDOW_WIDTH

    return doors_amount, windows_amount, round(needed_amount_of_paint)

a = input_f("Podaj długość pomieszczenia (a): ")
b = input_f("Podaj szerokość pomieszczenia (b): ")
c = input_f("Podaj wysokość pomieszczenia (c): ")
z = input_f("Podaj wydajność farby (z): ")

doors, windows, paint_needed = calculate_paint_needed(a, b, c, z)

print(f'Amount of doors: {doors}\nAmount of windows: {windows}\n\nTo paint it all u\'ll need {paint_needed} jars of paint')
