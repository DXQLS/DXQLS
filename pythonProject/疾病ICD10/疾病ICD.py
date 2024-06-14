import time

import pandas as pd
from selenium import webdriver
import pandas as ps
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
url = 'https://code.nhsa.gov.cn/jbzd/public/dataWesterSearch.html?batchNumber=https://code.nhsa.gov.cn/'
# 在循环之前创建WebDriverWait对象
wait = WebDriverWait(driver, 2)
driver.get(url)
time.sleep(1)
script = 'arguments[0].style.display = "block";'
result = driver.find_elements(By.XPATH, '//*[@id="treeDemo1"]/li/span')
for index, drvier_son in enumerate(result):
    # 点开最外层
    if index != 0:
        drvier_son.click()
    time.sleep(1)
    # 获取每一大章节中的小节
    data = drvier_son.find_elements(By.XPATH, '//*[@id="treeDemo1_' + f'{index + 1}' + '_ul"]/li/span')
    all_data = drvier_son.find_elements(By.XPATH, '//*[@id="treeDemo1_' + f'{index + 1}' + '_ul"]/li')

    # data = drvier_son.find_elements(By.XPATH, '//*[@id="treeDemo1_23_ul"]/li/span')
    # all_data = drvier_son.find_elements(By.XPATH, '//*[@id="treeDemo1_23_ul"]/li')
    for index_2, drvier_son_2 in enumerate(data):
        time.sleep(1)
        drvier_son_2.click()
        time.sleep(1)
        try:
            drvier_child = all_data[index_2].find_elements(By.XPATH, './ul[@class="level1 line"]/li')
            for child in drvier_child:
                time.sleep(1)
                child.click()
                wait.until(EC.frame_to_be_available_and_switch_to_it("ICDMainframe"))
                time.sleep(1)
                # 现在可以在iframe内执行操作，比如查找元素
                elements = driver.find_elements(By.XPATH, '//*[@class="els-doc-con"]')
                # print(44444,elements)
                for element in elements:
                    driver.execute_script(script, element)
                # 执行JavaScript脚本获取页面上所有元素的文本内容
                text = driver.execute_script("return document.body.innerText")
                with open('data.txt', mode='a', encoding='utf-8') as f:
                    f.write(text + '\n')
                print(text)
                # 切回主页面
                driver.switch_to.default_content()
        except:
            print('没有数据')
