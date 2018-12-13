# Program will draw a shape using nested loops
# 10/28/2018
# P4LAB - Nested Loops
# Jacob White
#
# Import Turtle
def main():
    import turtle
# Assign varibale t to turtle
    t = turtle.Turtle()
# Make turtle program background black
    turtle.Screen().bgcolor('black')
# Pen color cyan
    t.color('cyan')
# Display shape
    for i in range(10):
        for i in range(2):
            t.forward(100)
            t.right(60)
            t.forward(100)
            t.right(120)
            t.right(36)

main()

