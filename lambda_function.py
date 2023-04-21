from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Downloader:
    def __init__(self, url):
        self.driver = None
        self.url = url
        self.wait = None

    def get_driver(self):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-gpu-compositing')
        chrome_options.add_argument('--disable-sync')
        chrome_options.add_argument('--disable-translate')
        chrome_options.add_argument('--disable-web-security')
        chrome_options.add_argument('--disable-web-autofill')
        chrome_options.add_argument('--disable-web-share')
        chrome_options.add_argument('--disable-web-updates')
        chrome_options.add_argument("enable-automation")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument('--disable-sync-autoupdate')
        chrome_options.add_argument('--disable-sync-autoupdate-service')
        chrome_options.add_argument('--disable-sync-autoupdate-service-on-startup')

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(5)
        self.wait = WebDriverWait(self.driver, 10)

        chrome_options.add_experimental_option("prefs", prefs)

    def saveFromNet(self):
        print("saveFromNet")
        self.get_driver()
        self.driver.get("https://en.savefrom.net/")

        self.driver.find_element(By.ID, "sf_url").send_keys(self.url)
        self.driver.find_element(By.ID, "sf_submit").click()

        try:
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".link-download.download-icon")))
        except TimeoutException:
            raise Exception("Timeout waiting for download button")

        try:
            download_elem = self.driver.find_element(By.CSS_SELECTOR, ".link-download.download-icon")
            content_url = download_elem.get_attribute("href")

            return content_url

        except NoSuchElementException:
            raise Exception("Error finding download button")

    def snapSave(self):
        print("snapSave")
        self.get_driver()
        self.driver.get("https://snapsave.app/")

        self.driver.find_element(By.ID, "url").send_keys(self.url)
        self.driver.find_element(By.ID, "send").click()

        try:
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button.is-success")))
        except TimeoutException:
            raise Exception("Timeout waiting for download button")

        try:
            if "facebook" in self.url:
                download_elem = self.driver.find_element(By.XPATH, "//a[@title='Download HD']")
                content_url = download_elem.get_attribute("href")
            else:
                download_elem = self.driver.find_element(By.CSS_SELECTOR, ".button.is-success")
                content_url = download_elem.get_attribute("href")

            return content_url

        except NoSuchElementException:
            raise Exception("Error finding download button")

    def saveTikCo(self):
        print("saveTikCo")
        self.get_driver()
        self.driver.get("https://savetik.co/en")

        self.driver.find_element(By.ID, "s_input").send_keys(self.url)
        self.driver.find_element(By.CLASS_NAME, "btn-red").click()

        try:
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".tik-button-dl.button.dl-success")))
        except TimeoutException:
            raise Exception("Timeout waiting for download button")

        try:
            download_elem = self.driver.find_element(By.CSS_SELECTOR, ".tik-button-dl.button.dl-success")
            content_url = download_elem.get_attribute("href")

            return content_url

        except NoSuchElementException:
            raise Exception("Error finding download button")

    def tiktokDownloadOnline(self):
        print("tiktokDownloadOnline")
        self.get_driver()
        self.driver.get("https://tiktokdownload.online/")

        self.driver.find_element(By.ID, "main_page_text").send_keys(self.url)
        self.driver.find_element(By.ID, "submit").click()

        try:
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".without_watermark.download_link")))
        except TimeoutException:
            raise Exception("Timeout waiting for download button")

        try:
            download_elem = self.driver.find_element(By.CSS_SELECTOR, ".without_watermark.download_link")
            content_url = download_elem.get_attribute("href")

            return content_url

        except NoSuchElementException:
            raise Exception("Error finding download button")

    def pinterestDownloader(self):
        print("pinterestDownloader")
        self.get_driver()
        self.driver.get("https://pinterestdownloader.com/")

        self.driver.find_element(By.ID, "download_input").send_keys(self.url)
        self.driver.find_element(By.ID, "download_button").click()

        try:
            self.wait.until(EC.element_to_be_clickable((By.ID, "video_down")))
        except TimeoutException:
            raise Exception("Timeout waiting for download button")

        try:
            download_elem = self.driver.find_element(By.ID, "video_down")
            content_url = download_elem.get_attribute("href")

            return content_url

        except NoSuchElementException:
            raise Exception("Error finding download button")


# def lambda_handler(event, context):

#     # parsing query string params
#     # url = event['queryStringParameters']['url']
#     url = event['url']
#     # url = "https://www.facebook.com/watch?v=324199376484038"

#     download_inst = Downloader(url)
#     download_options = [download_inst.saveFromNet]

#     if 'facebook' in url or 'instagram' in url:
#         download_options.append(download_inst.snapSave)
#     elif 'tiktok' in url:
#         download_options.extend([download_inst.saveTikCo, download_inst.tiktokDownloadOnline, download_inst.snapSave])
#     elif 'pinterest' in url:
#         download_options.append(download_inst.pinterestDownloader)
#     elif 'twitter' in url:
#         pass

#     final_choice = random.choice(download_options)
#     content = final_choice()

#     # construct the body of the response object
#     dlResponse = {}
#     dlResponse['content'] = content

#     # Construct http response object
#     responseObj = {}
#     responseObj['statusCode'] = 200
#     responseObj['body'] = json.dumps(dlResponse)

#     # return the response object
#     return {
#         'statusCode':200,
#         'body': responseObj
    # }


url = "https://www.facebook.com/watch?v=324199376484038"
dl = Downloader(url)
dl.saveFromNet()
