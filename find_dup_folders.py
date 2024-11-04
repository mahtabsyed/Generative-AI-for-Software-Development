# Can you write a code in Python to search folders in current folder and all sub folders iteratively. In current and every subfolder if you find a folder name with name "x" and another folder name in same folder with name "x 2" then can you list the folder with name "x 2" - (x means any name)

import os

def find_matching_folders(root_dir):
    for dirpath, dirnames, _ in os.walk(root_dir):
        for dirname in dirnames:
            if dirname.endswith(" 2"):
                base_name = dirname[:-2].strip()
                if base_name in dirnames:
                    print(os.path.join(dirpath, dirname))

# Call the function with the current directory
find_matching_folders('.')