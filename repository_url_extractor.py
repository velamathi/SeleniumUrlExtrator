from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
binary = FirefoxBinary('/usr/bin/firefox')
from selenium import webdriver


class UrlExtracter():
    # Webpage that is used to extract link
    url='https://github.com'

    def __init__(self, repo_name="pers1"):
        self.browser = webdriver.Firefox(firefox_binary=binary)
        self.repo_name = repo_name

    def process(self):
        # Creating dictionary to save all the files and their links
        urls = dict()
        # Opening the browser for the given URL
        self.browser.get(UrlExtracter.url)

        # navigating to the Sign in Page
        self.browser.find_elements_by_xpath('/html/body/div[1]/header/div/div[2]/div/span/div/a[1]')[0]\
                    .click()
        # Navigating to the Login field in the page using Xpath
        self.browser.find_elements_by_xpath('//*[@id="login_field"]')
        login_field = self.browser.find_elements_by_xpath('//*[@id="login_field"]')
        # Passing the login id to the password_field.
        login_field[0].send_keys('xxxxx@gmail.com')
        # Navigating to the Password field in the webpage
        password_field = self.browser.find_elements_by_xpath('//*[@id="password"]')[0]
        # Passing the password value to the password field
        password_field.send_keys('xxxxx')
        self.browser.find_elements_by_xpath('//*[@id="login"]/form/div[3]/input[3]')[0].click()

        # Generating the repo xpath dynamically from the repo name
        repo_xpath = '//li[@class="public source"]//*[contains(text(),"{0}")]'.format(self.repo_name)

        # Navigating to the Repo webpage
        self.browser.find_elements_by_xpath(repo_xpath)[0].click()
        # Going through all the files and extracting the href link
        # and saving them to the urls dictionary
        for file in self.browser.find_elements_by_xpath('//span[@class="css-truncate css-truncate-target"]//a'):
            urls[file.text]=file.get_attribute('href')

        print (" Found {0} links in the repo".format(len(urls)))
        return urls



if __name__ == "__main__":
    test= UrlExtracter('fast')
    values = test.process()
    print (values)



