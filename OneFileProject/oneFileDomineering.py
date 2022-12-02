import pygame, sys, random, pymsgbox
#import AI
#import UserInterface as UserInterface

ROWS = COLS = 8 #default values

AI_TURN = 0 #0=pvp, 1=prvi igra AI, 2=drugi

length = len(sys.argv)
if length >= 3:
    ROWS = int(sys.argv[1])
    COLS = int(sys.argv[2])
    if length >= 4:
        AI_TURN = int(sys.argv[3])

WIDTH = COLS * 80
HEIGHT = ROWS * 80

SQSIZE = WIDTH // COLS

def getNextMove(matrix, isMoveValid):
    while True:
        i=random.randrange(0, len(matrix))
        j=random.randrange(0, len(matrix[0]))
        if(isMoveValid(i, j, matrix)):
            return (i, j)
        
CountMove = 0
#trenutno ima duplikati svih funkcija za svakog igraca jer mi bilo lakse tako da testiram 
def CreateMatrix(rows: int, cols: int):
    Matrix = [[(0,0) for x in range(cols)] for y in range(rows)]
    return Matrix

def IsMoveValidOne(rows : int, cols : int, Mat):
    if Mat[rows-1][cols][0] == 0 and Mat[rows][cols][0] == 0 and rows != 0:
        return True
    else:
        return False

def IsMoveValidTwo(rows : int, cols : int, Mat):
    if cols >= len(Mat[0])-1:
        return False
    if Mat[rows][cols+1][0] == 0 and Mat[rows][cols][0] == 0:
        return True
    else:
        return False

def CalcAvalaibleMovesPlayerOne(Mat):
    count = 0
    for x in range(1, len(Mat)):
        #print(x)
        for i in range(len(Mat[0])):
            #print(i)
            if IsMoveValidOne(x,i,Mat):
                count+=1
    return count

def CalcAvalaibleMovesPlayerTwo(Mat):
    count = 0
    for x in range(len(Mat)):
        #print(x)
        for i in range(len(Mat[0])-1):
            #print(i)
            if IsMoveValidTwo(x,i,Mat):
                count+=1
    return count
    
def PlayerOneMove(rows : int, cols : int, Mat):
    if IsMoveValidOne(rows,cols,Mat):
        global CountMove
        Mat[rows - 1][cols] = (-1,CountMove)
        Mat[rows][cols] = (1,CountMove)
        CountMove+=1
        PrintField(Mat)
        if CalcAvalaibleMovesPlayerTwo(Mat) == 0:
            print("Player one wins")
            pymsgbox.alert('Player 1!', 'The winner is:', button='OK') #alert(text='', title='', button='OK')
            #Tk().wm_withdraw()        
            #messagebox.showinfo("Domineering","Player one wins")           
        else:
            print("Available moves for player Two:", CalcAvalaibleMovesPlayerTwo(Mat))
        return True    
    else:
        pymsgbox.alert('Try again!', 'Invalid move')
        #pygame.display.set_caption('INVALID MOVE - try again') #stampa u zaglavlju
        print("Invalid move")
    return False

def PlayerTwoMove(rows : int, cols : int, Mat):
    if IsMoveValidTwo(rows,cols,Mat):
        global CountMove
        Mat[rows][cols] = (-2,CountMove)
        Mat[rows][cols+1] = (2,CountMove)
        CountMove+=1
        PrintField(Mat)
        if CalcAvalaibleMovesPlayerOne(Mat) == 0:
            print("Player two wins")  
            pymsgbox.alert('Player 2!', 'The winner is:', button='OK')
            #Tk().wm_withdraw() 
            #messagebox.showinfo("Domineering","Player two wins")
        else:
            print("Available moves for player One:", CalcAvalaibleMovesPlayerOne(Mat))
        return True
    else:
        pymsgbox.alert('Try again!', 'Invalid move')
        #pygame.display.set_caption('INVALID MOVE - try again') #stampa u zaglavlju
        print("Invalid move")
    return False
    
