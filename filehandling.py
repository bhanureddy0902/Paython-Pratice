import os
path = "C:\\Test"
if os.path.exists(path):
    for foldername, subfolders, filenames in os.walk(path):
        if len(filenames)>0:
            print(foldername,len(filenames))
else:
    print("Path not found.")




