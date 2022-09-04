#def reverse_string(str):  
#    str1 = ""   # Declaring empty string to store the reversed string  
#    for i in str:  
#        str1 = i + str1  
#    return str1    # It will return the reverse string to the caller #function  
#     
#str2 = "String"   # Given String       
#print("The original string is: ",str2)  
#print("The reverse string is " + reverse_string(str2)) # Function call 
#
#print("".join(reversed("Hello")))

#
#def reverse_word(str):
#    str2 = ""
#    for i in str:
#        str2 = i + str2
#    return str2
#
#word = "piel"
#
#print(reverse_word(word))
#
#if word == reverse_word(word):
#    print("yes")
#else:
#    print("no")
#

#with open('new_file.txt', 'w+') as f:
#    f.write("Added words")

#s = 'hello'
#n = s[::-1]
#print(n)
#
#mylist= [0, 0]
#mylist.append(0)
#print(mylist)
#
#list3 = [1,2,[3,4,'hello']]
#list3[2][2] = 'goodbye'
#print(list3)
#
#list4 = [5,3,4,6,1]
#list4.sort()
#print(list4)
#
#d = {'simple_key':'hello'}
#print(d['simple_key'])
#
#d = {'k1':{'k2':'hello'}}
#print(d['k1']['k2'])
#
#d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
#print(d['k1'][0]['nest_key'][1][0])
#
#d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
#print(d['k1'][2]['k2'][1]['tough'][2][0])
#
#list5 = [1,2,2,33,4,4,11,22,3,3,2]
#print(set(list5))
#
#print(4**0.5 != 2)

#st = 'Sam Print only the words that start with s in this sentence'
#new_list = st.split()
#list2 = []
#
#for word in new_list: 
#    if 's' in word[0].lower():
#        print(word)
#        list2.append(word)
#
#print(list2) 
#
#w = [x for x in new_list if x[0] == 's' ]
#
#print(w)
#
#num_list = []
#
#for num in range(0,11):
#    if num%2 == 0:
#        print(num)
#        num_list.append(num)
#
#print(num_list)
#
#num_list2 = [x for x in range(0,11) if x%2 == 0]
#
#print(num_list2)
#
#num_list3 = [num for num in range(0,51) if num%3 == 0 ]
#
#print(num_list3)
#
#st2 = 'Print every word in this sentence that has an even number of #letters'
#split_st2 = st2.split()
#
#e = 0
#
#for word in split_st2:
#    if len(word)%2 == 0:
#        print("even!")
#        e += 1
#
#print(e)
#
#for num in range(0,101):
#    if num%3 == 0 and num%5 == 0:
#        print("FizzBuzz")
#    elif num%3 == 0:
#        print("Fizz")
#    elif num%5 == 0:
#        print("Buzz")
#    else:
#        print(num)
#
#st3 = 'Create a list of the first letters of every word in this string'
#
#list5 = [letter[0] for letter in st3.split()]
#
#print(list5)
#
#def check_even_list(num_list = []):
#    list5 = []
#    for number in num_list:
#        if number%2 == 0:
#            list5.append(number)
#    return list5
#
#   # for number in num_list:
#   #     if number%2 == 0:
#   #         return list5
#   # return False
#
#        
#print(check_even_list([1,5,7,6,7,8,9]))

#work_hours = [('Abby', 200),('Jerry', 400),('Mike',3000)]
#
#
#def employee_year(tuple1):
#    hour_list = []
#    for name,hours in tuple1:
#        hour_list.append(hours)
#    most_hours = max(hour_list)
#    for name,hours in tuple1:
#        if hours == most_hours:
#            return name
#
#print(employee_year(work_hours))
#
#def employee_check(work_hours):
#    current_max = 0
#    employee = ""
#
#    for name,hour in work_hours:
#        if hour > current_max:
#            current_max = hour
#            employee = name
#        else:
#            pass
#    return(employee,current_max)
#
#print(employee_check(work_hours))

