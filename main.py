import turtle
import time
import random

delay = 0.1

score = 0
high_score = 0

#Fenster einrichten
wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

#Kopf
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

#Essen
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Körper
segments = []

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Punke: 0 Beste Punktzahl: 0", align="center", font=("Courier", 24, "normal"))

#Funktionen
def go_up():
  if head.direction !="down":
    head.direction = "up"
def go_down():
  if head.direction !="up":
    head.direction = "down"
def go_left():
  if head.direction != "right":
    head.direction = "left"
def go_right():
  if head.direction != "left":
    head.direction = "right"

def move():
  if head.direction == "up":
    y = head.ycor()
    head.sety(y + 20)
  if head.direction == "down":
    y = head.ycor()
    head.sety(y-20)
  if head.direction == "left":
    x = head.xcor()
    head.setx(x+20)
  if head.direction == "right":
    x = head.xcor()
    head.setx(x-20)

#Kontrolle
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_right, "d")

#GameLoop
while True:
  wn.update()

  #Kollisionscheck
  if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "Stop"
    food.goto(0, 100)
    score = 0
    pen.clear()
    pen.write("Punke: {} Beste Punktzahl: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    #Köper verstecken
    for segment in segments:
      segment.goto(1000, 1000)

    #Köperarray clearen
    segments.clear()

  if head.distance(food) < 20:
    #Essen zu einer zufälligen Position bringen
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    food.goto(x, y)
    score += 10
    if score>high_score:
      high_score = score
    pen.clear()
    pen.write("Score: {} Beste Punktszahl: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    #Körper hinzufügen
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("grey")
    new_segment.penup()
    segments.append(new_segment)

  for index in range(len(segments)-1, 0, -1):
    x = segments[index-1].xcor()
    y = segments[index-1].ycor()
    segments[index].goto(x, y)

  if len(segments) > 0:
    x = head.xcor()
    y = head.ycor()
    segments[0].goto(x, y)

  move()

  #Kollisionscheck mit Körper
  for segment in segments:
    if segment.distance(head) < 20:
      time.sleep(1)
      head.goto(0, 0)
      head.direction = "stop"
      food.goto(0, 100)
      score = 0
      pen.clear()
      pen.write("Punke: {} Beste Punktzahl: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

      #Körper verstecken
      for segment in segments:
        segment.goto(1000, 1000)

        segments.clear()

    time.sleep(delay)

wn.mainloop()
