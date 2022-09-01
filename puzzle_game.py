import shutil
import os


shutil.unpack_archive("unzip_me_for_instructions.zip","unzipped_puzzle_game","zip")

import re
def check_num(file):
    return re.findall(r"(\d{3})-(\d{3})-(\d{4})",file)

mydict = {1:"One", 2: "Two", 3:"Three",4:"Four",5:"Five"}
n = 1

while True:
    file_path = f"F:\\Pyphon practice\\unzipped_puzzle_game\\extracted_content\\{mydict[n]}"
    for folder, sub_folder, files in os.walk(file_path):
        
        for file in files:
            f = open(file_path + "\\" + file,'r')
            for word in f:
                cell_num = check_num(word)
            f.close()
            if len(cell_num) > 0:
                cell_num_str = " "
                for i in cell_num:
                    print(cell_num_str.join(i))
                
    n+=1
    if n == 6:
        break   

        
    #phone_pattern = re.findall(r"(\d{3})-(\d{3})-(\d{4})")