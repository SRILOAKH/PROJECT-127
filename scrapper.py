from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By
import csv
START_URL="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars/"
browser=webdriver.Chrome("/Users/M V R CHOWDHARY/OneDrive/Desktop/PYTHON/chromedriver")
browser.get(START_URL)
time.sleep(10)
def scrape():
    headers=["name","distance","mass","radius",]
    stars_data=[]
    for i in range(0, 428): 
        soup = BeautifulSoup(browser.page_source, "html.parser") 
        for ul_tag in soup.find_all("ul", attrs={"class", "stars"}): 
            li_tags = ul_tag.find_all("li") 
            temp_list = []
            for index, li_tag in enumerate(li_tags): 
                if index == 0: 
                    temp_list.append(li_tag.find_all("a")[0].contents[0]) 
                else: 
                    try: 
                        temp_list.append(li_tag.contents[0]) 
                    except: 
                        temp_list.append("") 
                    stars_data.append(temp_list)
            stars_data.append(temp_list) 
        browser.find_element(By.XPATH,'//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click() 
    with open("scrapper_2.csv", "w") as f: 
        csvwriter = csv.writer(f) 
        csvwriter.writerow(headers) 
        csvwriter.writerows(stars_data) 
scrape()

