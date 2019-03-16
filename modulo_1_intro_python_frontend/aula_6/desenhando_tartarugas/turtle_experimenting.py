import turtle


def draw_square():
	window = turtle.Screen()
	window.bgcolor("black")

	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.speed (12)

	steps = 300
	angle = 90

	colors = ["red", "blue", "yellow", "green"]

	while (steps > 0):
		steps = steps - 10
		for i in range(0, 4):
			brad.color(colors[i])
			brad.forward(steps)
			brad.right(angle)

		pos = brad.pos()
		brad.goto(pos[0] + 5, pos[1] - 5)

	window.exitonclick()

draw_square()