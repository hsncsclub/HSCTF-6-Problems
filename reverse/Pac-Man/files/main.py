import sys, random, copy, os, pygame, base64
from pygame.locals import *

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
SCREEN_COLOR = (0,0,0)  # black
FONT_COLOR = (255,255,255)  # white
START_FONT_COLOR = (255,255,0)  # yellow

def main():
    global CLOCK, SCREEN, FONT, LARGEFONT, PACMAN, PLAYER_IMAGE

    pygame.init()
    CLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pac-Man")
    pygame.display.set_icon(pygame.image.load("assets/pacmanR.png"))
    LARGEFONT = pygame.font.Font("freesansbold.ttf", 30)
    FONT = pygame.font.Font("freesansbold.ttf", 18)
    PACMAN = {"right": pygame.image.load("assets/pacmanR.png"),
              "left": pygame.image.load("assets/pacmanL.png"),
              "up": pygame.image.load("assets/pacmanU.png"),
              "down": pygame.image.load("assets/pacmanD.png")}
    PLAYER_IMAGE = PACMAN["right"]

    start()  # goes to start() function

    levels = read("assets/levels.txt")  # goes to read() function

    currentLevelIndex = 0  # Sets the starting level to Level 1 (Ex. If you set currentLevelIndex to 5, the game will start at level 4)

    while True:
        result = runLevel(levels, currentLevelIndex)  # goes to runLevel() function

        if result in ("finished"):
            currentLevelIndex += 1
            
        elif result in ("gameover"):
            currentLevelIndex = currentLevelIndex

        elif result in ("complete"):
            pygame.quit()
            sys.exit()

