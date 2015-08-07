for a in [1,2]:
    print a

for l in 'python':
    print l

color=['red','yellow','black']
color.append(2)
color.sort()
print color
color=['red','yellow','black']
for c in color:
    print c

a=int(raw_input("Enter the value:-"))
for tmp in [a]:
    if tmp>=31 and tmp<=35:
        print"Sunny Day"
    elif tmp>=35 and tmp<=40:
        print "warm day"
    elif tmp>=40 and tmp<=50: 
        print "high"
    else:
        print "Err"

for tmp in range(1,10):
    if tmp>=31 and tmp<=35:
        print"Sunny Day"
    elif tmp>=35 and tmp<=40:
        print "warm day"
    elif tmp>=40 and tmp<=50: 
        print "high"
    else:
        print "Err"


    #print ab