#from random import shuffle
#
#
#def shuffle_list(mylist):
#    shuffle(mylist)
#    return mylist
#
#def playe_guess():
#    guess = ''
#    while guess not in ['1','2','3']:
#        guess = input("Enter a number between 1 and 3: ")
#    return int(guess) - 1
#
#def number_game(guess,ball_at):
#
#    if  'ball' == ball_at[guess] :
#        return 'You Win!!' 
#    return "You Lose!"
#
#three_cups = ['','ball',''] 
#
#print(number_game(playe_guess(),shuffle_list(three_cups)))



#def myfunc(str1):
#    str2 = ''
#    i = 1
#    for letter in str1:
#        if i % 2 == 0: 
#            letter = letter.upper() 
#        if i % 2 != 0:
#            letter = letter.lower()
#        str2 = str2 + ''.join(letter)
#        i += 1
#    return str2
#
#print(myfunc("Menique is so Mooi Mooi"))

#-----------------------------------------------------------


from itertools import count


def lesser_of_two_evens(a,b):
    if a%2 == 0 and b % 2 == 0:
        return min(a,b)
    else:
        return max(a,b)


print(lesser_of_two_evens(2,5))

###############
print("-----------------------")

def animal_crackers(text):
    first_word = ' '
    for word in text.lower().split():
        if first_word[0] == word[0]:
            return True
        first_word = word
    return False

def animal_crackers2(text):
    word_list = text.split()
    return word_list[0][0] == word_list[1][0]

print(animal_crackers2('Levelheaded Llama'))
print(animal_crackers2('Crazy Kangaroo'))


##################
print("-----------------------")

def makes_twenty(n1,n2):
    return n1 == 20 or n2 == 20 or n1 + n2 == 20



print(makes_twenty(20,10))
print(makes_twenty(2,3))
print(makes_twenty(12,8))

#####################
print("--------Level 1---------")

def old_macdonald(name):
    name_cap = ''
    i = 0
    for letter in name:
        if i == 0:
            letter = letter.upper()
        if i == 3:
            letter = letter.upper()
        name_cap = name_cap + ''.join(letter)
        i += 1
    return name_cap

def old_macdonald2(name):
    first_letter = name[0]
    inbetween = name[1:3]
    fourth_letter = name[3]
    rest = name[4:]

    return first_letter.upper() + inbetween + fourth_letter.upper() + rest    

print(old_macdonald2('macdonald'))

#####################
print("--------Level 1---------")

def master_yoda(text):
    new_list = text.split()[::-1]
    return ' '.join(new_list)

print(master_yoda("I am home"))
print(master_yoda('We are ready'))

#####################
print("--------Level 1---------")

def almost_there(n):
    if n in range(90, 111):
        return True
    elif n in range(190, 211):
        return True
    else:
        return False

def almost_there2(n):
    return (abs(100-n)<=10) or(abs(200-n) <= 10)
    

print(almost_there2(104))
print(almost_there2(150))
print(almost_there2(209))

#####################
print("--------Level 2---------")

def has_33(nums):
    num_string = ' '
    while type(nums) != int and float:
        for num in nums:
            num_string = num_string + num_string.join(str(num))

        if '33' in num_string:
            return True
        return False
    return "Can't process int or float values"

def has_332(nums):
    for i in range(0,len(nums)-1):
        if nums[i] ==3 and nums[i+1] == 3:
            return True
    return False
    


print(has_332([1, 3, 3]))
print(has_332([1, 3, 1, 3]))
print(has_332([3, 1, 3]))
print(has_33(33))

#####################
print("--------Level 2---------")

def paper_doll(text):
    new_string = ''
    for letter in text:
        new_string += letter*3
    return new_string

print(paper_doll('hi'))
print(paper_doll('Hello'))
print(paper_doll('Mississippi')
)

#####################
print("--------Level 2---------")

