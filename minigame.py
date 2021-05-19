from turtle import Turtle

# Inicializar uma turtle
t = Turtle()

# Definir a velocidade
t.speed(1)


def obter_distancia():
    resposta = int(input('Quantos pixels devemos movimentar para a frente?  '))
    return resposta


def rotacionar_turtle(turtle):
    movimentar_para_lado = input(
        'Rotacionar para "d:direita", "e:esquerda" ou "n:nao rotacionar"  ')
    if movimentar_para_lado == 'd':
        rotacionar_para_direita(turtle)
    elif movimentar_para_lado == 'e':
        rotacionar_para_esquerda(turtle)


def rotacionar_para_direita(turtle):
    angulo = int(input('Quanto para a direita devemos rotacionar  '))
    t.right(angulo)


def rotacionar_para_esquerda(turtle):
    angulo = int(input('Quanto para a direita devemos rotacionar  '))
    t.left(angulo)


while True:

    direcao = input('Para qual direcao devemos ir? "f:frente" ou "t:tras"  ')

    if direcao == 'f':
        distancia = obter_distancia()
        rotacionar_turtle(t)
        t.forward(distancia)
    if direcao == 't':
        distancia = obter_distancia()
        rotacionar_turtle(t)
        t.backward(distancia)
    resposta = input('Continua andando: ')
    if resposta not in ('sim', 's'):
        break


""" # Movimentar a turtle para frente
t.forward(100)

# Rotacionar em X graus para a direita
t.right(90)
t.forward(100)

# Rotacionar em x graus para a esquerda
t.left(90)
t.forward(100)

# Movimentar a turtle para tras
t.backward(200)

input() """
