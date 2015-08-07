def sum(a,b):
    c=a+b
    return c 
def sub(a,b):
    c=a-b
    return c
def mul(a,b):
    c=a*b
    return c

a=eval(raw_input ("Enter a"))
b=eval(raw_input ("Enter b"))

if a>15:
 print "fun:",sum(a,b)
elif a>1:
 print "fun:",sub(a,b)
 
else: 
 print "fun:",mul(a,b)
    
   
