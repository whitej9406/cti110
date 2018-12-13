# This program takes a number grade and outputs a letter grade.
# 10/28/2018
# CTI-110 P3LAB Debugging
# Jacob White
#
def main():
# Define A-F Scores
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
# Get input from user
    score = int(input('Enter grade: '))
# Display the output
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
