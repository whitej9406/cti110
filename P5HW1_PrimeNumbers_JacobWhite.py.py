# Program takes user input and tells whether a number is prime or not
# 11/11/2018
# CTI-110 P5HW1 - Prime Numbers
# Jacob White
# Define isPrime function
# Use for and if statements to determine whether input is prime or not
# Define the main function
# get input
# display output
# call main function
def isPrime(num):
    evenDivisions = 0
    if num <= 1:
        return False
    for currentNumber in range(1, num + 1):
        if num % currentNumber == 0:
            evenDivisions = evenDivisions + 1
            if evenDivisions > 2:
                return False
    return True

def main():
    num = int(input('Please enter a number: '))
    if isPrime(num):
        print(num, 'is a prime number')
    else:
        print(num, 'is not a prime number')

main()

        
    
