# Name: Mekan Bayramov
# Date: October 17, 2026
# Description: Checks numbers from 1 to 50 for divisibility.

for number in range(1, 51):
    if number % 3 == 0 and number % 5 == 0:
        print("Divisible by both")
    elif number % 3 == 0:
        print("Divisible by three")
    elif number % 5 == 0:
        print("Divisible by five")
    else:
        print(number)