def runLevel(levels, num):
    global PLAYER_IMAGE
    levelObj = levels[num]
    mazeObj = levelObj["mazeObj"]  # levelObj created in the read() function
    gameObj = copy.deepcopy(levelObj["startState"])
    mazeRedraw = True  # screen update boolean value
    mousex = 0
    mousey = 0

    # Text that shows the levels
    levelScreen = FONT.render("Level %s of %s" % (num + 1, len(levels)), 1, FONT_COLOR)
    levelRect = levelScreen.get_rect()
    levelRect.bottomleft = (20, SCREEN_HEIGHT - 35)

    # 'HOME' button
    text = FONT.render("HOME", 1, FONT_COLOR)
    textrect = text.get_rect()
    textrect.top = 675
    textrect.centerx = 1160 

    mazeWidth = len(mazeObj) * 50
    mazeHeight = (len(mazeObj[0]) - 1) * 40 + 85

    levelIsFinished = False
    flag = False
    ans = ""
    count = 0

    while True:
        keyPressed = False
        mousePressed = False
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN: # Pac-Man's direction changes based on arrow keys
                keyPressed = True
                if event.key == K_LEFT:
                    PLAYER_IMAGE = PACMAN["left"]
                elif event.key == K_RIGHT:
                    PLAYER_IMAGE = PACMAN["right"]
                elif event.key == K_UP:
                    PLAYER_IMAGE = PACMAN["up"]
                elif event.key == K_DOWN:
                    PLAYER_IMAGE = PACMAN["down"]
                elif event.key == K_a:
                	ans += "a"
               	elif event.key == K_b:
                	ans += "b"
               	elif event.key == K_c:
                	ans += "c"
                elif event.key == K_d:
                	ans += "d"
                elif event.key == K_e:
                	ans += "e"
                elif event.key == K_f:
                	ans += "f"
                elif event.key == K_g:
                	ans += "g"
                elif event.key == K_h:
                	ans += "h"
                elif event.key == K_i:
                	ans += "i"
               	elif event.key == K_j:
                	ans += "j"
               	elif event.key == K_k:
                	ans += "k"
                elif event.key == K_l:
                	ans += "l"
                elif event.key == K_m:
                	ans += "m"
                elif event.key == K_n:
                	ans += "n"
                elif event.key == K_o:
                	ans += "o"
                elif event.key == K_p:
                	ans += "p"
                elif event.key == K_q:
                	ans += "q"
               	elif event.key == K_r:
                	ans += "r"
               	elif event.key == K_s:
                	ans += "s"
                elif event.key == K_t:
                	ans += "t"
                elif event.key == K_u:
                	ans += "u"
                elif event.key == K_v:
                	ans += "v"
                elif event.key == K_w:
                	ans += "w"
                elif event.key == K_x:
                	ans += "x"
                elif event.key == K_y:
                	ans += "y"
                elif event.key == K_z:
                	ans += "z"
                elif event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mousePressed = True

        keys_pressed = pygame.key.get_pressed()

        if mousex >= 1120 and mousex <= 1200 and mousey >= 670 and mousey <= 700: # HOME button
            if mousePressed:
                main()  # go back to the start screen
        
        if not levelIsFinished:
            playerx, playery = gameObj["player"]
            pacdots = gameObj["pacdots"]
            addX = addY = 0

            # Player movement
            if keys_pressed[K_UP]:
                addY = -1
            elif keys_pressed[K_RIGHT]:
                addX = 1
            elif keys_pressed[K_DOWN]:
                addY = 1
            elif keys_pressed[K_LEFT]:
                addX = -1

            if mazeObj[playerx + addX][playery + addY] not in ("#"):  # if player did not collide with wall
                if (playerx + addX, playery + addY) in pacdots:  # if player made contact with pac-dot
                    gameObj["pacdotCounter"] += 1
                    gameObj["pacdots"].remove((playerx + addX, playery + addY))
                if (playerx + addX, playery + addY) == gameObj["blinky"] or (playerx + addX, playery + addY) == gameObj["pinky"] or (playerx + addX, playery + addY) == gameObj["clyde"] or (playerx + addX, playery + addY) == gameObj["inky"]:  # if player made contact with enemy
                    if gameObj["lives"] > 0:
                        gameObj["lives"] -= 1
                if (playerx + addX, playery + addY) in gameObj["bonus"]:  # if player made contact with bonus
                    gameObj["lives"] += 1
                    gameObj["bonus"].remove((playerx + addX, playery + addY))
                gameObj["player"] = (playerx + addX, playery + addY)
                mazeRedraw = True  # update screen

            if gameObj["pacdotCounter"] == gameObj["total_pacdots"]:  # level is finished if all pac-dots are eaten
                levelIsFinished = True
                keyPressed = False

            # Blinky AI
            if gameObj["blinky"] != (None, None):
                enemyxB, addYB = gameObj["blinky"]
                addXB = addyB = 0
                direction = random.randint(1,4)
                if direction == 1: #up
                    addyB = -1
                elif direction == 2: #right
                    addXB = 1
                elif direction == 3: #down
                    addyB = 1
                elif direction == 4: #left
                    addXB = -1

                if mazeObj[enemyxB + addXB][addYB +addyB] not in ("#"):  # if enemy did not collide with wall
                    gameObj["blinky"] = (enemyxB + addXB, addYB + addyB)
                    mazeRedraw = True

            # Pinky AI
            if gameObj["pinky"] != (None, None):
                enemyxP, addYP = gameObj["pinky"]
                addXP = addyP = 0
                direction = random.randint(1,4)
                if direction == 1: #up
                    addyP = -1
                elif direction == 2: #right
                    addXP = 1
                elif direction == 3: #down
                    addyP = 1
                elif direction == 4: #left
                    addXP = -1

                if mazeObj[enemyxP + addXP][addYP +addyP] not in ("#"):  # if enemy did not collide with wall
                    gameObj["pinky"] = (enemyxP + addXP, addYP + addyP)
                    mazeRedraw = True
            
            # Clyde AI
            if gameObj["clyde"] != (None, None):
                enemyxC, addYC = gameObj["clyde"]
                addXC = addyC = 0
                direction = random.randint(1,4)
                if direction == 1: #up
                    addyC = -1
                elif direction == 2: #right
                    addXC = 1
                elif direction == 3: #down
                    addyC = 1
                elif direction == 4: #left
                    addXC = -1

                if mazeObj[enemyxC + addXC][addYC +addyC] not in ("#"):  # if enemy did not collide with wall
                    gameObj["clyde"] = (enemyxC + addXC, addYC + addyC)
                    mazeRedraw = True
                
            # Inky AI
            if gameObj["inky"] != (None, None):
                enemyxI, addYI = gameObj["inky"]
                addXI = addyI = 0
                direction = random.randint(1,4)
                if direction == 1: #up
                    addyI = -1
                elif direction == 2: #right
                    addXI = 1
                elif direction == 3: #down
                    addyI = 1
                elif direction == 4: #left
                    addXI = -1

                if mazeObj[enemyxI + addXI][addYI +addyI] not in ("#"):  # if enemy did not collide with wall
                    gameObj["inky"] = (enemyxI + addXI, addYI + addyI)
                    mazeRedraw = True


        SCREEN.fill(SCREEN_COLOR)

        if mazeRedraw:  # if need screen update
            mazeScreen = draw(mazeObj, gameObj)  # go to draw() function
            mazeRedraw = False

        # draw onto screen using blit()
        mazeRect = mazeScreen.get_rect()
        mazeRect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        SCREEN.blit(mazeScreen, mazeRect)
        SCREEN.blit(levelScreen, levelRect)
        livesScreen = FONT.render("Lives: %s" % gameObj["lives"], 1, FONT_COLOR)
        livesRect = livesScreen.get_rect()
        livesRect.bottomleft = (20, SCREEN_HEIGHT-10)
        SCREEN.blit(livesScreen, livesRect)
        pygame.draw.rect(SCREEN, (255,0,0), (1120,670,80,30), 0)
        SCREEN.blit(text, textrect)

        if levelIsFinished and gameObj["lives"] > 0:  # if level finished (NOTE: the number of lives remaining must be greater than 0)
            if num == len(levels) - 1:  # if last level
                SCREEN.fill(SCREEN_COLOR)
                completedRect = pygame.image.load("assets/completed.png").get_rect()
                completedRect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
                SCREEN.blit(pygame.image.load("assets/completed.png"), completedRect)

                if keyPressed:
                	count += 1
                	if base64.b64encode(ans.encode('utf8')) == b'Z2l2ZW1ldGhlZmxhZ3BsZWFzZQ==':
	                	flag = True
	                if count >= 20:
	                	return "complete"

                if flag:
                	SCREEN.fill(SCREEN_COLOR)
                	Text = ["Good! Here is your flag:",
                            "flag{bl3nky_m3g3c_133t_28e972}",
                            "xDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD"]
                	top = 100
                	for i in range(len(Text)):
                		text = LARGEFONT.render(Text[i], 1, FONT_COLOR)
                		instructions = text.get_rect()
                		top += 30
                		instructions.top = top
                		instructions.centerx = SCREEN_WIDTH/2
                		top += instructions.height
                		SCREEN.blit(text, instructions)
            else:  # if not last level
                finishedRect = pygame.image.load("assets/finished.png").get_rect()
                finishedRect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
                SCREEN.blit(pygame.image.load("assets/finished.png"), finishedRect)

                if keyPressed:
                    return "finished"

        if gameObj["lives"] == 0:  # if number of lives is 0
            gameOverRect = pygame.image.load("assets/gameover.png").get_rect()
            gameOverRect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
            SCREEN.blit(pygame.image.load("assets/gameover.png"), gameOverRect)
            
            if keyPressed:
                return "gameover"
            
        pygame.display.update()
        CLOCK.tick(10)

