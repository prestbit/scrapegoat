from selenium import webdriver

class Website(Object):
    def init(self):
        self.url = "google.com"
        self.category = "search_engine"
        self.webdriver = webdriver.Chrome()

    def init(self, url, category, browser):
        self.url = url
        self.category = url
        if browser.lower() == "firefox":
            self.webdriver = webdriver.Firefox()
        else:
            self.webdriver = webdriver.Chrome()
    def process():
        self.webdriver.get(self.url)


def main():
    w = Website()
    w.process()
    ww = Website("drudgereport.com", "news_agg", "Chrome")
    ww.process()
