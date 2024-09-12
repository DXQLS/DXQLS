
import pandas as pd
import json

# 读取JSON文件
file_path = r'D:\pythonProject\result_芜湖_西药中成药_1725842312.json'

# 打开文件，逐行读取JSON对象
data_list = []
with open(file_path, 'r', encoding='gbk') as file:
    for line in file:
        print(line)
        try:
            data_list.append(json.loads(line.rstrip(',\n')))
        except json.JSONDecodeError as e:
            print(f"JSONDecodeError: {e}")

# 将数据转换为DataFrame
data = pd.DataFrame(data_list)

# 将自付比例信息展开
expanded_data_list = []

for index, row in data.iterrows():
    base_info = {
        "医保目录编码": row["医保目录编码"],
        "医保目录名称": row["医保目录名称"],
        "开始日期": row["开始日期"],
        "收费项目等级": row["收费项目等级"],
        "目录类别": row["目录类别"],
        "药品通用名称": row["药品通用名称"],
        "药品剂型名称": row["药品剂型名称"],
        "计价单位类型": row["计价单位类型"],
        "限制使用范围": row["限制使用范围"],
        "备注": row["备注"]
    }
    for proportion_info in row["自付比例信息"]:
        row_data = base_info.copy()
        row_data["自付比例人员类别"] = proportion_info["自付比例人员类别"]
        row_data["自付比例"] = proportion_info["自付比例"]
        expanded_data_list.append(row_data)

# 创建新的DataFrame
expanded_df = pd.DataFrame(expanded_data_list)

# 将DataFrame保存为Excel文件
output_file = '安徽省_芜湖_西药中成药.xlsx'
expanded_df.to_excel(output_file, index=False)

print(f"数据已成功保存到 {output_file}")
