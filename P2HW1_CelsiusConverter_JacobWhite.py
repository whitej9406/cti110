# Convert Celsius to Fahrenheit.
# 9/22/2018.
# CTI-110 P2HW1 - Celsius Fahrenheit Converter.
# Jacob White.
# Pseudocode - Input the Celsius, Convert Celsius to Fahrenheit using the formule F = 9/5*C + 32, Display output.
celsius = float(input('Enter the celsius: '))

#Convert the Celsius to Fahrenheit
fahrenheit = celsius * 1.8 + 32

#Display the Conversion
print('The fahrenheit is ', format(fahrenheit, ',.2f'))
