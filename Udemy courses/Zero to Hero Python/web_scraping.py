import requests
import bs4
import os
'''
Creates folder with images from a wikipidia page in this top level directory
'''

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        
image_folder = createFolder('./images/')

result = requests.get("https://en.wikipedia.org/wiki/Animal")

soup = bs4.BeautifulSoup(result.text,"lxml")
print(soup.select("title")[0].getText())
f = open("page.txt", "w+")
f.write(soup.select("title")[0].getText() + "\n")
f.write(soup.select("h1")[0].getText() + "\n" + "\n")
f.write(soup.select(".toc")[0].getText() + "\n" + "\n")


i = 1
for image in soup.select(".thumbimage"):

    image_link = requests.get(f"https:{image['src']}")
    f1 = open(f"{os.getcwd()}\\images\\image{str(i)}.jpg", "wb")
    f1.write(image_link.content)
    f1.close()
    i+=1


f.close()