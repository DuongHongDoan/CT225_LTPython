n = int(input("Nhap vao 1 so nguyen duong: "))
while(n<=0):
    print("Nhap vao 1 so nguyen duong, lon hon 0!!!")
    n = int(input("Nhap vao 1 so nguyen duong: "))
    if n>0:
        continue
sum=sum1=sum2=sum3=sum4 = 0
#   S  = 1 + 2 + ... + n
for i in range(n+1):
    sum += i
print("Tong cac so tu 1 den n la:", sum)

#S1 = 1 + 3 + ... + (2n - 1)
for i in range(1,n+1,2):
    sum1 += i
print("Tong cac so le tu 1 den n la:", sum1)

#S2 = 2 + 4 + ... + 2n
for i in range(2, n+1, 2):
    sum2 += i
print("Tong cac so chan tu 2 den n la:", sum2)

#S3 = 1 + 2^2 + ... + n^2
for i in range(1, n+1):
    sum3 += i**2
print("Tong binh phuong la:", sum3)

#S4 = 1 + 1/2 + ... + 1/2^n
for i in range(0, n+1):
    sum4 += 1/(2**i)
print("Tong phan so 1/2^n:", sum4)