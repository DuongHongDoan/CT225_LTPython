f = open("D:\python.txt", "r")
lis = f.read().replace('\n', ' ').split(' ')
cnt = {}
for i in lis:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1
print(cnt)
f.close()