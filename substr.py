s =input("enter a str:")
longest_palindrome = ""
for i in range(len(s)):
    for j in range(i, len(s)):
        substring = s[i:j+1]
        if substring == substring[::-1] and len(substring) > len(longest_palindrome):
            longest_palindrome = substring
print("longest palindrome in given str is:{}".format(longest_palindrome))
#test res:
#input:enter a str:heismalayalam
#output:longest palindrome in given str is:malayalam
