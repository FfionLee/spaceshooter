import pgzrun
import random

WIDTH=900
HEIGHT=600

ship=Actor('ship')
ship.pos=450,550

gameover=False
score=0

bullets=[]         

bees=[]
for i in range (random.randint(1,10)):
    bees.append(Actor('creature'))
    bees[i].x=random.randint(50,850)
    bees[i].y=50
 


def draw():
    screen.fill('black')
    ship.draw()
    for i in bees:
        i.draw()
    for i in bullets:
        i.draw()
    if gameover==True:
        screen.fill('red')
        screen.draw.text('Game Over',center=(250,300),color='black')
        '''screen.draw.text(str(score),center=(250,200),color='blue')'''

def update():
    global score, gameover
    if keyboard.left and ship.x>50:
        ship.x=ship.x-5
    if keyboard.right and ship.x<850:
        ship.x=ship.x+5
    if keyboard.space:
        '''print('hello')'''
        bullets.append(Actor('bullet'))
        bullets[-1].x=ship.x
        bullets[-1].y=ship.y
    for b in bullets:
        b.y=b.y-5
    for i in bees[:]:
        i.y=i.y+random.randint(1,3)
        for b in bullets[:]:
            if b.colliderect(i):
                bees.remove(i)
                score=score+1
    for e in bees:
        if e.y>600:
            gameover=True


pgzrun.go()