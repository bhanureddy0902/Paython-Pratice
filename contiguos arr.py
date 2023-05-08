arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
num1=num2=arr[0]
for val in arr[1:]:
    num1=max(val,num1+val)
    num2=max(num2,num1)
print("largest sum of contiguos sub array is={}".format(num2))
