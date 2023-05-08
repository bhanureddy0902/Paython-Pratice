arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]
union=sorted(set(arr1)|set(arr2))
intersection=sorted(set(arr1)&set(arr2))
print("union elements are={}".format(union))
print("intersection elements are={}".format(intersection))
