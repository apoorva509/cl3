import json

def isattack(board, r, c):
	for i in range(r):
		if board[i][c]==1:
			return True
			
	i=r-1
	j=c-1
	while(i>=0 and j>=0):
		if board[i][j]==1:
			return True
		i-=1
		j-=1
	
	i=r-1
	j=c+1
	while(i>=0 and j<8):
		if board[i][j]==1:
			return True
		i-=1
		j+=1
	return False



def solve(board, row):
	i = 0
	while(i<8):
		if(not isattack(board, row, i)):
			board[row][i]=1
			if row==7:
				return True
			else:
				if(solve(board, row+1)):
					return True
				else:
					board[row][i]=0
		i+=1
	if i==8:
		return False



def display(board):
	for i in range(8):
		for j in range(8):
			print str(board[i][j])+" ",
		print "\n"
		
board = [[0 for x in range(8)]for x in range(8)]

if __name__ == '__main__':
	pos = []
	f = open('input.json')
	pos = json.load(f)
	
	if( pos["start"]<0 or pos["start"]>7):
		print "Invalid JSON input!"
		exit()
	
	board[0][pos["start"]] = 1
	if(solve(board,1)):
		print "\nSuccess!\n"
		print "\nBoard Configuration : \n"
		display(board)
	else:
		print "Failure!"
