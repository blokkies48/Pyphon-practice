
import timeit

stmt = '''
func1(100)
'''

setup = '''
def func1(n):
    return [str(num) for num in range(n)]
'''

stmt2 = '''
func2(100)
'''

setup2 = '''
def func2(n):
    return list(map(str,range(n)))
'''

t = 10
print("func1")
print(timeit.timeit(stmt,setup,number=t))
print("func2")
print(timeit.timeit(stmt2,setup2,number=t))

map1 = set(map(str,range(10)))
print(map1)

f = open("fileone.txt", "w+")
f.write("One file")
f.close()

f = open("filetwo.txt", "w+")
f.write("Two file")
f.close()

import zipfile

comp_file = zipfile.ZipFile("comp_file.zip", "w")


comp_file.write("fileone.txt", compress_type=zipfile.ZIP_DEFLATED)
comp_file.write("filetwo.txt", compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

zip_obj = zipfile.ZipFile("comp_file.zip", "r")
zip_obj.extractall("extracted_content")

import shutil
import os

print(os.getcwd())

dir_to_zip = "F:\\Pyphon practice\\extracted_content"

output_filename = "example"

shutil.make_archive(output_filename,"zip",dir_to_zip)

shutil.unpack_archive("example.zip","final_unzip","zip")