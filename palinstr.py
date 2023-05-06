a=input("enter the word need to be checked:")
if a==a[::-1]:
    print("{} is a palindrome".format(a))
else:
    print("{} is not a palindrome".format(a))

#test results:
#input:enter the word need to be checked:mom
#output:mom is a palindrome


