# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# # Define the base URL
# base_url = "http://www.stealmyrolodex.com/viewPeople/"

# # Define the range of URLs to scrape
# start_id = 1
# end_id = 10  # Adjust the range as needed

# # List to store the scraped data
# data = []

# # Function to extract data from the HTML content
# def extract_data(soup):
#     person_data = {}
#     person_data["Name"] = soup.find("input", {"id": "name"}).get("value", "").strip()
#     person_data["Address"] = soup.find("input", {"id": "address"}).get("value", "").strip()
#     person_data["Email"] = soup.find("input", {"id": "email"}).get("value", "").strip()
#     person_data["Secondary Email"] = soup.find("input", {"id": "secondemail"}).get("value", "").strip()
#     person_data["Phone"] = soup.find("input", {"id": "phone"}).get("value", "").strip()
#     person_data["Role"] = soup.find("input", {"id": "role"}).get("value", "").strip()

#     # person_data["Company"] = soup.find_all("input", {"class": "form-control"})[3].get("value", "").strip()
#     # person_data["Company Address"] = soup.find_all("input", {"class": "form-control"})[5].get("value", "").strip()
#     # person_data["Category"] = soup.find_all("input", {"class": "form-control"})[4].get("value", "").strip()
    
#     company_section = soup.find("div", {"class": "card card-secondary"})
#     company_inputs = company_section.find_all("input", {"class": "form-control"})

#     person_data["Company"] = company_inputs[0].get("value", "").strip() if len(company_inputs) > 0 else ""
#     person_data["Category"] = company_inputs[1].get("value", "").strip() if len(company_inputs) > 1 else ""
#     person_data["Company Address"] = company_inputs[2].get("value", "").strip() if len(company_inputs) > 2 else ""




#     person_data["Linkedin Name"] = soup.find_all("input", {"class": "form-control"})[7].get("value", "").strip()
#     person_data["Linkedin Connections"] = soup.find_all("input", {"class": "form-control"})[8].get("value", "").strip()
#     person_data["Decision Maker"] = soup.find_all("input", {"class": "form-control"})[10].get("value", "").strip()
    
#     return person_data





# # Loop through the range of URLs
# for person_id in range(start_id, end_id + 1):
#     url = base_url + str(person_id)
#     response = requests.get(url)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.content, "html.parser")
#         person_data = extract_data(soup)
#         data.append(person_data)
#     else:
#         print(f"Failed to retrieve data for ID {person_id}")

# # Create a DataFrame from the scraped data
# df = pd.DataFrame(data)
# print(df)
# # # Save the DataFrame to a CSV file
# df.to_csv("scraped_data.csv", index=False)

# print("Data scraping completed and saved to scraped_data.csv")






import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the base URL
base_url = "http://www.stealmyrolodex.com/viewPeople/"

# Start from ID 1
start_id = 1

# Loop until no data is found on the page
while True:
    url = base_url + str(start_id)
    response = requests.get(url)
    
    # If response status is not OK, break the loop
    if response.status_code != 200:
        break
    
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Extract data for the current person
    person_data = {}
    try:
        person_data["Name"] = soup.find("input", {"id": "name"}).get("value", "").strip()
        person_data["Address"] = soup.find("input", {"id": "address"}).get("value", "").strip()
        person_data["Email"] = soup.find("input", {"id": "email"}).get("value", "").strip()
        person_data["Secondary Email"] = soup.find("input", {"id": "secondemail"}).get("value", "").strip()
        person_data["Phone"] = soup.find("input", {"id": "phone"}).get("value", "").strip()
        person_data["Role"] = soup.find("input", {"id": "role"}).get("value", "").strip()
        
        # Extract company details
        company_section = soup.find("div", {"class": "card card-secondary"})
        company_inputs = company_section.find_all("input", {"class": "form-control"})
        person_data["Company"] = company_inputs[0].get("value", "").strip() if len(company_inputs) > 0 else ""
        person_data["Category"] = company_inputs[1].get("value", "").strip() if len(company_inputs) > 1 else ""
        person_data["Company Address"] = company_inputs[2].get("value", "").strip() if len(company_inputs) > 2 else ""
        
        person_data["Linkedin Name"] = soup.find_all("input", {"class": "form-control"})[7].get("value", "").strip()
        person_data["Linkedin Connections"] = soup.find_all("input", {"class": "form-control"})[8].get("value", "").strip()
        person_data["Decision Maker"] = soup.find_all("input", {"class": "form-control"})[10].get("value", "").strip()
        
        # Check if any of the values are unwanted
        unwanted_values = ['<div style=']
        if any(value in person_data.values() for value in unwanted_values):
            raise AttributeError("Unwanted values found.")
        
        # Create a DataFrame from the person's data
        df = pd.DataFrame([person_data])
        
        # Save the DataFrame to a CSV file
        if start_id == 1:
            df.to_csv("scraped_data1.csv", index=False, encoding='utf-8-sig')
        else:
            with open("scraped_data1.csv", "a", encoding='utf-8-sig') as f:
                df.to_csv(f, index=False, header=False, encoding='utf-8-sig')
    except AttributeError:
        print(f"No data found for ID {start_id}. Moving to the next page.")
    
    # Move to the next ID
    start_id += 1

