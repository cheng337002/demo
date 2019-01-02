# -*- coding: utf-8 -*-
from pprint import pprint
import getpass


from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def main():
    driver = webdriver.Firefox()
    driver.get("https://www.facebook.com/")
    email_field = driver.find_element_by_id("email")
    email = input("Type your facebook email: ")
    email_field.send_keys(email)
    password_field = driver.find_element_by_id("pass")
    password = getpass.getpass("Type your facebook password: ")
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)


if __name__ == "__main__":
    main()
