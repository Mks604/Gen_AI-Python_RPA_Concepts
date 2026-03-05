RPA Automation using Selenium
📌 Overview

This project demonstrates Robotic Process Automation (RPA) using Python and Selenium WebDriver.

Selenium is a widely used open-source automation framework that allows developers to automate interactions with web browsers. It simulates real user actions such as clicking buttons, entering text, navigating pages, and extracting information from websites.

The purpose of this project is to automate browser-based tasks using Selenium and Python.

🚀 Features

Automates web browser interactions

Supports automated form filling

Simulates user actions such as:

Clicking buttons

Entering text

Navigating pages

Extracts information from websites

Helps reduce repetitive manual work

🛠️ Technologies Used

Python 3

Selenium WebDriver

Chrome WebDriver

Selenium WebDriver allows programs to control a browser and automate testing or web workflows programmatically.

📂 Project Structure
RPA_selenium/
│
├── automation_script.py
├── requirements.txt
└── README.md
⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/Mks604/Gen_AI-Week_1.git
2️⃣ Navigate to the Project Folder
cd Gen_AI-Week_1/RPA_selenium
3️⃣ Install Dependencies
pip install selenium
4️⃣ Download ChromeDriver

Download the compatible version of ChromeDriver and add it to your system path.

▶️ Usage

Run the Selenium automation script:

python automation_script.py

Example Selenium Script:

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.google.com")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Automation")

search_box.submit()

driver.quit()
📸 Example Use Cases

Automating login to websites

Automated testing of web applications

Web scraping and data extraction

Repetitive browser tasks automation

⚠️ Notes

Ensure ChromeDriver version matches your Chrome browser version.

Avoid running automation scripts too fast; add delays if needed.

Website UI changes may break element locators.



📜 License

This project is open-source and available under the MIT License.
