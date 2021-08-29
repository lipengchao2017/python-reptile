from selenium import webdriver
import time

if __name__ == '__main__':
    driver = webdriver.Chrome()
    # 隐性等待 最长20秒
    driver.implicitly_wait(20)
    driver.get("http://www.santostang.com/2018/07/04/hello-world/")
    time.sleep(5)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    for i in range(3):
        # 下滑到页面底部
        driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere-comment']"))
        load_more = driver.find_elements_by_css_selector('button.page-btn ')[i]
        load_more.click()
        print('Click and waiting loading --- please waiting for 8 s')
        driver.switch_to.default_content()
        time.sleep(8)  # 点击后需要等待，否则评论还没加载出来，数据抓取的代码已经跑完了，结果就是没抓到数据，而代码会正常的在运行

        driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere-comment']"))
        comment = driver.find_elements_by_css_selector('div.reply-content')
        for eachcomment in comment:
            content = eachcomment.find_element_by_tag_name('p')
            print(content.text)
        driver.switch_to.default_content()  # 执行页面滑动的脚本需要将driver转换到正常的模式
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        time.sleep(4)
        # if i > 11:
        #     x_path = './/div[@class="more-wrapper"]/button[' + str(i - 9) + ']'
        # else:
        #     x_path = './/div[@class="more-wrapper"]/button[' + str(i) + ']'
        # click_btn = driver.find_element_by_xpath(x_path)
        # click_btn = driver.find_element_by_css_selector('button.page-btn')
        # click_btn.send_keys("Tab")  # 点击前先按下Tab（其他键也可以考虑），可以解决因跳转点击时出现失去焦点而导致的click单击无效的情况
        # click_btn.click()
        # 应该是正则定位
