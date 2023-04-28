#prob 1- file handling integers

# Open the input file for reading
with open("numbers.txt", "r") as input_file:
# Read the contents of the file into a list of integers
    numbers = [int(line.strip()) for line in input_file]