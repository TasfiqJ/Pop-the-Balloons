import pygame
import sys
import time
import random


Display_width = 1000
Display_height = 500
pygame.init()       
screen = pygame.display.set_mode((1000,500)) #Thescreen
#set the caption to the window 
pygame.display.set_caption("pop balloons") #Title
clock = pygame.time.Clock() #helps with like fps and making it smoother
ball = pygame.image.load('balloon.png')#ball image
popSound = pygame.mixer.Sound('snap.wav')#snap sound
popSound.set_volume(0.2)#turn the volume down 

#i created individual ballons, each has a x and y coordinate
def balloon1(bx,by):
    screen.blit(ball, (bx,by))#screen blit just makes the image ready to appear, it only appears after pygame.display.update()
def balloon2(bx2,by2):
    screen.blit(ball, (bx2,by2))
def balloon3(bx3,by3):
    screen.blit(ball, (bx3,by3))
def balloon4(bx4,by4):
    screen.blit(ball, (bx4,by4))
def balloon5(bx5,by5):
    screen.blit(ball, (bx5,by5))
def balloon6(bx6,by6):
    screen.blit(ball, (bx6,by6))
def balloon7(bx7,by7):
    screen.blit(ball, (bx7,by7))
def balloon8(bx8,by8):
    screen.blit(ball, (bx8,by8))

#constants white , black, and dark blue
white = ((255,255,255))
black = ((0,0,0))
darkblue = ((0,0,255))
font = pygame.font.Font(None, 70)#a font with size 70
font2 = pygame.font.Font(None, 50)#a font with size 50
def gameover(lastscore):#this def just displayes the gameover text
    
    while True:

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                quit()
            if ev.type == pygame.KEYDOWN:#if a key is pressed on the keyboard
                if ev.key == pygame.K_RETURN:#if you press enter after losing 
                    game()#restart game

                             
                             
        gameovertext = font.render("Game over", True, white)  #this is the gameover text, set to have a white color                                
        finalscore = font.render("Your final score is:  " + str(lastscore), True, white)#+str because the score is a string    #this is the score, it knows the score because when i called this function, it came with the score parameter   
        restart = font.render("Press Enter to restart" , True, white)#Press enter to restart text
        screen.blit(gameovertext, [351, 100])#positioning the gamveover text
        screen.blit(finalscore, [255, 200])#positioning the finalscore text
        screen.blit(restart, [255,300])#positioning the restart text 
        pygame.display.flip()  #update all of these things on the screen now 

def startupscreen():
    
    
    while True:
        for ev in pygame.event.get(): 
            if ev.type == pygame.QUIT:
                sys.exit()
            if ev.type == pygame.KEYDOWN:      #if they press a key                     
                if ev.key == pygame.K_RETURN:#if enter is pressed
                    game()#start the game 
        screen.fill(darkblue)#make the bakgorund color dark blue
        welcome = font.render("Welcome", True, white)
        instruction = font.render("Click the balloons to make them dissapear", True, white)
        moreinstruction = font2.render("Do not let 5 balloons get passed the bottom of the screen", True, white)
        moretext = font.render( "Try to get the highest score possible", True, white)
        pressenter = font.render("Press ENTER to start", True, white)
              
        screen.blit(welcome, (393,0))#putting it in the center and making text appear
        screen.blit(instruction, (0.5,200))#same thing for other text
        screen.blit(moreinstruction, (31,130))
        screen.blit(moretext, (82.5,340))
        screen.blit(pressenter, (252,270))        
        
        
    
        pygame.display.update()  #show it    

