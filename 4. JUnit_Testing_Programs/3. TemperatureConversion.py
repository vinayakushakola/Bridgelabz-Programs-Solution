"""
3. To the Util Class add temperaturConversion static function,
   given the temperature in fahrenheit as input
   outputs the temperature in Celsius
   or viceversa using the formula
   a. Celsius to Fahrenheit:   (°C × 9/5) + 32 = °F
   b. Fahrenheit to Celsius:   (°F − 32) x 5/9 = °C
"""


def celsius_to_fahrenheit(value):
    return (value * (9/5)) + 32


def fahrenheit_to_celsius(value):
    return (value - 32) * (5/9)


def main():
    value = int(input("Enter the value: "))
    op = int(input("Enter 1 for Celsius & 2 for Fahrenheit: "))
    if op == 1:
        print("Celsius to Fahrenheit:", celsius_to_fahrenheit(value))
    elif op == 2:
        print("Fahrenheit to Celsius:", fahrenheit_to_celsius(value))
    else:
        print("Invalid input!")

if __name__ == '__main__':
    main()

