import pygame
import math
import random
pygame.init()
pygame.mixer.init()
#set title
pygame.display.set_caption("SPACE WAR")
#game display
gamedisplay=pygame.display.set_mode([1156,650])

"""
load all images and sounds
"""
background=pygame.image.load("images/background.png")
background_start=pygame.image.load("images/background_start.jpg")
myship=pygame.image.load("images/myship.png")
enemy1=pygame.image.load("images/enemy1.png")
enemy2=pygame.image.load("images/enemy2.png")
enemy3=pygame.image.load("images/enemy3.png")
enemy4=pygame.image.load("images/enemy4.png")
healthbar=pygame.image.load("images/healthbar.png")
healthbarme=pygame.image.load("images/healthbarme.png")
healthbarenemy1=pygame.image.load("images/healthbarenemy1.png")
healthbarenemy2=pygame.image.load("images/healthbarenemy2.png")
healthbarenemy3=pygame.image.load("images/healthbarenemy3.png")
healthbarenemy4=pygame.image.load("images/healthbarenemy4.png")
myshipbullet=pygame.image.load("images/bullet1.png")
enemy1bullet=pygame.image.load("images/enemy1bullet.png")
enemy2bullet=pygame.image.load("images/enemy2bullet.png")
enemy3bullet=pygame.image.load("images/enemy3bullet.png")
enemy4bullet=pygame.image.load("images/enemy4bullet.png")
gameover_background=pygame.image.load("images/gameover_background.png")
gameover_text=pygame.image.load("images/gameover_text.png")
win_background=pygame.image.load("images/win_background.png")
win_text=pygame.image.load("images/win_text.png")

