def num_square():
    while True:
        try:
            num = int(input("Enter a number to square: "))
            num_sqr = num ** 2
            return f"Number suared is {num_sqr}"  
        except ValueError:
            print("Not a number")
        
           


print(num_square())