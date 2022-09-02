import shutil
import os


shutil.unpack_archive("unzip_me_for_instructions.zip","unzipped_puzzle_game","zip")

import re
def check_num(str1):
    return re.search(r"(\d{3})-(\d{3})-(\d{4})",str1)

mydict = {1:"One", 2: "Two", 3:"Three",4:"Four",5:"Five"}
n = 1

while True:
    file_path = f"{os.getcwd()}\\unzipped_puzzle_game\\extracted_content\\{mydict[n]}"
    for folder, sub_folder, files in os.walk(file_path):
        
        for file in files:
            #f = open(file_path + "\\" + file,'r')
            with open(file_path + "\\" + file) as f:
                for word in f:
                    cell_num = check_num(word)
                if cell_num != None:
                    print(cell_num.group())            
    n+=1
    if n == 6:
        break   

        
    #phone_pattern = re.findall(r"(\d{3})-(\d{3})-(\d{4})")