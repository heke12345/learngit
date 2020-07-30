import re
import time
from selenium import webdriver
import requests  # 导入requests包
# url = 'https://job.alibaba.com/zhaopin/positionList'
# strhtml = requests.get(url)  # Get方式获取网页数据
# print(strhtml.text)


opt = webdriver.ChromeOptions()  # 创建浏览器
# opt.set_headless()                            #无窗口模式
driver = webdriver.Chrome(options=opt)  # 创建浏览器对象
driver.get('https://job.alibaba.com/zhaopin/positionList')  # 打开网页
# driver.maximize_window()                      #最大化窗口
time.sleep(2)  # 加载等待

driver.find_element_by_xpath(
    "./*//span[@class='bg s_ipt_wr quickdelete-wrap']/input").send_keys("云存储")  # 利用xpath查找元素进行输入文本
strhtml = requests.get(url)  # Get方式获取网页数据
print(strhtml.text)
