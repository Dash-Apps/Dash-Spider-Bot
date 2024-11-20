from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import selenium

def initialize_driver():
    options = webdriver.ChromeOptions()
    options.headless = True  # Optional
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver


def crawl_website(start_url, max_pages=10):
    driver = initialize_driver()
    visited_links = set()
    to_visit_links = [start_url]
    
    while to_visit_links and len(visited_links) < max_pages:
        current_url = to_visit_links.pop(0)
        
        if current_url in visited_links:
            continue
        
        try:
            driver.get(current_url)
            print(f"Crawling URL: {current_url}")

            # Custom logic to extract information (e.g., titles, links, data)
            title = driver.title
            print(f"Title: {title}")
            
            # Extract links from the page (customize as needed)
            links = driver.find_elements(By.TAG_NAME, 'a')
            for link in links:
                href = link.get_attribute('href')
                if href and href.startswith('http'):
                    to_visit_links.append(href)
        
        except Exception as e:
            print(f"Error crawling {current_url}: {e}")
        
        visited_links.add(current_url)
        time.sleep(1)  # Delay to avoid being blocked by the server
    
    driver.quit()
    print("Crawling completed.")

# Run the spider bot
start_url = 'https://example.com'  # Replace with your desired start URL
crawl_website(start_url)