def start():
    instructions_Screen = False  # boolean value that tells whether currently on start screen or instructions screen
    mousex = 0
    mousey = 0

    # Title image
    title = pygame.image.load("assets/title.png").get_rect()
    title.top = 50
    title.centerx = SCREEN_WIDTH/2
    SCREEN.fill(SCREEN_COLOR)
    SCREEN.blit(pygame.image.load("assets/title.png"), title)

    START_FONT = pygame.font.Font("freesansbold.ttf", 40)

    # Draw the buttons
    pygame.draw.rect(SCREEN, (0,0,255), (630,410,100,60), 0)
    pygame.draw.rect(SCREEN, (0,0,255), (630,480,320,60), 0)
    pygame.draw.rect(SCREEN, (0,0,255), (630,550,230,60), 0)

    # Text for 'PLAY'
    text1 = START_FONT.render("PLAY", 1, START_FONT_COLOR)
    textrect1 = text1.get_rect()
    textrect1.top = 420
    textrect1.centerx = 680
    SCREEN.blit(text1, textrect1)

    # Text for 'INSTRUCTIONS'
    text2 = START_FONT.render("INSTRUCTIONS", 1, START_FONT_COLOR)
    textrect2 = text2.get_rect()
    textrect2.top = 490
    textrect2.centerx = 790
    SCREEN.blit(text2, textrect2)

    # Text for 'EXIT GAME'
    text3 = START_FONT.render("EXIT GAME", 1, START_FONT_COLOR)
    textrect3 = text3.get_rect()
    textrect3.top = 560
    textrect3.centerx = 745
    SCREEN.blit(text3, textrect3)
    
    while True:
        mousePressed = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mousePressed = True

        if instructions_Screen == False:  # if start screen
            if mousex >= 630 and mousex <= 730 and mousey >= 410 and mousey <= 470: # PLAY button
                pygame.draw.rect(SCREEN, (0,155,155), (630, 410, 100, 60), 4)  # highlight around button
                if mousePressed:
                    return

            if mousex < 630 or mousex > 730 or mousey < 410 or mousey > 470: # erase the highlight
                pygame.draw.rect(SCREEN, (0,0,0), (630, 410, 100, 60), 4)

            if mousex >= 630 and mousex <= 950 and mousey >= 480 and mousey <= 540: # INSTRUCTIONS button
                pygame.draw.rect(SCREEN, (0,155,155), (630, 480, 320, 60), 4)  # highlight the button
                if mousePressed:  # go to instructions screen
                    mousePressed = False
                    SCREEN.fill(SCREEN_COLOR)
                    Text = ["Get all the pac-dots to go to the next level.",
                            "Arrow keys to move, Esc to quit.",
                            "",
                            "There are 20 levels in the game.",
                            "Bonuses (circles that have a '+1' sign) give you an extra life.",
                            "You have 3 lives for each level.",
                            "Avoid enemies.",
                            "You will lose a life every time Pac-Man comes into contact with an enemy.",
                            "If you lose all 3 lives in a level, you will start over with the level you lost at."]
                    top = 100
                    for i in range(len(Text)):
                        text = LARGEFONT.render(Text[i], 1, FONT_COLOR)
                        instructions = text.get_rect()
                        top += 30
                        instructions.top = top
                        instructions.centerx = SCREEN_WIDTH/2
                        top += instructions.height
                        SCREEN.blit(text, instructions)

                    pygame.draw.rect(SCREEN, (0,0,255), (630, 30, 120, 60), 0)  # BACK button

                    # Text for 'BACK'
                    text4 = START_FONT.render("BACK", 1, START_FONT_COLOR)
                    textrect4 = text4.get_rect()
                    textrect4.top = 40
                    textrect4.centerx = 690
                    SCREEN.blit(text4, textrect4)

                    instructions_Screen = True

            if mousex < 630 or mousex > 950 or mousey < 480 or mousey > 540:
                pygame.draw.rect(SCREEN, (0,0,0), (630, 480, 320, 60), 4)  # erase the highlight
            
            if mousex >= 630 and mousex <= 860 and mousey >= 550 and mousey <= 610: # EXIT GAME button
                pygame.draw.rect(SCREEN, (0,155,155), (630, 550, 230, 60), 4)  # highlight around button
                if mousePressed:  # terminate game
                    pygame.quit()
                    sys.exit()

            if mousex < 630 or mousex > 860 or mousey < 550 or mousey > 610:
                pygame.draw.rect(SCREEN, (0,0,0), (630, 550, 230, 60), 4)  # erase the highlight
        
        if instructions_Screen == True:  # if instructions screen
            if mousex >= 630 and mousex <= 750 and mousey >= 30 and mousey <= 90:
                pygame.draw.rect(SCREEN, (0,155,155), (630, 30, 120, 60), 4)  # highlight around the BACK button
                if mousePressed:
                    main()

            if mousex < 630 or mousex > 750 or mousey < 30 or mousey > 90:
                pygame.draw.rect(SCREEN, (0,0,0), (630, 30, 120, 60), 4)  # erase the highlight
        
        pygame.display.update()
        CLOCK.tick()

