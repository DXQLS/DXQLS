import pandas as pd
import pymysql


file_path = r'D:\pythonProject\pythonProject\tools\安诚机构最新数据维护202406292352.xlsx'
df = pd.read_excel(file_path)


table_name = 'ancheng_org'
ancheng_org_columns = [
    'id', 'org_name', 'short_name', 'org_code', 'org_level', 'parent_id', 'org_path', 'org_addr', 'province_id',
    'city_id', 'county_id', 'street_name', 'org_uscc', 'business_license_url', 'visible_range_flag', 'remark',
    'state', 'version', 'created_at', 'created_operator_id', 'created_operator_name', 'updated_at', 'updated_operator_id',
    'updated_operator_name'
]
columns = ", ".join(ancheng_org_columns)
values_template = ", ".join(["'%s'"] * len(ancheng_org_columns))


insert_statements = []
for index, row in df.iterrows():
    values = tuple(row[col] for col in ancheng_org_columns)
    insert_statement = f"INSERT INTO {table_name} ({columns}) VALUES ({values_template})" % values
    insert_statements.append(insert_statement)



with open('insert_statements.sql', 'w', encoding='utf-8') as file:
    for statement in insert_statements:
        file.write(statement + ';\n')

print("SQL插入语句已生成并保存到 insert_statements.sql 文件中。")
