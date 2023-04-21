from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from flask import Flask, request

app = Flask(__name__)

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

@app.route('/')
def main():
    driver.get("https://www.google.com/")
    title = driver.title
    print(title)

if __name__ == '__main__':
    app.run(host="0.0.0.0")