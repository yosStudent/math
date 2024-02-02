import math

volume_of_the_can = float(1.25)

def input_f(prompt):
    while True:
        try:
            user_input = float(input(prompt).replace(',', '.'))
            return user_input
        except ValueError:
            print("Podaj poprawną liczbę.")

a = input_f("Podaj długość pomieszczenia (a): ")
b = input_f("Podaj szerokość pomieszczenia (b): ")
c = input_f("Podaj wysokość pomieszczenia (c): ")
z = input_f("Podaj wydajność farby (z): ")

room_area=2*(a*b+a*c+b*c)
from_1_bucket=z*volume_of_the_can


Window_width=0.9
Door_width=0.9
Window_height=1
Door_height=2

doors_amount=0
windows_amount=0

limit_of_windows=3
limit_of_doors=2

if c >= 2:
    for i in range(1, 6):
        if i == 1 and (0.3 * a >= Door_width or 0.3 * b >= Door_width) and doors_amount < limit_of_doors:
            doors_amount += 1
        elif i in [2, 3, 4] and windows_amount < limit_of_windows:
            if doors_amount==1 and i==2:
                windows_amount+=1
            elif (0.3 * a) - (doors_amount * Door_width) >= Window_width:
                windows_amount += 1
            elif (0.3 * b) - (doors_amount * Door_width) >= Window_width:
                windows_amount += 1
        elif i == 5 and (0.3 * a) - (doors_amount * Door_width) - (windows_amount * Window_width) >= Door_width and doors_amount < limit_of_doors:
            doors_amount += 1
else:
    print('Too low to make doors')



doors_and_windows_area=windows_amount*0.9+doors_amount*1.8

needed_amount_of_paint=(room_area/from_1_bucket-doors_and_windows_area)+1

print(f'Amount of doors: {doors_amount}\nAmount of windows: {windows_amount}\n\nTo paint it all u\'ll need {round(needed_amount_of_paint)} jars of paint')

    