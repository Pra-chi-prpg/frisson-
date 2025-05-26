from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv

def scrape_it_companies(output_csv="it_companies_noida.csv", scrolls=15):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.google.com/maps")
    time.sleep(5)

    search_box = driver.find_element(By.ID, "searchboxinput")
    search_box.send_keys("IT companies in Noida")
    search_box.send_keys(Keys.ENTER)
    time.sleep(10)

    # Scroll to load more listings
    for _ in range(scrolls):
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        time.sleep(2)

    listings = driver.find_elements(By.CSS_SELECTOR, 'div.Nv2PK')
    data = []

    for listing in listings[:50]:  
        try:
            listing.click()
            time.sleep(5)

            name = driver.find_element(By.CSS_SELECTOR, 'h1.DUwDvf').text
            address = driver.find_element(By.CSS_SELECTOR, 'div.Io6YTe span').text

            phone = "N/A"
            details = driver.find_elements(By.CSS_SELECTOR, 'div.Io6YTe')
            for d in details:
                if "+" in d.text:
                    phone = d.text
                    break

            data.append([name, phone, address])
            print(f"Collected: {name}")
        except:
            continue

    driver.quit()

    with open(output_csv, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Company Name", "Phone Number", "Address"])
        writer.writerows(data)

    return output_csv, data
