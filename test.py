from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Specify the path to the ChromeDriver executable
chrome_driver_path = "C:\\Users\\91881\\Desktop\\sih\\product development\\chromedriver-win64\\chromedriver.exe"

# Create Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = "C:\\Users\\91881\\Downloads\\ChromeSetup.exe"  # Update with the actual path to Chrome
chrome_options.add_argument("--headless")

# Initialize the Chrome driver with options and the driver path
#driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=chrome_options)

# Define the URL of the webpage to interact with
webpage_url = "https://khaanvaani.streamlit.app/"

# Navigate to the webpage
#chrome_driver_path.get(webpage_url)

# Find the chat input field by tag name (input)
driver.find_element(By.TAG_NAME,'input')

# Start a conversation
chat_input.send_keys("How can I assist you?")
chat_input.send_keys(Keys.RETURN)

# Wait for the chatbot's response (you may need to adjust the wait time)
driver.implicitly_wait(5)

# Capture the chatbot's response by finding a message element
response = driver.find_element_by_class_name("st-dc")
print("Chatbot: " + response.text)

# Continue the conversation (repeat the same pattern for other interactions)

# Close the browser when done
driver.quit()
