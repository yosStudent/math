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

if c>=2:
    for i in range(1,5):
        if i==1:
            if 0.3*a>=0.9:
                doors_amount+=1
            elif 0.3*b>=0.9 and doors_amount<1:
                doors_amount+=1
                if doors_amount>1:
                    doors_amount=1
        if i!=1 and i!=5:
            if(0.3*a)-(doors_amount*0.9)>=0.9:
                windows_amount+=2
                if(0.3*a)-(doors_amount*0.9)-(windows_amount*0.9)>=0.9:
                    windows_amount+=1
            elif(0.3*b)-(doors_amount*0.9)>=0.9:
                windows_amount+=2
                if windows_amount>3:
                    windows_amount=3
                if(0.3*b)-(doors_amount*0.9)-(windows_amount*0.9)>=0.9:
                    windows_amount+=1
                    if windows_amount>3:
                        windows_amount=3
        if i==5:
            if(0.3*a)-(doors_amount*0.9)-(windows_amount*0.9)>=0.9:
                doors_amount+=1
                if doors_amount>1:
                    doors_amount=1
            elif 0.3*b>=0.9 and doors_amount<1:
                doors_amount+=1
else:
    print('Too low to made doors')

doors_and_windows_area=windows_amount*0.9+doors_amount*1.8

needed_amount_of_paint=room_area/from_1_bucket-doors_and_windows_area

print(needed_amount_of_paint)