print("Data scraping completed and saved to scraped_data1.csv")

# ////////////


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # Initialize the WebDriver (Make sure the WebDriver executable is in your PATH or provide the executable path)
# driver = webdriver.Chrome()

# try:
#     # Open the webpage
#     driver.get("https://www.gassaferegister.co.uk/FindBusinessResults")

#     # Locate the postal code input box
#     postal_code_input = driver.find_element(By.ID, "postCodeTownlabel")

#     # Clear the input box and enter the new postal code
#     postal_code_input.clear()
#     postal_code_input.send_keys("NEW_POSTAL_CODE")

#     # Locate and click the update button
#     update_button = driver.find_element(By.ID, "update_button_id")
#     update_button.click()

#     # Wait for the new page to load
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "some_element_on_new_page")))

#     # Get the current URL
#     current_url = driver.current_url
#     print("Current URL:", current_url)

# finally:
#     # Close the WebDriver
#     driver.quit()





# import csv
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # Initialize the WebDriver (Make sure the WebDriver executable is in your PATH or provide the executable path)
# driver = webdriver.Chrome()

# try:
#     with open('Scotland postcodes.csv', 'r') as file:
#         reader = csv.reader(file)
#         next(reader)  # Skip header row
#         for row in reader:
#             postal_code = row[0]
#             # Open the webpage
#             driver.get("https://www.gassaferegister.co.uk/FindBusinessResults")

#             # Wait for the postal code input box to be present
#             postal_code_input = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.ID, "postCodeTownlabel"))
#             )

#             # Clear the input box and enter the new postal code
#             postal_code_input.clear()
#             postal_code_input.send_keys(postal_code)

#             # Locate and click the update button (adjust the ID if needed)
#             update_button = WebDriverWait(driver, 10).until(
#                 EC.element_to_be_clickable((By.ID, "update_button_id"))
#             )
#             update_button.click()

#             # Wait for the new page to load and locate an element on the new page
#             WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.ID, "some_element_on_new_page"))
#             )

#             # Get the current URL
#             current_url = driver.current_url
#             print("Current URL:", current_url)

#             # Store the URL in the CSV file
#             with open('output.csv', 'a', newline='') as output_file:
#                 writer = csv.writer(output_file)
#                 writer.writerow([postal_code, current_url])

#             # Add some delay before processing the next postal code
#             time.sleep(1)

# finally:
#     # Close the WebDriver
#     driver.quit()




# import csv
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # Initialize the WebDriver (Make sure the WebDriver executable is in your PATH or provide the executable path)
# driver = webdriver.Chrome()

# try:
#     with open('Scotland postcodes.csv', 'r') as file:
#         reader = csv.reader(file)
#         next(reader)  # Skip header row
#         for row in reader:
#             postal_code = row[0]
#             # Open the webpage
#             driver.get("https://www.gassaferegister.co.uk/FindBusinessResults")

#             # Wait for the postal code input box to be present
#             postal_code_input = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.ID, "postCodeTownlabel"))
#             )

#             # Clear the input box and enter the new postal code
#             postal_code_input.clear()
#             postal_code_input.send_keys(postal_code)

#             # Locate and click the update button using the data-testid attribute
#             update_button = WebDriverWait(driver, 10).until(
#                 EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='Update']"))
#             )
#             update_button.click()

#             # Wait for the new page to load and locate an element on the new page
#             WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='pgFirst']"))
#             )

#             # # Extract all href attributes from the specified <a> tags
#             href_elements = driver.find_elements(By.CSS_SELECTOR, "a[data-testid='pgFirst']")
#             hrefs = [element.get_attribute('href') for element in href_elements]
#             print("Extracted hrefs:", hrefs)
#             # current_url = driver.current_url
#             # print("Current URL:", current_url)
            
#             # Store the postal code and hrefs in the CSV file
#             with open('output.csv', 'a', newline='') as output_file:
#                 writer = csv.writer(output_file)
#                 for href in hrefs:
#                     writer.writerow([postal_code, href])

