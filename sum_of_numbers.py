# sum_of_numbers.py
# Exercise selected: Chapter 10 program 3
# Name of program: Sum of Numbers
# Description of program: This program opens a file named numbers.dat
#   that contains a list of integers and calculates the sum of all the
#   integers.
#
# Ivan Boatwright
# March 19, 2016

def main():
    # Local variables
    fileName = 'numbers.dat'
    nums = []
    numSum = 0

    # Display the intro to the user.
    fluffy_intro()

    # Assign the integer contents of the file to the nums array.
    get_file_contents(fileName, nums)

    # Store the sum of the nums array in the numSum variable.
    numSum = sum(nums)

    # Display the results to the user.
    display_results(fileName, numSum)
    return None


# Displays an introduction to the program and describes what it does.
def fluffy_intro():
    print('Welcome to the Sum of Numbers program.')
    print('This program opens the numbers.dat file and displays')
    print('the sum of the integers read from the file.')
    return None


# This module accepts the filename and an array by reference as parameters.
#   It opens the file and converts each line into an integer and stores
#   it in the array.
def get_file_contents(fName, nums):
    with open(fName,'r') as f:
        nums.append(int(f.read()))
    f.close()
    return None

# Displays the summation results to the user.
def display_results(fName, numSum):
    print('The sum of all the integers in the {} file is: {}'.format(
                                                            fName, numSum))
    return None


###  temp functions for creating numbers.dat file  ###
# Returns a list of random ints. p is basically any formatting. r is the set the
#   random numbers are pulled from. l is how many elements to generate.
def rin(p='{}\n',r=(1,25),l=12):
    return [p.format(x) for x in [(int(x) * (random.random()+1.0)) for x in random.sample(range(*r),l)]]

# Call the main program.
main()