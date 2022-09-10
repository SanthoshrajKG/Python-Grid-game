class gridgame():
    
    board=[(['.']*5)[:] for i in range(5)]
    
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

    def changeBoard(self,cmd):
        if(cmd[3:] in ['L','R','B']):
            print("invalid command..")
            return False
        return True

    def printboard(self):
        for i in self.board:
            print(i)

grid=gridgame()
grid.printboard()
opt='y'
while(opt=='y'):
    while(1):
        print("Enter the Player1 command...")
        p1=input()
        if grid.changeBoard(p1):
            break
    while(1):
        print("Enter the Player2 command...")
        p2=input()
        if grid.changeBoard(p2):
            break
    opt=input("y/n to continue?...")




