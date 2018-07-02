##Finger exercise:  Write a program that asks the user to input 10 integers, and 
##then prints the largest odd number that was entered. If no odd number was 
##entered, it should print a message to that effect.




x=[]
y=[]
for i in range(10):
    i=i+1
    num=int(raw_input('introduzca el '+str(i)+'avo numero entero  '))
    if num%2!=0:
         x.append([num])
    else:
        y.append([num])


if not x:
    print'no hay ningun numero impar'
else:
    for j in range(len(x)):
        if (x[j]>x[j-1]):
                mayor_impar=x[j]
    print 'el mayor numero impar introducido es ', mayor_impar





    



            
