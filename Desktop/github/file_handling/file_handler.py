#prob 1- file handling integers

# Open the input file for reading
with open("numbers.txt", "r") as input_file:
# Read the contents of the file into a list of integers
    numbers = [int(line.strip()) for line in input_file]
# Open the output files for writing
with open("even.txt", "w") as even_file, open("odd.txt", "w") as odd_file:
    # Loop over the numbers
    for number in numbers:
        # Check if the number is even
        if number % 2 == 0:
            even_file.write(str(number) + "\n")
        else:
            