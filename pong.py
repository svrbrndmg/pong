import pygame as pg
import random as rm

pg.init()
pg.font.init()
run = True
begingame = True
clock = pg.time.Clock()
last = pg.time.get_ticks()
easycooldown = 450
mediumcooldown = 300
hardcooldown = 150

gamefont = pg.font.SysFont('Calibri', 24)

WIDTH = 300
HEIGHT = 300
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Pong")

leftwall = pg.draw.line(screen, "white", [0, 0], [0, HEIGHT], 5)
rightwall = pg.draw.line(screen, "white", [WIDTH, 0], [WIDTH, HEIGHT], 5)
topwall = pg.draw.line(screen, "white", [0, 0], [WIDTH, 0], 5)
bottomwall = pg.draw.line(screen, "white", [0, HEIGHT], [WIDTH, HEIGHT], 5)

ballx, bally = WIDTH/2 - 10, HEIGHT/2 - 10
ball = pg.draw.rect(screen, "white", pg.Rect(ballx, bally, 20, 20))

mousepos = pg.mouse.get_pos()
paddle1y = mousepos[1]
paddle2y = 40
paddle1 = pg.draw.rect(screen, "white", pg.Rect(5, paddle1y, 20, 60))
paddle2 = pg.draw.rect(screen, "white", pg.Rect(275, paddle2y, 20, 60))

velocity = pg.Vector2(3.5, 3)
ballpos = pg.Vector2(150, 150)

p1victory = 0
p2victory = 0

difficulty = input("Select your difficulty: ")
if difficulty == "easy":
    cooldown = easycooldown
elif difficulty == "medium":
    cooldown = mediumcooldown
elif difficulty == "hard":
    cooldown = hardcooldown
    
pg.time.delay(750)
while run:
    clock.tick(60)
    
    difference = [ballpos.y - 30, ballpos.y + 30, ballpos.y - 10, ballpos.y + 10]
    ballpos += velocity
    now = pg.time.get_ticks()
    if now - last >= cooldown:
          last = now
          paddle2y = rm.choice(difference)
    
    screen.fill("black")
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            
        if event.type == pg.MOUSEMOTION:
            mousepos = pg.mouse.get_pos()
            paddle1y = mousepos[1]

    if rightwall.colliderect(ball) and velocity.x > 0:
            p1victory += 1
            ballpos.x = 150
            ballpos.y = 150
    if leftwall.colliderect(ball) and velocity.x < 0:
            p2victory += 1
            ballpos.x = 150
            ballpos.y = 150
    if topwall.colliderect(ball) and velocity.y < 0:
            velocity.y *= -1
    if bottomwall.colliderect(ball) and velocity.y > 0:
            velocity.y *= -1
    if paddle1.colliderect(ball) and velocity.x < 0:
        velocity.x *= -1
        if velocity.y < 0:
            velocity.y *= 1
        if velocity.y > 0:
            velocity.y *= 1
    if paddle2.colliderect(ball) and velocity.x > 0:
        velocity.x *= -1
        if velocity.y > 0:
            velocity.y *= 1
        if velocity.y < 0:
            velocity.y *= 1
    if paddle1y > 240:
        paddle1y = 240
 
    paddle1 = pg.draw.rect(screen, "white", pg.Rect(5, paddle1y, 20, 60))
    paddle2 = pg.draw.rect(screen, "white", pg.Rect(275, paddle2y, 20, 60))
    net = pg.draw.line(screen, "white", [WIDTH/2, 0], [WIDTH/2, HEIGHT], 5)
    ball = pg.draw.rect(screen, "white", pg.Rect(ballpos.x, ballpos.y, 20, 20))
    leftwall = pg.draw.line(screen, "white", [0, 0], [0, HEIGHT], 5)
    rightwall = pg.draw.line(screen, "white", [WIDTH, 0], [WIDTH, HEIGHT], 5)
    topwall = pg.draw.line(screen, "white", [0, 0], [WIDTH, 0], 5)
    bottomwall = pg.draw.line(screen, "white", [0, HEIGHT], [WIDTH, HEIGHT], 5)

    p1points = gamefont.render(str(p1victory), False, "white")
    p2points = gamefont.render(str(p2victory), False, "white")
    screen.blit(p1points, (120, 10))
    screen.blit(p2points, (170, 10))
    
    pg.display.flip()
pg.quit()
