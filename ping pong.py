player1 = input('Enter Player 1 name : ')
player2 = input('Enter Player 2 name : ')
restart = 'y'
countdown = ['3','2','1','GO']
pause_countdown = ['10','9','8','7','6','5','4','3','2','1','GO']

while restart == 'y' or restart == 'Y':
  import turtle
  import time

  wind = turtle.Screen()
  wind.title('Ping Pong by Bremb')
  wind.bgcolor('black')
  wind.setup(width = 1000 , height = 800)
  wind.tracer(0)

  paddle1 = turtle.Turtle()
  paddle1.speed(0)
  paddle1.shape('square')
  paddle1.shapesize(stretch_wid= 6 , stretch_len= 1)
  paddle1.color('blue')
  paddle1.penup()
  paddle1.goto(-450,0)

  paddle2 = turtle.Turtle()
  paddle2.speed(0)
  paddle2.shape('square')
  paddle2.shapesize(stretch_wid= 6 , stretch_len= 1)
  paddle2.color('red')
  paddle2.penup()
  paddle2.goto(450,0)

  ball = turtle.Turtle()
  ball.speed(0)
  ball.shape('circle')
  ball.color('white')
  ball.penup()
  ball.goto(0,0)
  ball.dx = 0.7
  ball.dy = 0.7

  score1 = 0
  score2 = 0
  score = turtle.Turtle()
  score.speed(0)
  score.hideturtle()
  score.color('white')
  score.penup()
  score.goto(0,350)
  score.write(player1+' : '+str(score1)+'\t\t'+player2+' : '+str(score2) , align= 'center' , font= ('courier', 24 , 'normal'))

  pause_text = turtle.Turtle()
  pause_text.speed(0)
  pause_text.hideturtle()
  pause_text.color('grey')
  pause_text.penup()
  pause_text.goto(0,200)

  standby = turtle.Turtle()
  standby.speed(0)
  standby.hideturtle()
  standby.color('white')
  standby.penup()
  standby.goto(0,200)
  def paddle1_up():
    y = paddle1.ycor()
    if y < 320:
      y += 20
    paddle1.sety(y)
  def paddle1_down():
    y = paddle1.ycor()
    if y > -320:
      y -= 20
    paddle1.sety(y)
  def paddle2_up():
    y = paddle2.ycor()
    if y < 320:
      y += 20
    paddle2.sety(y)
  def paddle2_down():
    y = paddle2.ycor()
    if y > -320:
      y -= 20
    paddle2.sety(y)
  def pause():
    for sec in pause_countdown:
      pause_text.write( 'Game has been Paused\n\t '+sec , align= 'center' , font= ('courier', 40 , 'bold'))
      wind.update()
      time.sleep(1)
      pause_text.clear()

  for num in countdown:
    standby.write( num , align= 'center' , font= ('courier', 40 , 'bold'))
    wind.update()
    time.sleep(1)
    standby.clear()

  wind.listen()
  wind.onkeypress(paddle1_up , 'w')  
  wind.onkeypress(paddle1_down , 's') 
  wind.onkeypress(paddle2_up , 'Up') 
  wind.onkeypress(paddle2_down , 'Down') 
  wind.onkeypress(pause , 'Escape') 

  while True:
    wind.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() > 385 or ball.ycor() < -380 :
      ball.dy *= -1
    if ball.xcor() > 500 :
      ball.goto(0,0)
      ball.color('white')
      ball.dx *= -1
      score1 += 1
      score.clear()
      score.write(player1+' : '+str(score1)+'\t\t'+player2+' : '+str(score2) , align= 'center' , font= ('courier', 24 , 'normal'))
    elif ball.xcor() < -500 :
      ball.goto(0,0)
      ball.color('white')
      ball.dx *= -1
      score2 += 1
      score.clear()
      score.write(player1+' : '+str(score1)+'\t\t'+player2+' : '+str(score2) , align= 'center' , font= ('courier', 24 , 'normal'))
    if (ball.dx < 0) and (-450 < ball.xcor() < -430) and (paddle1.ycor() + 50 > ball.ycor() > paddle1.ycor() - 50):
      ball.color("blue")
      ball.dx *= -1
    elif (ball.dx > 0) and (450 > ball.xcor() > 430) and (paddle2.ycor() + 50 > ball.ycor() > paddle2.ycor() - 50):
      ball.color("red")
      ball.dx *= -1 
    if score1 == 5 :
      winner = turtle.Turtle()
      winner.speed(0)
      winner.hideturtle()
      winner.color('blue')
      winner.penup()
      winner.goto(0,200)
      winner.write(player1+' is the Winner' , align= 'center' , font= ('courier', 40 , 'bold'))
      break
    if score2 == 5 :
      winner = turtle.Turtle()
      winner.speed(0)
      winner.hideturtle()
      winner.color('red')
      winner.penup()
      winner.goto(0,200)
      winner.write(player2+' is the Winner' , align= 'center' , font= ('courier', 40 , 'bold'))
      break

  paddle1.goto(-450,0)
  paddle2.goto(450,0)
  wind.update()
  restart = input('Play again ? ')
  wind.clear()

print('Game Over')