def PrintField(Field):
    for x in range(len(Field)):
        print(Field[x])
    print("----------------")

PlayerOneImg = pygame.transform.scale(pygame.image.load("images/player_1.png"), (SQSIZE, (SQSIZE*2)))
PlayerTwoImg = pygame.transform.scale(pygame.image.load("images/player_2.png"), ((SQSIZE*2), SQSIZE))
black = (0, 0, 0)
white = (255, 255, 255)
        
def show_bg(surface, field):
    for row in range(ROWS):
        for col in range (COLS):
            if (row + col) % 2 == 0:
                color = (153,153,153) #gray
            else:
                color = (255,250,250)  #white
            
            rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)  
            
            pygame.draw.rect(surface, color, rect) 

            #Font
            font = pygame.font.Font('freesansbold.ttf', 18)
            text = str(field[row][col][1]+1)
            text = font.render(text, True, white)
            textRect = text.get_rect()

            if field[row][col][0] == 1:
                surface.blit(PlayerOneImg, pygame.Rect(col*SQSIZE, (row-1)*SQSIZE, SQSIZE, 2*SQSIZE))
                textRect.center = ((col*SQSIZE)+(SQSIZE//2), ((row-1)*SQSIZE)+SQSIZE)
                surface.blit(text, textRect)
            elif field[row][col][0] == 2:
                surface.blit(PlayerTwoImg, pygame.Rect((col-1)*SQSIZE, row*SQSIZE, 2*SQSIZE, SQSIZE))
                textRect.center = ((col*SQSIZE), ((row-1)*SQSIZE)+(SQSIZE*1.5))
                surface.blit(text, textRect)

def HoverPlayerOne(rows:int, cols:int, field, surface):
    if IsMoveValidOne(rows, cols, field):
        surface.blit(PlayerOneImg, pygame.Rect(cols*SQSIZE, (rows-1)*SQSIZE, SQSIZE, 2*SQSIZE)) 

def HoverPlayerTwo(rows:int, cols:int, field, surface):
    if IsMoveValidTwo(rows, cols, field):
        surface.blit(PlayerTwoImg, pygame.Rect(cols*SQSIZE, rows*SQSIZE, 2*SQSIZE, SQSIZE))

class Main:        
    def __init__ (self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Domineering')      #naziv prozora
        Icon = pygame.image.load('images/logo.png')     #logo igrice/prozora
        pygame.display.set_icon(Icon)     

    def mainLoop(self):
            
        Field = CreateMatrix(ROWS,COLS)
        screen = self.screen
        GameState = True
        
        while True:
            
            # show methods
            show_bg(screen, Field)
                
            for event in pygame.event.get():  
                if event.type == pygame.MOUSEBUTTONDOWN:
                    location = pygame.mouse.get_pos()
                    col = location[0]//SQSIZE # x koordinata pozicije klika
                    row = location[1]//SQSIZE # y koordinata pozicije klika

                    if GameState == True:
                        if PlayerOneMove(row,col,Field):
                            pygame.display.set_caption('Player 2 is on the move') #when state changes other player is on the move
                            GameState = False
                    else:
                        if PlayerTwoMove(row,col,Field):
                            pygame.display.set_caption('Player 1 is on the move') #when state changes other player is on the move
                            GameState = True
                #keypress
                elif event.type == pygame.KEYDOWN:

                        # reseting game
                    if event.key == pygame.K_r:
                        main.mainLoop()
                        
                        #### OVO OSTAJE JOS ####
                        
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            #ovo se uvek izvrsava nma nikakv if samo se vidi ko je na potez
            location = pygame.mouse.get_pos()
            col = location[0]//SQSIZE
            row = location[1]//SQSIZE
            if GameState == True:
                HoverPlayerOne(row, col, Field, screen)
            else:
                HoverPlayerTwo(row, col, Field, screen)

            pygame.display.update()         
               
main = Main()
main.mainLoop()