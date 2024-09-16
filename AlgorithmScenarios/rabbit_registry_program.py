'''
Task Description:
Write a program that allows a user to create and store new rabbits. Each rabbit is identified by a unique
name. The program also allows the user to enter a rabbit's age and displays a list of all rabbits.

Main Menu
The program prompt of the main menu should look like this:

==================================
Enter your choice:
1. Create a Rabbit.
2. Input Age of a Rabbit.
3. List Rabbits.
0. Quit.
==================================
When the user selects one of the options (1, 2, 3, or 0), the corresponding function should be executed. If the user inputs
any other value, the prompt should be displayed again.

We recommend you create a function for each menu option.

Menu Options:
1. Create a Rabbit
When the user selects option 1, the program prompts:

Input the new rabbit's name:
If the user enters a name that is not already in the database, the program saves the rabbit and returns to the main menu.
If the name already exists, the program prints:

That name is already in the database.
Input the new rabbit's name:
This repeats until a unique name is provided.

2. Input Age of a Rabbit
When the user selects option 2, the program prompts:

Input the rabbit's name:
If the entered name is in the database, the program then asks for the rabbit's age:

Input <rabbit_name>'s age:
Once the age is provided, it updates the rabbit’s information and returns to the main menu.

If the name doesn't exist, the program prints:

That name is not in the database.
Input the rabbit's name:
This repeats until a valid name is provided.

3. List Rabbits
When the user selects option 3, the program prints:

Rabbits:
Followed by a list of all created rabbits. If the age of a rabbit has been input, it displays the rabbit’s age. If the age
hasn’t been input, it displays "Unknown." For example:

rabbie (42)
not_rabbie (Unknown)
The list should display the rabbits in the order they were created.

0. Quit
If the user selects option 0, the program exits.

Assumptions:
The rabbit's age is an integer.
The user can freely set or update a rabbit's age, even if it already has one.
The program should display the rabbits in the order they were created.
Example:
Main Menu:

==================================
Enter your choice:
1. Create a Rabbit.
2. Input Age of a Rabbit.
3. List Rabbits.
0. Quit.
==================================
Example 1 - Creating a Rabbit:

Enter your choice: 1
Input the new rabbit's name: rabbie
==================================
Enter your choice: 0
Example 2 - Handling Duplicate Name:

Enter your choice: 1
Input the new rabbit's name: undercover_robbie
==================================
Enter your choice: 1
Input the new rabbit's name: undercover_robbie
That name is already in the database.
Input the new rabbit's name: robbie_the_rabbit
==================================
Enter your choice: 0
Example 3 - Inputting Age:

Enter your choice: 2
Input the rabbit's name: rabbie
Input rabbie's age: 42
==================================
Enter your choice: 0
Example 4 - Listing Rabbits:

Enter your choice: 3
Rabbits:
rabbie (42)
robbie_the_rabbit (Unknown)
==================================
Enter your choice: 0
'''
# Dictionary to store rabbit data
rabbits = {}

def create_rabbit():
    while True:
        rabbit_name = input("Input the new rabbit's name: ").strip()
        if rabbit_name not in rabbits:
            rabbits[rabbit_name] = None  # Age is not set yet, so it's None
            break
        else:
            print("That name is already in the database.")

def input_age():
    while True:
        rabbit_name = input("Input the rabbit's name: ").strip()
        if rabbit_name in rabbits:
            try:
                age = int(input(f"Input {rabbit_name}'s age: "))
                rabbits[rabbit_name] = age
                break
            except ValueError:
                print("Invalid age. Please enter an integer.")
        else:
            print("That name is not in the database.")

def list_rabbits():
    print("Rabbytes:")
    for rabbit_name, age in rabbits.items():
        if age is None:
            print(f"{rabbit_name} (Unknown)")
        else:
            print(f"{rabbit_name} ({age})")

def main_menu():
    while True:
        print("=" * 30)
        print("Enter your choice:")
        print("1. Create a Rabbit.")
        print("2. Input Age of a Rabbit.")
        print("3. List Rabbytes.")
        print("0. Quit.")
        print("=" * 30)

        choice = input().strip()
        if choice == "1":
            create_rabbit()
        elif choice == "2":
            input_age()
        elif choice == "3":
            list_rabbits()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the program
main_menu()
