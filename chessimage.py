import pgzrun

HEIGHT = 800
WIDTH = 800

pawn = Actor("chesspiece")
direction = 1

pawn.pos = (200,300)

def draw():
    screen.fill((100,100,100))
    pawn.draw()

def update():
    global direction
    if pawn.x > 800 or pawn.x<0:
        direction = direction*-1
    if keyboard.W:
        pawn.y = direction*-1
    if keyboard.A:
        pawn.x = direction*-1
    if keyboard.S:
        pawn.y += 5*direction

pgzrun.go()
