# sum_of_numbers.py
# Exercise selected: Chapter 10 program 3
# Name of program: Sum of Numbers
# Description of program: This program opens a file named numbers.dat
#   that contains a list of integers and calculates the sum of all the
#   integers.  The numbers.dat file is assumed to be a string of positive
#   integers separated by \n.
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
#   It opens the file, splits the string of integers by the '\n' delimiter,
#   converts each string into an integer and stores them in the nums list.
def get_file_contents(fName, nums):
    with open(fName,'r') as f:
        nums.extend([int(x) for x in f.read().split('\n')[:-1]])
    return None


# Displays the summation results to the user.
def display_results(fName, numSum):
    sep = '\n\n{}\n\n'.format('-'*79)
    print('{0}The sum of all the integers in the {1} file is: {2:>23} {0}'
          ''.format(sep, fName, numSum))
    return None


# Call the main program.
main()