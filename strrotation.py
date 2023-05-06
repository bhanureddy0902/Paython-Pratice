s1=input("enter str1:")
s2=input("enter second str2:")
if len(s1)==len(s2):
    print(" ")
else:
    print(" ")
temp=s1+s1
if temp.count(s2)>0:
    print("Both the strings are rotational")
else:
    print("Both the strings are not rotational")