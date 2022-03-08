import random

current_index = 0


def stylize_even(num):
    print("========== Even =============")
    print(num )
    print()
    current_index = 0

def stylize_odd(num):
    print("========== Odd =============")
    print(num )
    print()
    current_index = 51

print("this is an exaple of common coupling as stylize even and odd funtions both change the state of global variable ")

while (current_index < 100):
    print("=============")
    if (current_index % 2 ==0):
        stylize_even(current_index)
    else :
        stylize_odd(current_index)
    



