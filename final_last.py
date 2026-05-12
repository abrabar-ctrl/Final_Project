import turtle
import random
import time
import math

# Advanced settings
city_turtle = turtle.Turtle()
city_turtle.color("lightgray")
city_turtle.speed(3)
city_turtle.shape("blank")
city_bay = turtle.Turtle()
city_bay.shape("blank")
city_bay.color("skyblue")
t1 = turtle.Turtle() # stars
t2 = turtle.Turtle() # stars
moon = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t1.speed(0) # Fastest
t1.width(1)
t1.shape("blank")
t2.shape("blank")
t2.speed(0)
t2.width(1)
moon.shape("circle")
moon.color(random.choice(["gold","maroon", "navy", "chocolate", "saddlebrown", "darkolivegreen", "purple"]))
moon.shapesize(7)

cloud_turtle = turtle.Turtle()
cloud_turtle.speed(0)
cloud_turtle.shape("blank")

track = turtle.Turtle()
track.hideturtle()
light = turtle.Turtle()
light.hideturtle()



for i in range(1): # moon
    moon.penup()
    moon.color(random.choice(["gold","maroon", "navy", "chocolate", "saddlebrown", "darkolivegreen", "purple"]))
    moon.speed(1.43)
    moon.goto(-287, 0)
    moon.color(random.choice(["gold","maroon", "navy", "chocolate", "saddlebrown", "darkolivegreen", "purple"]))
    moon.shapesize(6)
    moon.goto(-157, 0)
    moon.color(random.choice(["gold","maroon", "navy", "chocolate", "saddlebrown", "darkolivegreen", "purple"]))
    moon.goto(140, 0)
    moon.color(random.choice(["gold","maroon", "navy", "chocolate", "saddlebrown", "darkolivegreen", "purple"]))
    moon.goto(200, 0)
    moon.color(random.choice(["gold","maroon", "navy", "chocolate", "saddlebrown", "darkolivegreen", "purple"]))
    moon.goto(260, 0)
    moon.color(random.choice(["gold","maroon", "navy", "chocolate", "saddlebrown", "darkolivegreen", "purple"]))
    moon.goto(210, 0)
    moon.color(random.choice(["gold","maroon", "navy", "chocolate", "saddlebrown", "darkolivegreen", "purple"]))
    moon.goto(-187, 0)
    moon.color(random.choice(["gold","maroon", "navy", "chocolate", "saddlebrown", "darkolivegreen", "purple"]))
    moon.goto(-247, 0)
    moon.color(random.choice(["gold","maroon", "navy", "chocolate", "saddlebrown", "darkolivegreen", "purple"]))
    moon.goto(-347, 0)
    moon.shapesize(5)
    moon.color(random.choice(["gold","maroon", "navy", "chocolate", "saddlebrown", "darkolivegreen", "purple"]))
    moon.speed(1)
    moon.shapesize(5)
    moon.goto(-347, 175)
    moon.color(random.choice(["gold","maroon", "navy", "chocolate", "saddlebrown", "darkolivegreen", "purple"]))
    moon.goto(-347, 343)
    moon.color("powderblue")
    moon.shapesize(3)






