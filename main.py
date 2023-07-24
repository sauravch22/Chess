from flask import Flask , request
import numpy as np

Mapper = {
    1 : 'A', 2 : 'B', 3:'C', 4:'D', 5:'E',  6:'F', 7:'G', 8:'H',
    'A' : 1, 'B' : 2, 'C' : 3, 'D': 4, 'E':5, 'F':6, 'G':7, 'H':8
}

app = Flask(__name__)

def moves(name,pos,board):
    if name == "Queen":
        print('Queen Moves')
        posX = 8 - (ord(pos[0]) - 64)
        posY = 8 - (ord(pos[1]) - 48)
        for i in range(1,posY+1):
            if i!= posY:
                board[posX][i] = 1
        for i in range(1,posX+1):
            if i!=posX:
                board[i][posY] = 1

        moving_pos_x = posX
        moving_pos_y = posY
        while moving_pos_x > 1 and moving_pos_y > 1:
            board[moving_pos_x-1][moving_pos_y-1] = 1
            moving_pos_x -= 1
            moving_pos_y -= 1

        moving_pos_x = posX
        moving_pos_y = posY
        while moving_pos_x < 7 and moving_pos_y > 1:
            board[moving_pos_x+1][moving_pos_y-1] = 1
            moving_pos_x += 1
            moving_pos_y -= 1
        
        moving_pos_x = posX
        moving_pos_y = posY
        while moving_pos_x < 7 and moving_pos_y < 9:
            board[moving_pos_x+1][moving_pos_y+1] = 1
            moving_pos_x += 1
            moving_pos_y += 1

        moving_pos_x = posX
        moving_pos_y = posY
        while moving_pos_x < 1 and moving_pos_y < 7:
            board[moving_pos_x-1][moving_pos_y+1] = 1
            moving_pos_x -= 1
            moving_pos_y += 1


    elif name == "Bishop":
        print('Bishop Moves')
        posX = 8 - (ord(pos[0]) - 64)
        posY = 8 - (ord(pos[1]) - 48)
        moving_pos_x = posX
        moving_pos_y = posY
        while moving_pos_x > 1 and moving_pos_y > 1:
            board[moving_pos_x-1][moving_pos_y-1] = 1
            moving_pos_x -= 1
            moving_pos_y -= 1

        moving_pos_x = posX
        moving_pos_y = posY
        while moving_pos_x < 7 and moving_pos_y > 1:
            board[moving_pos_x+1][moving_pos_y-1] = 1
            moving_pos_x += 1
            moving_pos_y -= 1
        
        moving_pos_x = posX
        moving_pos_y = posY
        while moving_pos_x < 7 and moving_pos_y < 7:
            board[moving_pos_x+1][moving_pos_y+1] = 1
            moving_pos_x += 1
            moving_pos_y += 1

        moving_pos_x = posX
        moving_pos_y = posY
        while moving_pos_x < 1 and moving_pos_y < 7:
            board[moving_pos_x-1][moving_pos_y+1] = 1
            moving_pos_x -= 1
            moving_pos_y += 1
        

    elif name == "Rook":
        print("Rook moves")
        posX = 8 - (ord(pos[0]) - 64)
        posY = 8 - (ord(pos[1]) - 48)
        for i in range(1,posY+1):
            if i!= posY:
                board[posX][i] = 1
        for i in range(1,posX+1):
            if i!=posX:
                board[i][posY] = 1

    else:
        print("Kinght moves")
        posX = 8 - (ord(pos[0]) - 64)
        posY = 8 - (ord(pos[1]) - 48)
        currPosX = posX+2
        currPosY = posY+1
        if currPosX >= 1 and currPosY >= 1 and currPosX <9 and currPosY <9:
            board[currPosX][currPosY] = 1
        currPosX = posX+1
        currPosY = posY+2
        if currPosX >= 1 and currPosY >= 1 and currPosX <9 and currPosY <9:
            board[currPosX][currPosY] = 1
        currPosX = posX-2
        currPosY = posY-1
        if currPosX >= 1 and currPosY >= 1 and currPosX <9 and currPosY <9:
            board[currPosX][currPosY] = 1
        currPosX = posX-1
        currPosY = posY-2
        if currPosX >= 1 and currPosY >= 1 and currPosX <9 and currPosY <9:
            board[currPosX][currPosY] = 1


