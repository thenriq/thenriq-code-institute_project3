# Books Catalog Shopping System

Books Catalog Shopping System is a Python virtual book store, which runs on Heroku mock terminal.

All books available are stored in a google spreadsheet, and users can interact with it by consulting books in different ways. It also simulates a virtual shop, which will store all purchages back in the spreadsheet

[The live version is available HERE.](https://books-catalog-shopping-system.herokuapp.com/)

![Books Catalog](https://raw.githubusercontent.com/thenriq/thenriq-code-institute_project3/main/assets/readme_images/Am_I_Responsive_.png)

## Features

### Existing Features

The app can be controlled by using the main menu available, from options 1 to 5

![Main Menu](https://raw.githubusercontent.com/thenriq/thenriq-code-institute_project3/main/assets/readme_images/main_menu.png)

If an invalid choice is made, the menu will refresh, until a valid option is chosen. The option `x` is the choice to leave the app.

Within the option 1 to 4, if no books matches with the search term, the user will be informed and then asked to try again.

### Menu Items:

**1. View Books**:

This option will list all books, with their names and codes, on batches of 5. Each time `ENTER` is pressed, the next batch of 5 will be displayed. If, while listing the books, the key `q` is pressed followed by `ENTER`, the loop will terminate and the main menu will be displayed again.

![View all books](https://github.com/thenriq/thenriq-code-institute_project3/blob/main/assets/readme_images/menu_item_1.png?raw=true)

<br>

<br>

- Search Books:

In the option 1, a book can be searched by its name (partial names accepted), and all books found will also be listed on batches of 5, and the next batch of five will be displayed when pressing `ENTER`

![Search books](https://github.com/thenriq/thenriq-code-institute_project3/blob/main/assets/readme_images/menu_item_1_search.png?raw=true)

<br>

**2. View books by author**

This option will list books, followed by its author name. Like in the option 1, a search can also be made, but this time it will search by an author (partial names are also accepted).

![Search by Author](https://github.com/thenriq/thenriq-code-institute_project3/blob/main/assets/readme_images/menu_item_2_search.png?raw=true)

<br>

**3. View Books by Year of Publishing**

This option will list books, followed by its publishing date. Like in the other options, a search can also be made, but this time it will search by the publishing date (partial terms are also accepted).

![Search by date](https://github.com/thenriq/thenriq-code-institute_project3/blob/main/assets/readme_images/menu_item_3_search.png?raw=true)

<br>

**4. View Publishers**

This option will list books, followed by its publishers. Like in the other options, a search can also be made, but this time it will search by the book publisher (partial terms are also accepted).

![Search by publisher name](https://github.com/thenriq/thenriq-code-institute_project3/blob/main/assets/readme_images/menu_item_4_search.png?raw=true)

<br>

**5. Buy a book**

This option simulates a books store. The customer will start by searching a book name. Then, a result list will be displayed, with the book name and book code. The next step is to enter the book code and press `ENTER`. The book will be located, displaying it's price and asking user if it should be added to its basket. The system will keep asking for a choice (only `y` or `n` is accepted as input), until a valid option is chosen

![Search a book](https://github.com/thenriq/thenriq-code-institute_project3/blob/main/assets/readme_images/menu_item_5_search_and_buying.png?raw=true)

<br>

The book will then be added to the customer's basket, and the basket items will be displayed. At this stage, the sales can either be completed, by chosing `y`, or customer can opt to add more items to the basket, if chosing `n`

![Add to basket](https://github.com/thenriq/thenriq-code-institute_project3/blob/main/assets/readme_images/menu_item_5_add_basket.png?raw=true)

<br>

If customer decides to include more items, the system will ask again for a book name

![Searc more items](https://github.com/thenriq/thenriq-code-institute_project3/blob/main/assets/readme_images/menu_item_5_add_more_items.png?raw=true)

<br>

After added the new item, the basket will be displayed again, showing all items so far in the basket with the total price

![Add more items to basket](https://github.com/thenriq/thenriq-code-institute_project3/blob/main/assets/readme_images/menu_item_5_basket_updated.png?raw=true)

<br>

The purchase can now be completed. The system will ask for customer's name, and then it will record the sales in the google spreadsheet

![Sales completed](https://github.com/thenriq/thenriq-code-institute_project3/blob/main/assets/readme_images/menu_item_5_purchase_complete.png?raw=true)

<br>

### Future features

* Allow customer to preview its cart after the purchase is completed
* Give customer the option to scrap the sale after basket already contain items

## Data Model

This app was made by following the paradigm  of *[Structured programming](https://www.techtarget.com/searchsoftwarequality/definition/structured-programming-modular-programming)*, utilizing a **Procedural programming (functional programming)**. Each function is dedicated to a particular task in the program

<br>

The data this app uses is stored on a Google spreadsheet, in my particular Google account.

<br>

In order to read and record data in this spreadsheet, the app uses the *[gspread](https://docs.gspread.org/en/v5.7.0/)* module.

<br>

The system interface and some functionalities were based on a previous project I created while I was studying on [ATU](https://www.atu.ie/) (former GMIT). The repository for it can be found on [my Github page](https://github.com/thenriq/PythonApp-Movies)

<br>

The `main` function controls which tasks will be performed: search on a particular way, activate the shop module, or leave the app. All the search options in the app use the same shared function. 

<br>

The shop module, on the other hand, utilizes other several functions, but including the shared function above, that helps on shopping tasks, such as add an item to the basket, add more items, finish purchase, or abandon the purchase module

<br>

The flowchart below ilustrates how the system works:

![App Flowchart](https://github.com/thenriq/thenriq-code-institute_project3/blob/main/assets/readme_images/app_flowchart.png?raw=true)

<br>

### Testing

The following ways were undertaken to perform tests on this app:

* Passed through PEP8 linter and confirmed it has no issues
* Attempted invalid and out of range inputs, such as string instead of numbers, or very long integer numbers
* Tested locally and in the Heroku terminal, hosted by Code Institute

#### Bugs

**Solved Bugs**

- Found an incompatibility when testing on Heroku: the functions `os.system('pause')` and `keyboard.is_pressed('q')` could not be used on Heroku, with the error `ImportError: You must be root to use this library on linux.`  I fixed that by using `input` to simulate the system pause.

**Remaining Bugs** 

- No remaining bugs found

<br>

### Deployment

This project was deployed on Code Institute's mock terminal for Heroku.

- Steps for deployment:
  - Clone this repository
  - Create a new Heroku app
  - Set the buildbacks to `Python` and `NoteJS` in that order
  - Link the Heroku app to the repository
  - Click on deploy

<br>

### Credits

- Code Institute for Heroku terminal
- [GeeksforGeeks](https://www.geeksforgeeks.org/python-substring-key-match-in-dictionary/) for substring search
- My [app movies](https://github.com/thenriq/PythonApp-Movies) repository