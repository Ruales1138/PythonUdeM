import random as rd

def matrizCC():
    MCC=[]
    for i in range(5):
        MCC.append([0]*10)
    for i in range(5):
        for j in range(10):
            MCC[i][j] = rd.randint(0, 20)
    return MCC

MCC = matrizCC()
for i in MCC:
    print(i)