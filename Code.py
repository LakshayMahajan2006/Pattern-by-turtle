# Pattern-by-turtle
#importing packages
import time
import math
import random

wn = turtle.Screen()
wn.title("By Lakshay Mahajan")

# Printing Pattern

lakshay = turtle.Turtle()

lakshay.color("red", "yellow")
lakshay.speed(500000)

for i in range(2000):
    lakshay.forward(10)
    lakshay.left(math.sin(i/10)*25)
    lakshay.left(20)
    
    
    
turtle.done()
