board={ '1':' ','2':' ','3':' ',
'4':' ','5':' ','6':' ',
'7':' ','8':' ','9':' '}

def printboard(board):
    print(board['1']+"|"+board['2']+"|"+board['3'])
    print("-+-+-")
    print(board['4']+"|"+board['5']+"|"+board['6'])
    print("-+-+-")
    print(board['7']+"|"+board['8']+"|"+board['9'])

def playgame():
    print("_"*50)
    print("\n********** WELCOME **********\n")
    turn='x'
    count=0
    for _ in range(1,10):
        printboard(board)
        print("\nNow "+turn+" turn\n")
        move=input("enter position : ")
        if board[move]==' ':
            board[move]=turn
            count+=1
        else:
            print("\n--Position Already Filled--\n")
            continue
        if count>=5:
            if board['1']==board['2']==board['3']!=" ":
                printboard(board)
                print("\n!!!!! Game Over !!!!!")
                print("\n******** "+turn+" WIN THE GAME ********")
                break
            elif board['4']==board['5']==board['6']!=" ":
                printboard(board)
                print("\n!!!!! Game Over !!!!!")
                print("\n******** "+turn+" WIN THE GAME ********")
                break
            elif board['7']==board['8']==board['9']!=" ":
                printboard(board)
                print("\n!!!!! Game Over !!!!!")
                print("\n******** "+turn+" WIN THE GAME ********")
                break
            elif board['1']==board['4']==board['7']!=" ":
                printboard(board)
                print("\n!!!!! Game Over !!!!!")
                print("\n******** "+turn+" WIN THE GAME ********")
                break
            elif board['2']==board['5']==board['8']!=" ":
                printboard(board)
                print("\n!!!!! Game Over !!!!!")
                print("\n******** "+turn+" WIN THE GAME ********")
                break
            elif board['3']==board['6']==board['9']!=" ":
                printboard(board)
                print("\n!!!!! Game Over !!!!!")
                print("\n******** "+turn+" WIN THE GAME ********")
                break
            elif board['1']==board['5']==board['9']!=" ":
                printboard(board)
                print("\n!!!!! Game Over !!!!!")
                print("\n******** "+turn+" WIN THE GAME ********")
                break
            elif board['3']==board['5']==board['7']!=" ":
                printboard(board)
                print("\n!!!!! Game Over !!!!!")
                print("\n******** "+turn+" WIN THE GAME ********")
                break

        if count==9:
            printboard(board)
            print("\n!!!!! Game Over !!!!!\n")
            print("******** GAME TIE ********")
            

        if turn=='x':
            turn='o'
        else:
            turn='x'

    print("\n********** THANK YOU FOR PLAYING **********\n")
    print("_"*50)
    restart=input("\nDo you want to play Again?\nYes\nNo\n")
    if restart=="Yes" or restart=="yes":
        for key in board:
            board[key]=" "
        playgame()
        
if __name__=="__main__":
    playgame()