for i in range(6):  # stars
        t1.penup()
        t2.penup()
        t1.goto(-290, 340)
        t1.pendown()
        t2.goto(-220, 310)
        t2.pendown()
        t1.color("white")
        t2.color("blue")
        t1.forward(i * .25)
        t2.forward(i * .25)
        t1.right(251)
        t2.left(251)
        t1.color("white")
        t2.color("white")
        t1.forward(i * .72)
        t2.forward(i * .72)
        t1.right(251)
        t2.left(251)
        t1.penup()
        t2.penup()
        t1.goto(-170, 340)
        t1.pendown()
        t2.goto(-40, 320)
        t2.pendown()
        t1.color("white")
        t2.color("yellow")
        t1.forward(i * .20)
        t2.forward(i * .20)
        t1.right(251)
        t2.left(251)
        t1.color("white")
        t2.color("white")
        t1.forward(i * .72)
        t2.forward(i * .72)
        t1.right(251)
        t2.left(251)
        t1.penup()
        t2.penup()
        t1.goto(50, 330)
        t1.pendown()
        t2.goto(140, 300)
        t2.pendown()
        t1.color("white")
        t2.color("orange")
        t1.forward(i * .20)
        t2.forward(i * .20)
        t1.right(251)
        t2.left(251)
        t1.color("white")
        t2.color("white")
        t1.forward(i * .72)
        t2.forward(i * .72)
        t1.right(251)
        t2.left(251)
        t1.penup()
        t2.penup()
        t1.goto(270, 350)
        t1.pendown()
        t2.goto(360, 275)
        t2.pendown()
        t1.color("white")
        t2.color("white")
        t1.forward(i * .20)
        t2.forward(i * .20)
        t1.right(251)
        t2.left(251)
        t1.color("white")
        t2.color("white")
        t1.forward(i * .72)
        t2.forward(i * .72)
        t1.right(251)
        t2.left(251)
        t1.penup()
        t1.goto(-105,380)
        t1.pendown()
        t1.color("white")
        t1.forward(i * .20)
        t1.right(251)
        t1.color("white")
        t1.forward(i * .72)
        t1.right(251)

 # cityline
for i in range(1):  #cityline
    city_turtle.penup()
    city_turtle.pensize(3.7)
    city_turtle.goto(-355, 300)
    city_turtle.pendown()
    city_turtle.circle(40)
    city_turtle.penup()
    city_turtle.goto(-450, 0)
    city_turtle.pendown()
    city_turtle.begin_fill()
    city_turtle.goto(-450, 100)
    city_turtle.goto(-410, 100)
    city_turtle.goto(-410, 250)
    city_turtle.goto(-380, 250)
    city_turtle.goto(-380, 140)
    city_turtle.goto(-340, 140)
    city_turtle.goto(-340, 180)
    city_turtle.goto(-315, 180)
    city_turtle.goto(-315, 250)
    city_turtle.goto(-290, 250)
    city_turtle.goto(-290, 170)
    city_turtle.goto(-280, 170)
    city_turtle.goto(-280, 140)
    city_turtle.goto(-245, 140)
    city_turtle.goto(-245, 200)
    city_turtle.goto(-220, 200)
    city_turtle.goto(-220, 210)
    city_turtle.goto(-200, 210)
    city_turtle.goto(-200, 150)
    city_turtle.goto(-180, 150)
    city_turtle.goto(-180, 280)
    city_turtle.goto(-150, 280)
    city_turtle.goto(-150, 205)
    city_turtle.goto(-115, 205)
    city_turtle.goto(-115, 160)
    city_turtle.goto(-95, 160)
    city_turtle.goto(-95, 240)
    city_turtle.goto(-65, 240)
    city_turtle.goto(-65, 200)
    city_turtle.goto(-30, 200)
    city_turtle.goto(-30, 275)
    city_turtle.goto(15, 275)
    city_turtle.goto(15, 245)
    city_turtle.goto(43, 245)
    city_turtle.goto(43, 150)
    city_turtle.goto(76, 150)
    city_turtle.goto(76, 120)
    city_turtle.goto(106, 120)
    city_turtle.goto(106, 270)
    city_turtle.goto(140, 270)
    city_turtle.goto(140, 140)
    city_turtle.goto(180, 140)
    city_turtle.goto(180, 200)
    city_turtle.goto(205, 200)
    city_turtle.goto(205, 280)
    city_turtle.goto(235, 280)
    city_turtle.goto(235, 150)
    city_turtle.goto(275, 150)
    city_turtle.goto(275, 250)
    city_turtle.goto(305, 250)
    city_turtle.goto(305, 240)
    city_turtle.goto(345, 240)
    city_turtle.goto(345, 190)
    city_turtle.goto(385, 190)
    city_turtle.goto(385, 220)
    city_turtle.goto(420, 220)
    city_turtle.goto(420, 290)
    city_turtle.goto(465, 290)
    city_turtle.goto(465, 290)
    city_turtle.goto(500, 290)
    city_turtle.goto(500, 170)
    city_turtle.goto(530, 170)
    city_turtle.goto(530, 190)
    city_turtle.goto(560, 190)
    city_turtle.goto(560, 190)
    city_turtle.penup()







