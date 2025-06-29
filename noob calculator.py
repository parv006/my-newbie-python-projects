a=int(input("1st number"))
b=int(input("2nd number"))
c=input('''enter a mathematical operation to be employed between 1st and 2nd number
         option 1 : write mul for *
        option 2: write div for /
        option 3: write add for +
        option 4: write exp for **
        option 5: write bitN for ~x
        option 6: write flrdiv for //
        option 7: write rem for %
        option 8: write sub for - 
        option 9: write bitAnd for &
        option 10: write bitXor for ^
        option 11: write bitOr for | 
        your answer :   ''')
if c=="mul":
    print(a*b)
elif c=="div":
    print(a/b)
elif c=="add":
    print(a+b)  
elif c=="exp":
    print(a**b)        
elif c=="bitN":
    print(~a)
elif c=="flrdiv":
    print(a//b)  
elif c=="rem":
    print(a%b)
elif c=="sub":
    print(a-b) 
elif c=="bitAnd":
    print(a&b)  
elif c=="bitXor":
    print(a^b)  
elif c=="bitOr":
    print(a|b)                                   
else:
    print("please enter option carefully")    
    