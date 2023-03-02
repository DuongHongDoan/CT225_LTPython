def towerOfHaNoi(n, cotA, cotB, cotC):
    if n==1:
        print("Chuyen dia 1 tu {0} sang {1}".format(cotA, cotB))
    else:
        towerOfHaNoi(n-1, cotA, cotC, cotB)
        print("Chuyen dia {0} tu {1} sang {2}".format(n, cotA, cotB))
        towerOfHaNoi(n-1, cotC, cotB, cotA)
n = int(input("Nhap vao so dia: "))
towerOfHaNoi(n, 'A', 'B', 'C')