#             # Add some delay before processing the next postal code
#             time.sleep(1)

# finally:
#     # Close the WebDriver
#     driver.quit()

# //////////

# import csv
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # Initialize the WebDriver (Make sure the WebDriver executable is in your PATH or provide the executable path)
# driver = webdriver.Chrome()

# def close_popup(driver):
#     try:
#         popup = WebDriverWait(driver, 5).until(
#             EC.element_to_be_clickable((By.CSS_SELECTOR, ".chat-activate-wrapper"))
#         )
#         driver.execute_script("arguments[0].style.display = 'none';", popup)
#     except Exception as e:
#         # If no popup is found, just pass
#         pass

# try:
#     with open('Scotland postcodes.csv', 'r') as file:
#         reader = csv.reader(file)
#         next(reader)  # Skip header row
#         for row in reader:
#             postal_code = row[0]
#             try:
#                 # Open the webpage
#                 driver.get("https://www.gassaferegister.co.uk/FindBusinessResults")

#                 # Wait for the postal code input box to be present
#                 postal_code_input = WebDriverWait(driver, 10).until(
#                     EC.presence_of_element_located((By.ID, "postCodeTownlabel"))
#                 )

#                 # Clear the input box and enter the new postal code
#                 postal_code_input.clear()
#                 postal_code_input.send_keys(postal_code)

#                 # Close any potential pop-up that might be blocking the button
#                 close_popup(driver)

#                 # Locate and click the update button using the data-testid attribute
#                 update_button = WebDriverWait(driver, 10).until(
#                     EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='Update']"))
#                 )
#                 update_button.click()

#                 # Wait for the new page to load and locate an element on the new page
#                 WebDriverWait(driver, 10).until(
#                     EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='pgFirst']"))
#                 )

#                 # Extract all href attributes from the specified <a> tags
#                 href_elements = driver.find_elements(By.CSS_SELECTOR, "a[data-testid='pgFirst']")
#                 hrefs = [element.get_attribute('href') for element in href_elements]
#                 print("Extracted hrefs:", hrefs)

#                 # Store the postal code and hrefs in the CSV file
#                 with open('output.csv', 'a', newline='') as output_file:
#                     writer = csv.writer(output_file)
#                     for href in hrefs:
#                         writer.writerow([postal_code, href])

#                 # Add some delay before processing the next postal code
#                 time.sleep(1)

#             except Exception as e:
#                 print(f"Error processing postal code {postal_code}: {e}")
#                 continue

# finally:
#     # Close the WebDriver
#     driver.quit()


# ////// selenium code 



# import csv
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # Initialize the WebDriver (Make sure the WebDriver executable is in your PATH or provide the executable path)
# driver = webdriver.Chrome()

# def close_popup(driver):
#     try:
#         popup = WebDriverWait(driver, 5).until(
#             EC.element_to_be_clickable((By.CSS_SELECTOR, ".chat-activate-wrapper"))
#         )
#         driver.execute_script("arguments[0].style.display = 'none';", popup)
#     except Exception as e:
#         # If no popup is found, just pass
#         pass

# def check_for_captcha(driver):
#     try:
#         captcha = WebDriverWait(driver, 5).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, ".captcha"))
#         )
#         if captcha:
#             input("CAPTCHA detected. Please solve it manually and press Enter to continue...")
#     except Exception as e:
#         # No CAPTCHA found
#         pass

# try:
#     with open('Scotland postcodes.csv', 'r') as file:
#         reader = csv.reader(file)
#         next(reader)  # Skip header row
#         for row in reader:
#             postal_code = row[0]
#             try:
#                 # Open the webpage
#                 driver.get("https://www.gassaferegister.co.uk/FindBusinessResults")

#                 # Wait for the postal code input box to be present
#                 postal_code_input = WebDriverWait(driver, 10).until(
#                     EC.presence_of_element_located((By.ID, "postCodeTownlabel"))
#                 )

#                 # Clear the input box and enter the new postal code
#                 postal_code_input.clear()
#                 postal_code_input.send_keys(postal_code)

#                 # Close any potential pop-up that might be blocking the button
#                 close_popup(driver)

#                 # Locate and click the update button using the data-testid attribute
#                 update_button = WebDriverWait(driver, 10).until(
#                     EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='Update']"))
#                 )
#                 update_button.click()

#                 # Check for CAPTCHA and prompt for manual resolution if detected
#                 check_for_captcha(driver)

#                 # Wait for the new page to load and locate an element on the new page
#                 WebDriverWait(driver, 10).until(
#                     EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='pgFirst']"))
#                 )

