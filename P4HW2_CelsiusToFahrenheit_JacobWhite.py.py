# Program should list 0-20 celsius and show fahrenheit conversion
# 10/28/2018
# CTI-110 P4HW2 = Celsius to Fahrenheit Table
# Jacob White
#
# Add headers and separate them
def main():
    print('Celsius\tFahrenheit')
    print('--------------')
# Add loop
    for celsius in range(21):
    # Calculate celsius to fahrenheit
        fahrenheit = ( 9 / 5 * celsius)  + 32
    # Display output
        print( celsius, '\t', format(fahrenheit, '.2f'))

main()