for i in range(1):  # WATER 
    city_bay.penup()    
    city_bay.speed(7)
    city_bay.goto(-425,-100)
    city_bay.pendown()
    city_bay.fillcolor("steelblue")
    city_bay.begin_fill()
    city_bay.pensize(4)
    city_bay.goto(-330, -97)
    city_bay.goto(-260, -105)
    city_bay.goto(-200, -97)
    city_bay.goto(-116, -104)
    city_bay.goto(-500, -350)
    city_bay.goto(-425, -100)
    city_bay.penup()
    city_bay.end_fill()
    city_bay.goto(109,-99)
    city_bay.pendown()
    city_bay.begin_fill()
    city_bay.fillcolor("steelblue")
    city_bay.goto(500, -365)
    city_bay.goto(420,-103)
    city_bay.goto(109, -99)
    city_bay.pendown()
    city_bay.end_fill()
    city_bay.goto(185,-98)
    city_bay.penup()
    city_bay.goto(238, -101)
    city_bay.pendown()
    city_bay.goto(270, -106)
    city_bay.goto(342,-98)
    city_bay.goto(420,-103)
    city_bay.penup()










for i in range(1):      # B R I D G E L I N E
    track.penup()          
    track.goto(-17, -40)     # bridge structure
    track.pendown()
    track.color("darkgoldenrod")
    track.speed(10.5)
    track.width(3.5)
    track.goto(17,-40)
    track.goto(17, 80)
    track.penup()
    track.goto(-17, 60)
    track.pendown()
    track.goto(17, 40)
    track.penup()
    track.goto(-17, 40)
    track.pendown()
    track.goto(17, 40)
    track.penup()
    track.goto(-17, 60)
    track.pendown()
    track.goto(17, 60)
    track.penup()
    track.goto(-17, 80)
    track.pendown()
    track.goto(-17, 40)
    track.pendown()
    track.goto(17, 60)
    track.penup()
    track.goto(-17, 40)
    track.pendown()
    track.goto(-17, -40) 
    track.goto(-500, -350)
    track.penup()
    track.pensize(1)
    track.goto(17, 80)
    track.pendown()
    track.goto(4, -15)
    track.goto(4, -40)
    track.goto(-4, -40)
    track.goto(-4, -15)
    track.goto(-17, 80)
    track.penup()
    track.goto(-4, -15)
    track.pendown()
    track.goto(4, -15)
    track.goto(4, -19)
    track.goto(-4, -19)
    track.penup()
    track.goto(10, 30)
    track.pendown()
    track.goto(10, -40)
    track.penup()
    track.goto(-10, 30)
    track.pendown()
    track.goto(-10, -40)
    track.penup()











    track.penup()
    track.pensize(3)
    track.goto(-17,80)       # bridge horizontal
    track.pendown()
    track.circle(425, extent=-180)
    track.penup()
    track.goto(17, 80)
    track.pendown()
    track.circle(-418, extent=-200)
    track.penup()
    track.goto(17, -40)
    track.pendown()
    track.goto(500, -365)
    track.penup()             #  VERT BRIDGE LINES
    track.goto(-28, -47) # line 1 L
    track.width(2)
    track.pendown()
    track.goto(-28, 81)
    track.penup()
    track.goto(-42, -58)   # lines 2 L
    track.pendown()
    track.goto(-42, 82)
    track.penup()
    track.goto(-59, -69)   # line 3  L
    track.width(3)
    track.pendown()
    track.goto(-59, 81)
    track.penup()
    track.goto(-86, -87) # line 4  L
    track.width(3)
    track.pendown()
    track.goto(-86, 86)
    track.penup()
    track.goto(-125, -111)   # lines 5  L
    track.pendown()
    track.goto(-125, 96)
    track.penup()
    track.goto(-175, -140)   # line 6  L
    track.width(3.5)
    track.pendown()
    track.goto(-175, 110)
    track.penup()
    track.goto(-245, -187)   # lines 7  L
    track.pendown()
    track.goto(-245, 151)
    track.penup()
    track.goto(-322, -232) # lines 8  L
    track.width(4.0)
    track.pendown()
    track.goto(-322, 211)
    track.penup()
    track.goto(-420, -295)   # lines 9  L
    track.width(4.5)
    track.pendown()
    track.goto(-420, 366)
    track.penup()
    track.goto(28, -47) # line 1 R
    track.width(2)
    track.pendown()
    track.goto(28, 81)
    track.penup()
    track.goto(42, -58)   # lines 2 R
    track.pendown()
    track.goto(42, 82)
    track.penup()
    track.goto(59, -69)   # line 3 R
    track.width(3)
    track.pendown()
    track.goto(59, 81)
    track.penup()
    track.goto(86, -87) # line 4 R
    track.width(3)
    track.pendown()
    track.goto(86, 86)
    track.penup()
    track.goto(125, -111)   # lines 5 R
    track.pendown()
    track.goto(125, 96)
    track.penup()
    track.goto(175, -142)   # line 6 R
    track.width(3.5)
    track.pendown()
    track.goto(175, 110)
    track.penup()
    track.goto(245, -189)   # lines 7 R
    track.pendown()
    track.goto(245, 149)
    track.penup()
    track.goto(322, -241) # lines 8 R
    track.width(4.0)
    track.pendown()
    track.goto(322, 211)
    track.penup()
    track.goto(410, -301)   # lines 9 R
    track.width(4.5)
    track.pendown()
    track.goto(410, 357)
    track.penup()
    

    












    track.color("gainsboro")    # R O A D   L I N E S
           
    track.goto(0, -42)
    track.pendown()
    track.goto(0, -50)
    track.penup()
    track.goto(0, -65)
    track.pendown()
    track.goto(0, -75)
    track.penup()
    track.goto(0, -90)
    track.pendown()
    track.goto(0, -105)
    track.penup()
    track.goto(0, -120)
    track.pendown()
    track.goto(0, -138)
    track.penup()
    track.goto(0, -158)
    track.pendown()
    track.goto(0, -178)
    track.penup()
    track.goto(0, -202)
    track.pendown()
    track.goto(0, -228)
    track.penup()
    track.goto(0, -260)
    track.pendown()
    track.goto(0, -300)
    track.penup()
    track.goto(0, -340)
    track.pendown()
    track.goto(0, -390)
    track.penup()
    track.goto(210, -180)      # S I G N
    track.pendown()
    track.pensize(4)
    track.color("darkgreen")
    track.goto(210, -123)
    track.fillcolor("goldenrod")
    track.begin_fill()
    track.goto(255, -78)
    track.goto(210, -33)
    track.goto(164,-78)
    track.goto(210, -123)
    track.end_fill()
    track.penup()