#                 # Extract all href attributes from the specified <a> tags
#                 href_elements = driver.find_elements(By.CSS_SELECTOR, "a[data-testid='pgFirst']")
#                 hrefs = [element.get_attribute('href') for element in href_elements]
#                 print("Extracted hrefs:", hrefs)

#                 # Store the postal code and hrefs in the CSV file
#                 with open('output.csv', 'a', newline='') as output_file:
#                     writer = csv.writer(output_file)
#                     for href in hrefs:
#                         writer.writerow([postal_code, href])

#                 # Add some delay before processing the next postal code
#                 time.sleep(1)

#             except Exception as e:
#                 print(f"Error processing postal code {postal_code}: {e}")
#                 continue

# finally:
#     # Close the WebDriver
#     driver.quit()



# import csv
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # Initialize the WebDriver (Make sure the WebDriver executable is in your PATH or provide the executable path)
# driver = webdriver.Chrome()

# def close_popup(driver):
#     try:
#         popup = WebDriverWait(driver, 5).until(
#             EC.element_to_be_clickable((By.CSS_SELECTOR, ".chat-activate-wrapper"))
#         )
#         driver.execute_script("arguments[0].style.display = 'none';", popup)
#     except Exception as e:
#         print("No popup found or could not close popup:", e)
#         pass

# def check_for_captcha(driver):
#     try:
#         captcha = WebDriverWait(driver, 5).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, ".captcha"))
#         )
#         if captcha:
#             input("CAPTCHA detected. Please solve it manually and press Enter to continue...")
#     except Exception as e:
#         # No CAPTCHA found
#         pass

# try:
#     with open('Scotland postcodes.csv', 'r') as file:
#         reader = csv.reader(file)
#         next(reader)  # Skip header row
#         for row in reader:
#             postal_code = row[0]
#             try:
#                 # Open the webpage
#                 driver.get("https://www.gassaferegister.co.uk/FindBusinessResults")

#                 # Wait for the postal code input box to be present
#                 postal_code_input = WebDriverWait(driver, 10).until(
#                     EC.presence_of_element_located((By.ID, "postCodeTownlabel"))
#                 )

#                 # Clear the input box and enter the new postal code
#                 postal_code_input.clear()
#                 postal_code_input.send_keys(postal_code)

#                 # Close any potential pop-up that might be blocking the button
#                 close_popup(driver)

#                 # Locate and click the update button using the data-testid attribute
#                 update_button = WebDriverWait(driver, 10).until(
#                     EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='Update']"))
#                 )
#                 update_button.click()

#                 # Check for CAPTCHA and prompt for manual resolution if detected
#                 check_for_captcha(driver)

#                 # Wait for the new page to load and locate an element on the new page
#                 WebDriverWait(driver, 10).until(
#                     EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='pgFirst']"))
#                 )

#                 # Extract all href attributes from the specified <a> tags
#                 href_elements = driver.find_elements(By.CSS_SELECTOR, "a[data-testid='pgFirst']")
#                 hrefs = [element.get_attribute('href') for element in href_elements]

#                 # Debug print the hrefs and the current URL to verify correctness
#                 # print(f"Postal code: {postal_code}")
#                 # print("Extracted hrefs:", hrefs)
#                 current_url = driver.current_url
#                 print("Current URL after search:", current_url)

#                 # Store the postal code and hrefs in the CSV file
#                 with open('output.csv', 'a', newline='') as output_file:
#                     writer = csv.writer(output_file)
#                     # for current_urls in current_url:
#                     writer.writerow([postal_code, current_url])

#                 # Add some delay before processing the next postal code
#                 time.sleep(1)

#             except Exception as e:
#                 print(f"Error processing postal code {postal_code}: {e}")
#                 continue

# finally:
#     # Close the WebDriver
#     driver.quit()






# import csv
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import logging

# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# driver = webdriver.Chrome()

# # def close_popup(driver):
# #     try:
# #         popup = WebDriverWait(driver, 5).until(
# #             EC.element_to_be_clickable((By.CSS_SELECTOR, ".chat-activate-wrapper"))
# #         )
# #         driver.execute_script("arguments[0].style.display = 'none';", popup)
# #     except Exception as e:
# #         print("No popup found or could not close popup:", e)
# #         pass

# # def check_for_captcha(driver):
# #     try:
# #         captcha = WebDriverWait(driver, 5).until(
# #             EC.presence_of_element_located((By.CSS_SELECTOR, ".captcha"))
# #         )
# #         if captcha:
# #             input("CAPTCHA detected. Please solve it manually and press Enter to continue...")
# #             return True
# #     except Exception as e:
# #         # No CAPTCHA found
# #         pass
# #     return False

