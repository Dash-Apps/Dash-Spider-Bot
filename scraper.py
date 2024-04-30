#methods and functions used by scraper spiderbots
from bs4 import BeautifulSoup,element
from selenium import webdriver
from selenium.webdriver.common.by import By
def generate_xpath():
    pass
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run Chrome in headless mode
driver = webdriver.Chrome(options=options)
url = "https://stackoverflow.com/questions/34377211/why-is-google-coms-source-code-so-messy"
driver.get(url)
for _ in range(5):
    pass
elements = driver.find_elements(By.XPATH,"//*")
for element in elements:
    print(element)
source = "the fox quickly jumped over the lazy dog"
soup = BeautifulSoup(driver.page_source,'html5lib')

#for i in soup.descendants :
 #    if type(i) == element.Tag and i.name:
  #      if i.attrs != {} and 'href' in i.attrs or 'src' in i.attrs :
   #        print(i.name)
    #       print(i.attrs)
     #      print(i.)
           
driver.quit()