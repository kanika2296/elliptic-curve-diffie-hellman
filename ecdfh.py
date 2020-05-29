import numpy as np
class Point:
    def __init__(self,x_init,y_init):
        self.x = x_init
        self.y = y_init

# calculate modular inverse
def inv(n):
    for i in range(p):
        if (n * i) % p == 1:
            return i

# check if point lies on the curve
def isPoint(a1):
    y=a1.y*a1.y
    y=np.mod(y,p)
    x=(a1.x*a1.x*a1.x + a*a1.x + b)
    x=np.mod(x,p)
    if(x==y):
        return True
    else:
        return False

# print all point on the curve
def allPoints(p,a,b):
    for i in range(0, p):
        for j in range(0,p):
            a2=Point(i,j)
            if(isPoint(a2)==True):
                print((i,j))

# addition of point on the curve
# 1) when P+(-P)=O (addition to inverse)
# 2) when P+(-P) !=O (yp != yq)
# 3) when xp != xq
def addPoints(a1,a3):
    	if a1.x == a3.x and (a1.y != a3.y):
       		return(a1)
	if a1.x == a3.x:
		l = ((3 * a1.x * a1.x  + a ) * inv(2 * a1.y)) % p
		xr= (l*l - a1.x - a3.x) % p
		yr= (l*(a1.x-xr)-a1.y)%p
		a3=Point(xr,yr)    
		return(a3)
        else:
		l = ((a3.y - a1.y) * inv(a3.x - a1.x))% p
		xr= (l*l - a1.x - a3.x) % p
		yr= (l*(a1.x-xr)-a1.y)%p
		a3=Point(xr,yr)    
		return(a3)


def genPA(na,genr):
    g2=genr
    for k in range(1,na):
        g2=addPoints(g2,genr)
    return(g2)

def encrypt(Pm,na):
    g=int(raw_input("Enter generator (i,j) cordinate i : "))
    h=int(raw_input("Enter generator (i,J) cordinate j : "))
    genr=Point(g,h)
    pa=genPA(na,genr)
    k=41
    c1=genPA(k,genr)
    c2=genPA(k,pa)
    c2=addPoints(c2,Pm)
    return c1,c2

def decrypt(na,a3,a4):
    h1=genPA(na,a3)
    h1.y=-1*h1.y
    h2=addPoints(a4,h1)
    return h2

if __name__ == "__main__":
    # input d
    a=int(raw_input("Enter a : "))
    #input e
    b=int(raw_input("Enter b : "))
    p=int(raw_input("Enter p : "))
# input a point
    x=int(raw_input("Enter x : "))
    y=int(raw_input("Enter y : "))
    a1=Point(x,y)
# validate point on the curve
    print("Check if point lies on the curve ?")
    print(isPoint(a1))

    print("Adding points: ")
    x1=int(raw_input("Enter xq: "))
    y1=int(raw_input("Enter yq: "))
    a3=Point(x1,y1)
    print("Sum : ")
    a3=addPoints(a1,a3)
    print(a3.x,a3.y)

    x2=int(raw_input("Enter message(x,y) point x : "))
    y2=int(raw_input("Enter message(x,y) point y :"))
    Pm=Point(x2,y2)
    na=int(raw_input("Enter na (private key): "))
    a3,a4=encrypt(Pm,na)
    print("Encrypted message: ")
    print((a3.x,a3.y),(a4.x,a4.y))
    a6=decrypt(na,a3,a4)
    print("Decrypted message: ")
    print(a6.x,a6.y)
# prints all point on the curve
    print("All Points on the curve are :")
    print(allPoints(p,a,b))
