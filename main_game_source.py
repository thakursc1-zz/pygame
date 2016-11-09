###################################AQUA BALL#############################
#Game drama is simple....
#Player has a aqua ball
#recently there has been a rain of fireballs
#Player has to save himself from the balls by moving around the
#rainbow arena with keys ("w","S","A","B")
#The Score is shown at the end
#NOTE: The aquaball can sustain only 25 collides with fireball
import pygame
from pygame.locals import *
from os import sys
import random

#intialization of game window
pygame.init()
width,height = 800,600
screen = pygame.display.set_mode((width,height))
#key state array (Keeps keys state track)
keys = [False, False, False, False]
#intial player pos
playerpos=[350,500]
score=0
#(Enemy Details FireBALL!!!)
badtimer=100
badtimer1=0
badguys=[[350,0]]
healthvalue=10
myfont = pygame.font.SysFont("monospace", 25)


#load Ball Image
player = pygame.image.load("ball.png")
background = pygame.image.load("background.jpg")
badguyimg1 = pygame.image.load("fireball1.png")
badguyimg=badguyimg1
screen.blit(background,(0,0))

#loop
while 1:
    #FIll SCREEN WITH BLACK
    screen.fill(0)
    #Set background
    screen.blit(background,(0,0))
    #set timer for appereance of fireball
    if badtimer==0:
        badtimer=100-(badtimer1*2)
        badguys.append([random.randint(20,750),0])
        score  = score+10
        if badtimer1>=35:
            badtimer1=35
        else :
            badtimer1+=5
            
    for badguy in badguys:

        if badguy[1]>600:
            badguys.remove(badguy)
        badguy[1]+=5
    #Geting rectangles
    badrect=pygame.Rect(badguyimg.get_rect())
    playerrect=pygame.Rect(player.get_rect())
    playerrect.top=playerpos[1]
    playerrect.bottom = playerpos[1]+53
    playerrect.left=playerpos[0]
    playerrect.left=playerpos[0]+53


    #moving bad guys on the screen using blit()
    for badguy in badguys:
        scoretext = myfont.render("Score = "+str(score), 1, (1,1,1))
        screen.blit(scoretext, (5, 10))
        Healthtext = myfont.render("Health = "+str(healthvalue), 0, (0,0,0))
        screen.blit(Healthtext, (600,10))
        screen.blit(badguyimg, badguy)
        badrect.top=badguy[1]
        badrect.left = badguy[0]
        badrect.right=badguy[0]+85
        badrect.bottom=badguy[1]+85
        if(healthvalue<0):
            print "\n\n\nGame OVER", "Score ",score
            pygame.quit()
            sys.exit()
        else:
            if badrect.colliderect(playerrect):
                badguys.remove(badguy)
                healthvalue = healthvalue - 1
                pygame.display.update()
                print "Score:",score," Health:",healthvalue



    #Position Ball IN center bottom
    screen.blit(player,playerpos)
        
            
    pygame.display.flip()
    for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                    
                if event.type == pygame.KEYDOWN:
                    if event.key==K_w:
                        keys[0]=True
                    elif event.key==K_a:
                        keys[1]=True
                    elif event.key==K_s:
                        keys[2]=True
                    elif event.key==K_d:
                        keys[3]=True

                
                if event.type == pygame.KEYUP:
                    if event.key==pygame.K_w:
                        keys[0]=False
                    elif event.key==pygame.K_a:
                        keys[1]=False
                    elif event.key==pygame.K_s:
                        keys[2]=False
                    elif event.key==pygame.K_d:
                        keys[3]=False
    badtimer-=1
                
#ACTIONS OF THE KEYS... MOmvement and ball speed
    if keys[0]:
        playerpos[1]-=9
    elif keys[2]:
        playerpos[1]+=9
    if keys[1]:
        playerpos[0]-=9
    elif keys[3]:
        playerpos[0]+=9

