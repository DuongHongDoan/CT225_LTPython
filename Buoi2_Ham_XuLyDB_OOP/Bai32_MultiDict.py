dict = {
    "Coc": 15,
    "Oi": 10,
    "Mia": 7,
    "Cam": 12
}
def multi(dict):
    multi=1
    for i in dict.values():
        multi *= i
    print("Tong cac gia tri trong dictionary la:", multi)

multi(dict)
