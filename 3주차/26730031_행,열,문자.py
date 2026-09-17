def printPattern(rows=5, cols=5, char="*"):
    for i in range(rows):
        for i in range(cols):
            print(char,end="")
        print()
     
printPattern(3,10,"%")
