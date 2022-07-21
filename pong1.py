# Write your code here :-)
import turtle
import time
import random
import winsound


wn=turtle.Screen()
wn.title("pong by akanksha")
wn.bgcolor('black')
wn.setup(width=800,height=600)
wn.tracer(0)



#scoreboard
score_a=0
score_b=0
start = time.time()





#paddle a
pad_a=turtle.Turtle()
pad_a.speed(0)
pad_a.shapesize(stretch_wid=5,stretch_len=1)
pad_a.shape("square")
pad_a.color('white')
pad_a.penup()
pad_a.goto(-350,0)



#paddle b
pad_b=turtle.Turtle()
pad_b.speed(0)
pad_b.shapesize(stretch_wid=5,stretch_len=1)
pad_b.shape("square")
pad_b.color('white')
pad_b.penup()
pad_b.goto(350,0)



#ball
pad_c=turtle.Turtle()
pad_c.speed(0)
pad_c.shape("square")
pad_c.color('white')
pad_c.penup()
pad_c.goto(0,0)

pad_c.dx=0.02
pad_c.dy=-0.02






#scoreboard
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()



pen.goto(0,260)
pen.write("player a:0 player b:0",align="center", font=("Courier",24,"normal"))


#fuction to define paddle
def pad_a_up():
    y=pad_a.ycor()
    y+=20
    pad_a.sety(y)
def pad_a_down():
    y=pad_a.ycor()
    y-=20
    pad_a.sety(y)
def pad_b_up():
    y=pad_b.ycor()
    y+=20
    pad_b.sety(y)
def pad_b_down():
    y=pad_b.ycor()
    y-=20
    pad_b.sety(y)
#keyboardbinding
wn.listen()
wn.onkeypress(pad_a_up,'w')
wn.onkeypress(pad_a_down,'s')
wn.onkeypress(pad_b_up,'Up')
wn.onkeypress(pad_b_down,'Down')





#main game loop
flag=True
while flag:

    wn.update()


    #Wmove
    pad_c.setx(pad_c.xcor()+pad_c.dx)
    pad_c.sety(pad_c.ycor()+pad_c.dy)
    #bordercheck
    pad_c.setx(pad_c.xcor()+pad_c.dx)
    if pad_c.ycor()>290:
        pad_c.sety(290)
        pad_c.dy*=-1
        winsound.PlaySound('C:/Users/Akankashagowri/Music/bounce.wave',winsound.SND_ASYNC)


    if pad_c.ycor()<-290:
        pad_c.sety(-290)
        pad_c.dy*=-1
        winsound.PlaySound('C:/Users/Akankashagowri/Music/bounce.wave',winsound.SND_ASYNC)

    if pad_c.xcor()>390:
         pad_c.goto(0,0)
         pad_c.dx*=-1
         score_a+=1
         pen.clear()
         pen.write("player a:{} player b:{}".format(score_a,score_b),align="center", font=("Courier",24,"normal"))

    if pad_c.xcor()<-390:
         pad_c.goto(0,0)
         pad_c.dx*=-1
         score_b+=1
         pen.clear()
         pen.write("player a:{} player b:{}".format(score_a,score_b),align="center", font=("Courier",24,"normal"))

    if(pad_c.xcor()>340 and pad_c.xcor()<350) and (pad_c.ycor()<pad_b.ycor()+40 and pad_c.ycor()>pad_b.ycor()-50):
        pad_c.dx*=-1
        pad_c.setx(340)
        winsound.PlaySound('C:/Users/Akankashagowri/Music/bounce.wave',winsound.SND_ASYNC)


    if(pad_c.xcor()<-340 and pad_c.xcor()>-350) and (pad_c.ycor()<pad_a.ycor()+40 and pad_c.ycor()>pad_a.ycor()-50):
        pad_c.dx*=-1
        pad_c.setx(-340)
        winsound.PlaySound('C:/Users/Akankashagowri/Music/bounce.wave',winsound.SND_ASYNC)





