n = int(input("Nhap so bit: "))
lis = [0]*n

def out(lis):
    newStr = ''
    for i in lis:
        newStr += str(i)
    return newStr

def generation(n):
    while True: #dieu kien luon dung -> vong lap luon chay
        print(out(lis)) # thi in ra chuoi dau tien la '000'(duoc noi lai tu 1 danh sach dau vao) 
        i = n-1 # gan cho i la vi tri bit cuoi cua day nhi phan. vd: 110 thi i=3-1=2 -> i la bit '0'
        while i>=0 and lis[i]==1: # khi i chua den bit dau va tai vi tri i trong danh sach la bit '1'
            lis[i]=0 #gan tai vi tri i trong danh sach la bit '0'
            i -= 1
        if i>=0: # nguoc lai, neu tai vi tri i la bit '0' va van chua den bit dau
            lis[i]=1 # gan tai vi tri i la bit '1'
        else: #neu vuot vi tri dau -> thoat vong lap
            break
generation(n)