dict = {
    "Coc": 15,
    "Oi": 10,
    "Mia": 7,
    "Cam": 12
}
def sum(dict):
    sum=0
    for i in dict.values():
        sum += i
    print("Tong cac gia tri trong dictionary la:", sum)

sum(dict)
