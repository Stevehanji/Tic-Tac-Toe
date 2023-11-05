import pygame

pygame.init()

screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))

caption = "Tic Tac Toe"
pygame.display.set_caption(caption)

icon = pygame.image.load("icon.ico")
pygame.display.set_icon(icon)

edge = 3
width = 10

# Color
BG = (255, 204, 153)
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (102, 255, 102)
RED = (255,0,0)
BLUE = (0,0,255)

def draw():
    # Draw Background
    screen.fill(BG)

    # Draw Line
    for i in range(1,edge):
        pygame.draw.line(screen,BLACK,(i*200,0),(i*200,screen_height),width)
        pygame.draw.line(screen,BLACK,(0,i*200),(screen_width,i*200),width)

def draw_x_and_o():
    x_pos = 0
    for x in a:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.circle(screen,GREEN,((x_pos * 200) + 101, y_pos * 200 + 100),90,width)
            
            elif y == 2:
                pygame.draw.line(screen,RED,((x_pos * 200) + 20,(y_pos * 200) + 20),((x_pos * 200) + 180, (y_pos * 200) + 180),width)
                pygame.draw.line(screen,RED,((x_pos * 200) + 180, (y_pos * 200) + 20),((x_pos * 200) + 20,(y_pos * 200) + 180),width)

            y_pos += 1
        
        x_pos += 1

def covert_to_vertical(arr):
    A = []

    for i in range(len(arr)):
        B = []
        
        for j in range(len(arr)):
            B.append(arr[j][i])
        
        A.append(B)

    return A
    

def ARRAY2_TO_ARRAY1(arr):
    b = []
    for i in arr:
        b.extend(i)

    return b

def check_win():
    # Row

    for i in a:
        if i == [1,1,1]:
            return 1
            
        elif i == [2,2,2]:
            return 2
    
    # Col
    for i in covert_to_vertical(a):
        if i == [1,1,1]:
            return 1
            
        elif i == [2,2,2]:
            return 2
    
    # Horizontal
    if a[0][0] == 1 and a[1][1] == 1 and a[2][2] == 1:
        return 1
    
    elif a[0][0] == 2 and a[1][1] == 2 and a[2][2] == 2:
        return 2
    
    if a[2][0] == 1 and a[1][1] == 1 and a[0][2] == 1:
        return 1
    
    elif a[2][0] == 2 and a[1][1] == 2 and a[0][2] == 2:
        return 2

    if ARRAY2_TO_ARRAY1(a).count(0) == 0:
        return 3

    return 0

a = []
for i in range(edge):
    b = []

    for j in range(edge):
        b.append(0)
    
    a.append(b)
    
player_o = False
player_x = True

winner = 0


def Text(TEXT, COLOR,size,p = True,x = None, y = None, background = None):
    font = pygame.font.SysFont("Sans",size)
    text = font.render(TEXT,1,COLOR,background)
    if p:
        screen.blit(text,(screen_width // 2 - size, screen_height // 2 - size // 2))
    
    else:
        screen.blit(text,(x,y))

def won(player):
    Text("Press Space to Play Again",BLUE,50, p = False, x = screen_width // 2 - 230, y = screen_height // 2 + 100, background=BLACK)
    if player == 1:
        Text("O Win",WHITE,100,background=RED)
    
    if player == 2:
        Text("X Win",WHITE,100,background=RED)

def draw_():
    Text("DRAW",WHITE,100,background=RED)
    Text("Press Space to Play Again",BLUE,50, p = False, x = screen_width // 2 - 230, y = screen_height // 2 + 100, background=BLACK)
    

running = True
while running:
    draw()
    draw_x_and_o()
    winner = check_win()

    if winner == 1:
        won(1)
    
    elif winner == 2:
        won(2)
    
    elif winner == 3:
        draw_()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and winner == 0:
            if event.button == 1:
                mouse = pygame.mouse.get_pos()
                mouse_x = mouse[0] // 200
                mouse_y = mouse[1] // 200

                if player_o and a[mouse_x][mouse_y] == 0:
                    a[mouse_x][mouse_y] = 1
                    player_o = False
                    player_x = True
                
                elif player_x and a[mouse_x][mouse_y] == 0:
                    a[mouse_x][mouse_y] = 2
                    player_o = True
                    player_x = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and winner != 0:
                winner = 0
                a = []
                for i in range(edge):
                    b = []

                    for j in range(edge):
                        b.append(0)
                    
                    a.append(b)

            if event.key == pygame.K_ESCAPE:
                running = False
                
    pygame.display.update()

pygame.quit()