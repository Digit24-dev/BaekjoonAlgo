
a, b = input().split()

ca = str()
cb = str()

for i in range(len(a)-1, -1, -1):
    ca += a[i]

for i in range(len(b)-1, -1, -1):
    cb += b[i]

if int(ca) > int(cb):
    print(ca)
else:
    print(cb)