word = input("Enter a word: ").lower().replace(" ","")

reversed_word = word[::-1]

if word == reversed_word:
    print("is palindrome")
else:
    print("isn't palindrome")

