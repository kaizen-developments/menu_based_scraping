import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

# Global state data
state_data = {
    'currentUrl': None,
    'links': [],
    'currentPattern': None,
    'currentState': 1
}

# State functions
def state_choose_website():
    state_data['currentUrl'] = input("Enter a website URL to start: ")
    state_data['currentState'] = 2

def state_go_to_website_and_find_links():
    html_content = fetch_page(state_data['currentUrl'])
    if html_content:
        state_data['links'] = extract_links(html_content, state_data['currentUrl'])
        print("\nNeighboring websites found:")
        for i, (link_text, link_url) in enumerate(state_data['links'], 1):
            print(f"{i}. {link_text} - {link_url}")
    state_data['currentState'] = 3

def state_operate_with_options():
    print("\nAvailable operations:")
    print("1. Go to a new website")
    print("2. Apply a new pattern")
    print("3. Show the current tree")
    # Add more operations as needed

    choice = input("Enter your choice: ")
    # Implement logic based on the choice
    # ...

# Utility functions for fetching pages and extracting links (same as before)
# ...

# Main loop
while True:
    if state_data['currentState'] == 1:
        state_choose_website()
    elif state_data['currentState'] == 2:
        state_go_to_website_and_find_links()
    elif state_data['currentState'] == 3:
        state_operate_with_options()
    else:
        print("Invalid state. Exiting program.")
        break