def game():
    #this is the game, really messy, but i didn't know how else to do it... as long as it works
    strikes = 5
    score = 0#keeps track of the score
    strikestext = font.render(str(strikes), True , white)
    textForTheScore = font.render(str(score), True, white)#using one of the fonts, create  the text in white                  
    click = pygame.mouse.get_pressed()#tells me where the mouse was when i clicked 
   
    #making random positions for the balloons within the walls of the screen , the y coordinates are negative because i want it to appear above the screen when theyre falling down
    bx = random.randrange(0, 870)
    by = random.randrange(-300,-50)
    bx2 = random.randrange(0, 870)
    by2 = random.randrange(-300,-50)
    bx3 = random.randrange(0, 870)
    by3 = random.randrange(-300,-50)
    bx4 = random.randrange(0, 870)
    by4 = random.randrange(-300,-50)  
    bx5 = random.randrange(0, 870)
    by5 = random.randrange(-300,-50)
    bx6 = random.randrange(0, 870)
    by6 = random.randrange(-300,-50)
    bx7 = random.randrange(0, 870)
    by7 = random.randrange(-300,-50)
    bx8 = random.randrange(0, 870)
    by8 = random.randrange(-300,-50)    
   
    speed = 1#i will use this variable to adjust the speed , every click makes it go faster
    
    while True:
        for event in pygame.event.get():#basic stuff, if u click to exit it exits
            if event.type == pygame.QUIT:
                sys.exit()   #exit the system   
                break#break out of the while loop
                  
            if event.type == pygame.MOUSEBUTTONDOWN:#if you click 
                mx, my = pygame.mouse.get_pos()#mx is the horizontal coordinate of the mouse, my is the vertical cooridnate
                
                
                if (mx+117 > bx+112 and mx< bx+112 and by + 153 > my and my>by):#so bassically if the mouse is over this ballon for both the x and y coordinates of the balloon 
                    popSound.play()#play the pop sound , because this is after they have clicked. so play pop
                    speed +=0.05#increase the speed by 0.05
                    
                    #reset their position so they fall from the top again 
                    by = random.randrange(-300,-50)
                    bx = random.randrange(0, 870) 
                    score += 1 #add one to the score since they poped a ballon 
                    textForTheScore = font.render(str(score), True, white)#update the score by taking in count the added +1
                    
                #same exact thing for all the other balloons 
                if (mx+117 > bx2+112 and mx< bx2+112 and by2 + 153 > my and my>by2):
                    popSound.play()
                    speed +=0.05
                    by2 = random.randrange(-300,-50)
                    bx2 = random.randrange(0, 870) 
                    score += 1 
                    textForTheScore = font.render(str(score), True, white)
                if (mx+117 > bx3+112 and mx< bx3+112 and by3 + 153 > my and my>by3):
                    popSound.play()
                    speed +=0.05
                    by3 = random.randrange(-300,-50)
                    bx3 = random.randrange(0, 870) 
                    score += 1 
                    textForTheScore = font.render(str(score), True, white)  
                if (mx+117 > bx4+112 and mx< bx4+112 and by4 + 153 > my and my>by4):
                    popSound.play()
                    speed +=0.05
                    by4 = random.randrange(-300,-50)
                    bx4 = random.randrange(0, 870) 
                    score += 1 
                    textForTheScore = font.render(str(score),True, white)  
                if (mx+117 > bx5+112 and mx< bx5+112 and by5 + 153 > my and my>by5):
                    popSound.play()
                    speed +=0.05
                    by5 = random.randrange(-300,-50)
                    bx5 = random.randrange(0, 870) 
                    score += 1 
                    textForTheScore = font.render(str(score), True, white)  
                if (mx+117 > bx6+112 and mx< bx6+112 and by6 + 153 > my and my>by6):
                    popSound.play()
                    speed +=0.05
                    by6 = random.randrange(-300,-50)
                    bx6 = random.randrange(0, 870) 
                    score += 1 
                    textForTheScore = font.render(str(score), True, white)  
                if (mx+117 > bx7+112 and mx< bx7+112 and by7 + 153 > my and my>by7):
                    popSound.play()
                    speed +=0.05
                    by7 = random.randrange(-300,-50)
                    bx7 = random.randrange(0, 870) 
                    score += 1 
                    textForTheScore = font.render(str(score), True, white)  
                if (mx+117 > bx8+112 and mx< bx8+112 and by8 + 153 > my and my>by8):
                    popSound.play()
                    speed +=0.05
                    by8 = random.randrange(-300,-50)
                    bx8 = random.randrange(0, 870) 
                    score += 1 
                    textForTheScore = font.render(str(score), True, white)  
                
        screen.fill(black)#background color is set to black
        screen.blit(textForTheScore, [0,0])#put the score text on the screen at 0,0 (top left corner)
        screen.blit(strikestext , [920,0])#put the strikes at 900, 0 on the screen
        #now, lets put the images of all the balloons on the screen ,since we already made them move and disapear after every click
        balloon1(bx,by)#this goes to the balloon1 def and uses the x and y coordinates given in the brackets to then show the image at that coordinate
        balloon2(bx2,by2)#same thing for the other balloons 
        balloon3(bx3,by3)
        balloon4(bx4,by4)
        balloon5(bx5,by5)
        balloon6(bx6,by6)
        balloon7(bx7,by7)
        balloon8(bx8,by8)        
        by += speed#add the speed to how fast the balloons are falling for all y coordinates of balloons 
        by2 += speed#added it to all balloon y coordinates 
        by3 += speed
        by4 += speed
        by5 += speed
        by6 += speed
        by7 += speed
        by8 += speed
        
        #if any of the balloons get past the bottom of the screen without being clicked 
        if by > Display_height or by2 > Display_height or by3 > Display_height or by4 > Display_height or by5 > Display_height or by6 > Display_height or by7 > Display_height or by8 > Display_height:
            strikes = strikes -1#minus 1 to the number of strikes
            
            strikestext = font.render(str(strikes), True , white)
       
            if strikes == 0:#if you miss 5 ballons 
                gameover(score)   #go to gameover screen, which just says gameover and says the score 
            else:#else, respawn the balloons at the top of the screen
                if by > Display_height:
                    by = random.randrange(-300,-50)
                if by2 > Display_height:
                    by2 = random.randrange(-300,-50)
                if by3 > Display_height:
                    by3 = random.randrange(-300,-50)
                if by4 > Display_height:
                    by4 = random.randrange(-300,-50)
                if by5 > Display_height:
                    by5 = random.randrange(-300,-50)
                if by6 > Display_height:
                    by6 = random.randrange(-300,-50)
                if by7 > Display_height:
                    by7 = random.randrange(-300,-50)
                if by8 > Display_height:
                    by8 = random.randrange(-300,-50)

        pygame.display.update()#update the screen. AKA show the images moving smoothly 
      

startupscreen()
