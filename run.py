# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


from IPython.display import display
import gspread
from google.oauth2.service_account import Credentials

import os
import keyboard

import pandas as pd

from pprint import pprint

import yaml



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

book_title = []
book_author = []
book_price = []
#book_published_date = []



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
    print("\n")
    while choice not in ['y', 'n']:
        choice=input("Enter your choice: (y/n): ")
    return choice


def choose_book():
    """
    Allows user to choose a book and choose 
    whether or not this book will be added to the basket

    Returns:
        boolean: add_basket
    """
    
    # Validating if book id chosen is within book list available to purchase
    # This will prevent error 'NoneType' object has no attribute 'row'
    #while True:
    x = 'b_code'
    books_search_default(x)
    book_was_found = True
    while book_was_found:
        try:
            book_code = get_book_id()
            book_found = (books.row_values(books.find(book_code).row))
            print(f"You've chosen '{book_found[1]}'.\nPrice: ${book_found[5]}. Add to basket? y/n\n")
            add_choice = get_choice()
            
            if add_choice == "y":
                add_to_basket(book_found)
            else:
                add_more_items()
            book_was_found = False
        except Exception as e:
            print("book not found, try again. ", e)
            book_was_found = True
                        

def add_more_items():
    """
    Add more books to the list on demand
    """

    print("add more books?")
    add_more  = get_choice()
    if add_more == "y":
        choose_book()
    else:
        add_more =  "n"
        finish_purchase()

def add_to_basket(book_found):
    """
    Add book to the basket and ask whether more books will be chosen
    Args:
        book_found (type = list): Holds all book information found on function choose_book()
    """
    book_title.append(book_found[1])
    book_author.append(book_found[2])
    book_price.append(book_found[5])
    print(f"'{book_found[1]}' added to basket\n")
   
    length = len(book_title)
    total_cart = 0
    for i in range(length):
        total_cart += float(book_price[i])
        print(f"Item {i+1}:")
        print(f"Title: {book_title[i]}\nAuthor: {book_author[i]}\nPrice: {book_price[i]}\n")
    print(f"Total cart: {total_cart}\n")
    finish_purchase()
    


def finish_purchase():
    """
    Check whether or not the purchase will be completed. If not,
    then it offers user to purchase more books
    """
    
    print("finish purchase?")
    finish_sell = get_choice()
    if finish_sell == "y":
        if len(book_title) != 0:
            print("Recording your sales...")
            commit_purchase(book_title, book_author, book_price)
            #finish_sell = "y"
            clear_basket(book_title, book_author, book_price)
        else:
            print("No items found in your basket. Sales will not be recorded. Good bye!")
        os.system('pause')
    else:
        add_more_items()
        
def commit_purchase(arr1, arr2, arr3):
    """Recording sales into spreadsheet

    Args:
        arr1 (list): book_title
        arr2 (list): book_author
        arr3 (list): book_price
    """
    
    # Getting last sales number
    length = len(arr1)
    sales = SHEET.worksheet("sales")
    items_sales = SHEET.worksheet("sales_items")
    total_items = items_sales.col_values(1)
    last_item = total_items[-1]
    
    # If table sales_number does not contain an item, the next_item will be 1
    if isinstance(last_item, str):
        try:
            next_item = int(last_item)
            next_item = next_item + 1
        except ValueError:
            next_item = int(1)
    
    total_sale = [float(i) for i in arr3]
    customer_name = input("Enter your name:\n")
    
    sales_details = (next_item, customer_name, sum(total_sale))
    sales.append_row(sales_details)
        
    for i in range(length):
        items_details = (next_item, arr1[i], arr2[i], arr3[i])
        items_sales.append_row(items_details)
    print("Sales completed. Good bye!")


def clear_basket(title, author, price):
    """
    Clear basket items after a sell is complete

    Args:
        title (list): Books titles
        author (list): Books author
        price (list): Books price
    """
    title.clear()
    author.clear()
    price.clear()

def books_search_default(header):
    res = {}
    books_title = books.col_values(2)
    if header == "b_code":
        master_list = books.col_values(1)
        search_term = "book name"
        search_item = "Book"
        for_y = "Code"
        item_search = 0
    
    elif header == "b_author":
        master_list = books.col_values(3)
        search_term = "book author"
        search_item = "Author"
        for_y = "Author"
        item_search = 1
        
    elif header == "b_year":
        master_list = books.col_values(14)
        search_term = "year of publishing"
        search_item = "Year"
        for_y = "Date"
        item_search = 1
        
    elif header == "b_publisher":
        master_list = books.col_values(9)
        search_term = "publisher name"
        search_item = "Publisher"
        for_y = "Publisher"
        item_search = 1
    
    else:
        header = "b_choose"
        master_list = books.col_values(1)
        
    books_dict = dict({books_title[i]:master_list[i] for i in range(len(sorted(books_title)))})
    
    while len(res) == 0:
        skip = True
        search_item = input(f"Enter {search_term}. Press ENTER to list ALL: ")
        print("")
        
        #https://www.geeksforgeeks.org/python-substring-key-match-in-dictionary/
        res = dict(filter(lambda item: search_item.casefold() in (item[item_search]).casefold(), books_dict.items()))
        if len(res) == 0:
            print(f"{search_item} not found, try again")
        
        # printing result
        else:
            count = 0
            for x, y in sorted(res.items()):
                print(f"Book name: {x}\n{for_y}: {y},\n")
                count += 1
                
                if (count % 5) == 0:
                    print("-- Quit (q) --")
                    os.system('pause')

                    # Breaks the looping if q is pressed
                    if keyboard.is_pressed('q'):
                        skip = False
                        break  # finishing the loop
    if skip:    
        os.system('pause')
            
    



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
            #books_by_code()
            x = 'b_code'
            books_search_default(x)
            display_menu()

        elif(choice == "2"):
            #books_by_author()
            x =  "b_author"
            books_search_default(x)
            display_menu()

        elif(choice == "3"):
            #books_year_publishing()
            x = "b_year"
            books_search_default(x)
            display_menu()

        elif(choice == "4"):
            #books_publishers()
            x = "b_publisher"
            books_search_default(x)
            display_menu()

        elif(choice == "5"):
            choose_book()
            display_menu()
         
        else:
            if (choice == 'x'):
                break
            else:
                display_menu()

if __name__== "__main__":
    main()