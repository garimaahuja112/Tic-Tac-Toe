import numpy as np
import pygame
import math

ROWS=3
COLS=3
board=np.zeros((ROWS,COLS))       #creates a 3*3 matrix of zeros

WIDTH=600
HEIGHT=600

WHITE=(255,255,255)
BLACK=(0,0,0)
BLUE=(0,0,255)
RED=(255,0,0)

CIRCLE=pygame.image.load("circle.png")   #load(import) an image from your computer
CROSS=pygame.image.load("x.png")

def draw_lines():
	# pygame.draw.line(display,color,start_point,end_point,width)
	# (0,0) is at top left corner of display
	# X increases as we move right
	# Y increases as we move down 
	pygame.draw.line(window,BLACK,(200,0),(200,600),10)
	pygame.draw.line(window,BLACK,(400,0),(400,600),10)
	pygame.draw.line(window,BLACK,(0,200),(600,200),10)
	pygame.draw.line(window,BLACK,(0,400),(600,400),10)

def draw_mark():
	for r in range(ROWS):
		for c in range(COLS):
			if board[r][c]==1:
				window.blit(CIRCLE,(c*200+50,r*200+50))  #Top left corner of the image will be placed at the given position
			elif board[r][c]==2:
				window.blit(CROSS,(c*200+50,r*200+50))

	pygame.display.update()

def mark(row,col,player):
	board[row][col]=player

def is_valid_mark(row,col):
	return board[row][col]==0

def is_board_full():
	for r in range(ROWS):
		for c in range(COLS):
			if board[r][c]==0:
				return False

	return True			

def is_winning_move(player):
	if player==1:
		winning_color=BLUE
	elif player==2:
		winning_color=RED

	#Horizontal Check
	for r in range(ROWS):
		if board[r][0]==board[r][1]==board[r][2]==player:
			pygame.draw.line(window,winning_color,(10,r*200+100),(WIDTH-10,r*200+100),10)
			return True

	#Vertical Check
	for c in range(COLS):
		if board[0][c]==board[1][c]==board[2][c]==player:
			pygame.draw.line(window,winning_color,(c*200+100,10),(c*200+100,HEIGHT-10),10)
			return True

	#Positive Diagonal Check
	if board[0][0]==board[1][1]==board[2][2]==player:
			pygame.draw.line(window,winning_color,(10,10),(WIDTH-10,HEIGHT-10),10)
			return True

	#Negative Diagonal Check
	if board[0][2]==board[1][1]==board[2][0]==player:
			pygame.draw.line(window,winning_color,(WIDTH-10,10),(10,HEIGHT-10),10)
			return True

game_over=False
Turn=0

pygame.init()  #initialize pygame
window=pygame.display.set_mode((WIDTH,HEIGHT))  #Create game window(display surface) of the given size 
pygame.display.set_caption("Tic Tac Toe")  #Set title of the game window
window.fill(WHITE)  #Set background color
draw_lines()
pygame.display.update()  #Always write this line after changing anything in the display
pygame.time.wait(10000)  #Window will show for 2sec and terminate after that 

while not game_over:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
				pygame.quit()
		if event.type==pygame.MOUSEBUTTONDOWN:
			print(event.pos)   #pos is mouse click position on our window
			if Turn%2==0:
				#Player1
				row=math.floor(event.pos[1]/200)
				col=math.floor(event.pos[0]/200)

				if is_valid_mark(row,col):
					mark(row,col,1)
					if is_winning_move(1):
						game_over=True
				else:
					Turn-=1

			else:
				#Player2
				row=math.floor(event.pos[1]/200)
				col=math.floor(event.pos[0]/200)

				if is_valid_mark(row,col):
					mark(row,col,2)
					if is_winning_move(2):
						game_over=True
				else:
					Turn-=1

			Turn+=1
			print(board)
			draw_mark()
	
	if is_board_full():
		game_over=True

	if game_over==True:
		print("Game Over!")
		pygame.time.wait(2000)  #Delay of 2sec
		board.fill(0)
		game_over=False
		Turn=0
		window.fill(WHITE)
		draw_lines()
		pygame.display.update()
		