def result(name, pos, board):
    print(name, " " ,pos)
    valid_moves = []
    if name == 'Queen' :
        posX = 8 - (ord(pos[0]) - 64)
        posY = 8 - (ord(pos[1]) - 48)
        for i in range(1,posY+1):
            if i!= posY and board[posX][i] == 0:
                valid_moves.append(Mapper[posX]+""+str(i))

        for i in range(1,posX+1):
            if i!=posX and board[i][posY] == 0:
                valid_moves.append(Mapper[i]+""+str(posY))

        moving_pos_x = posX
        moving_pos_y = posY
        while moving_pos_x > 1 and moving_pos_y > 1:
            #print(moving_pos_x-1," ",moving_pos_y-1)
            if board[moving_pos_x-1][moving_pos_y-1] == 0:
                valid_moves.append(Mapper[moving_pos_x-1]+""+str((moving_pos_y-1)))
            moving_pos_x -= 1
            moving_pos_y -= 1

        moving_pos_x = posX
        moving_pos_y = posY
        while moving_pos_x < 7 and moving_pos_y > 1:
            if board[moving_pos_x+1][moving_pos_y-1] == 0:
                valid_moves.append(Mapper[moving_pos_x+1]+""+str(moving_pos_y-1))
            moving_pos_x += 1
            moving_pos_y -= 1
        
        moving_pos_x = posX
        moving_pos_y = posY
        while moving_pos_x < 7 and moving_pos_y < 7:
            if board[moving_pos_x+1][moving_pos_y+1] == 0:
                valid_moves.append(Mapper[moving_pos_x+1]+""+str(moving_pos_y+1))
            moving_pos_x += 1
            moving_pos_y += 1

        moving_pos_x = posX
        moving_pos_y = posY
        while moving_pos_x >1 and moving_pos_y < 7:
            if board[moving_pos_x-1][moving_pos_y+1] == 0:
                valid_moves.append(Mapper[moving_pos_x-1]+""+str(moving_pos_y+1))
            moving_pos_x -= 1
            moving_pos_y += 1
                


    elif name == "Bishop":
        posX = 8 - (ord(pos[0]) - 64)
        posY = 8 - (ord(pos[1]) - 48)

        moving_pos_x = posX
        moving_pos_y = posY

        #print(moving_pos_x," ",moving_pos_y)

        while moving_pos_x > 1 and moving_pos_y > 1:
            #print("->",moving_pos_x," ",moving_pos_y)
            if board[moving_pos_x-1][moving_pos_y-1] == 0:
                valid_moves.append(Mapper[moving_pos_x-1]+""+str(moving_pos_y-1))
            moving_pos_x -= 1
            moving_pos_y -= 1

        print(valid_moves)

        moving_pos_x = posX
        moving_pos_y = posY

        while moving_pos_x < 7 and moving_pos_y > 1:
            if board[moving_pos_x+1][moving_pos_y-1] == 0:
                valid_moves.append(Mapper[moving_pos_x+1]+""+str(moving_pos_y-1))
            moving_pos_x += 1
            moving_pos_y -= 1
        
        moving_pos_x = posX
        moving_pos_y = posY
        print(valid_moves)

        while moving_pos_x < 7 and moving_pos_y < 7 :
            if board[moving_pos_x+1][moving_pos_y+1] == 0:
                valid_moves.append(Mapper[moving_pos_x+1]+""+str(moving_pos_y+1))
            moving_pos_x += 1
            moving_pos_y += 1

        moving_pos_x = posX
        moving_pos_y = posY
        print(valid_moves)

        while moving_pos_x < 1 and moving_pos_y < 7:
            if board[moving_pos_x-1][moving_pos_y+1] == 1:
                valid_moves.append(Mapper[moving_pos_x+1]+""+str(moving_pos_y+1))
            moving_pos_x -= 1
            moving_pos_y += 1

        print(valid_moves)



    elif name == "Rook":

        posX = 8 - (ord(pos[0]) - 64)
        posY = 8 - (ord(pos[1]) - 48)
        for i in range(1,posY+1):
            if i!= posY and board[posX][i] == 0:
                valid_moves.append(Mapper[posX]+""+str(i))
                
        for i in range(1,posX+1):
            if i!=posX and board[i][posY] == 0:
                valid_moves.append(Mapper[i]+""+str(posY))

    else:
        print(board)
        posX = 8 - (ord(pos[0]) - 64)
        posY = 8 - (ord(pos[1]) - 48)

        currPosX = posX+2
        currPosY = posY+1
        print(currPosX," ",currPosY)

        if currPosX >= 1 and currPosY >= 1 and currPosX <9 and currPosY <9:
            if board[currPosX][currPosY] == 0:
                valid_moves.append(Mapper[8-currPosX]+""+str(8-currPosY))

        currPosX = posX+1
        currPosY = posY+2

        if currPosX >= 1 and currPosY >= 1 and currPosX <9 and currPosY <9:
            if board[currPosX][currPosY] == 0:
                valid_moves.append(Mapper[8-currPosX]+""+str(8-currPosY))

        currPosX = posX-2
        currPosY = posY-1

        if currPosX >= 1 and currPosY >= 1 and currPosX <9 and currPosY <9:
            if board[currPosX][currPosY] == 0:
                valid_moves.append(Mapper[8-currPosX]+""+str(8-currPosY))

        currPosX = posX-1
        currPosY = posY-2

        if currPosX >= 1 and currPosY >= 1 and currPosX <9 and currPosY <9:
            if board[currPosX][currPosY] == 0:
                valid_moves.append(Mapper[8-currPosX]+""+str(8-currPosY))

    return valid_moves
            