for i in range(1):         # BIRDS?
    track.color("lightcyan")
    track.speed(7.5)
    track.width(2)
    track.penup()          
    track.goto(-270, 110)
    track.pendown()
    track.setheading(135)
    track.circle(5, extent=105)
    track.circle(-5, extent=-105)
    track.penup()
    track.goto(-335, 0)
    track.pendown()
    track.setheading(105)
    track.circle(5, extent=100)
    track.circle(-5, extent=-100)
    track.penup()
    track.goto(-255, -60)
    track.pendown()
    track.setheading(140)
    track.circle(5, extent=105)
    track.circle(-5, extent=-105)
    track.penup()
    track.goto(-195, -35)
    track.pendown()
    track.setheading(145)
    track.circle(5, extent=100)
    track.circle(-5, extent=-100)
    track.penup()
    track.goto(-145, -55)
    track.pendown()
    track.setheading(120)
    track.circle(5, extent=100)
    track.circle(-5, extent=-100)
    track.penup()

    








def blink(): # sign
    global visible
    # 1. Clear previous text
    text_turtle.clear()
    
    # 2. Write text only if visibility is True
    if visible:
        text_turtle.write(" Turtle-Town\n     0.1 MPH", align="center", font=("Arial", 8, "bold"))
    
    # 3. Flip the flag and schedule the next blink
    visible = not visible
    screen.ontimer(blink, 500) # 500ms = 0.5 seconds

# Setup
screen = turtle.Screen()
screen.bgcolor("black")
text_turtle = turtle.Turtle()
text_turtle.color("black")
text_turtle.hideturtle()
text_turtle.penup()
text_turtle.goto(210, -93)
text_turtle.pendown()

visible = True
blink()

screen.mainloop()


turtle.done()
