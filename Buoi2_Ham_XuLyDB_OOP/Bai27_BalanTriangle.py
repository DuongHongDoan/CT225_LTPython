n = int(input("Nhap vao do dai canh la so nguyen duong: "))

for i in range(1, n+1):
    edge = '*'*i
    print(edge)
for j in range(n-1, 0, -1):
    Reedge = '*'*j
    print(Reedge)