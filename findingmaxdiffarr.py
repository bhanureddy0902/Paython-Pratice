def minimize_max_difference(arr, n, k):
    arr.sort()
    ans = arr[-1] - arr[0]
    for i in range(n-1):
        min_height = min(arr[0]+k, arr[i+1]-k)
        max_height = max(arr[-1]-k, arr[i]+k)
        ans = min(ans, max_height - min_height)
    return ans
arr = [1, 5, 8, 10]
n = len(arr)
k = 2
result = minimize_max_difference(arr, n, k)
print("Minimum maximum difference is", result)
#test results:
#Minimum maximum difference is 5
