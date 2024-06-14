import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

list_01, list_02, list_03, list_04, list_05, list_06, list_07, list_08, list_09, list_10, list_11, list_12 = [], [], [], [], [], [], [], [], [], [], [], []


def extract_data():
    # 找到表格的tbody
    tbody = driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[2]/div[1]/div[3]/div[3]/div/div[2]/section/div/div/div[2]/div[1]/div/div[2]/div[2]/div[3]/table/tbody')
    rows = tbody.find_elements(By.TAG_NAME, 'tr')

    cell_data = []
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, 'td')
        cell_data = [col.text for col in cols]
        data.append(cell_data)
        print(cell_data)
        list_01.append(cell_data[0])
        list_02.append(cell_data[1])
        list_03.append(cell_data[2])
        list_04.append(cell_data[3])
        list_05.append(cell_data[4])
        list_06.append(cell_data[5])
        list_07.append(cell_data[6])
        list_08.append(cell_data[7])
        list_09.append(cell_data[8])
        list_10.append(cell_data[9])
        list_10.append(cell_data[10])
        list_10.append(cell_data[11])
    return data


def set_page_size(size_xpath='/html/body/div[2]/div[1]/div[1]/ul/li[4]/span'):
    # 点击显示条数输入框
    page_size_input = driver.find_element(By.XPATH,
                                          '/html/body/div[1]/div[2]/div[1]/div[3]/div[3]/div/div[2]/section/div/div/div[2]/div[1]/div/div[2]/div[3]/div/span/div/div/input')
    page_size_input.click()

    # 选择50条/页
    option = wait.until(EC.element_to_be_clickable((By.XPATH, size_xpath)))
    time.sleep(1.5)  # 等待下拉菜单稳定
    option.click()

    # 等待页面更新
    # time.sleep(2)
    wait.until(EC.presence_of_element_located((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[1]/div[3]/div[3]/div/div[2]/section/div/div/div[2]/div[1]/div/div[2]/div[2]/div[3]/table/tbody')))
    time.sleep(10)  # 额外等待确保数据加载完成
    print('状态已更新为50条')


# 设置每页显示50条数据
# set_page_size()
def go_to_page(page_number):
    # 找到页码输入框
    page_input = driver.find_element(By.XPATH,
                                     '/html/body/div[1]/div[2]/div[1]/div[3]/div[3]/div/div[2]/section/div/div/div[2]/div[1]/div/div[2]/div[3]/div/slot/span[2]/div/input')
    page_input.clear()
    page_input.send_keys(str(page_number))

    # 点击页面的某个地方刷新数据（这里点击表格标题栏）
    refresh_element = driver.find_element(By.XPATH,
                                          '/html/body/div[1]/div[2]/div[1]/div[3]/div[3]/div/div[2]/section/div/div/div[1]')
    refresh_element.click()

    # 等待页面更新
    time.sleep(2)
    wait.until(EC.presence_of_element_located((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[1]/div[3]/div[3]/div/div[2]/section/div/div/div[2]/div[1]/div/div[2]/div[2]/div[3]/table/tbody')))


all_data = []
# while True:
#     # 提取当前页面的数据
#     all_data.extend(extract_data())
#     time.sleep(5)
#
#     try:
#         # 找到并点击下一页按钮
#         next_button = wait.until(EC.element_to_be_clickable((By.XPATH,
#                                                              '/html/body/div[1]/div[2]/div[1]/div[3]/div[3]/div/div[2]/section/div/div/div[2]/div[1]/div/div[2]/div[3]/div/button[2]')))
#         next_button.click()
#
#         # 等待下一页加载
#         time.sleep(2)
#         wait.until(EC.presence_of_element_located((By.XPATH,
#                                                    '/html/body/div[1]/div[2]/div[1]/div[3]/div[3]/div/div[2]/section/div/div/div[2]/div[1]/div/div[2]/div[2]/div[3]/table/tbody')))
#     except Exception as e:
#         print("No more pages or an error occurred:", e)
#         break

if __name__ == '__main__':
    # 初始化WebDriver（这里使用的是Chrome）

    driver = webdriver.Chrome()

    # 打开目标网址
    url = 'https://ggfw.ybj.ln.gov.cn/hsa-local/web/hallEnter/Personal/#/search/MedicalTreatment'
    driver.get(url)

    # 等待页面加载完成
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[1]/div[3]/div[3]/div/div[2]/section/div/div/div[2]/div[1]/div/div[2]/div[2]/div[3]/table/tbody')))

    total_pages = 2
    time.sleep(4)
    set_page_size()
    time.sleep(4)

    for page in range(1, total_pages + 1):
        data = []
        time.sleep(5)
        # 前往指定页码
        go_to_page(page)
        data = extract_data()
        # 提取当前页面的数据
        all_data.extend(data)

        print(data)
    # 关闭WebDriver
    driver.quit()

    # 打印提取的数据
    # for item in all_data:
    #     print(item)
    data_dict = {
        'list_01': list_01,
        'list_02': list_02,
        'list_03': list_03,
        'list_04': list_04,
        'list_05': list_05,
        'list_06': list_06,
        'list_07': list_07,
        'list_08': list_08,
        'list_09': list_09,
        'list_10': list_10,
        'list_11': list_11,
        'list_12': list_12
    }
    df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in data_dict.items()]))
    df.to_excel('辽宁医保局_西药中成药.xlsx', index=False)
