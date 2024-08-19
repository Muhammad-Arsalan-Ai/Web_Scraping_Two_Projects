# import csv
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import logging

# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# driver = webdriver.Chrome()

# def allow_all_cookies(driver):
#     try:
#         allow_cookies_button = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"))
#         )
#         allow_cookies_button.click()
#         logging.info("Clicked 'Allow all cookies' button.")
#     except Exception as e:
#         logging.warning("No 'Allow all cookies' button found or could not click it: %s", e)
# try:
#     with open('Cities.csv', 'r') as file:
#         reader = csv.reader(file)
#         next(reader)  # Skip header row
#         for row in reader:
#             postal_code = row[0]
#             try:
#                 # Open the webpage
#                 driver.get("https://www.gassaferegister.co.uk/FindBusinessResults")
#                 logging.info(f"Opened Gas Safe Register website for postal code {postal_code}.")

#                 allow_all_cookies(driver)

#                 postal_code_input = WebDriverWait(driver, 20).until(
#                     EC.presence_of_element_located((By.ID, "postCodeTownlabel"))
#                 )

#                 postal_code_input.clear()
#                 postal_code_input.send_keys(postal_code)
#                 logging.info(f"Entered postal code: {postal_code}")

#                 update_button = WebDriverWait(driver, 20).until(
#                     EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='Update']"))
#                 )
#                 update_button.click()
#                 logging.info("Clicked update button.")

#                 WebDriverWait(driver, 20).until(
#                     EC.url_changes(driver.current_url)
#                 )
#                 current_url = driver.current_url
#                 logging.info(f"Current URL after search: {current_url}")

#                 with open('output2.csv', 'a', newline='') as output_file:
#                     writer = csv.writer(output_file)
#                     writer.writerow([postal_code, current_url])

#                 time.sleep(1)

#             except Exception as e:
#                 logging.error(f"Error processing postal code {postal_code}: {e}")
#                 continue

# finally:
#     driver.quit()
#     logging.info("Closed the WebDriver.")




from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load tokenizer and model (replace with your chosen model)
tokenizer = AutoTokenizer.from_pretrained("facebook/bart-base")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-base")

# Sample documents (replace with your actual data source)
documents = [
    "This is a document about natural language processing (NLP).",
    "This document covers the fundamentals of machine learning (ML).",
]

# User query
question = "What is natural language processing?"

# Simple search function to find relevant documents (replace with a more robust search depending on your data)
def find_relevant_documents(query, documents):
  relevant_docs = []
  for doc in documents:
    if query.lower() in doc.lower():  # Basic keyword search
      relevant_docs.append(doc)
  return relevant_docs

# Find relevant documents based on the query
relevant_docs = find_relevant_documents(question, documents)

# Combine retrieved document content (modify for specific information extraction)
retrieved_text = " ".join(relevant_docs)

# Define a template for the prompt (adapt for your use case)
prompt = f"Answer the following question in detail, considering the provided information:\nQuestion: {question}\nAdditional Information: {retrieved_text}"

# Generate response using the model and prompt
input_ids = tokenizer.encode(prompt, return_tensors="pt")
output = model.generate(input_ids)
answer = tokenizer.decode(output[0], skip_special_tokens=True)

print(f"Answer: {answer}")
