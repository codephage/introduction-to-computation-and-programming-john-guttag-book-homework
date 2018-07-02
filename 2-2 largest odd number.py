# -*- coding: cp1252 -*-
#Write a program that examines three variables—x, y, and z—
#and prints the largest odd number among them. If none of them are odd, it 
#should print a message to that effect.
x=8
y=4
z=2
    
if x%2!=0:
    flagX=True
else:
    flagX=False
if y%2!=0:
    flagY=True
else:
    flagY=False
if z%2!=0:
    flagZ=True
else:
    flagZ=False

if flagX==True and flagY==True and flagZ==True:
    if x>y and x>z:
        print'x es el impar mayor'
    elif y>x and y>z:
        print'y es el impar mayor'
    else:
        print'z es el impar mayor'
elif flagX==True and flagY==True and flagZ==False:
    if x>y:
        print'x es el impar mayor'
    else:
        print' Y es el impar mayor'
elif  flagX==True and flagY==False and flagZ==True:
    if x>z:
        print'x es el impar mayor'
    else:
        print' Z es el impar mayor'
elif  flagX==False and flagY==True and flagZ==True:
    if y>z:
        print'Y es el impar mayor'
    else:
        print' Z es el impar mayor'
elif  flagX==True and flagY==False and flagZ==False:
    print'X es el unico numero impar'
elif  flagX==False and flagY==True and flagZ==False:
    print'Y es el unico numero impar'
elif  flagX==False and flagY==False and flagZ==True:
    print'Z es el unico numero impar'
elif  flagX==False and flagY==False and flagZ==False:
    print'Ningun numero es impar'
else:
    print' no se que paso'


    
    
    
    
