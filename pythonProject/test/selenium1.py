from selenium import webdriver

if __name__ == '__main__':
    # 是大写的Chrome
    driver = webdriver.Chrome()
    driver.get("http://www.santostang.com/2018/07/04/hello-world/")