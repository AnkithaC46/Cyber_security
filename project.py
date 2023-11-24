import cv2
import string 
import os 

d={}
c={}   

for i in range(255): 
    d[chr(i)]=i
    c[i]=chr(i)
    

x=cv2.imread("flower.jpg")

i=x.shape[0]
j=x.shape[1]
text=input("enter message to hide:") 
key=input("enter Password:")  

 

k1=0
t1n=len(text) 
z=0
n=0 
m=0

l=len(text)

for i in range(l):
    x[n,m,z]=d[text[i]]^d[key[k1]]
    n=n+1
    m=m+1
    m=(m+1)%3

    k1=(k1+1)%len(key)

cv2.imwrite("encrypted-img.jpg",x)
os.startfile("encrypted-img.jpg")
print("data hiding completed successfully")

k1=0
t1n=len(text) 
z=0
n=0 
m=0 

ch=int(input("\nenter 1 to extract data from image:"))
if ch==1:
    key1=input("\nenter password:")
    decrypt=""
    if key == key1:
        for i in range(l):
            decrypt += c[x[n,m,z]^d[key[k1]]]
            n=n+1
            m=m+1
            m=(m+1)%3
            k1=(k1+1)%len(key)
        print("decrypted message:",decrypt)
    else:
           print("key not found")
