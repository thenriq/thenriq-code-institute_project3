# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


from IPython.display import display
import gspread
from google.oauth2.service_account import Credentials

import os
import keyboard

import pandas as pd



SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('books_catalog')

books = SHEET.worksheet('books')

data = books.get_all_values()


def get_book_id():
    """
    testing if book_id is an integer value
    """
    while True:
        try:
            book_code = input("Enter book code: ")
            book_code = int(book_code)
            break
        except ValueError:
            print("Invalid book number, try again")
    return str(book_code)



def get_choice():
    """
    Check if user choice is whether yes (y) or no (n)
    """
    choice=input("Enter your choice: (y/n): ")
    while choice not in ['y', 'n']:
        choice=input("Enter your choice: (y/n): ")
    return(choice)


def choose_book():
    """
    Allows user to choose a book and choose 
    whether or not this book will be added to the basket

    Returns:
        boolean: add_basket
    """
    book_code = get_book_id()
    book_found = (books.row_values(books.find(book_code).row))
    #print(f"You've chosen '{book_found[1]}'. Add to basket? y/n\n")
    #add_choice = get_choice()
   # if add_choice == "y":
    #    add_basket = True
    #else:
    #    add_basket = False
    return book_found

def add_chart():
    """
    add a book to chart and ask if user wants to add more items
    to the basket
    """
    
    add_basket = choose_book()
    print(f"You've chosen '{add_basket[1]}'. Add to basket? y/n\n")
    add_choice = get_choice()
    if add_choice == "y":
        add_basket = True
    else:
        add_basket = False
        
    while add_basket:
        print("book added to chart")
        print("add more items? y/n")
        choice_more = get_choice()
        if choice_more == "y":
            choose_book()
        else:
            break
                
    
        
    


def display_menu():
    """
    creates main menu - function called within all 6 options in main menu
    """
    
    print("")
    print("Books Catalog")
    print("-"*9)
    print("")
    print("MENU")
    print("="*4)
    print("1 - View Books")
    print("2 - View Books by Author")
    print("3 - View Books by Year of Publishing")
    print("4 - View Publishers")
    print("5 - Buy a book")
    print("x - Exit")
    print("")


def main():
    """
    Creates main menu and calls all functions above
    """
    
    display_menu()
    
    while True:
        choice = input("Choice: ")
        if (choice == "1"):
            print("option 1")
            count = 0

            book_name = books.col_values(2)
            #book_rating = books.col_values(4)
            book_index = books.col_values(1)
            data.sort()
            
            for name, index in zip((book_name), (book_index)):
                print(f"Code: {index} - {name}")
                
                count += 1
                
                # prints book list in batches of 15
                # If count mod 15 = 0, asks to press key
                if (count % 15) == 0:
                    print("-- Quit (q) --")
                    os.system('pause')

                    # Breaks the looping if q is pressed
                    if keyboard.is_pressed('q'): 
                        break  # finishing the loop
        
            display_menu()

        elif(choice == "2"):
            print("option 2")
            display_menu()

        elif(choice == "3"):
            print("option 3")
            display_menu()

        elif(choice == "4"):
            print("option 4")
            display_menu()

        elif(choice == "5"):
            
            #choose_book()
            add_chart()
                
            
            #continue_sell = True
            #book_code = get_book_id()
            #book_found = (books.row_values(books.find(book_code).row))
            #add_basket = input((f"You've chosen '{book_found[1]}'. Add to basket? y/n\n"))
            #print (add_basket)

            #new_sales_item = {
            #    'Code':[book_found[0]],
            #    'Title':[book_found[1]],
            #    'Author':[book_found[2]],
            #    'Price': [book_found[5]]
            #}
            
            #df = pd.DataFrame(new_sales_item)
            #display(df)
            #print("")
            
            #os.system('pause')
            #while continue_sell:
            #    print("add more books? y/n")
            #    add_more = get_choice()
            #    if add_more == "y":
            #        continue_sell = True
            #    else:
            #        continue_sell = False
                
            
            
            display_menu()
         
        else:
            if (choice == 'x'):
                break
            else:
                display_menu()

if __name__== "__main__":
    main()