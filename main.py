import buttons
import pygame
import os
pygame.mixer.init()
pygame.font.init()
WIDTH,HEIGHT=900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
white=(255,255,255)
dblue=(0,0,90)
b=(0,0,0)
Y=(255,255,0)
R=(255,0,0)
FPS=60
bullethitsnd=pygame.mixer.Sound(os.path.join('Assets','Grenade+1.mp3'))
bulletfire=pygame.mixer.Sound(os.path.join('Assets','Gun+Silencer.mp3'))
fnt=pygame.font.Font('times.ttf',30)
fnt2=pygame.font.Font('times.ttf',60)
border=pygame.Rect(445,0,10,500)
yelspcimage=pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
yelspc=pygame.transform.rotate(pygame.transform.scale(yelspcimage,(40,30)),90)
redspcimage=pygame.image.load(os.path.join('Assets','spaceship_red.png'))
redspc=pygame.transform.rotate(pygame.transform.scale(redspcimage,(40,30)),270)
redbullets=[]
yellowbullets=[]
YELLOWHIT=pygame.USEREVENT+1
REDHIT=pygame.USEREVENT+2
backgrn=pygame.image.load(os.path.join('Assets','coolspace.jpg'))
backgrnd=pygame.transform.scale(backgrn,(900,500))
startimg= pygame.image.load(os.path.join('Assets','start.png')).convert_alpha()
exitimg= pygame.image.load(os.path.join('Assets','exit.png')).convert_alpha()
startbutton= buttons.Button(100,200, startimg, 0.25)
exitbutton= buttons.Button(550,180, exitimg, 0.25)
        
def draw_window(yellow,red,redbullets,yellowbullets,redh,ye):

    WIN.blit(backgrnd,(0,0))
    pygame.draw.rect(WIN,b,border)
    yellhtxt=fnt.render('HEALTH : '+str(ye),True,white)
    redhtxt = fnt.render('HEALTH : ' + str(redh),True, white)
    WIN.blit(yellhtxt,(10,10))
    WIN.blit(redhtxt, (900-redhtxt.get_width()-10,10))
    WIN.blit(yelspc,(yellow.x,yellow.y))
    WIN.blit(redspc, (red.x,red.y))
    for bullet in yellowbullets:
        pygame.draw.rect(WIN,Y,bullet)
    for bullet in redbullets:
        pygame.draw.rect(WIN, R, bullet)
    pygame.display.update()
def drawwinner(txt):
    dr=fnt2.render(txt,1,white)
    WIN.blit(dr,(450-dr.get_width()/2,250-dr.get_height()/2))
    pygame.display.update()
    pygame.time.delay(4000)
def handlebullet(yellowbullets,redbullets,yellow,red):
    for bullet in yellowbullets:
        bullet.x+=10
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(REDHIT))
            yellowbullets.remove(bullet)
        elif bullet.x>900:
            yellowbullets.remove(bullet)
    for bullet in redbullets:
        bullet.x-=10
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOWHIT))
            redbullets.remove(bullet)
        elif bullet.x<0:
            redbullets.remove(bullet)
def main():
    red=pygame.Rect(800,400,40,30)
    yellow=pygame.Rect(100,400,40,30)
    clock=pygame.time.Clock()
    redh=10
    yellowh=10
    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x and len(yellowbullets)<4:
                    bullet=pygame.Rect(yellow.x+40,yellow.y+15-2.5,10,5)
                    yellowbullets.append(bullet)
                    bulletfire.play()
                if event.key == pygame.K_SPACE and len(redbullets)<4:
                    bullet = pygame.Rect(red.x, red.y + 15 - 2.5,10,5)
                    redbullets.append(bullet)
                    bulletfire.play()
            if event.type==REDHIT:
                redh-=1
                bullethitsnd.play()
            if event.type==YELLOWHIT:
                yellowh-=1
                bullethitsnd.play()
        txt=''
        if redh<=0:
            txt='YELLOW POLI'
        if yellowh<=0:
            txt='RED AATTA POLI'
        if txt!='':
            drawwinner(txt)
            break
        keypress=pygame.key.get_pressed()

        handlebullet(yellowbullets,redbullets,yellow,red)
        if keypress[pygame.K_a] and yellow.x-5>0:
            yellow.x -= 5
        if keypress[pygame.K_d] and yellow.x+5<405:
            yellow.x += 5
        if keypress[pygame.K_w] and yellow.y-5>0:
            yellow.y -= 5
        if keypress[pygame.K_s] and yellow.y+5<470:
            yellow.y += 5
        if keypress[pygame.K_LEFT] and red.x-5>455:
            red.x -= 5
        if keypress[pygame.K_RIGHT] and red.x+5<860:
            red.x += 5
        if keypress[pygame.K_UP] and red.y-5>0:
            red.y -= 5
        if keypress[pygame.K_DOWN] and red.y+5<470:
            red.y += 5



        draw_window(yellow,red,redbullets,yellowbullets,redh,yellowh)
        
    
run=True
while run:
    WIN.blit(backgrn,(0,0))
    if startbutton.draw()==True:
        main()
    if exitbutton.draw()==True:
        run=False
    pygame.display.update()
    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()
    