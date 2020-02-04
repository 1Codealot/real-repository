import random
lastMove=7

# MOVES
U=["U","U2","U'"]
R=["R","R2","R'"]
F=["F","F2","F'"]
B=["B","B2","B'"]
L=["L","L2","L'"]
D=["D","D2","D'"]


for i in range(0,5):
    move=random.randint(1,6)
    lastMove=move
    moveType=random.randint(0,2)
    if move == 1:
        print(U[moveType])
    elif move == 2:
        print(R[moveType])
    elif move == 3:
        print(F[moveType])
    elif move == 4:
        print(B[moveType])
    elif move == 5:
        print(L[moveType])
    elif move == 6:
        print(D[moveType])
