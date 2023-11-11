import pygame
import random
pygame.init()
size=width,height=(1000,800)
screen=pygame.display.set_mode(size)
p1=pygame.Rect(0,height/2-100/2,20,150)
p2=pygame.Rect(width-20,height/2-100/2,20,150)
bg=pygame.transform.scale(pygame.image.load("bg.png"),(width,height))
##ball=pygame.Rect(width/2,height/2)
ball=pygame.transform.scale(pygame.image.load("ball.gif"),(80,80))
ballr=ball.get_rect()
ballr.x=width/2-ballr.width/2
ballr.y=height/2-ballr.height/2
ok=False
move=15
move2=16
def reset():
    global x,y,move
    p1.y=height/2-100/2
    p2.y=p1.y
    ballr.x=width/2-ballr.width/2
    ballr.y=height/2-ballr.height/2
    if random.randint(0,1)==0:
        x=move-1
    else:
        x=-move+1
    y=0
reset()
run=True
score1=0
score2=0
win=pygame.font.SysFont("arial",60,True)
clock=pygame.time.Clock()
while run:
    clock.tick(60)
    screen.blit(bg,(0,0))
    msg=win.render(f"{score1}  :  {score2}",1,(255,255,255))
    mgr=msg.get_rect()
    mgr.center=width/2-mgr.width/2,10
    ballr.move_ip([x,y])
    if ballr.colliderect(p1):
        x=move
        if p2.y>height/2:
            y=move
        if p2.y<height/2:
            y=-move
    if ballr.colliderect(p2):
        x=-move
        if p1.y>height/2:
            y=move
        if p1.y<height/2:
            y=-move
    if ballr.y>=height-80:
        y=-move
    if ballr.y<=0:
        y=move
    if ballr.x>=width+400:
        reset()
        score1+=1
    if ballr.x<=-400:
        reset()
        score2+=1
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    key=pygame.key.get_pressed()
    if key[pygame.K_w]:
        p1.y-=move2
    if key[pygame.K_z]:
        p1.y+=move2
    if key[pygame.K_UP]:
        p2.y-=move2
    if key[pygame.K_DOWN]:
        p2.y+=move2

    if p1.y>=height-p1.height:
        p1.y=height-p1.height
    if p1.y<=0:
        p1.y=0
    if p2.y>=height-p2.height:
        p2.y=height-p2.height
    if p2.y<=0:
        p2.y=0
    screen.blit(msg,mgr)
    pygame.draw.rect(screen,((r,g,b)),p1,0,10)
    pygame.draw.rect(screen,((r,g,b)),p2,0,10)
    screen.blit(ball,(ballr.x,ballr.y))
    pygame.display.update()
pygame.quit()
