import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# 初始化列表
list_01, list_02, list_03, list_04, list_05, list_06, list_07, list_08, list_09, list_10 = [], [], [], [], [], [], [], [], [], []
list_no_deal = []
# 读取文件中的诊疗项目名称
with open('辽宁诊疗_0605.txt', 'r', encoding='utf8') as fp:
    project_names = [line.strip() for line in fp]
# 遍历诊疗项目名称
for j, project_name in enumerate(project_names):
    # 初始化 WebDriver（假设使用 Chrome）
    driver = webdriver.Chrome()

    # 打开目标网页
    driver.get('https://ggfw.ybj.dl.gov.cn/dl-medical/hall/#/search/getTrtitem')
    print(f'正在爬取第{j + 1}条数据')
    # 等待输入框加载并输入数据
    wait = WebDriverWait(driver, 10)
    input_box = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="请输入诊疗项目名称"]')))
    input_box.clear()
    input_box.send_keys(project_name)
    input_box.send_keys(Keys.RETURN)

    # 等待页面加载数据
    time.sleep(1)  # 您可以调整等待时间或使用其他等待条件
    # 获取总条目数
    total_items_text = driver.find_element(By.XPATH,
                                           '/html/body/div[1]/div[2]/div[3]/div[3]/div/div[2]/section/div/div/div[3]/div/span[1]').text
    try:
        total_items = int(''.join(filter(str.isdigit, total_items_text)))
        print(f"该药品共数据: {total_items}条")
        if total_items > 10:
            list_no_deal.append(project_name)
    except:
        print(f"该药品{project_name}无数据")
        continue
        # items_per_page_input.clear()
        # items_per_page_input.send_keys('50')
        # items_per_page_input.send_keys(Keys.RETURN)
    # if total_items > 10:
    #     # 设置每页显示50条记录
    #     items_per_page_input = driver.find_element(By.XPATH,
    #                                                '/html/body/div[1]/div[2]/div[3]/div[3]/div/div[2]/section/div/div/div[3]/div/span[2]/div/div/input')
    #     items_per_page_input.click()
    #     # 点击显示50条记录的选项
    #     option_50 = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'50条/页')]")))
    #     time.sleep(1.5)  # 您可以调整等待时间或使用其他等待条件
    #     option_50.click()
    #     time.sleep(1.5)  # 您可以调整等待时间或使用其他等待条件

    # time.sleep(0.7)  # 您可以调整等待时间或使用其他等待条件
    # 获取表格数据

    # print(rows)
    # 遍历前10行数据
    # 计算页数
    # print(total_items)
    if total_items > 10:
        total_pages = (total_items + 9) // 10
    else:
        total_pages = 1
    print(f'该药品{project_name}共{total_pages}页')
    # 遍历每一页
    for page in range(total_pages):
        rows = driver.find_elements(By.XPATH,
                                    '/html/body/div[1]/div[2]/div[3]/div[3]/div/div[2]/section/div/div/div[2]/div[3]/table/tbody/tr')
        time.sleep(1)
        for i, row in enumerate(rows[:10]):
            # cells = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.TAG_NAME, "td")))
            cells = row.find_elements(By.TAG_NAME, 'td')
            cell_data = [cell.text for cell in cells]
            # print(cell_data)
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
        # 点击下一页按钮
        if page < total_pages - 1:
            next_page_button = driver.find_element(By.XPATH,
                                                   '/html/body/div[1]/div[2]/div[3]/div[3]/div/div[2]/section/div/div/div[3]/div/button[2]')
            next_page_button.click()
            time.sleep(1)

    # 关闭 WebDriver
    driver.quit()
    #
# 将列表转换为字典
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
    'list_10': list_10
}
#
# 使用 Pandas 将字典转换为 DataFrame 并写入 Excel
df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in data_dict.items()]))
df.to_excel('辽宁诊疗_0605.xlsx', index=False)
print(list_no_deal)
# print("数据已成功写入到 output.xlsx")
# with open('辽宁诊疗_0605.txt', 'w+', encoding='utf8') as fp:
#     for i in list_no_deal:
#         fp.write(i.strip() + '\n')
