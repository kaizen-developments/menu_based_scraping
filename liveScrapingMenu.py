import requests
from bs4 import BeautifulSoup
import inspect
import liveScrapingStrategies
from liveScrapingClasses import *
import liveScrapingPatterns

import liveScrapingMenuNavigation

# def show_strategies_menu():
#     print("\nStrategies Menu:")
#     print("0. Start scraping!")
#     print("1. List all scraping methods")
#     print("2. List all scraping strategies for websites")
#     print("3. List all scraping patterns for websites")
#     print("4. Return to Main Menu")

#     while True:
#         state_data = {
#             'currentUrl': None,
#             'links': [],
#             'currentPattern': None,
#             'currentState': 1
#         }

#         choice = input("Enter your choice, or type '-options' to show options: ")

#         if choice == '-options':
#             show_strategies_menu()
#         elif choice == '0':
#             start_scraping()
#         elif choice == '1':
#             list_scraping_methods()
#         elif choice == '2':
#             list_scraping_strategies()
#         elif choice == '3':
#             list_scraping_patterns()
#         elif choice == '4':
#             break
#         else:
#             print("Invalid choice. Please enter a valid option.")

# def start_scraping():
    

# def list_scraping_methods():
#     print("\nAvailable scraping methods:")
#     methods = inspect.getmembers(liveScrapingStrategies, inspect.isfunction)
#     for i, method in enumerate(methods, 1):
#         print(f"{i}. {method[0]}")

# def list_scraping_strategies():
#     print("\nStrategies for accessing relevant content of websites:")
    
#     # Get all attributes of the Content class that are not magic methods or functions
#     content_attributes = {attr for attr in dir(Content) 
#                           if not (attr.startswith('__') or callable(getattr(Content, attr)))}
    
#     # Mapping strategy names to Content class attributes
#     strategy_to_content_mapping = {
#         'url': 'url',
#         'title': 'title',
#         'body': 'body'
#     }

#     for key, value in liveScrapingStrategies.strategies.items():
#         print(f"\n  {key}:")
#         for strategy_name, strategy_func in value.items():
#             mapped_attribute = strategy_to_content_mapping.get(strategy_name, 'Unknown')
#             if mapped_attribute in content_attributes:
#                 print(f"    {strategy_name}: {strategy_func.__name__}")
#                 print(f"      Corresponds to Content class attribute: {mapped_attribute}")

# def list_scraping_patterns():
#     print("\nPatterns for accessing relevant content of websites:")
#     for domain, patterns in liveScrapingPatterns.domainPatterns.items():
#         print(f"\n  {domain}:")
#         for content_type, pattern in patterns.items():
#             print(f"    {content_type}: {pattern}")

# # Rest of the menu-based program
# show_strategies_menu()

#Menu
#   Scrape!
#       Choose a website!
#           Operating Loop:
#               Add new strategy to website!
#               Go to new website!
#                   Choose from the existing websites!
#                       Operating Loop:
#       Choose from existing scraping!
#       
#   Strategies:
#       Websites:
#           bookings.edu
#               Content
#           nytimes.com
#               Content
#   Patterns:
#       Websites:
#           
#   Data Models:
#There is always a choice to go back, from main menu this exits from the program.
from functools import partial 
fetch_in_the_websites_available = partial(liveScrapingMenuNavigation.extract_links, base_url = "")

state = "Menu"
website = ""
availableWebsites = []
pattern = ""
while(True):
    if state == "Menu":
        print("\nStrategies Menu:")
        print("0. Start scraping!")
        print("1. List all scraping methods")
        print("2. List all scraping strategies for websites")
        print("3. List all scraping patterns for websites")
        print("4. Return to Main Menu")

        choice = input("Enter your choice, or type '-options' to show options: ")

        if choice == '-options':
            "Not implemented"
        elif choice == '0':
            state = "Scrape"
        elif choice == '1':
            "Not implemented"
        elif choice == '2':
            "Not implemented"
        elif choice == '3':
            "Not implemented"
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a valid option.")
    elif state == "Scrape":
        print("0. Choose a website!")
        print("1. Choose from existing scraping!")

        choice = input("Enter your choice, or type '-options' to show options: ")

        if choice == '-options':
            "Not implemented"
        elif choice == '0':
            state = "Choose a website!"
        elif choice == '1':
            state = "Choose from existing scraping!"

        #strategies 
    elif state == "Patterns":
        "Not implemented yet"
    elif state == "DataModels":
        "Not implemented yet"
    elif state == "Choose a website!":
        website = input("Type in a website!")
        #availableWebsites = fetch_in_the_websites_available(website)
        state = "Operating Loop"

    elif state == "Choose from existing scraping!":
        "Not implemented yet"

    elif state == "Operating Loop":
        print("Current website:", website)
        print("Current pattern:", pattern)
        print("To choose a new website, type \"Choose a new website!\"")
        operation = input("Choose an operation!")
        if operation == "Choose a new website!":
            print("Available websites:")
            for site in availableWebsites:
                print(site)
            print("Choose a website!")
            website = input("Choose a website!")
            availableWebsites = fetch_in_the_websites_available(website)
            state = "Operating Loop"
            
    elif state == "Choose a new website":
        "Not implemented yet"
    elif state == "Switch to a new website":
        "Not implemented yet"