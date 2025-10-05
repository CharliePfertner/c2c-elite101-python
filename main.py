
"""
    Welcome to Elite 101 this program is a starter for your chatbot project.
    The starter prompts the user to enter their name and then greets them with a personalized message.

    Functions:
        get_user_name(): Prompts the user to enter their name and returns it.
        greet_user(name): Prints a greeting message using the provided name.
        main(): Main function that orchestrates the user input and greeting process.

    Execution:
        When the script is run directly (not imported as a module), it will execute the main() function.



def get_user_name():
    return input("Please enter your name: ")

def greet_user(name):
    print(f"Hello, {name}, how are you?")

def main():
    user_name = get_user_name()
    greet_user(user_name)

if __name__ == "__main__":
    main()

"""
from datetime import date, datetime
print("Welcome to the tech support chatbot!")
name = input("Please enter your name: ")
age = int(input("Hello "+ name + ", how old are you? "))
current_time = datetime.now()
your_time = current_time.hour -5

def time():
    if your_time == 23 or your_time<=3:
        print(f"\nWow {name}, I guess you're a night owl!")
    elif your_time >=4 and your_time <=7:
        print(f"\nWow {name}, why are you doing this so early in the morning?")
    elif your_time >=8 and your_time <=11:
        print(f"\nGood morning, {name}!")
    elif your_time >=12 and your_time <= 16:
        print(f"\nGood afternoon, {name}!")
    elif your_time >=17 and your_time <= 22:
        print(f"\nGood evening, {name}!")

def myAge(age):
    if age <15:
        print("\nWelcome! You're a young fellow!\n")
    elif age >=15 and age < 18:
        print("\nI wish I was in high school again... how may I help you?\n")
    elif age >=18 and age <55:
        print("\nNot too old yet.. how may I help you?\n")
    elif age >=55 and age <120:
        print("\nWow! Good job taking care of yourself and living. Welcome! How may I help you?\n")
    elif age >=120:
        print("\nI don't think anyone living is that age right now.. but whatever.\n")
time()

myAge(age)



time_until_delivery = None
the_choice = None
while True:
    print("Here are the following options you can choose from:\n1. Re-Schedule Order\n2. Check Delivery Status\n3. Contact Information\n4. Placeholder 4 \n5. Exit the conversation.")
    try:
        the_choice = input("Enter the number of your choice: ")
        if the_choice not in ['1','2','3','4','5', 'help']:
            raise ValueError
    except ValueError:
        print("\nInvalid value. Please enter a number.\n")
        continue
    if the_choice == '1':
        the_choice = 0
        while time_until_delivery == None:
            try:
                time_until_delivery = int(input("\n In how many minutes do you want the food to be delivered?\n"))
            except ValueError:
                print("Invalid value. Please enter a number.")
        the_choice = input(f"Okay, your order will be delivered in {time_until_delivery} minutes. Type 'help' if you need anything else.")

    elif the_choice == '2':
        print("\nWhen there is something here, I will tell you the answer to the problem you selected.\n")
    elif the_choice == '3':
        print("\nWhen there is something here, I will tell you the answer to the problem you selected.\n")
    elif the_choice == '4':
        print("\nWhen there is something here, I will tell you the answer to the problem you selected.\n")
    elif the_choice == '5':
        print("\nThank you for using the chatbot, "+name+". Have a great rest of your day!")
        exit()
    elif the_choice == 'help':
        print("Here are the following options you can choose from:\n1. Re-Schedule Order\n2. Check Delivery Status\n3. Contact Information\n4. Placeholder 4 \n5. Exit the conversation.")
        the_choice = input("Enter the number of your choice: ")
