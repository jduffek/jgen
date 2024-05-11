import argparse
import random

# Define ANSI escape codes for text colors
COLOR_BLUE = '\033[0;34m'
COLOR_END = '\033[0m'  # Reset color to default

def generate_random_number(num_digits):
    # Generate a random number with the specified number of digits
    min_value = 10 ** (num_digits - 1)
    max_value = (10 ** num_digits) - 1
    return random.randint(min_value, max_value)

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Generate a random number with a specified number of digits")
    parser.add_argument("-d", "--digits", type=int, default=2, help="Number of digits for the random number (default: 2)")
    args = parser.parse_args()
    
    # Generate a random number with the specified number of digits
    random_number = generate_random_number(args.digits)
    
    # Print the random number to the command line in blue color
    print(COLOR_BLUE + "Random number:", random_number, COLOR_END)

if __name__ == "__main__":
    main()

#python3 jgen.py -d x  x=number of digits