#def blackjack(args):
#    numbers_card = []
#    for arg in args:
#        numbers_card.append(arg)
#
#    if sum(numbers_card) <= 21:
#        return sum(numbers_card)
#    elif sum(numbers_card)> 21 and 11 in numbers_card:
#        if sum(numbers_card) - 10 > 21:
#            return sum(numbers_card)
#        return sum(numbers_card) -10
#    elif sum(numbers_card)> 21:
#        return sum(numbers_card)
#
#
#def player_hand():
#    card_amount = 0
#    hand_total = []
#    player_input = input("Type 'h' to hit or anything else to stop ")
#
#    while player_input.upper() == 'H':
#        card_amount = randint(1,11)
#        hand_total.append(card_amount)
#        print(hand_total)
#        player_input = input("Type hit to hit or anything else to stop #")
#
#    return hand_total
#
#def dealer(player_hand):
#    dealer_hand = 0
#    while dealer_hand < 17:
#        dealer_hand += randint(1,10)
#    if dealer_hand > 21 and player_hand < 21:
#        return f"----Dealer bust!! Dealer hand = {dealer_hand}, Yours =#{player_hand}"
#    elif player_hand > 21 and dealer_hand < 21:
#        return f"----Bust!! Dealer hand = {dealer_hand}, Yours =#{player_hand}"
#    elif player_hand > 21 and dealer_hand > 21:
#        return f"----Bust Both!! Dealer hand = {dealer_hand}, Yours =#{player_hand}"
#    elif dealer_hand == player_hand:
#        return f"----Draw!! Dealer hand = {dealer_hand}, Yours =#{player_hand}"
#    elif dealer_hand > player_hand:
#        return f"----Dealer wins!! Dealer hand = {dealer_hand}, Yours =#{player_hand}"
#    elif dealer_hand < player_hand:
#        return f"----You win!! Dealer hand = {dealer_hand}, Yours =#{player_hand}"
#    elif dealer_hand == 21:
#        return f"----Dealer wins!! Dealer hand = {dealer_hand}, Yours =#{player_hand}"
#    elif player_hand == 21:
#        return f"----You win!! Dealer hand = {dealer_hand}, Yours =#{player_hand}"
#
#play_game = input("Do you want to play y/n? ")
#
#while play_game.upper() == 'Y':
#    
#        print(dealer(blackjack(player_hand())))
#        play_game = input("Do you want to play y/n? ")

#####################
print("--------Level 2---------")

def summer_69(arr):
    sum_of_num = 0
    for num in arr:
        if num == 6:
            pass
        sum_of_num += num


def count_primes(num):
    list_range = list(range(1,num + 1))
    prime_numbers = num

    for number in list_range:
        if number == 1:
            prime_numbers = prime_numbers - 1
        elif number % 2 == 0 and number != 2:
            prime_numbers = prime_numbers - 1
        elif number % 3 == 0 and number !=3:
            prime_numbers = prime_numbers - 1
        elif number % 5 == 0 and number != 5:
            prime_numbers = prime_numbers - 1
        elif number % 7 == 0 and number != 7:
            prime_numbers = prime_numbers - 1
                
    return prime_numbers

def count_primes2(num):
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        for y in range(3,x,2):  # test all odd factors up to x-1
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

print(97 % 5)
print(count_primes2(100))

def count_primes3(num):
    
    primes= [2]
    x = 3

    if num <2:
        return 0

    while x <= num:
        for y in range(3,x,2):
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x+=2
    print(primes)

    return len(primes)


    
print(count_primes3(200))

#####################
print("--------Level 2---------")


#def spy_game(nums):
#    str_007 = ''
#    for num in nums:
#        if num == 0 or num == 7:
#            str_007 += ''.join(str(num))
#    return str_007 == '007'







import timeit

start = timeit.default_timer()
def spy_game(nums):
    str_007 = ''
    for num in nums:
        if num == 0 or num == 7:
            str_007 += ''.join(str(num))
    return str_007 == '007'

# All the program statements

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,7,2,0,4,5,0]))



stop = timeit.default_timer()
execution_time = stop - start

print("Program Executed in "+str(execution_time)) # It returns time in seconds


start = timeit.default_timer()

# All the program statements

def spy_game2(nums):
    code = [0,0,7,'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)

    return len(code) == 1

print(spy_game2([1,2,4,0,0,7,5]))
print(spy_game2([1,7,2,0,4,5,0]))

stop = timeit.default_timer()
execution_time = stop - start

print("Program Executed in "+str(execution_time)) # It returns time in seconds