def read(file):
    # Read the maze file
    #
    # Wall: #
    # Player starting position: *
    # Pacdot: o
    # Enemy starting positions: B (blinky), P (pinky), C (clyde), I (inky)
    # Bonus: O
    maze = open(file, "r")
    content = maze.readlines() + ["\r\n"]
    maze.close()

    levels = []
    levelNum = 0
    mazeTextLines = []
    mazeObj = []
    for lineNum in range(len(content)):
        line = content[lineNum].rstrip("\r\n")

        if "@" in line:  # @ is a comment (not part of level)
            line = line[:line.find("@")]
        if line != "":
            mazeTextLines.append(line)

        elif line == "" and len(mazeTextLines) > 0:
            for x in range(len(mazeTextLines[0])):
                mazeObj.append([])
            for y in range(len(mazeTextLines)):
                for x in range(len(mazeTextLines[0])):
                    mazeObj[x].append(mazeTextLines[y][x])

            startx = starty = startxB = startyB = startxP = startyP = startxC = startyC = startxI = startyI = None  # starting position for gameObj
            pacdots = []
            bonus = []
            for x in range(len(mazeTextLines[0])):
                for y in range(len(mazeObj[x])):
                    if mazeObj[x][y] in ("*"): # player starting position
                        startx = x
                        starty = y
                    elif mazeObj[x][y] in ("o"): # pac-dot
                        pacdots.append((x, y))
                    elif mazeObj[x][y] in ("O"): # bonus
                        bonus.append((x, y))
                    elif mazeObj[x][y] in ("B"): # Blinky(enemy) starting position
                        startxB = x
                        startyB = y
                    elif mazeObj[x][y] in ("P"): # Pinky(enemy) starting position
                        startxP = x
                        startyP = y
                    elif mazeObj[x][y] in ("C"): # Clyde(enemy) starting position
                        startxC = x
                        startyC = y
                    elif mazeObj[x][y] in ("I"): # Inky(enemy) starting position
                        startxI = x
                        startyI = y

            gameObj = {"player": (startx, starty),
                       "blinky": (startxB, startyB),
                       "pinky": (startxP, startyP),
                       "clyde": (startxC, startyC),
                       "inky": (startxI, startyI),
                       "pacdotCounter": 0,
                       "pacdots": pacdots,
                       "total_pacdots": len(pacdots),
                       "bonus": bonus,
                       "lives": 3}
            levelObj = {"width": len(mazeTextLines[0]),
                        "height": len(mazeObj),
                        "mazeObj": mazeObj,
                        "startState": gameObj}

            levels.append(levelObj)

            # Renew settings for next level
            mazeTextLines = []
            mazeObj = []
            gameObj = {}
            levelNum += 1
            
    return levels  

