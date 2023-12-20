import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from liveScrapingCommonFunctionalities import getPage

# A simple structure to hold the derived data
derivedDataFromUrl = {
    'currentUrl': None,
    'links': []
}

def fetch_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Error accessing page: HTTP {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def extract_links(htmlLink, base_url):
    soup = getPage(htmlLink)
    links = []
    for link in soup.find_all('a', href=True):
        # Create an absolute URL
        abs_url = urljoin(base_url, link['href'])
        links.append((link.text.strip(), abs_url))
    return links

def navigate_to_page():
    html_content = fetch_page(derivedDataFromUrl['currentUrl'])
    if html_content:
        derivedDataFromUrl['links'] = extract_links(html_content, derivedDataFromUrl['currentUrl'])
        
        print("\nAvailable pages to navigate to:")
        for i, (link_text, link_url) in enumerate(derivedDataFromUrl['links'], 1):
            print(f"{i}. {link_text} - {link_url}")
        
        choice = input("\nEnter the number of the page to navigate or type a URL: ")

        # If the choice is a number, get the corresponding URL
        try:
            if choice.isdigit():
                selected_index = int(choice) - 1
                derivedDataFromUrl['currentUrl'] = derivedDataFromUrl['links'][selected_index][1]
            else:
                # Validate if the entered URL is in the list
                if choice in (url for _, url in derivedDataFromUrl['links']):
                    derivedDataFromUrl['currentUrl'] = choice
                else:
                    print("Invalid URL. Please select a URL from the list.")
            
            # Refresh the derived data from the new URL
            print(f"Navigating to {derivedDataFromUrl['currentUrl']}...")
            # Call navigate_to_page again to refresh the list of links from the new URL
            navigate_to_page()

        except IndexError:
            print("Invalid selection. Please select a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number or a URL.")

# Initialize the current URL for the sake of example
derivedDataFromUrl['currentUrl'] = 'http://example.com'

# Example usage
#navigate_to_page()