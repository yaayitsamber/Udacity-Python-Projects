import os
def rename_undascore():
    #1 Get File Names From Folder
    file_list = os.listdir("/Users/Amber/Desktop/prank")
    print (file_list)
    saved_path = os.getcwd()
    os.chdir("/Users/Amber/Desktop/prank")
    #2 Rename File Names
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)      
rename_undascore()
