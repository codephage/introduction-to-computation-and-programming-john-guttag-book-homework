
##Finger exercise: Write a program that asks the user to enter an integer and 
##prints two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal 
##to the integer entered by the user. If no such pair of integers exists, it should 
##print a message to that effect.




num=int(raw_input('introduzca un numero entero'))
test=0
while test**1<num:
    test=test+1
    if test**1==num:
        print 'la raiz del numero es ',test,' y la potencia es 1'
    elif test**1!=num:
        while test**2<num:
            test=test+1
            if test**2==num:
                print 'la raiz del numero es ',test,' y la potencia es 2'
            elif test**2!=num:
                while test**3<num:
                    test=test+1
                    if test**3==num:
                        print 'la raiz del numero es ',test,' y la potencia es 3'
                    elif test**3!=num:
                        while test**4<num:
                            test=test+1
                        if test**4==num:
                            print 'la raiz del numero es ',test,' y la potencia es 4'
                        elif test**4!=num:
                            while test**5<num:
                                    test=test+1
                            if test**5==num:
                                print 'la raiz del numero es ',test,' y la potencia es 5'
                            elif test**5!=num:
                                while test**6<num:
                                    test=test+1
                                if test**6==num:
                                    print 'la raiz del numero es ',test,' y la potencia es 6'
                                else:
                                    print 'no se encuentra la raiz y la pontencia de ese numero dentro de los rangos permitidos'
                

