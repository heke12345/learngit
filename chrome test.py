from selenium import webdriver
opt = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=opt)  # 创建浏览器对象
driver.get('https://job.alibaba.com/zhaopin/positionList')
