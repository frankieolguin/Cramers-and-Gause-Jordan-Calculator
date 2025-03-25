
# calculates the determinant of a 3x3 matrix
def det3x3(mat):
    """
    
    | a0 a1 a2 |
    | b0 b1 b2 |
    | c0 c1 c2 |
    
    det = a0( b1 x c2 - b2 x c1 ) 
        - a1( b0 x c2 - b2 x c0 ) 
        + a2( b0 x c1 - b1 x c0 )
        
    """
    
    det = 0
    # a0( b1 x c2 - b2 x c1 ) 
    det += mat[0][0]*(mat[1][1]*mat[2][2] - mat[1][2]*mat[2][1]) 
    # - a1( b0 x c2 - b2 x c0 ) 
    det -= mat[0][1]*(mat[1][0]*mat[2][2] - mat[1][2]*mat[2][0])
    # + a2( b0 x c1 - b1 x c0 )
    det += mat[0][2]*(mat[1][0]*mat[2][1] - mat[1][1]*mat[2][0])
    
    return det 

# Takes a system of equations in the form of a 3x3 matrix and 1x3 coefficient matrix
# calcultes the values of 3 variables (if able to) using Cramer's Rule and returns a list of 3 values
def solveCramers(mat,co_mat):
    
    matA = [row[:] for row in mat]
    matB = [row[:] for row in mat]
    matC = [row[:] for row in mat]
    sol = []
    det = 0
    detA = 0 
    detB = 0 
    detC = 0
    sol_x = 0 
    sol_y = 0 
    sol_z = 0
     
    for i in range(len(mat)):
        matA[i][0] = co_mat[i]
    for j in range(len(mat)):
        matB[j][1] = co_mat[j]
    for k in range(len(mat)):
        matC[k][2] = co_mat[k]
    # the new matrices for Cramers Rule should be ready for calculations
    print("This is Matrix A")
    printMatrix(matA)
    print("This is Matrix B")
    printMatrix(matB)
    print("This is Matrix C")
    printMatrix(matC)
    det = det3x3(mat)
    if det == 0:
        sol.append(0)
        sol.append(0)
        sol.append(0)
        print("Determinant is 0, therfore Cramer's Rule will not work. ")
        return sol
    detA= det3x3(matA)
    detB= det3x3(matB)   
    detC= det3x3(matC)
    sol_x = detA/det
    sol_y = detB/det
    sol_z = detC/det
    sol.append(sol_x)
    sol.append(sol_y)
    sol.append(sol_z)
    return sol

def printMatrix(m):
    # prints the matrix in a readable format
    for row in m:
        print(row)
    
    print()
    return

def rowEchelonReduction(m):
    
    # diagonal elements should be non-zero
    # this loop makes sure all diagonal elements are non zero
    for i in range(3):
        # m[i][i] is always diagonal
        if m[i][i] == 0:
            for j in range(i + 1, 3):
                if m[j][i] != 0:
                    # we swap entire rows here
                    m[i], m[j] = m[j], m[i]
                    # we break from internal for loop once we swap our incompatible rows
                    break
                
        # The reduce the diagonal to a 1 by dividing each value in the row by the diagonal value
        diagonal_val=m[i][i]
        if m[i][i] != 1:
            for j in range(4):
                if diagonal_val==0:
                    print("ERROR/n Attempting to divbe by a diagonal that is ZERO!")
                    print("THE system of equations resulted in a singular matrix which is not solvable using this method.")
                    error = []
                    return error
                m[i][j] /= diagonal_val
                
        # we reduce the the remaining values in the collumn to 0's by adding riws together
        # the diagonal should be a zero which makes the process simpler!
        for j in range(3):
            if i==j:
                continue
            target  = m[j][i]
            if target != 0:
                for k in range (4):
                    m[j][k]-=m[i][k]*target
    #
    return m

# This contains our Gauss-Jordan operations
def gaussJordan():
    # The user fills in 3x3 Matrix
    matrix = []
    co_matrix = []
    
    # The user fills in the 3x3 matrix
    for i in range(3):
        row = []
        for j in range(3):
            element = int(input(f"Enter element for position ({i},{j}): "))
            row.append(element)
        matrix.append(row)
        
    # The user fills in the answer collumn
    print("\nPlease enter the 3 values of the answer collumn for our system of equations. \n")    
    for i in range(3):
        element = int(input(f"Enter element for position ({i}): "))
        co_matrix.append(element)
        
    # we append the answer collumn to our original 3x3 matrix to create an augmented matrix which is 3x4
    for i in range(len(matrix)):
        matrix[i].append(co_matrix[i])
        
    # We can now begin row echelon reduction operations on our augmented matrix
    print("This is our augmented matrix\n")
    printMatrix(matrix)
    reduced_matrix = []    
    reduced_matrix = rowEchelonReduction(matrix)
    # an invalid matrix will return a null matrix and that signifies an error so we return!
    if len(reduced_matrix) == 0:
        return
    print("This is our reduced matrix!\n")
    printMatrix(reduced_matrix)
    for i in range (3):
        xy_or_z = 0
        for j in range (3):
            if reduced_matrix[i][j] == 1:
                xy_or_z = j
                break
        match xy_or_z:
            case 0:
                print("X is = " + str(reduced_matrix[i][3]))
            case 1:
                print("Y is = " + str(reduced_matrix[i][3]))
            case 2:
                print("Z is = " + str(reduced_matrix[i][3]))
            case _:
                print("Something went wrong! \n")

    return

# This contains our Cramer's Rule operations
def cramersRule():
    matrix = []
    co_matrix = []
    for i in range(3):
        row = []
        for j in range(3):
            element = int(input(f"Enter element for position ({i},{j}): "))
            row.append(element)
        matrix.append(row)
    # The user fills in the answer collumn
    print("\nPlease enter the 3 values of the answer collumn for our system of equations. \n")    
    for i in range(3):
        element = int(input(f"Enter element for position ({i}): "))
        co_matrix.append(element)

    printMatrix(matrix)
    # print("This is the determinant of our original Matrix: ")
    # print(det3x3(matrix))
    # print("\n")
    xyz=[]
    xyz = solveCramers(matrix,co_matrix)
    print("x = " + str(xyz[0]))
    print("y = " + str(xyz[1]))
    print("z = " + str(xyz[2]))
    return

# this is our main program with a menu for parts 1 and 2
flag=True
while (flag):
    menu_input = input("Enter 1 for Cramers \nEnter 2 for Gauss Jordan \nEnter anything else to exit the program! \n")
    match menu_input:
        case '1':
            cramersRule()
        case '2':
            gaussJordan()
        case _:
            flag = False
            print("Exiting the program!")
            continue
            
    print("\nOperation Complete!\n")
