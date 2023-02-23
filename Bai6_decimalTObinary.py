n = int(input("Nhap so nguyen duong: "))
binary = " "
tmp = n
while(tmp>0):
    bi = tmp % 2
    binary = str(bi) + binary
    tmp = tmp // 2
print(n, "chuyen thanh nhi phan la:", binary)