
from config import DEFAULT_NAME
from utils import square, is_even, celsius_to_fahrenheit, greet


def main():
    raw_value = input("Enter a number: ").strip()

    try:
        value = float(raw_value)
    except ValueError:
        print("Please enter a valid number.")
        return

    print(f"Square: {square(value)}")
    print(f"Even: {is_even(int(value))}")
    print(f"Fahrenheit: {celsius_to_fahrenheit(value)}")
    print(greet(DEFAULT_NAME))


if __name__ == "__main__":
    main()
