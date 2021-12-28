# Criação de tela virtual.
import turtle
# Módulo de tempo.
import time
# Módulo aleatório.
import random

# Delay e pontos.
delay = 0.1
ponto = 0

# Função de criação de tela.
tela = turtle.Screen()
# Nome
tela.title('Jogo da Cobrinha')
# Background color
tela.bgcolor('black')
# A largura e altura
tela.setup(width=700, height=700)
tela.tracer(0)

# Cobrinha
cobra = turtle.Turtle()
cobra.shape('square')
cobra.color('white')
cobra.penup()
cobra.goto(0, 0)
cobra.direction = 'Stop'

# Comida da cobra
comida = turtle.Turtle()
cores = random.choice(['red', 'green', 'blue'])
formas = random.choice(['square', 'triangle', 'circle'])
comida.speed(0)
comida.shape(formas)
comida.color(cores)
comida.penup()
comida.goto(0, 100)


pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0 High Score: 0 ", align="center",
          font=("candara", 24, "bold"))


def cima():
    if cobra.direction != 'down':
        pass


def baixo():
    if cobra.direction != 'up':
        cobra.direction = "down"


def esquerda():
    if cobra.direction != 'right':
        cobra.direction = "left"


def direita():
    if cobra.direction != 'left':
        cobra.direction = "right"


def mover():
    if cobra.direction == 'up':
        y = cobra.ycor()
        cobra.sety(y+20)
    if cobra.direction == 'down':
        y = cobra.ycor()
        cobra.sety(y-20)
    if cobra.direction == 'left':
        x = cobra.ycor()
        cobra.sety(x-20)
    if cobra.direction == 'right':
        x = cobra.ycor()
        cobra.sety(x+20)


tela.listen()
tela.onkeypress(cima, "w")
tela.onkeypress(baixo, "s")
tela.onkeypress(esquerda, "a")
tela.onkeypress(direita, "d")

segments = []
# Jogo
while True:
    tela.update()
    if cobra.xcor() > 290 or cobra.xcor() < -290 or cobra.ycor() > 290 or cobra.ycor() < -290:
        time.sleep(1)
        cobra.goto(0, 0)
        cobra.direction = 'Stop'
        cores = random.choice(['red', 'green', 'blue'])
        formas = random.choice(['square', 'triangle', 'circle'])
        for segment in segments:
            segment.goto(1000, 1000)
        segment.clear()
        delay = 0.1
        ponto = 0
        pen.clear()
        pen.write("Score : {} High Score : {}".format(ponto, high_score), align="center", font=("candara", 24,"bold"))
        mover()