# This program uses a loop to display tuition increase at a college for
# five years time
# 10/28/2018
# CTI-110 P4HW3 - Tuition Increase
# Jacob White
#
def main():
    currentTuition = 8000

# Print Table Headings
    print('Year\tTuition\n------\t-------')

# Print the Years and Tuition Increases

    for currentYear in range(1, 6):
        currentTuition += (0.03 * currentTuition)
        print( currentYear, '\t$', format( currentTuition, '.2f'))

main()



    
    
