import csv
from os import close

# csv file name
My_Players_Files = "My_Players_File.csv"

# Pick from menu 
def menu():
    print("Please select from one of the options below: \n 1. Time remaining for each players contracts to expire \n 2. Players contract time with each time in total \n 3. Teams with female players")
    menu_choice = input()

    if menu_choice == "1":
        print("\n Time remaining for each players contracts to expire \n")
        contract_expiry()
        exit_menu()

    if menu_choice == "2":
        print("\n Players contract time with each time in total \n")
        exit_menu()

    if menu_choice == "3":
        print("\n Teams with female players \n")
        female_players()
        print("\n")
        exit_menu()

# Exit Menu
def exit_menu():
    print("Is there anything else you would like to look at: \n 1. Yes \n 2. No")
    menu_choice = input()
    
    if menu_choice == "1":
            menu()
    if menu_choice == "2":
            print("\n Session has ended")
            exit

def contract_expiry():
    with open("My_Players_File.csv") as playerFile:
        playerFileReader = csv.reader(playerFile,delimiter=',')
    

def female_players():
    with open("My_Players_File.csv") as playerFile:
        playerFileReader = csv.reader(playerFile,delimiter=',')
        gender = "F"
        for row in playerFileReader:
            if row[2] == gender:
                print(row[4],row[0],"£"+row[7]+"K")
               

menu()    


# with open("My_Players_File.csv") as playerFile:
#     playerFileReader = csv.reader(playerFile)
#     gender = input("Enter Gender: ")
#     for row in playerFileReader:
#         if row[2] == gender:
#             print(row)
