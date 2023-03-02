def factory(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*factory(n-1)

n = int(input("Nhap vao mot so nguyen duong: "))
print("{0}! = {1}".format(n, factory(n)))