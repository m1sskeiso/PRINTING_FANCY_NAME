import colorama
import random

# Initialize colorama
colorama.init()

# Function to print text in rainbow colors
def print_rainbow(text):
    colors = [colorama.Fore.RED, colorama.Fore.YELLOW, colorama.Fore.GREEN, colorama.Fore.CYAN, colorama.Fore.BLUE, colorama.Fore.MAGENTA]
    rainbow_text = ''
    for char in text:
        rainbow_text += random.choice(colors) + char
    print(rainbow_text + colorama.Style.RESET_ALL)
    
# Main program
if __name__ == "__main__":
    
    # Prompt user to input their name
    name = input("Enter your name: ")
    
    # Prompt user to input their dream job
    dream_job = input("Enter your dream job: ")
    
    # Print name in rainbow colors
    print("\nYour name:", name)
    
    # Print dream job in rainbow colors
    print("\nYour dream job: ", dream_job)
