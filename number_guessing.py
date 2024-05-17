import random


while True:

    flag = True
    while flag:
        num = input('Type a number for an upper bound:  ')  #message received by the user

        if num.isdigit():   #checks if the input is a digit
            print("Let's play!")
            num = int(num)
            flag = False

        else:
            print('invalid input!  Try again')  


#the logic of the program starts from here
    secret = random.randint(1, num) #thw secret function randomly chooses a number between 1 and the number given by the user.

    guess = None
    count = 1
#execution
    while guess != secret: 
        guess = input('Please type a number between 1 and ' + str(num) + ": ")

        if guess.isdigit():
            guess = int(guess)

        if guess == secret:
            print('Yaayy! You got it') 

        elif guess < 1 or guess > num:
            print('Please enter a number between 1 and', num)    

        elif guess < secret:
            print('Try a higher number!')
            count += 1
        else:
            print('Try a lower number!')
            count += 1  
    else:
          
     print('It took you' , count, 'guesses')  
             

