

def printb(b):
    cli = ""
    for i in range(9):

        if i%3==0:
            cli += 22*"▉" + "\n"
        
        for j in range(9):
            if j%3==0:
                cli += "▉"
            
            cli += str(b[i][j]) + " "
        
        cli += "▉\n"

    cli += 22*"▉" + "\n"

    print(cli)