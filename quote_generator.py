import requests
import random
print("Are you a teacher and want to give your students advice?") 
print("Are you a student and want to know the minds of the great philosphers?") 
print("Worry no more... you are in the right place!")
print("Enjoy your quotes!")
def get_random_quote():
    url = "https://api.quotable.io/random"
    response = requests.get(url)
    
    if response.status_code == 200:
        quote_data = response.json()
        content = quote_data["content"]
        author = quote_data["author"]
        return f'"{content}" - {author}'
    else:
        return "Failed to fetch a quote"
    

while True:
        input("Press Enter to get a random quote or type 'exit' to quit: ")
        
        random_quote = get_random_quote()
        print("\nYour random quote is:")
        print(random_quote)

        exit_command = input("\nType 'exit' to quit or press Enter to get another quote: ")
        if exit_command.lower() == 'exit':
            break


