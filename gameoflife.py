from pygame import *
from random import *

X = 80
Y = 50
size = 10
N = 800
fps = 10 				
life_survive = [2,3,4,5] # labirynty 12345/3 # 1358/357	# miasta 2345/45678	
dead_resurection = [4,5,6,7,8]
color = [(255,0,0),(255,128,0),(0,255,128),(0,128,255),(255,0,128),(128,255,0),(128,0,255),(0,255,0),(0,0,255)]


init()
window = display.set_mode((size*X,size*Y+30))
clock = time.Clock()
Font=font.SysFont("comicsansms",32)

def new_game():
	board = []
	for i in range(X):
		boardtmp = []
		for j in range(Y):
			boardtmp.append(0)
		board.append(boardtmp)

	i = 0
	while i<N:
		x = randint(0,X-1)
		y = randint(0,Y-1)
		if board[x][y] == 0:
			i = i + 1
			board[x][y] = 1
	return board

def num_neigh(i,j,board):
	res = 0
	if board[(i-1+X)%X][j] == 1:
		res = res + 1
	if board[(i-1+X)%X][(j-1+Y)%Y] == 1:
		res = res + 1
	if board[(i-1+X)%X][(j+1+Y)%Y] == 1:
		res = res + 1
	if board[i][(j-1+Y)%Y] == 1:
		res = res + 1
	if board[i][(j+1+Y)%Y] == 1:
		res = res + 1
	if board[(i+1+X)%X][j] == 1:
		res = res + 1
	if board[(i+1+X)%X][(j-1+Y)%Y] == 1:
		res = res + 1
	if board[(i+1+X)%X][(j+1+Y)%Y] == 1:
		res = res + 1		
	return res

def game(board):
	old_board = []
	for i in range(X):
		tmp = []
		for j in range(Y):
			tmp.append(board[i][j])
		old_board.append(tmp)
		
	for j in range(Y):
		for i in range(X):
			if old_board[i][j] == 0: 
				if num_neigh(i,j,old_board) in dead_resurection:
					board[i][j] = 1
			elif old_board[i][j] == 1: 
				if not num_neigh(i,j,old_board) in life_survive:
					board[i][j] = 0
					
					
					
					
					
end = False
board = new_game()

while not end:
	for z in event.get():
		if z.type == QUIT:
			end = True
	keys=key.get_pressed()
	if keys[K_n]:
		board = new_game()
	if keys[K_a]:
		N = N+1
		board = new_game()
	if keys[K_z]:
		N = N-1
		board = new_game()
	window.fill((0,0,0))
	for i in range(X):
		for j in range(Y):
			if board[i][j] == 1:
				draw.rect(window,color[num_neigh(i,j,board)],Rect(i*size,j*size,size-1,size-1))		
				draw.rect(window,(0,0,0),Rect(i*size+1,j*size+1,size-3,size-3))
	
	
	text = Font.render("Board "+str(X)+"x"+str(Y)+", cells at the beginning: "+str(N),True,(255,255,255))
	window.blit(text,(20,Y*size+3))			
	game(board)
	
	clock.tick(fps)
	display.flip()