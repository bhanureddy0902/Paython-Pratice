def find_duplicates(s):
    seen = set()
    duplicates = set()
    for char in s:
        if char in seen:
            duplicates.add(char)
        else:
            seen.add(char)
    return list(duplicates)
s = "hello world"
duplicates = find_duplicates(s)
print(duplicates)
