# CTI-110
# P3LAB - Debugging
# Jacob White
# 10/4/2018
# This program takes numeric grade input and outputs the letter grade.

def main():

    # system uses 10-point grading scale
    # Define scores
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    


    # user input
    score = input('Enter grade: ')
    # display output
    if score >= A_score:
        print('Your grade is: A')
    elif score >= B_score:
        print('Your grade is: B')
    elif score >= C_score:
        print('Your grade is: C')
    elif score >= D_score:
        print('Your grade is: D')

    else:
        print('Your grade is: F') 
    

# program start
main()
