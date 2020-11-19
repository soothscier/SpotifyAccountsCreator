from selenium import webdriver

from multiprocessing import Process, Lock

from time import sleep
import csv
import random
import string

def getRandomString(length): #Letters and numbers
    pool=string.ascii_lowercase+string.digits
    return "".join(random.choice(pool) for i in range(length))

def getRandomText(length): #Chars only
    return "".join(random.choice(string.ascii_lowercase) for i in range(length))

def createSpotifyAccounts(fileName, numberOfAccounts):
    # Creating chrome webdriver instance
    driver = webdriver.Chrome()
    
    
    with open('./accounts/' + str(fileName) + '.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        for i in range(int(numberOfAccounts)):

            driver.get('https://spotify-upgrade.net/upgrade')
            sleep(1)

            password = getRandomString(8)
            email = getRandomText(5)+"@"+getRandomText(5)+".com"
            
            driver.find_element_by_xpath('//*[@id="mainLogin"]/div/div[2]/div/div[2]/label[2]').click()

            sleep(2)
            driver.find_element_by_xpath('//*[@id="mainLogin"]/div/div[2]/div/div[1]/form[2]/div[2]/input').send_keys(email)
            driver.find_element_by_xpath('//*[@id="mainLogin"]/div/div[2]/div/div[1]/form[2]/div[3]/input').send_keys(password)
            driver.find_element_by_xpath('//*[@id="mainLogin"]/div/div[2]/div/div[1]/form[2]/div[4]/input').click()

            sleep(3)

            writer.writerow([email, password])

    driver.quit()

if __name__ == "__main__":
    Processes = []

    for num in range(5):
        # change 10 with the number of accounts you want to create
        a = Process(target=createSpotifyAccounts, args=(num,10,))
        a.start()
        Processes.append(a)
        
    
    for p in Processes:
        p.join() 





