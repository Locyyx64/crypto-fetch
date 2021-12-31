#!/usr/bin/python3

import math
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By


options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, service=Service('/usr/local/bin/geckodriver'))

def get_max(list):
    max = list[0]
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
    return max


print("             .__                              __    \n  ____  ____ |__| ____    ____   ____   ____ |  | __\n_/ ___\/  _ \|  |/    \  / ___\_/ __ \_/ __ \|  |/ /\n\  \__(  <_> )  |   |  \/ /_/  >  ___/\  ___/|    <          by @SussyDev\n \___  >____/|__|___|  /\___  / \___  >\___  >__|_ \ \n     \/              \//_____/      \/     \/     \/\n")
while 1:
    command = input("\n>")

    if command == "crypto":
        driver.get("https://www.coingecko.com")
        n = int(input("How many cryptocurrencies do you want to see the price of? "))
        print("\033[1m" + "\nNote: " + "\033[0m" + "The currencies are listed by market cap.\n")
        cryptolist = []
        numberlist = []
        lengthlist = []

        if n > 100:
            for i in range(int(n / 100)):
                numberlist.append(100)
            numberlist.append(n % 100)
            for j in range(len(numberlist)):
                print('Searching the {}. page...'.format(j+1))
                for i in range(numberlist[j]):

                    price = driver.find_element(By.XPATH,
                                                "/html/body/div[3]/div[4]/div[6]/div[1]/div/table/tbody/tr[{}]/td[4]/span".format(i+1))
                    name = driver.find_element(By.XPATH,
                                               "/html/body/div[3]/div[4]/div[6]/div[1]/div/table/tbody/tr[{}]/td[3]/div/div[2]/a[1]".format(i+1))
                    try:
                        change1_day = driver.find_element(By.XPATH,
                                                          "/html/body/div[3]/div[4]/div[6]/div[1]/div/table/tbody/tr[{}]/td[6]/span".format(i+1))
                    except selenium.common.exceptions.NoSuchElementException:
                        change1_day = driver.find_element(By.XPATH,
                                                          "/html/body/div[3]/div[4]/div[6]/div[1]/div/table/tbody/tr[{}]/td[6]".format(i+1))
                    crypto = "{} = \033[1m{}\033[0m    {}".format(name.text, price.text, change1_day.text)
                    cryptolist.append(crypto)
                driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/button").click()
                driver.find_element(By.XPATH, "/html/body/div[3]/div[4]/div[6]/div[2]/nav/ul/li[{}]/a".format(j+3)).click()
            for i in range(len(cryptolist)):
                print("-------------------------------------------")
                print("{}. {}".format(i+1, cryptolist[i]))
        elif n < 0:
            print("\nPlease enter a positive value.")
        else:
            for i in range(1, n + 1):
                price = driver.find_element(By.XPATH,
                                            "/html/body/div[3]/div[4]/div[6]/div[1]/div/table/tbody/tr[{}]/td[4]/span".format(i))
                name = driver.find_element(By.XPATH,
                                            "/html/body/div[3]/div[4]/div[6]/div[1]/div/table/tbody/tr[{}]/td[3]/div/div[2]/a[1]".format(i))
                try:
                    change1_day = driver.find_element(By.XPATH,
                                                        "/html/body/div[3]/div[4]/div[6]/div[1]/div/table/tbody/tr[{}]/td[6]/span".format(i))
                except selenium.common.exceptions.NoSuchElementException:
                    change1_day = driver.find_element(By.XPATH,
                                                        "/html/body/div[3]/div[4]/div[6]/div[1]/div/table/tbody/tr[{}]/td[6]".format(i))
                crypto = "{}. {}  =  \033[1m{}\033[0m   {}".format(i, name.text, price.text, change1_day.text)
                cryptolist.append(crypto)
                lengthlist.append(len(crypto))
            max = get_max(lengthlist)
            for i in range((len(cryptolist)-1)):
                print(cryptolist[i])
                print((max-8) * "-")
            print(cryptolist[len(cryptolist)-1])
        driver.quit()
    elif command == "quit":
        break
    elif command == "help":
        print("\nhelp -- list all commands \n"
              "crypto -- check crypto prices \n"
              "quit -- stop the command")
