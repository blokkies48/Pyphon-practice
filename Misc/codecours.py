word = str(input('Enter word ')).lower()
if word == word[::-1]:
    print('the word the user input is a palindrome')
else:
    print('the word the user input is NOT a palindrome')




word = int(input('Input a whole number: '))

if word%2 == 0:
    print('Fizz')
else:
    print('Buzz')
