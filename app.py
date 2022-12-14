class gridgame():
    
    board=[(['....']*5)[:] for i in range(5)]
    
    def __init__(self): 
        print("Player 1 enter the initial values..eg(p1 p2 p3 p4 p5) :")
        p1="P3 P4 P5 P1 P2"#input() # 
        p1=list(p1.split(" "))
        print("Player 2 enter the initial values..eg(p1 p2 p3 p4 p5) :")
        p2="P1 P2 P3 P4 P5"#-input() # 
        p2=list(p2.split(" "))
        for i in range(5):
            self.board[4][i]="A-"+p1[i]
            self.board[0][i]="B-"+p2[i]

    def changeBoard(self,player,cmd):
        for i in range(5):
            for j in range(5):
                if(self.board[i][j]==player+'-'+cmd[:2]):
                    newi=i
                    newj=j
                    if((cmd[3:]=='F' and player=='A') or (cmd[3:]=='B' and player=='B')):
                        newi=i-1
                    elif((cmd[3:]=='B' and player=='A') or (cmd[3:]=='F' and player=='B') ):
                        newi=i+1
                    elif((cmd[3:]=='L' and player=='A') or (cmd[3:]=='R' and player=='B') ):
                        newj=j-1
                    elif((cmd[3:]=='R' and player=='A') or (cmd[3:]=='L' and player=='B')):
                        newj=j+1
                    if(newi<0 or newj <0 or newi>4 or newj > 4):
                        print("invalid command..")
                        return False
                    if(self.board[newi][newj]!='....' and  self.board[newi][newj][:1]==player):
                        print("Targeted a friendly character...")
                        return False
                    self.board[newi][newj]=self.board[i][j]
                    self.board[i][j]='....'
                    return True
    def checkboard(self,player):
        for i in range(5):
            for j in range(5):
                if(self.board[i][j]=='....'):
                    continue
                elif(self.board[i][j][:1]==player):
                    return False
        return True

    def printboard(self):
        for i in self.board:
            print(i)

grid=gridgame()
grid.printboard()
opt='Y'
while(opt=='Y'):
    while(1):
        print("Enter the Player1 command...")
        p1=input()
        if grid.changeBoard('A',p1):
            break
    grid.printboard()
    if(grid.checkboard('B')):
        print("Player A won the game !!!")
        break
    while(1):
        print("Enter the Player2 command...")
        p2=input()
        if grid.changeBoard('B',p2):
            break
    grid.printboard()
    if(grid.checkboard('A')):
        print("Player B won the game !!!")
        break
    opt='Y'#input("Y/N to continue?.....")




