print('Welcome to the palindrome checker. Your reversed words in a few!')
#palindrome refers to a word that can be read the same forward or backward.

while True:
    def is_palindrome(text):
        length = len(text)

        for i in range(0, length // 2):
            if(text[i] != text[length-i-1]):
                return False
            
        return True

    user_input = input("Enter a word: ")
    if is_palindrome(user_input): #checks if the user input is palindrome
        print(f"{user_input} is a palindrome.") #returns this message if the above is true

    else:
        print(f"{user_input} is not a palindrome.") #returns this message if the above is not true