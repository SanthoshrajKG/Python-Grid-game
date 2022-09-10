class gridgame():
    
    board=[(['....']*5)[:] for i in range(5)]
    
    def __init__(self): 
        print("Player 1 enter the initial values..eg(p1 p2 p3 p4 p5) :")
        p1="P3 P4 P5 P1 P2" #input()
        p1=list(p1.split(" "))
        print("Player 2 enter the initial values..eg(p1 p2 p3 p4 p5) :")
        p2="P1 P2 P3 P4 P5" #input()
        p2=list(p2.split(" "))
        for i in range(5):
            self.board[4][i]="A-"+p1[i]
            self.board[0][i]="B-"+p2[i]

    def changeBoard(self,player,cmd):
        if(player=='A'):
            for i in range(5):
                for j in range(5):
                    if(self.board[i][j]==player+'-'+cmd[:2]):
                        if((cmd[3:]=='L' and j==0) or (cmd[3:]=='R' and j==4) or (cmd[3:]=='B' and i==4) or (cmd[3:]=='F' and i==0 )):
                                print("invalid command..")
                                return False
                        elif(cmd[3:]=='F'):
                            self.board[i-1][j]=self.board[i][j]
                            self.board[i][j]='....'
                            return True
                        elif(cmd[3:]=='B'):
                            self.board[i+1][j]=self.board[i][j]
                            self.board[i][j]='....'
                            return True
                        elif(cmd[3:]=='L'):
                            self.board[i][j-1]=self.board[i][j]
                            self.board[i][j]='....'
                            return True
                        elif(cmd[3:]=='R'):
                            self.board[i][j+1]=self.board[i][j]
                            self.board[i][j]='....'
                            return True

                    
        if(player=='B'):
            for i in range(5):
                for j in range(5):
                    print(self.board[i][j],player+'-'+cmd[:2])
                    if(self.board[i][j]==player+'-'+cmd[:2]):
                        if((cmd[3:]=='L' and j==0) or (cmd[3:]=='R' and j==4) or (cmd[3:]=='B' and i==0) or (cmd[3:]=='F' and i==4 )):
                                print(cmd[3:],i,j)
                                print("invalid command..")
                                return False
                        elif(cmd[3:]=='F'):
                            print("reached",i,j)
                            self.board[i+1][j]=self.board[i][j]
                            self.board[i][j]='....'
                            return True
                        elif(cmd[3:]=='B'):
                            self.board[i-1][j]=self.board[i][j]
                            self.board[i][j]='....'
                            return True
                        elif(cmd[3:]=='L'):
                            self.board[i][j+1]=self.board[i][j]
                            self.board[i][j]='....'
                            return True
                        elif(cmd[3:]=='R'):
                            self.board[i][j-1]=self.board[i][j]
                            self.board[i][j]='....'
                            return True
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
    while(1):
        print("Enter the Player2 command...")
        p2=input()
        if grid.changeBoard('B',p2):
            break
    grid.printboard()
    opt=input("Y/N to continue?.....")




