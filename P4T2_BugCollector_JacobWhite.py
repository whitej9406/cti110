# Program will collect bugs over a period of time and then display the total amt.
# 10/28/2018
# CTI-110 P4T2 - Bug Collector
# Jacob White
#
# Initialize the accumulator.
total = 0

# Get the bugs collected for each day.
for day in range(1, 8):
    # Prompt the user.
    print('Enter the bugs collected on day', day)

    # Input the number of bugs.
    bugs = int(input())

    # Add bugs to total.
    total += bugs

# Display the total bugs.
print('You collected a total of', total, 'bugs.')


    
