from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class SpiderBot:
    def __init__(self, start_url, max_depth=2):
        self.start_url = start_url
        self.max_depth = max_depth
        self.visited_links = set()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def get_links(self, url):
        """Extracts all links from a webpage."""
        self.driver.get(url)
        time.sleep(2)  # Give time for page to load
        links = self.driver.find_elements(By.TAG_NAME, 'a')
        return [link.get_attribute('href') for link in links if link.get_attribute('href')]

    def crawl(self, url, depth=0):
        """Recursively crawls webpages up to max_depth."""
        if depth > self.max_depth or url in self.visited_links:
            return
        
        print(f"Crawling: {url} (Depth: {depth})")
        self.visited_links.add(url)
        
        try:
            links = self.get_links(url)
            for link in links:
                self.crawl(link, depth + 1)
        except Exception as e:
            print(f"Error crawling {url}: {e}")
    
    def run(self):
        """Starts the crawling process."""
        self.crawl(self.start_url)
        self.driver.quit()

if __name__ == "__main__":
    bot = SpiderBot("https://www.youtube.com/", max_depth=1)
    bot.run()