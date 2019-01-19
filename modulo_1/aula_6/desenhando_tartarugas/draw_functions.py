import turtle

def draw_function():
	window = turtle.Screen()
	
	drawer = turtle.Turtle()
	drawer.speed(10)

	for x in range(-20, 20):
		y = f(x)
		drawer.setx(x)
		drawer.sety(y)
		drawer.dot()
		print("x: " + str(x) + " - y: " + str(y))

	window.exitonclick()

def f(num):
	return num*num


draw_function()
