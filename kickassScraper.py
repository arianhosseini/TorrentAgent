__author__ = 'arian'
#from BeautifulSoup import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Scrape:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def scrape(self,link):
        self.driver.get(link)
        self.name_elems = self.driver.find_elements_by_class_name("cellMainLink")
        self.magnet_elems = self.driver.find_elements_by_class_name("imagnet")
        names = [i.text for i in self.name_elems]
        magnets = [i.get_attribute("href") for i in self.magnet_elems]
        self.name_mag_dict = {}
        for index,i in enumerate(names):
            self.name_mag_dict[i] =magnets[index]
        print self.name_mag_dict



scp = Scrape("https://kickass.so/search/1080p%20category:xxx/")

