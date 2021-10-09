def determinant(n):
    if len(n) == 1:
        return n[0][0]
    res = 0
    for i in range(len(n)):
        res += (1 if i % 2 == 0 else -1) * n[0][i] * determinant([j[:i] + j[(i+1):] for j in n[1:]])
    return res

# buat nyari kofaktornya pake ini
# for j in range(len(m)):
#     for i in m[1:]:
#         print(i[:j] + i[(j+1):])

def inverse(a):
    n = len(a) #defining the range through which loops will run
    #constructing the n X 2n augmented matrix
    P = [[0.0 for i in range(len(a))] for j in range(len(a))]
    for i in range(3):
        for j in range(3):
            P[j][j] = 1.0
    for i in range(len(a)):
        a[i].extend(P[i])
    #main loop for gaussian elimination begins here
    for k in range(n):
        if abs(a[k][k]) < 1.0e-12: #jika 0 tuker
            for i in range(k+1, n):
                if abs(a[i][k]) > abs(a[k][k]):
                    for j in range(k, 2*n):
                        a[k][j], a[i][j] = a[i][j], a[k][j] #swapping of rows
                    break
        pivot = a[k][k] #defining the pivot
        print(a)
        if pivot == 0: #checking if matrix is invertible
            print("This matrix is not invertible.")
            return
        else:
            for j in range(k, 2*n): #index of columns of the pivot row
                a[k][j] /= pivot
            for i in range(n): #index the subtracted rows
                if i == k or a[i][k] == 0: 
                    continue
                factor = a[i][k]
                for j in range(k, 2*n): #index the columns for subtraction
                    a[i][j] -= factor * a[k][j] #pivotbaris = a[k][j]
    for i in range(len(a)): #displaying the matrix
        for j in range(n, len(a[0])):
            print(round(a[i][j], 5), end = " ")
        print()

matrix = []

size = int(input())
for i in range(size):
    matrix.append(list(map(int, input().split())))

if determinant(matrix) == 0:
    print(f'Matrix tidak punya determinant.')
else:
    inverse(matrix)
