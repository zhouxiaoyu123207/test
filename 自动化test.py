#自动化web操作基础
#代码控制浏览器
import selenium
from selenium import  webdriver
import  time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")
driver.refresh()
driver.quit() #关闭浏览器窗口
driver.close()
#元素定位

driver.find_element_by_id("xxx").send_keys("values")
driver.find_element_by_id().send_keys()
#先切換frame框架,如果有多個frame框架
driver.switch_to.frame(1)

driver.find_element_by_xpath("//div[text()=’零售出库’]").click() #xpath定位查詢
driver.find_element_by_id("searchButton").click()
driver.find_element_by_id("name值").click()#id 屬性值查詢
driver.sleep()
# 打印搜搜結果
if "234" in number:
    print()
else:
    print()

#隐式等待
driver.implicitly_wait()
#强制等待
driver.sleep()

def login(username,password,driver):
    driver.find_element_by_id("xxx").send_keys("values")



