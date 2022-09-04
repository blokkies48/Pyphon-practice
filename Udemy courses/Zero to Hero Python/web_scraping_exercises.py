import bs4, requests, lxml

'''http://quotes.toscrape.com/'''

request = requests.get("http://quotes.toscrape.com/")

soup = bs4.BeautifulSoup(request.text,"lxml")

authors = set()
i = 1
while True:
    request = requests.get(f"http://quotes.toscrape.com/page/{i}")
    soup = bs4.BeautifulSoup(request.text,"lxml")

    try:
        for author in soup.select(".author"):
            authors.add(author.getText())
            print(author.getText())
        soup.select(".author")[0].getText
    except:
        break    
    i+=1

print(authors)


hello = print("hello")


'''quote_list = []
for quote in soup.select(".text"):
    quote_list.append(quote.getText()) 
print(quote_list)

for tag in soup.select(".tag-item"):
    print(tag.getText())'''

