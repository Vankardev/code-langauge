a = input("enter your massage: ")
b = list(a)
for i in range(len(b)):
    if b[i] == 'a':
        b[i] ='y'
    
    elif b[i] == 'i':
        b[i] = '*'
    elif b[i] == 'r':
        b[i] = '%'
    elif b[i] == 'l':
        b[i] = '@'
    elif b[i] == 'n':
        b[i] = '!!!'
    elif b[i] == 'z':
        b[i] = '$'
    elif b[i] == 'h':
        b[i] = '88'
    elif b[i] == 'w':
        b[i] = 'φ'
    elif b[i] == 's':
        b[i] = 'Φ'
    elif b[i] == 'x':
        b[i] = 'yxz'
    elif b[i] == 'g':
        b[i] = 'hfi'
    elif b[i] == 'o':
        b[i] = '0'
    elif b[i] == 'e':
        b[i] = 'pp'
    

b.reverse()
# print(b)
c=''.join(b)
print(c)