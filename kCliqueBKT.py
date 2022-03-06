import sys

lines=[]
with open(sys.argv[1]) as file:
    lines=file.readlines()

k = int(lines[0])
n = int(lines[1])

v = []
for i in range(n + 1):
    v.append(0)
matrice = []
for i in range(n + 1):
    aux = []
    for j in range(n + 1):
        aux.append(0)
    matrice.append(aux)
found = False


def verifyClique():   #i check if there is a clique
    for i in range(n + 1):
        if v[i] == 1:
            for j in range(i + 1, n + 1):
                if v[j] == 1:
                    if matrice[i][j] == 0:
                        return False
    return True


def solver(pas, nr):  #i start looking for edges
    global found
    if pas == n + 1:
        return 
    if nr == k:   # if the number of edges is equal to k => it is true and i stop
        if verifyClique():
            print(True)
            found = True
        return

    if not found:
        v[pas] = 1
        solver(pas + 1, nr + 1) # i use the backtracking method
        v[pas] = 0
        solver(pas + 1, nr)

#here I practically make the adjacency matrix
def kClique():
    m = int(lines[2])
    for i in range(m):
        a = int(lines[3+i].split(" ")[0])
        b = int(lines[3+i].split(" ")[1])
        matrice[a][b] = 1
        matrice[b][a] = 1
    solver(1,0)
    global found
    if found == False:
        print("False")
kClique()

