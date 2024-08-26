# Write a program that keeps on accepting a number 
# from the user until the user enters Zero. 
# Display the sum and average of all the numbers.
def main():
    total_sum = 0
    count = 0

    while True:
        try:
            # Accept input from the user
            number = float(input("Enter a number (0 to stop): "))

            # Check if the user entered zero
            if number == 0:
                break

            # Update total sum and count
            total_sum += number
            count += 1

        except ValueError:
            print("Please enter a valid number.")

    # Calculate average if count is greater than zero
    if count > 0:
        average = total_sum / count
        print(f"Sum of all numbers: {total_sum:.2f}")
        print(f"Average of all numbers: {average:.2f}")
    else:
        print("No numbers were entered.")

if __name__ == "__main__":
    main()