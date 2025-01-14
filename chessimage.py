import pgzrun
import random

score = 0
HEIGHT = 800
WIDTH = 800

bg = Actor("chessboard")
pawn = Actor("chesspiece")
coin = Actor("rookcoin")
enemy = Actor("enemy")

direction = 1

pawn.pos = (200,300)
enemy.pos = (600,600)

def place_coin():
    coin.x = random.randint(0,WIDTH)
    coin.y = random.randint(0,HEIGHT)

def draw():
    bg.draw()
    pawn.draw()
    coin.draw()
    enemy.draw()
    screen.draw.text(f'Score: {score}', (10,15), color = (0,0,0), fontsize = 30)

def update():
    global score
    global direction
    enemy_move()

    if pawn.x > 800 or pawn.x<0:
        direction = direction*-1
    if pawn.y > 800 or pawn.y<0:
        direction = direction*1
    if keyboard.W:
        pawn.y -= 5
    if keyboard.A:
        pawn.x -= 5
    if keyboard.S:
        pawn.y += 5*direction
    if keyboard.D:
        pawn.x += 5*direction

    if pawn.colliderect(coin):
        score += 1
        place_coin()

if enemy.colliderect(pawn):
        exit()

def enemy_move():
    if enemy.x < pawn.x:
        enemy.x += 2
    elif enemy.x > pawn.x:
        enemy.x -= 2
    if enemy.y > pawn.y:
        enemy.y -= 2
    elif enemy.y < pawn.y:
        enemy.y += 2

pgzrun.go()
