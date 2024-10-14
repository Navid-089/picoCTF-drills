def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

x = [268,413,438,313,426,337,272,188,392,338,77,332,139,113,92,239,247,120,419,72,295,190,131]
y= x 
s = " " 
for i in range(len(x)):
    y[i] = modinv(x[i] % 41, 41) 
    if (y[i] <=26) :
        s += chr(y[i]+96)
    elif (y[i] <= 36):
        s+= chr(ord('0') + y[i] - 27)
    else: 
        s+='_'
print(s)

   
        


