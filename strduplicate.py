a=input("enter the word to check the duplicates in it:")
s1d=set()
s2o=set()
for v in a:
    if v in s1d:
        s2o.add(v)
    else:
        s1d.add(v)
print("dup char are {}".format(s2o))
#test res:
#input:enter the word to check the duplicates in it:mom
#output:dup char are {'m'}