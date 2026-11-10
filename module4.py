# name: Mekan Bayramov
# Date: October 8,
#task1 - Prints Hello World to the screen.
print("Hello World")
#task2 - Asks the user for their name and greets them.
name = input("What is your name? ")
print("Hello", name )
#task3 -  Greets only Mekan and the Dr.Antonio.
name = input("What is your name? ")
if name == "Mekan":
    print("Hello Mekan!")
elif name == "Dr.Antonio":
    print("Hello Dr.Antonio!")
else:
    print("Sorry, you are not on the list.")
#task4 -Calculates the area of a circle.
radius = float(input("Enter the radius: "))
area = 3.14 * radius ** 2
print("The area of the circle is", area)
#task5 -Calculates miles per gallon for a car.
miles = float(input("Enter miles driven: "))
gallons = float(input("Enter gallons used: "))
mpg = miles / gallons
print("Your car gets", mpg, "miles per gallon.")
#task6 -Converts Fahrenheit to Celsius.
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print("The temperature is", celsius, "degrees Celsius.")
#task7 -Finds the day of the week when the user returns.
start_day = int(input("Enter starting day number (0-6): "))
stay = int(input("Enter number of nights: "))

return_day = (start_day + stay) % 7

print("You will return on day number", return_day)

