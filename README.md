# contact_book.py
 # Python Contact Book

## Project Overview

The Contact Book is a simple Python console application that allows users to add, view, search, and delete contacts. Each contact has a name and a phone number.

## Program Structure

The program uses a dictionary called `contacts` to store contact information. Each contact name is a key, and the phone number is its value.

The application contains five main functions and a main menu:

- **`add_contact()`**: Collects a name and phone number, validates the input, and prevents duplicate contact names.
- **`view_contacts()`**: Displays all saved contacts in alphabetical order or informs the user when the list is empty.
- **`search_contact()`**: Searches for contacts using a full name or part of a name.
- **`delete_contact()`**: Removes a contact when it exists in the dictionary.
- **`main()`**: Displays the menu, accepts the user's choice, and calls the appropriate function.

## Python Concepts Used

- Variables and data types
- Input and output using `input()` and `print()`
- Dictionaries and dictionary operations
- Conditional statements (`if`, `elif`, and `else`)
- Loops (`while` and `for`)
- Functions and parameters
- String methods and f-strings
- Exception handling using `try` and `except`
- Input validation and list comprehensions

## Challenges and Solutions

One challenge was preventing duplicate contact names. I solved this by comparing names without considering capitalization.

Another challenge was handling invalid menu input. I used `try` and `except ValueError` to prevent the program from stopping when the user enters text instead of a number.

I also implemented partial-name searches and checked phone-number input before saving a contact.

## Conclusion

This project helped me practice the fundamental concepts of Python by building a useful, interactive application. The program runs in the console and stores contacts in memory while it is running.

