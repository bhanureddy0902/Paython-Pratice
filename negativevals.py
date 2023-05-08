s=input("enter the values sepetrated by comma:").split(",")
s=list(map(int,s))
pval=[]
nval=[]
for val in s:
    if val<0:
        nval.append(val)
    else:
        pval.append(val)
print("+ ve vals are {}".format(pval))
print("- ve vals are {}".format(nval))