# def allow_all_cookies(driver):
#     try:
#         allow_cookies_button = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"))
#         )
#         allow_cookies_button.click()
#         logging.info("Clicked 'Allow all cookies' button.")
#     except Exception as e:
#         logging.warning("No 'Allow all cookies' button found or could not click it: %s", e)
#         pass

# try:
#     with open('Scotland postcodes.csv', 'r') as file:
#         reader = csv.reader(file)
#         next(reader)  # Skip header row
#         for row in reader:
#             postal_code = row[0]
#             try:
#                 # Open the webpage
#                 driver.get("https://www.gassaferegister.co.uk/FindBusinessResults")

#                 allow_all_cookies(driver)

#                 # Wait for the postal code input box to be present
#                 postal_code_input = WebDriverWait(driver, 10).until(
#                     EC.presence_of_element_located((By.ID, "postCodeTownlabel"))
#                 )

#                 # Clear the input box and enter the new postal code
#                 postal_code_input.clear()
#                 postal_code_input.send_keys(postal_code)

#                 # Close any potential pop-up that might be blocking the button
#                 # close_popup(driver)

#                 # Locate and click the update button using the data-testid attribute
#                 update_button = WebDriverWait(driver, 10).until(
#                     EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='Update']"))
#                 )
#                 update_button.click()

#                 # Check for CAPTCHA and prompt for manual resolution if detected
#                 # captcha_present = check_for_captcha(driver)

#                 # Extract the current URL after submitting the postal code
#                 current_url = driver.current_url
#                 print("Current URL after search:", current_url)

#                 # Store the postal code and current URL in the CSV file
#                 with open('output1.csv', 'a', newline='') as output_file:
#                     writer = csv.writer(output_file)
#                     writer.writerow([postal_code, current_url])

#                 # If CAPTCHA was present, prompt the user to solve it and continue
#                 # if captcha_present:
#                 #     input("CAPTCHA resolved. Press Enter to continue...")

#                 # Add some delay before processing the next postal code
#                 time.sleep(1)

#             except Exception as e:
#                 print(f"Error processing postal code {postal_code}: {e}")
#                 continue

# finally:
#     # Close the WebDriver
#     driver.quit()





# import csv
# import time
# import logging
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # Setup logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# # Initialize the WebDriver
# driver = webdriver.Chrome()

# def close_popup(driver):
#     try:
#         popup = WebDriverWait(driver, 5).until(
#             EC.element_to_be_clickable((By.CSS_SELECTOR, ".chat-activate-wrapper"))
#         )
#         driver.execute_script("arguments[0].style.display = 'none';", popup)
#     except Exception as e:
#         logging.warning("No popup found or could not close popup: %s", e)
#         pass

# def allow_all_cookies(driver):
#     try:
#         allow_cookies_button = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"))
#         )
#         allow_cookies_button.click()
#         logging.info("Clicked 'Allow all cookies' button.")
#     except Exception as e:
#         logging.warning("No 'Allow all cookies' button found or could not click it: %s", e)
#         pass

# try:
#     with open('Scotland postcodes.csv', 'r') as file:
#         reader = csv.reader(file)
#         next(reader)  # Skip header row
#         for row in reader:
#             postal_code = row[0]
#             try:
#                 driver.get("https://www.gassaferegister.co.uk/FindBusinessResults")
#                 logging.info("Opened Gas Safe Register website.")

#                 # Allow all cookies if the button is present
#                 allow_all_cookies(driver)

#                 postal_code_input = WebDriverWait(driver, 10).until(
#                     EC.presence_of_element_located((By.ID, "postCodeTownlabel"))
#                 )

#                 postal_code_input.clear()
#                 postal_code_input.send_keys(postal_code)
#                 logging.info("Entered postal code: %s", postal_code)

#                 close_popup(driver)

#                 update_button = WebDriverWait(driver, 10).until(
#                     EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='Update']"))
#                 )
#                 update_button.click()
#                 logging.info("Clicked update button.")

#                 current_url = driver.current_url
#                 logging.info("Current URL after search: %s", current_url)

#                 with open('output1.csv', 'a', newline='') as output_file:
#                     writer = csv.writer(output_file)
#                     writer.writerow([postal_code, current_url])

#                 time.sleep(1)

#             except Exception as e:
#                 logging.error("Error processing postal code %s: %s", postal_code, e)
#                 continue

# finally:
#     driver.quit()
#     logging.info("Closed the WebDriver.")











