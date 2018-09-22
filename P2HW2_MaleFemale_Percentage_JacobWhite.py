# Find percentage of males and females in a class
# 9/22/2018
# CTI-110 P2HW2 - Male Female Percentage
# Jacob White
# Pseudocode - Input number of males and females, calculate percentage of males and females, display percentage.
males = float( input( 'Enter number of males in the class: '))
females = float( input( 'Enter number of females in the class: '))
totalStudents = males + females

malePercentage = ( males / totalStudents ) * 100
femalePercentage = ( females / totalStudents ) * 100

print( 'The male percentage is: ' + format( malePercentage ) + '%')
print( 'The female percentage is: ' + format( femalePercentage ) + '%')
