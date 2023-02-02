# BOOKS CATALOG SHOPPING SYSTEM

Books Catalog Shopping System is a Python virtual book store, which runs on Heroku mock terminal.

All books available are stored in a google spreadsheet, and users can interact with it by consulting books in different ways. It also simulates a virtual shop, which will store all purchages back in the spreadsheet

[The live version is available HERE.](https://books-catalog-shopping-system.herokuapp.com/)

![Books Catalog](https://raw.githubusercontent.com/thenriq/thenriq-code-institute_project3/main/assets/readme_images/Am_I_Responsive_.png)

## How the app works

The app can be controlled by using the main menu available, from options 1 to 5

![Main Menu](https://raw.githubusercontent.com/thenriq/thenriq-code-institute_project3/main/assets/readme_images/main_menu.png)

If an invalid choice is made, the menu will refresh, until a valid option is chosen. The option `x` is the choice to leave the app.

### Menu Items:

1. View Books:

This option will list all books, with their names and codes, on batches of 5. Each time `ENTER` is pressed, the next batch of 5 will be displayed. If, while listing the books, the key `q` is pressed followed by `ENTER`, the loop will terminate and the main menu will be displayed again.

![View all books](https://github.com/thenriq/thenriq-code-institute_project3/blob/main/assets/readme_images/menu_item_1.png?raw=true)

<br>

<br>

- Search Books:

In the option 1, a book can be searched by its name (partial names accepted), and all books found will also be listed on batches of 5, and the next batch of five will be displayed when pressing `ENTER`

![Search books](https://github.com/thenriq/thenriq-code-institute_project3/blob/main/assets/readme_images/menu_item_1_search.png?raw=true)

<br>

2. View books by author

This option will list books, followed by its author name. Like in the option 1, a search can also be made, but this time it will search by an author (partial names are also accepted).

![Search by Author](https://github.com/thenriq/thenriq-code-institute_project3/blob/main/assets/readme_images/menu_item_2_search.png?raw=true)