def draw(mazeObj, gameObj):  # function to update screen (after player movement, etc.)
    width = len(mazeObj) * 50
    height= (len(mazeObj[0]) - 1) * 40 + 85
    mazeScreen = pygame.Surface((width, height))
    mazeScreen.fill(SCREEN_COLOR)

    for x in range(len(mazeObj)):
        for y in range(len(mazeObj[x])):
            spaceRect = pygame.Rect((x * 50, y * 40, 50, 85))
            if mazeObj[x][y] == "#":  # wall
                mazeScreen.blit(pygame.image.load("assets/wall.png"), spaceRect)
            elif (x, y) in gameObj["pacdots"]:
                mazeScreen.blit(pygame.image.load("assets/pacdot.png"), spaceRect)
            elif (x, y) in gameObj["bonus"]:
                mazeScreen.blit(pygame.image.load("assets/bonus.png"), spaceRect)
            elif (x, y) == gameObj["player"]:
                mazeScreen.blit(PLAYER_IMAGE, spaceRect)
            elif (x, y) == gameObj["blinky"]:
                mazeScreen.blit(pygame.image.load("assets/blinky.jpg"), spaceRect)
            elif (x, y) == gameObj["pinky"]:
                mazeScreen.blit(pygame.image.load("assets/pinky.jpg"), spaceRect)
            elif (x, y) == gameObj["clyde"]:
                mazeScreen.blit(pygame.image.load("assets/clyde.jpg"), spaceRect)
            elif (x, y) == gameObj["inky"]:
                mazeScreen.blit(pygame.image.load("assets/inky.jpg"), spaceRect)
            
    return mazeScreen

if __name__ == "__main__":
    main()
