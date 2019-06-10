import os
import shutil
import getpass

def copy_all_directories(source_dir, dest_dir):
    for item in os.listdir(source_dir):
        file_path = os.path.join(source_dir, item)

        if os.path.isfile(file_path):
            shutil.copy(file_path, dest_dir)
        elif os.path.isdir(file_path):
            new_dest = os.path.join(dest_dir, item)
            os.mkdir(new_dest)
            copy_all_directories(file_path,new_dest)


# source_dir = r"C:\Users\\" + getpass.getuser() + r"\AppData\Local\Google\Chrome\User Data"
source_dir = r"C:\Users\\" + getpass.getuser() + r"\AppData\Local\Google\Chrome\User Data\Default\Application Cache"
dest_dir = r"C:\Users\\" + getpass.getuser() + r"\Automation"
if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)
copy_all_directories(source_dir,dest_dir)
print("Creating Cache Directory Successfull")