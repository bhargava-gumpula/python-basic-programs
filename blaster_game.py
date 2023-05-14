import tkinter
import threading
import random

# Initialise coordinates of player and aliens
player_x = 2
player_y = 4
alien_y = 0
PIXEL_ON = 9
PIXEL_OFF = 0
SHOT_COLOR = 5
tk = Tk()

def displayGrid():
    canvas = Canvas(tk, width=400, height=400)
    canvas.pack()
    canvas.columnconfigure(4, 2)
    canvas.columnconfigure(4,2)

def playerMotion(player_x, player_y):
    oldx = player_x
    if button_a.was_pressed():
        player_x -= 1
    elif button_b.was_pressed():
        player_x += 1
        
    if player_x > 4:
        player_x = 4
    elif player_x < 0:
        player_x = 0
    display.set_pixel(player_x, player_y, PIXEL_ON)
    if oldx != player_x:
        display.set_pixel(oldx, player_y, PIXEL_OFF)

    
def shootAlien(player_x, player_y):
    if pin_logo.is_touched():
        preY = player_y
        for j in range(0, 4):
            display.set_pixel(player_x, player_y - 1, SHOT_COLOR)
            sleep(40)
            display.set_pixel(player_x, player_y - 1 , PIXEL_OFF)
              
            player_y -= 1
        player_y = preY  
         
def alienBomb(alien_y):
    preAlienY = alien_y
    randAlien_x = random.randint(0,4)
    for j in range(0, 4):
        display.set_pixel(randAlien_x, alien_y + 1, SHOT_COLOR)
        sleep(200)
        display.set_pixel(randAlien_x, alien_y + 1 , PIXEL_OFF)      
        alien_y += 1
        sleep(200)
    alien_y = preAlienY 

def gameEnded():
    # Check if player is dead
    if display.get_pixel(player_x, player_y) == 0:
        #display.scroll("Game Over", 35)
        return True

    # Check if aliens are dead
    x1, y1 = 0, 0
    while x1 <= 4:
        ledColor = display.get_pixel(x1, y1)       
        if ledColor == 9:
            # There are still aliens
            return False 
        x1 += 1
    # All aliens are shot
    #display.scroll("You Win", 35)
    return True
        
# main()
displayGrid()
while True:  
    playerMotion(player_x, player_y)
    shootAlien(player_x, player_y)
    alienBomb(alien_y)
    if gameEnded():
        break