myshipfire=pygame.mixer.Sound("audio/myshipfire.wav")
enemyexplosion=pygame.mixer.Sound("audio/enemyexplosion.wav")
myshipexplosion=pygame.mixer.Sound("audio/myshipexplosion.wav")
myshipcollide=pygame.mixer.Sound("audio/myshipcollide.wav")
winsound=pygame.mixer.Sound("audio/winsound.wav")
enemyexplosion.set_volume(0.5)
myshipfire.set_volume(0.55)
myshipexplosion.set_volume(0.5)
myshipcollide.set_volume(0.5)
winsound.set_volume(0.5)
pygame.mixer.music.load('audio/moonlight.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.55)

""" Accuracy Counter"""
accuracy=[0,0]

"""
start screen code 
"""
def startscreen():
    
    while 1:
        gamedisplay.blit(background_start,[0,0])
        pygame.display.update()
        for event in pygame.event.get():
            if (event.type==pygame.QUIT):
                pygame.quit()
                exit(0)
            elif (event.type==pygame.KEYDOWN and event.key==pygame.K_q):
                pygame.quit()
                exit(0)
            elif (event.type==pygame.KEYDOWN and event.key==pygame.K_s):
                run()
                
            
"""
when game is in running state
"""            
def run():
    
    """
    my and enemy position
    """
    myposition=[543,290]
    enemy1pos=[1030,60]
    enemy2pos=[1048,280]
    enemy3pos=[1110,70]
    enemy4pos=[1110,605]
    
    """
    bullet positions of enemy and my ship
    """
    mybulletpos=[]
    enemy1bulletpos=[]
    enemy2bulletpos=[]
    enemy3bulletpos=[]
    enemy4bulletpos=[]
    
    """LEFT,RIGHT,UP,DOWN key pressed or not"""
    keys=[False,False,False,False]
    
    """health, timer, accuracy and movement variables"""
    dir1=1
    clockwise=True
    up=True
    myhealth=200
    enemy1health=100
    enemy2health=100
    enemy3health=100
    enemy4health=100
    flagme=0
    flag1=0
    flag2=0
    flag3=0
    flag4=0
    enemy1timer=60
    enemy2timer=60
    enemy3timer=1000
    enemy4timer=1500
    
    while 1:
        """ set background """
        gamedisplay.blit(background,[0,0])
        
        """
        increment and display my bullet position
        """
        index=0
        for bullets in mybulletpos:
            x_inc=math.cos(bullets[0])*20
            y_inc=math.sin(bullets[0])*20
            bullets[1]+=x_inc
            bullets[2]+=y_inc
            if (bullets[1]>1156 or bullets[1]<0 or bullets[2]>650 or bullets[2]<0):
                myhealth-=3
                if (myhealth<0):
                    flagme=1
                mybulletpos.pop(index)
            
            index+=1
           
            
        enemy1rect=pygame.Rect(enemy1.get_rect())
        enemy1rect.left=enemy1pos[0]
        enemy1rect.bottom=enemy1pos[1]
        if (dir1==1):
            enemy1rect.top=enemy1pos[1]-35
        if (dir1==3):
            enemy1rect.top=enemy1pos[1]
        if (dir1==2):
            enemy1rect.right=enemy1pos[0]
            
        enemy2rect=pygame.Rect(enemy2.get_rect())
        enemy2rect.left=enemy2pos[0]
        enemy2rect.top=enemy2pos[1]
        
        enemy3rect=pygame.Rect(enemy3.get_rect())
        enemy3rect.left=enemy3pos[0]
        enemy3rect.bottom=enemy3pos[1]
        
        enemy4rect=pygame.Rect(enemy4.get_rect())
        enemy4rect.left=enemy4pos[0]
        enemy4rect.top=enemy4pos[1]
            
        
        index1=0
        for bullets in mybulletpos:
            bullrect=pygame.Rect(myshipbullet.get_rect())
            bullrect.left=bullets[1]
            bullrect.top=bullets[2]
            if (flag1==0):
                if (bullrect.colliderect(enemy1rect)):
                    accuracy[0]+=1
                    enemy1health-=random.randint(3,4)
                    mybulletpos.pop(index1)
                    if (enemy1health<0):
                        enemyexplosion.play()
                        flag1=1
            if (flag2==0):
                if (bullrect.colliderect(enemy2rect)):
                    accuracy[0]+=1
                    enemy2health-=random.randint(3,4)
                    mybulletpos.pop(index1)
                    if (enemy2health<0):
                        enemyexplosion.play()
                        flag2=1
            if (flag3==0):
                if (bullrect.colliderect(enemy3rect)):
                    accuracy[0]+=1
                    enemy3health-=random.randint(3,4)
                    mybulletpos.pop(index1)
                    if (enemy3health<0):
                        enemyexplosion.play()
                        flag3=1
            if (flag4==0):
                if (bullrect.colliderect(enemy4rect)):
                    accuracy[0]+=1
                    enemy4health-=random.randint(3,4)
                    mybulletpos.pop(index1)
                    if (enemy4health<0):
                        enemyexplosion.play()
                        flag4=1
                
                
            index1+=1
            
        
        for bullets in mybulletpos:
            arrow=pygame.transform.rotate(myshipbullet,360-bullets[0]*57.295779)
            gamedisplay.blit(arrow,[bullets[1],bullets[2]])
            
        """increment and display enemy1 bullet position"""
        index=0
        for bullets in enemy1bulletpos:
            x_inc=math.cos(bullets[0])*20
            y_inc=math.sin(bullets[0])*20
            bullets[1]+=x_inc
            bullets[2]+=y_inc
            if (bullets[1]>1156 or bullets[1]<0 or bullets[2]>650 or bullets[2]<0):
                enemy1bulletpos.pop(index)
            index+=1
            
        """write code for collide here"""
        myshiprect=pygame.Rect(myship.get_rect())
        myshiprect.left=myposition[0]-35
        myshiprect.bottom=myposition[1]+35
        if (flag1==0):
            if (myshiprect.colliderect(enemy1rect)):
                flagme=1
        if (flag2==0):
            if (myshiprect.colliderect(enemy2rect)):
                flagme=1
        if (flag3==0):
            if (myshiprect.colliderect(enemy3rect)):
                flagme=1
        if (flag4==0):
            if (myshiprect.colliderect(enemy4rect)):
                flagme=1
        
        index1=0
        for bullets in enemy1bulletpos:
            bullrect=pygame.Rect(enemy1bullet.get_rect())
            bullrect.left=bullets[1]
            bullrect.top=bullets[2]
            if (bullrect.colliderect(myshiprect)):
                myshipcollide.play()
                myhealth-=random.randint(10,16)
                enemy1bulletpos.pop(index1)
                if (myhealth<0):
                    flagme=1
            index1+=1
        
            
        for bullets in enemy1bulletpos:
            arrow=pygame.transform.rotate(enemy1bullet,360-bullets[0]*57.295779)
            gamedisplay.blit(arrow,[bullets[1],bullets[2]])
            
        """increment and display enemy2 bullet position"""
        index=0
        for bullets in enemy2bulletpos:
            bullets[0]-=10
            if (bullets[0]<0):
                enemy2bulletpos.pop(index)
            index+=1
        
        myshiprect=pygame.Rect(myship.get_rect())
        myshiprect.left=myposition[0]-35
        myshiprect.bottom=myposition[1]+35
        index1=0
        for bullets in enemy2bulletpos:
            bullrect=pygame.Rect(enemy2bullet.get_rect())
            bullrect.left=bullets[0]
            bullrect.top=bullets[1]
            if (bullrect.colliderect(myshiprect)):
                myshipcollide.play()
                myhealth-=random.randint(16,20)
                enemy2bulletpos.pop(index1)
                if (myhealth<0):
                    flagme=1
            index1+=1
            
        for bullets in enemy2bulletpos:
            gamedisplay.blit(enemy2bullet,[bullets[0],bullets[1]])
            
        """increment and display enemy3 bullet position"""
        index=0
        for bullets in enemy3bulletpos:
            x_inc=math.cos(bullets[0])*15
            y_inc=math.sin(bullets[0])*15
            bullets[1]+=x_inc
            bullets[2]+=y_inc
            if (bullets[1]>1156 or bullets[1]<0 or bullets[2]>650 or bullets[2]<0):
                enemy3bulletpos.pop(index)
            index+=1
            
        myshiprect=pygame.Rect(myship.get_rect())
        myshiprect.left=myposition[0]-35
        myshiprect.bottom=myposition[1]+35
        
        index1=0
        for bullets in enemy3bulletpos:
            bullrect=pygame.Rect(enemy3bullet.get_rect())
            bullrect.left=bullets[1]
            bullrect.top=bullets[2]
            if (bullrect.colliderect(myshiprect)):
                myshipcollide.play()
                myhealth-=random.randint(10,16)
                enemy3bulletpos.pop(index1)
                if (myhealth<0):
                    flagme=1
            index1+=1
            
        for bullets in enemy3bulletpos:
            arrow=pygame.transform.rotate(enemy3bullet,360-bullets[0]*57.295779)
            gamedisplay.blit(arrow,[bullets[1],bullets[2]])
        
        """increment and display enemy4 bullet position"""
        index=0
        for bullets in enemy4bulletpos:
            x_inc=math.cos(bullets[0])*15
            y_inc=math.sin(bullets[0])*15
            bullets[1]+=x_inc
            bullets[2]+=y_inc
            if (bullets[1]>1156 or bullets[1]<0 or bullets[2]>650 or bullets[2]<0):
                enemy4bulletpos.pop(index)
            index+=1
        
        myshiprect=pygame.Rect(myship.get_rect())
        myshiprect.left=myposition[0]-55
        myshiprect.bottom=myposition[1]+15
        index1=0
        for bullets in enemy4bulletpos:
            bullrect=pygame.Rect(enemy4bullet.get_rect())
            bullrect.left=bullets[1]
            bullrect.top=bullets[2]
            if (bullrect.colliderect(myshiprect)):
                myshipcollide.play()
                myhealth-=random.randint(10,16)
                if (myhealth<0):
                    flagme=1
                enemy4bulletpos.pop(index1)
            index1+=1
            
        for bullets in enemy4bulletpos:
            arrow=pygame.transform.rotate(enemy4bullet,360-bullets[0]*57.295779)
            gamedisplay.blit(arrow,[bullets[1],bullets[2]])
            
        
        """
        my ship position and rotation and display
        """
        if (flagme==0):
            mouseposition=pygame.mouse.get_pos()
            angle=math.atan2(mouseposition[1]-myposition[1],mouseposition[0]-myposition[0])
            rotate_myship=pygame.transform.rotate(myship,360-angle*57.295779)
            newposition=(myposition[0]-rotate_myship.get_width()/2,myposition[1]-rotate_myship.get_height()/2)
            gamedisplay.blit(rotate_myship,newposition)    
            
            
        """ Display all enemy ships """
        if (flag1==0):
            angle1=math.atan2(myposition[1]-enemy1pos[1],myposition[0]-enemy1pos[0])
            rotate_enemy1=pygame.transform.rotate(enemy1,360-angle1*57.295779)
            newposition1=(enemy1pos[0]-rotate_enemy1.get_width()/2,enemy1pos[1]-rotate_enemy1.get_height()/2)
            gamedisplay.blit(rotate_enemy1,newposition1)
            
        if (flag2==0):
            gamedisplay.blit(enemy2,enemy2pos)
            
        if (flag3==0):
            angle1=math.atan2(myposition[1]-enemy3pos[1],myposition[0]-enemy3pos[0])
            rotate_enemy3=pygame.transform.rotate(enemy3,360-angle1*57.295779)
            newposition1=(enemy3pos[0]-rotate_enemy3.get_width()/2,enemy3pos[1]-rotate_enemy3.get_height()/2)
            gamedisplay.blit(rotate_enemy3,newposition1)
            
        if (flag4==0):
            angle1=math.atan2(myposition[1]-enemy4pos[1],myposition[0]-enemy4pos[0])
            rotate_enemy4=pygame.transform.rotate(enemy4,360-angle1*57.295779)
            newposition1=(enemy4pos[0]-rotate_enemy4.get_width()/2,enemy4pos[1]-rotate_enemy4.get_height()/2)
            gamedisplay.blit(rotate_enemy4,newposition1)
            
            
        """ display title bar"""
        for i in range(enemy1health):
            gamedisplay.blit(healthbarenemy1,[(i+1039),8])
        for i in range(enemy2health):
            gamedisplay.blit(healthbarenemy2,[(i+929),8])
        for i in range(enemy3health):
            gamedisplay.blit(healthbarenemy3,[(i+819),8])
        for i in range(enemy4health):
            gamedisplay.blit(healthbarenemy4,[(i+709),8])
        gamedisplay.blit(healthbar,[137,5])
        for i in range(myhealth):
            gamedisplay.blit(healthbarme,[(i+140),8])
        health_string=str("Your Health: ")
        font=pygame.font.Font(None,30)
        heal=font.render(health_string,True,(200,200,200))
        health_rect=heal.get_rect()
        health_rect.topleft=[8,6]
        gamedisplay.blit(heal,health_rect)
            
        
        """ Update the Display """
        pygame.display.update()
        
        """ Handle all events """
        for event in pygame.event.get():
            if (event.type==pygame.QUIT):
                pygame.quit()
                exit(0)
                
            elif (event.type==pygame.KEYDOWN and event.key==pygame.K_q):
                pygame.quit()
                exit(0)
                
            elif (event.type==pygame.KEYDOWN and event.key==pygame.K_LEFT):
                keys[0]=True
            elif (event.type==pygame.KEYDOWN and event.key==pygame.K_RIGHT):
                keys[1]=True
            elif (event.type==pygame.KEYDOWN and event.key==pygame.K_UP):
                keys[2]=True
            elif (event.type==pygame.KEYDOWN and event.key==pygame.K_DOWN):
                keys[3]=True
            if (event.type==pygame.KEYUP):
                if (event.key==pygame.K_LEFT):
                    keys[0]=False
                elif (event.key==pygame.K_RIGHT):
                    keys[1]=False
                elif (event.key==pygame.K_UP):
                    keys[2]=False
                elif (event.key==pygame.K_DOWN):
                    keys[3]=False
                
            if (event.type==pygame.MOUSEBUTTONDOWN):
                myshipfire.play()
                accuracy[1]+=1
                mousepos=pygame.mouse.get_pos()
                ang=math.atan2(mousepos[1]-myposition[1],mousepos[0]-myposition[0])
                mybulletpos.append([ang,myposition[0],myposition[1]])
                
                
                
        """ increment my ship position """       
        if (keys[0]):
            myposition[0]-=10
            if (myposition[0]<0):
                myposition[0]=0
        if (keys[1]):
            myposition[0]+=10
            if (myposition[0]>1156):
                myposition[0]=1156
        if (keys[2]):
            myposition[1]-=10
            if (myposition[1]<60):
                myposition[1]=60
        if (keys[3]):
            myposition[1]+=10
            if (myposition[1]>650):
                myposition[1]=650
            
        """ increment all enemy position """
        if (flag1==0):
            if (clockwise):
                if (dir1==1):
                    enemy1pos[0]+=5
                    if (enemy1pos[0]>1030):
                        enemy1pos[0]=1030
                        clockwise=False
                elif (dir1==2):
                    enemy1pos[1]-=5
                    if (enemy1pos[1]<60):
                        enemy1pos[1]=60
                        dir1=1
                elif (dir1==3):
                    enemy1pos[0]-=5
                    if (enemy1pos[0]<30):
                        enemy1pos[0]=30
                        dir1=2
                    
            else:
                if (dir1==1):
                    enemy1pos[0]-=5
                    if (enemy1pos[0]<30):
                        enemy1pos[0]=30
                        dir1=2
                elif (dir1==2):
                    enemy1pos[1]+=5
                    if (enemy1pos[1]>620):
                        enemy1pos[1]=620
                        dir1=3
                elif (dir1==3):
                    enemy1pos[0]+=5
                    if (enemy1pos[0]>1030):
                        enemy1pos[0]=1030
                        clockwise=True
            
            
            if (enemy1timer<0):
                enemy1timer=150
                angle1=math.atan2(myposition[1]-enemy1pos[1],myposition[0]-enemy1pos[0])
                enemy1bulletpos.append([angle1,enemy1pos[0],enemy1pos[1]])
            else:
                enemy1timer-=2
        
        if (flag2==0):
            if (up):
                enemy2pos[1]-=3
                if (enemy2pos[1]<105):
                    enemy2pos[1]=105
                    up=False
            else:
                enemy2pos[1]+=3
                if (enemy2pos[1]>490):
                    enemy2pos[1]=490
                    up=True
                    
            if (enemy2timer<0):
                enemy2bulletpos.append([enemy2pos[0],enemy2pos[1]+40])
                enemy2timer=60
            else:
                enemy2timer-=2
                
        if (flag3==0):
            if (enemy3timer<0):
                enemy3timer=1500
            if (enemy3timer<500):
                if (enemy3timer%100==0):
                    angle1=math.atan2(myposition[1]-enemy3pos[1],myposition[0]-enemy3pos[0])
                    enemy3bulletpos.append([angle1,enemy3pos[0]-15,enemy3pos[1]-5])
            
            enemy3timer-=10
            
        if (flag4==0):
            if (enemy4timer<0):
                enemy4timer=1500
            if (enemy4timer<500):
                if (enemy4timer%100==0):
                    angle1=math.atan2(myposition[1]-enemy4pos[1],myposition[0]-enemy4pos[0])
                    enemy4bulletpos.append([angle1,enemy4pos[0]+5,enemy4pos[1]])
            
            enemy4timer-=10
            
        if (flag1 and flag2 and flag3 and flag4):
            for i in range(8):
                for j in range(5):
                    x=i*160
                    y=j*160
                    gamedisplay.blit(win_background,[x,y])
            gamedisplay.blit(win_text,[440,200])
            acc=0
            if (accuracy[1]!=0):
                acc=(accuracy[0]*100)/accuracy[1]
            acc=int(acc)
            accuracy_string=str("Your accuracy is: "+str(acc))
            font=pygame.font.Font(None,40)
            accu=font.render(accuracy_string,True,(0,255,0))
            accuracy_rect=accu.get_rect()
            accuracy_rect.topleft=[442,300]
            gamedisplay.blit(accu,accuracy_rect)
            s="Press 'S' to Start or 'Q' to Quit"
            font=pygame.font.Font(None,40)
            prnt=font.render(s,True,(100,100,255))
            prnt_rect=prnt.get_rect()
            prnt_rect.topleft=[370,380]
            gamedisplay.blit(prnt,prnt_rect)
            winsound.play()
            gamewon()
        if (flagme):
            for i in range(8):
                for j in range(5):
                    x=i*160
                    y=j*160
                    gamedisplay.blit(gameover_background,[x,y])
            gamedisplay.blit(gameover_text,[380,200])
            acc=0
            if (accuracy[1]!=0):
                acc=(accuracy[0]*100)/accuracy[1]
            acc=int(acc)
            accuracy_string=str("Your accuracy is: "+str(acc))
            font=pygame.font.Font(None,60)
            accu=font.render(accuracy_string,True,(255,0,0))
            accuracy_rect=accu.get_rect()
            accuracy_rect.topleft=[380,300]
            gamedisplay.blit(accu,accuracy_rect)
            s="Press 'S' to Start or 'Q' to Quit"
            font=pygame.font.Font(None,45)
            prnt=font.render(s,True,(100,100,255))
            prnt_rect=prnt.get_rect()
            prnt_rect.topleft=[360,380]
            gamedisplay.blit(prnt,prnt_rect)
            myshipexplosion.play()
            gamelose()
            
            
def gamewon():
    accuracy[0]=0
    accuracy[1]=0
    while 1:
        pygame.display.update()
        for event in pygame.event.get():
            if (event.type==pygame.QUIT):
                pygame.quit()
                exit(0)
            elif (event.type==pygame.KEYDOWN and event.key==pygame.K_q):
                pygame.quit()
                exit(0)
            elif (event.type==pygame.KEYDOWN and event.key==pygame.K_s):
                run()
    
  
def gamelose():
    accuracy[0]=0
    accuracy[1]=0
    while 1:
        pygame.display.update()
        for event in pygame.event.get():
            if (event.type==pygame.QUIT):
                pygame.quit()
                exit(0)
            elif (event.type==pygame.KEYDOWN and event.key==pygame.K_q):
                pygame.quit()
                exit(0)
            elif (event.type==pygame.KEYDOWN and event.key==pygame.K_s):
                run()
                
                
                
startscreen()
        
    
    


