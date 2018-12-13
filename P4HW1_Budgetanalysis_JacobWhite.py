# Program will get expenses for the month and tell whether user is over or under budget
# 10/28/2018
# CTI-110 P4HW1 - Budget Analysis
# Jacob White
#
# Initialize the accumulator.
def main():
    total = 0
    budget = float(input('Enter your monthly budget: '))

# Get the expenses for each day.
    for day in range(1, 31):
    # Promt the user.
        print('Enter the expenses on day' , day)

    # Input the expense
        expense = int(input())

    # Add expenses to total.
        total += expense

# Display the
    if total > budget:
        print('You are over your budget by', total - budget)
    elif total < budget:
        print('You are under your budget by', budget - total)

main()


