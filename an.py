# This function counts the number of digits after the decimal point
def count_floating_points(number):
    # Convert the number to a string and split at the decimal point
    # If there's a decimal, it will count how many digits are after it
    if '.' in str(number):
        # Split the number into two parts: before and after the decimal
        parts = str(number).split('.')
        # Return the length (number of digits) after the decimal point
        return len(parts[1])
    else:
        # If there's no decimal, return 0
        return 0

# Test the function with a number
number = 2.5
# Call the function and print the result
print(count_floating_points(number))  # Output will be 1 because there's 1 digit after the decimal
