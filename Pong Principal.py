import turtle

janela = turtle.Screen()
janela.title('Pong by C4mp3L0')
janela.bgcolor('black')
janela.setup(width=800, height=600)
janela.tracer(0)

# Pontuação
pontuacaoJogadorA = 0
pontuacaoJogadorB = 0


# Características da Minha Raquete:
minhaRaquete = turtle.Turtle()
minhaRaquete.speed(0)
minhaRaquete.shape('square')
minhaRaquete.color('white')
minhaRaquete.shapesize(stretch_wid=5, stretch_len=1)
minhaRaquete.penup()
minhaRaquete.goto(-350, 0)

# Características da Raquete do Oponente:
raqueteOponente = turtle.Turtle()
raqueteOponente.speed(0)
raqueteOponente.shape('square')
raqueteOponente.color('white')
raqueteOponente.shapesize(stretch_wid=5, stretch_len=1)
raqueteOponente.penup()
raqueteOponente.goto(350, 0)

# Bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape('square')
bola.color('white')
bola.penup()
bola.goto(0, 0)
bola.dx = 0.2
bola.dy = -0.2

# Placar
placar = turtle.Turtle()
placar.speed(0)
placar.color('white')
placar.penup()
placar.hideturtle()
placar.goto(0, 260)
placar.write('Jogador A: 0 | Jogador B: 0', align='center', font=('Courier', 24, 'normal'))


# Função
def minhaRaqueteParaCima():
    y = minhaRaquete.ycor()
    y += 20
    minhaRaquete.sety(y)


def minhaRaqueteParaBaixo():
    y = minhaRaquete.ycor()
    y -= 20
    minhaRaquete.sety(y)


def raqueteOponenteParaCima():
    y = raqueteOponente.ycor()
    y += 20
    raqueteOponente.sety(y)


def raqueteOponenteParaBaixo():
    y = raqueteOponente.ycor()
    y -= 20
    raqueteOponente.sety(y)


# Comandos no Teclado
janela.listen()
janela.onkeypress(minhaRaqueteParaCima, 'w')
janela.onkeypress(minhaRaqueteParaBaixo, 's')
janela.onkeypress(raqueteOponenteParaCima, 'Up')
janela.onkeypress(raqueteOponenteParaBaixo, 'Down')

# Loop do jogo principal.
while True:
    janela.update()

    # Movimento da Bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    # Limites da Borda
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1

    elif bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1

    elif bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dx *= -1
        pontuacaoJogadorA += 1
        placar.clear()
        placar.write(f'Jogador A: {pontuacaoJogadorA} | Jogador B: {pontuacaoJogadorB}', align='center', font=('Courier', 24, 'normal'))

    elif bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *= -1
        pontuacaoJogadorB += 1
        placar.clear()
        placar.write(f'Jogador A: {pontuacaoJogadorA} | Jogador B: {pontuacaoJogadorB}', align='center', font=('Courier', 24, 'normal'))

    # Colisão da bola com a raquete
    elif (bola.xcor() > 340 and bola.xcor() < 350) and (
            bola.ycor() < raqueteOponente.ycor() + 40 and bola.ycor() > raqueteOponente.ycor() - 40):
        bola.setx(340)
        bola.dx *= -1

    elif (bola.xcor() < -340 and bola.xcor() > -350) and (
            bola.ycor() < minhaRaquete.ycor() + 40 and bola.ycor() > minhaRaquete.ycor() - 40):
        bola.setx(-340)
        bola.dx *= -1
