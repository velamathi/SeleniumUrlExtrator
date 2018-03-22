from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
binary = FirefoxBinary('/usr/bin/firefox')
from selenium import webdriver

class UrlExtracter():
    url='https://github.com'
    def __init__(self, repo_name="pers1"):
        self.browser = webdriver.Firefox(firefox_binary=binary)

    def process(self):
        urls = dict()
        self.browser.get(UrlExtracter.url)
        self.browser.find_elements_by_xpath('/html/body/div[1]/header/div/div[2]/div/span/div/a[1]')[0]\
                    .click()
        self.browser.find_elements_by_xpath('//*[@id="login_field"]')
        login_field = self.browser.find_elements_by_xpath('//*[@id="login_field"]')
        login_field[0].send_keys('xxx@gmail.com')
        password_field = self.browser.find_elements_by_xpath('//*[@id="password"]')[0]
        password_field.send_keys('xxxx')
        self.browser.find_elements_by_xpath('//*[@id="login"]/form/div[3]/input[3]')[0].click()
        self.browser.find_elements_by_xpath('//*[@id="your_repos"]/div/div[2]/ul/li[1]/a')[0].click()
        for file in self.browser.find_elements_by_xpath('//tr[@class="js-navigation-item"]//td[@class="content"]//span//a'):
            urls[file.text]=file.get_attribute('href')
        print (" Found {0} links in the repo".format(len(urls)))

        return urls


test= UrlExtracter('adb')
values = test.process()
print (values)



