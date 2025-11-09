from datetime import date, datetime
from time import sleep as wait
import random
import threading

current_time = datetime.now()
your_time = current_time.hour -5
continuing_thread = True
time_until_delivery_minutes = None
time_until_delivery_seconds = None
count_thread = False
response = None
progress = None
delivered = None

seconds = 0
minutes = 0

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

def counting():
    global seconds
    global minutes
    while continuing_thread:
        seconds+=1
        if seconds >= int(delivered):
            seconds = int(delivered)
        minutes = int(seconds/60)
        wait(1)

print("Welcome to the tech support chatbot!")
name = input("Please enter your name: ")
age = int(input("Hello "+ name + ", how old are you? "))

time()
myAge(age)

while True:

    print("-------------------\nHere are the following options you can choose from:\n1. Re-Schedule Order\n2. Check Delivery Status\n3. Contact Information\n4. Exit the conversation.\n-------------------")
    try:
        the_choice = input("Enter the number of your choice: ")
        if the_choice not in ['1','2','3','4', 'help']:
            raise ValueError
    except ValueError:
        print("\nInvalid value. Please enter a number.\n")
        continue
    if the_choice == '1':
        the_choice = 0
        while time_until_delivery_minutes == None and time_until_delivery_seconds == None:
            try:
                cost_of_previous_order = float(input("-------------------\nWhat was the cost of your previous order? "))
                time_until_delivery_minutes = int(input("-------------------\nIn how many minutes do you want the food to be delivered? "))
                time_until_delivery_seconds = int(input("-------------------\nIn how many extra seconds do you want the food to be delivered? "))
            except ValueError:
                print("Invalid value. Please enter a number.")
        if progress == "Delivered":
            print("-------------------\nYour order has already been delivered.\n-------------------")
            continue
        the_choice = input(f"Okay, your order will be delivered in {time_until_delivery_minutes} minute(s) and {time_until_delivery_seconds} second(s). Type 'help' if you need anything else. ")

        total_seconds = (time_until_delivery_minutes*60) + time_until_delivery_seconds

        response = int(random.uniform(0,(total_seconds)*1/2))
        picking_up = int(random.uniform(response, (total_seconds)*9/10))
        delivering = int(random.uniform(picking_up, (total_seconds)*1.3))
        delivered = int(random.uniform(delivering, (total_seconds)*1.5))

        count_thread = threading.Thread(target = counting)
        count_thread.start()

    elif the_choice == '2':
        if response == None:
            print("You need to make an order before you can check its status.")
            continue
        progress = "No Response"
        if seconds >= response:
            progress = "Responded"
        if seconds >= picking_up:
            progress = "Picked Up"
        if seconds >= delivering:
            progress = "Delivering"
        if seconds >= delivered:
            progress = "Delivered"
        if progress != "Delivered":
            print(f"-------------------\nMinutes: {minutes}\nSeconds: {seconds%60}\nProgress: {progress}\n-------------------")
        if progress == "Delivered":
            print(f"-------------------\nMinutes: {minutes}\nSeconds: {delivered%60}\nProgress: {progress}\n")
            continuing_thread = False
            if total_seconds > delivered:
                print(f"Cost of the order: ${cost_of_previous_order:.2f}")
            if total_seconds < delivered:
                print(f"Cost of the order: ${(cost_of_previous_order-(delivered-total_seconds)/100):.2f}\n-------------------")


    elif the_choice == '3':
        print("-------------------\nCall 555-485-0994 for further assistance.\n-------------------")
    elif the_choice == '4':
        print("-------------------\nThank you for using the chatbot, "+name+". Have a great rest of your day!\n-------------------")
        if count_thread:
            continuing_thread = False
            exit()
        exit()
    elif the_choice == 'help':
        continue
