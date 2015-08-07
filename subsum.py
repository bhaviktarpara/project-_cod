subject=eval(raw_input ("Enter Subject list:"))
sub_list={}
for s in range(0,subject):
    key=raw_input("Enter Subject Name:-")
    mark=eval(raw_input("Enter Subject Masrk:-"))
    sub_list[key]= mark
    
print sub_list
for s1 in sub_list.items():
    print s1[0],"=",s1[1]
print sum(sub_list.values())
    
