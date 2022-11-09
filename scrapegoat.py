from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.chrome.options import Options

# configure the webdriver to run headless
options = Options()
options.headless = True # hide GUI
options.add_argument("--window-size=1920,1080") # set window size to native GUI size
options.add_argument("start-maximized") # ensure window is full-screen

...
#driver = webdriver.Chrome(options=options)

driver.get("path_to_data_source")