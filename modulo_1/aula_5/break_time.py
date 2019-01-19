import webbrowser
import time

print("This program started on" + time.ctime())

num = 1
while (num <= 3):
	time.sleep(3)
	webbrowser.open("https://www.youtube.com/watch?v=UrIiLvg58SY")
	num+=1