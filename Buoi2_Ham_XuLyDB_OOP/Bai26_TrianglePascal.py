n = int(input("Nhap n dong cua tam giac Pascal: "))

def pascal(k, n):
    if k==0 or k==n:
        return 1
    else:
        return pascal(k-1,n-1) + pascal(k, n-1)
    
for i in range(n+1):
    for k in range(i+1):
        print(pascal(k, i), end=' ')
    print('\n')