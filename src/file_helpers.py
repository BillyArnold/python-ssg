import os
import shutil

def copy_directory(current_path, target_path):
    #check public path exists
    if os.path.exists(current_path) == False:
        raise Exception(f'File path {current_path} not found')
    
    dir_listing = os.listdir(current_path)
    print(dir_listing)

    for item in dir_listing:
        path = os.path.join(current_path, item)
        file_target_path = os.path.join(target_path, item)
        if os.path.isfile(path):
            shutil.copyfile(path, file_target_path)
            continue

        #if is directory, create corresponding
        os.mkdir(file_target_path)
        copy_directory(path, file_target_path)