# This program will display a train station monitor

# Library's
import os
import random
import sys
import time

os.system("cls")  # Clears the screen

# vars & lists

Ticket_cost = 5

# Gen current time
Current_X_time = random.randint(1, 9)
Current_Y_time = random.randint(10, 59)

# Destination List
Destination_list = [
    "California",
    "Chicago",
    "New York",
    "New Orleans",
    "Seattle",
    "Atlanta",
    "Milwaukee",
    "Illinois",
    "Boston",
    "Washington",
    "Kansas City"]

# On_time train list
On_time_list = []

# All trains
All_trains = []

Current_time = f"Current time | {Current_X_time}:{Current_Y_time}"  # Displays fake current time



# Gen train station display

def Gen_Train():
    global Display

    print("")
    print("Time   Destination   Flat Form   Expected")
    print("-----------------------------------------\n")

    for i in range(5):  # Edit number to add more trains to list
        # Sets On time to false
        On_Time = False

        # Picks a random train from the rain_types list
        Destination = random.choice(Destination_list)

        # Gen a time for the train to arrive at the train station
        Train_X_time = random.randint(1, 9)
        Train_Y_time = random.randint(10, 59)
        Train_Time = f"{Train_X_time}:{Train_Y_time}"

        # Picks a random number from 1-3
        Flat_form = random.randint(1, 3)

        # Preforms a calculation to see if train is late based on time
        if Train_X_time < Current_X_time:
            Expected = "Delayed"
        else:
            Expected = "On Time"
            On_Time = True

        # Displays train model & time of arrival
        Display = f"{Train_Time} {Destination:>13}       {Flat_form}     {Expected:>9}"
        if On_Time:
            On_time_list.append(Display)  # Adds the on time train to list

        All_trains.append(Display)
        print(Display)
    print("")
    print(Current_time)

    # If train is even available
    if len(On_time_list) > 0:
        User_input_selection()



def output_available_trains():
    print("\n[AVAILABLE TRAINS]\n")
    print("Time   Destination   Flat Form   Expected")
    print("-----------------------------------------\n")

    for i in On_time_list:
        print(i)
    print("")
    print(Current_time)

def output_all_trains():
    print("\n[AVAILABLE TRAINS]\n")
    print("Time   Destination   Flat Form   Expected")
    print("-----------------------------------------\n")

    for i in All_trains:
        print(i)
    print("")
    print(Current_time)
    User_input_selection()


def User_input_selection():
    print("\n")  # Spaces out text
    amount_of_tickets = input("Number of Tickets: ")  # User input for amount of tickets

    try:
        amount_of_tickets = int(amount_of_tickets)
    except:
        os.system("cls")
        print("Please enter a int EX: 2")
        User_input_selection()

    if amount_of_tickets == 0:
        os.system("cls")
        output_all_trains()

    os.system("cls")
    output_available_trains()
    print(f"Tickets : {amount_of_tickets}")
    print(f"Train : {On_time_list[random.randint(0, len(On_time_list))]}")
    print(f"Price : ${amount_of_tickets * Ticket_cost}\n")
    Confirm = input("Confirm? Y or N: ")
    if Confirm == "Y":
        print("Confirmed Have a nice ride!")
        time.sleep(5)
        os.system("cls")
        output_all_trains()
    else:
        os.system("cls")
        output_all_trains()


# start
Gen_Train()
