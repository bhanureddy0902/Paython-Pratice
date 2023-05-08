def find_duplicates(lst):
    duplicates = []
    for i in range(len(lst)):
        if lst[i] in lst[i+1:] and lst[i] not in duplicates:
            duplicates.append(lst[i])
    print("duplicate elemets are={}".format(duplicates))

find_duplicates(lst=[1,2,1,44,5,3,4,55,5,44])
#test results;
#duplicate elemets are=[1, 44, 5]