import turtle
import pygame
import os

# Function to change the background color
def change_background_color():
    colors = ["white", "lightblue", "lightgreen", "lightcoral", "lightyellow"]
    current_color = win.bgcolor()
    new_color = colors[(colors.index(current_color) + 1) % len(colors)]
    win.bgcolor(new_color)
    message = f"Background color changed to {new_color}"
    win.title(message)

# Check if the music file exists before loading
music_file = 'Amar_Sonar_Bangla.mp3'
if os.path.exists(music_file):
    pygame.mixer.init()
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(1)

obj = turtle.Turtle()
obj.speed(1)

win = turtle.Screen()
win.bgcolor("white")

# Set up the onkeypress event
win.listen()
win.onkeypress(change_background_color, "b")  # Press 'b' to change background color

obj.penup()
obj.goto(-100, 150)
obj.pendown()
obj.begin_fill()
obj.fillcolor("seagreen")
obj.setheading(0)
obj.forward(250)
obj.setheading(270)
obj.forward(150)
obj.setheading(180)
obj.forward(250)
obj.setheading(90)
obj.forward(150)
obj.end_fill()

obj.setheading(270)
obj.forward(122)
obj.setheading(360)

obj.penup()
obj.forward(120)
obj.pendown()

obj.begin_fill()
obj.fillcolor("red")
obj.circle(50)
obj.end_fill()

obj.setheading(180)
obj.penup()
obj.forward(120)
obj.pendown()

obj.begin_fill()
obj.fillcolor("orange")

obj.setheading(90)
obj.forward(150)
obj.setheading(180)
obj.forward(20)
obj.setheading(270)
obj.forward(400)
obj.setheading(180)
obj.forward(50)
obj.setheading(270)
obj.forward(30)
obj.setheading(360)
obj.forward(120)
obj.setheading(90)
obj.forward(30)
obj.setheading(180)
obj.forward(50)
obj.setheading(90)
obj.forward(400)
obj.end_fill()

obj.hideturtle()

# To close the Turtle graphics window gracefully
def close_window():
    pygame.mixer.music.stop()  # Stop the music
    pygame.quit()  # Close Pygame
    win.bye()  # Close Turtle graphics window

# Set up the close event handler
win.bye = close_window

turtle.done()