def func(name,curr_pos_queen,curr_pos_knight,curr_pos_bishop,curr_pos_Rook):
    #print(curr_pos_queen," ",curr_pos_bishop," ",curr_pos_knight," ",curr_pos_Rook)
    board = np.zeros((10,10), dtype=int)
    eligible_moves = []
    if name == "Queen":
        print('Queen')
        moves('Bishop',curr_pos_bishop,board)
        moves('Knight',curr_pos_knight,board)
        moves('Rook',curr_pos_Rook,board)
        eligible_moves = result('Queen',curr_pos_queen,board)

    elif name == 'Bishop':
        print('Bishop')
        moves('Queen',curr_pos_knight,board)
        moves('Knight',curr_pos_Rook,board)
        moves('Rook',curr_pos_queen,board)
        eligible_moves = result('Bishop',curr_pos_bishop,board)

    elif name == 'Knight':
        print('Knight')
        moves('Rook',curr_pos_Rook,board)
        moves('Bishop',curr_pos_queen,board)
        moves('Queen',curr_pos_bishop,board)
        eligible_moves = result('Knight',curr_pos_knight,board)

    elif name == 'Rook' :
        print('Rook')
        moves('Bishop',curr_pos_bishop,board)
        moves('Knight',curr_pos_knight,board)
        moves('Queen',curr_pos_queen,board)
        eligible_moves = result('Rook',curr_pos_Rook,board)

    else :
        print('Pieces can be only Queen, Bishop, Knight, Rook')
    return eligible_moves



@app.route('/chess/<string:name>' , methods = ['GET', 'POST'])
def hello_world(name):
    data = request.json
    curr_pos_queen = data.get('positions').get('Queen')
    curr_pos_bishop = data.get('positions').get('Bishop')
    curr_pos_knight = data.get('positions').get('Knight')
    curr_pos_Rook = data.get('positions').get('Rook')
    validmoves = func(name,curr_pos_queen,curr_pos_knight,curr_pos_bishop,curr_pos_Rook)
    resultant_moves = {"valid_moves":validmoves}
    return resultant_moves

if __name__ == "__main__":
    app.run(port=8080,debug=True)