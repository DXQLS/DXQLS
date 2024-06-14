import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

class SQLGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("生成SQL文件")

        # 计算窗口居中的位置
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        window_width = int(screen_width * 0.4)  # 窗口宽度为屏幕宽度的40%
        window_height = int(screen_height * 0.4)  # 窗口高度为屏幕高度的40%
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.label_excel_path = tk.Label(root, text="选择Excel文件:")
        self.label_excel_path.pack()

        self.btn_browse = tk.Button(root, text="浏览...", command=self.browse_excel_file)
        self.btn_browse.pack()

        self.label_selected_excel = tk.Label(root, text="")
        self.label_selected_excel.pack()

        self.label_database_name = tk.Label(root, text="数据库名:")
        self.label_database_name.pack()
        self.entry_database_name = tk.Entry(root)
        self.entry_database_name.pack()

        self.label_table_name = tk.Label(root, text="表名:")
        self.label_table_name.pack()
        self.entry_table_name = tk.Entry(root)
        self.entry_table_name.pack()

        self.generate_sql_button = tk.Button(root, text="生成SQL文件", command=self.generate_sql_file, state=tk.DISABLED)
        self.generate_sql_button.pack()

    def browse_excel_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
        if file_path:
            self.excel_path = file_path
            self.label_selected_excel.config(text=f"已选择文件: {file_path}")
            self.generate_sql_button.config(state=tk.NORMAL)

    def generate_sql_file(self):
        if not hasattr(self, 'excel_path'):
            messagebox.showerror("错误", "请先选择要生成SQL文件的Excel文件！")
            return

        database_name = self.entry_database_name.get()
        if not database_name:
            messagebox.showerror("错误", "请输入数据库名！")
            return

        table_name = self.entry_table_name.get()
        if not table_name:
            messagebox.showerror("错误", "请输入表名！")
            return

        try:
            # 读取Excel文件的所有sheet页
            excel_data = pd.read_excel(self.excel_path, sheet_name=None)

            # 生成插入数据的SQL语句
            sql_statements = []
            for sheet_name, sheet_data in excel_data.items():
                sheet_data.fillna("", inplace=True)  # 将NaN值替换为空字符串

                for index, row in sheet_data.iterrows():
                    item_name = row.get("item_name")
                    item_code = row.get("item_code")
                    common_name = row.get("common_name")
                    fee_level = row.get("fee_level")
                    common_ratio = row.get("common_ratio")
                    include = row.get("include")
                    exception = row.get("exception")
                    unit = row.get("unit")
                    remark = row.get("remark")
                    bas_deduction_rule_id = row.get("bas_deduction_rule_id")
                    medicine_type = row.get("medicine_type")

                    values = (
                        item_name, item_code, common_name, fee_level, common_ratio, include, exception, unit, remark,
                        bas_deduction_rule_id, medicine_type)
                    query = f"INSERT INTO `{database_name}`.`{table_name}` (item_name, item_code, common_name, fee_level, common_ratio, include, exception, unit, remark, bas_deduction_rule_id, medicine_type) VALUES {values}"

                    sql_statements.append(query)

            # 生成SQL文件
            sql_file_name = f"{database_name}_{table_name}_zhenliao_insert.sql"
            with open(sql_file_name, "w", encoding="utf-8") as sql_file:
                for statement in sql_statements:
                    sql_file.write(statement + ";\n")

            messagebox.showinfo("成功", "SQL文件生成成功！")
        except Exception as e:
            messagebox.showerror("错误", f"生成SQL文件失败：{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SQLGenerator(root)
    root.mainloop()
