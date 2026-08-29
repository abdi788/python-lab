from utils import square, is_even, celsius_to_fahrenheit, greet

number = float(input("Enter a number: "))
name = input("Enter your name: ")

print("Square:", square(number))
print("Even:", is_even(number))
print("Fahrenheit:", celsius_to_fahrenheit(number))
print(greet(name))
