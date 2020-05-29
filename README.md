# elliptic-curve-diffie-hellman
Implemented in python , Elliptic-curve Diffie–Hellman (ECDH) is a key agreement protocol that allows two parties, each having an elliptic-curve public–private key pair, to establish a shared secret over an insecure channel. This shared secret may be directly used as a key, or to derive another key.

**How it works**
1) Takes input , curve and a point on curve
2) Check if point lies on the curve
3) Inputs second point

**Functions**
1) Calculate sum of two points on ECDFH
2) Encrypt a message 
   Encrypts a input message, with input generator and private key
3) Generate public key
4) Decrypt a message
5) Print all points on the curve

**How  to run**
```
#Enter a : 0  // y^2 = x^3+ax+b
#Enter b : -4
#Enter p : 257 // mod 
#Enter x : 0  // x cordinate of point
#Enter y : 1  // y cordinate of point
#Check if point lies on the curve ?
#False
#Adding points: 
#Enter xq: 3  // x cordinate of second point
#Enter yq: 10  // y cordinate of second point
#Sum : 
#(6, 238)
#Enter message(x,y) point x : 112  // message (m,m2)
#Enter message(x,y) point y :26
#Enter na (private key): 101  // private key
#Enter generator (i,j) cordinate i : 2  // generator (g,g)
#Enter generator (i,J) cordinate j : 2
#Encrypted message: 
#((136, 128), (246, 174))
#Decrypted message: 
#(112, 26)
#All Points on the curve are :
```
