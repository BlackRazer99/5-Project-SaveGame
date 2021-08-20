#Savestate kreieren
from datetime import datetime
from time import process_time
import time

gameTime = datetime.now()
gameOn = True
x = 0
y = 0
z = 0

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
    playTime = time.process_time()
    print ("Time played", playTime)
    savetheGame = input("Do you want to save the game? " )
    if savetheGame == "yes" :
        gameState = (x, y, z)
        saveGame()
        gameOn = False
        print("Game saved")
        Continue = input("Do you want to Continue?")
        if Continue == "yes":
            x = x + 1
            y = y - 1
            z = z + 10
            gameOn = True
        else:
            print("Close the Game")
            exit()  
    else:
        print("Failed to save the Game")
        print("Continue to play the Game")
        x = x + 1
        y = y - 1
        z = z + 10
        continue 

def test1():
    held = "King"
    print(held)

def test2():
    test1()

test2
