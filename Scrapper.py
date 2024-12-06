from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def setup_driver():
    """Set up Selenium WebDriver."""
    # Replace with the path to your WebDriver
    driver_path = "/path/to/chromedriver"
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(executable_path=driver_path, options=options)

def scrape_website(url, scrape_function):
    """Navigate to the URL and scrape data."""
    driver = setup_driver()
    try:
        driver.get(url)
        time.sleep(3)  # Let the page load

        # Use the provided scraping function
        data = scrape_function(driver)

        return data
    finally:
        driver.quit()

def basic_scraper(driver):
    """Define the basic scraping logic."""
    try:
        # Example: Get all links from the page
        links = driver.find_elements(By.TAG_NAME, "a")
        return [link.get_attribute("href") for link in links if link.get_attribute("href")]

    except Exception as e:
        print(f"Error occurred: {e}")
        return []

if __name__ == "__main__":
    target_url = "https://example.com"
    data = scrape_website(target_url, basic_scraper)
    print(f"Scraped Links: {data}")
