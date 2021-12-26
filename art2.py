from turtle import *

for i in range(100):
	for j in range(5):
		forward(i * j)
		left(60)
		hideturtle()
		width(i/5+1)
		pencolor("orange")
	left(90)

#With color

color = ["red", "violet", "blue", "orange"]

for i in range(100):
	for j in range(5):
		forward(i * j)
		left(60)
		hideturtle()
		width(i/5+1)
		pencolor(color[i % 4])
	left(127)
