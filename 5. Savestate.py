#Savestate kreieren
from datetime import datetime
from time import process_time
import time

#the foundation I am working with is that the game has already been started
gameTime = datetime.now()
gameOn = True

#player position on map
x = 0
y = 0
z = 0

#function to save the game writes in textfile
def saveGame (): 
    save = open("5. Savestate.txt", "w")
    save.writelines("Gamestate is ")
    save.writelines(str(gameState))
    save.writelines("\n")
    save.writelines("Gametime ")
    save.writelines(str(playTime))
    save.writelines("\nGame saved ")
    save.writelines(str(gameTime))
    save.close()

    
while gameOn :
    #counts ingame time
    playTime = time.process_time()
    print ("Time played", playTime)
    #window asks if you want to save the game
    savetheGame = input("Do you want to save the game? " )
    if savetheGame == "yes" :
        #position of charakter gets used
        gameState = (x, y, z)
        #function for saving gets loaded
        saveGame()
        #loop and game closes
        gameOn = False
        print("Game saved")
        #if continue game goes om
        Continue = input("Do you want to Continue?")
        if Continue == "yes":
            #simulates movement of the person on map
            x = x + 1
            y = y - 1
            z = z + 10
            gameOn = True
        else:
            #else force the game to close
            print("Close the Game")
            exit()  
    else: #if you dont want to save game goes on
        print("Failed to save the Game")
        print("Continue to play the Game")
        #simulates movement 
        x = x + 1
        y = y - 1
        z = z + 10
    #and loop continues
