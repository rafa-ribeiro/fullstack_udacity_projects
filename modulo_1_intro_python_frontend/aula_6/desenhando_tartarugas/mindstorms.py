import turtle


def draw_shapes():
	window = turtle.Screen()
	window.bgcolor("red")

	brad = turtle.Turtle()

	# for i in range (0, 360):
	# 	draw_square(brad, 200)
	# 	brad.right(1)

	bob = turtle.Turtle()
	for i in range (0, 61):
		draw_triangle(bob, 300)
		bob.right(5)	

	# draw_circle(150)
	# draw_triangle(300, 150)

	window.exitonclick()

def draw_square(some_turtle, width):
	
	some_turtle.shape("turtle")
	some_turtle.speed (50)
	some_turtle.color("yellow")
	
	for i in range(0, 4):
		some_turtle.forward(width)
		some_turtle.right(90)

def draw_circle(width):
	angie = turtle.Turtle()
	angie.shape("arrow")
	angie.color("blue")
	angie.circle(width)
	angie.speed(6)

def draw_triangle(some_turtle, side):
	some_turtle.color("white")
	some_turtle.speed(50)

	for i in range(0, 3):
		some_turtle.forward(side)
		some_turtle.left(120)

draw_shapes()

	