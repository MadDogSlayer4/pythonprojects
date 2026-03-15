# about: This function prints pascels triangle
# Author: Maddie

def triangle(h):

    # Allows sequences to be correct for odd and even triangle heights
    if h%2!=0:
        plusr1=-1
        plusr2=1
        makeEven=1
    else:
        plusr1=1
        plusr2=-1
        makeEven=0

    matrix = []
    for row in range(h):
        
        matrix.append([])

        for col in range(0,h*2):

            # Builds first row
            if row == 0:
                if col==h-1 or col==h:
                    a=1
                else: a=0
                matrix[row].append(a)

            # Builds all first and last columns
            elif col == 0:
                if (row+makeEven)%2!=0:
                    #seq 1
                    matrix[row].append(matrix[row-1][col]+matrix[row-1][col+1])
                else:
                    matrix[row].append(matrix[row-1][col])
            elif col == h*2-1:
                if (row+makeEven)%2!=0:
                    #seq 2
                    matrix[row].append(matrix[row-1][col]+matrix[row-1][col-1])
                else:
                    matrix[row].append(matrix[row-1][col])

            # Builds the rest
            else:
                #even
                if (row%2!=0 and col%2==0) or (row%2==0 and col%2!=0):
                    # seq 1
                    matrix[row].append(matrix[row-1][col]+matrix[row-1][col+plusr1])
                else:
                    #seq 2
                    matrix[row].append(matrix[row-1][col]+matrix[row-1][col+plusr2])  

    # Remove extra numbers
    i = 0
    for row in range(h):
        counter=False
        ran=False
        i=0
        for col in range(0,h*2):
            num = matrix[row][col]
            if num == 1 and ran==False:
                counter=True
                ran=True
            if i == 1:
                matrix[row][col] = 0
                i=-1 
            if counter==True:
                i += 1

    # print triangle - - - - - -

    # Finds max num and get its digits
    maxdigit = len(str(max(max(matrix))))

    for row in range(h):
        for col in range(0,h*2):
            num = matrix[row][col]
            digits = len(str(num))

            addspace=maxdigit-digits
            print(" "*addspace, end="")
            
            if num!=0:
                print(str(num), end="")
            else:
                print(" ", end="")

        print("\n")
    return matrix

triangle(20)