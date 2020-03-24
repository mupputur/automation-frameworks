"""
@Author - Amulya U
@Date: 23 Mar 2020

This is the module will get the folowing things  from the website https://www.flipkart.com/

1. List all titles from DOD
2. List all products from DOD
3. List all images from DOD
4. Moving left Arrow
5. Moving Right Arrow
"""

from selenium import webdriver
import time
import os

print (">>>Executed on : {}".format(time.ctime()))

class DealsOfTheday:

    def __init__(self):
        self.driver= None
        self.initlize_driver()

    def initlize_driver(self):
        """
        This function initilizes the driver object
        """
        path = os.getcwd()
        path = os.path.join("\\".join(path.split("\\")[:-1]), "dependecies", 'chromedriver.exe')
        if not os.path.exists(path):
            raise Exception("Driver path not found. {}".format(path))
        else:
            self.driver = webdriver.Chrome(path)

    def launch_app(self):
        """
        This function can be used to launch the flipkart app if there is no login pop-up window
        """
        try:
            self.driver.get("https://www.flipkart.com/")
            time.sleep(3)
        except Exception as e:
            print("Fail to launch the application. {} ".format(str(e)))

    def launch_app_by_skipping_login_screen(self):
        """
        This function can be used to launch the flipkart app and it will handles  the login window
        """
        try:
            self.driver.get("https://www.flipkart.com/")
            time.sleep(3)
            ignore_login = self.driver.find_element_by_xpath("//button[@class='_2AkmmA _29YdH8']")
            if ignore_login:
                ignore_login.click()
                print ("Successfully skipped login screen")
        except Exception as e:
            print("Fail to launch the application. {}".format(str(e)))

    def get_dod_titles(self):
        """
        This function returns all the dod products titles as a list
        """
        try:
            titles = self.driver.find_elements_by_xpath("//div[@class='iUmrbN']")
            dod_titles = []
            for title in titles:
                dod_titles.append(title.text)
            return (dod_titles)
        except Exception as e:
            print ("Fail to get the DOD Titles. Error: {}".format(str(e)))

    def get_dod_products(self):
        """
        This function returns all DOD products as a list
        """
        try:
            products = self.driver.find_elements_by_xpath("//div[@class='_3o3r66']")
            dod_products = []
            for product in products:
                dod_products.append(product.text)
            return (dod_products)
        except Exception as e:
            print ("Fail to get the DOD products. Error: {}".format(str(e)))

    def get_dod_discounts(self):
        """
        This function returns all the dicounts of a products from DOD in a list
        """
        try:
            dod_discounts = []
            discounts = self.driver.find_elements_by_xpath("//div[@class='BXlZdc']")
            for discount in discounts:
                dod_discounts.append(discount.text)
            return (dod_discounts)
        except Exception as e:
            print ("Fail to get the discounts. Error: {}".format(str(e)))

    def get_image_srcs(self):
        """
        This function returns all images from DOD in a list
        """
        try:
           dod_images = []
           images = self.driver.find_elements_by_tag_name('img')
           for image in images:
               dod_images.append(image.get_attribute('src'))
           return (dod_images)
        except Exception as e:
            print("Fail to get DOD images: Error: {}".format(str(e)))

    def is_dod_arrow_exist(self):
        """
        This function returns True when the right arrow present and it should be able to move
        the items towards left to right
        """
        try:
            arrow = self.driver.find_elements_by_xpath("//div[@class='_2AEDbQ _1V02gy']")
            for item in arrow:
                item.click()
                time.sleep(3)
            return True
        except Exception as e:
            print("Failed to click right arrow. Error: {}".format(str(e)))


    def close_driver(self):
        """
        Closes the driver object
        """
        self.driver.close()

if __name__ == "__main__":
    fkart = DealsOfTheday()
    fkart.launch_app_by_skipping_login_screen()
    products = fkart.get_dod_products()
    titles = fkart.get_dod_titles()
    discounts = fkart.get_dod_discounts()
    images = fkart.get_image_srcs()
    arrow = fkart.is_dod_arrow_exist()

    print("="*30)
    print("PRODUCTS: ")
    print(products)

    print("=" * 30)
    print("TITLES: ")
    print(titles)

    print("=" * 30)
    print("DISCOUNTS: ")
    print(discounts)

    print("=" * 30)
    print("IMAGES: ")
    print(images)

    print("=" * 30)
    print("ARROW: ")
    if arrow:
        print ("ARROW EXIST & ITS MOVING")
    fkart.close_driver()
