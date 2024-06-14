import tkinter as tk
import pyperclip

class CharacterTool:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("字符处理工具")
        self.root.geometry("500x400")

        self.create_widgets()

    def create_widgets(self):
        input_label = tk.Label(self.root, text="输入文本:")
        input_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.input_entry = tk.Text(self.root, height=10, width=40)
        self.input_entry.grid(row=0, column=1, padx=5, pady=5)

        output_label = tk.Label(self.root, text="输出文本:")
        output_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.output_textbox = tk.Text(self.root, height=10, width=40)
        self.output_textbox.grid(row=1, column=1, padx=5, pady=5)

        process_button = tk.Button(self.root, text="处理", command=self.process_input)
        process_button.grid(row=2, column=0, padx=5, pady=5)

        clear_input_button = tk.Button(self.root, text="清空输入", command=self.clear_input)
        clear_input_button.grid(row=2, column=1, padx=5, pady=5)

        clear_output_button = tk.Button(self.root, text="清空输出", command=self.clear_output)
        clear_output_button.grid(row=2, column=2, padx=5, pady=5)

        copy_output_button = tk.Button(self.root, text="复制输出", command=self.copy_output)
        copy_output_button.grid(row=2, column=3, padx=5, pady=5)

    def process_input(self):
        input_text = self.input_entry.get("1.0", "end-1c")
        lines = input_text.split("\n")
        processed_lines = []
        for line in lines:
            if line.strip():
                processed_line = "'" + line.strip() + "'"
                processed_lines.append(processed_line)
        output_text = ",".join(processed_lines)
        self.output_textbox.delete("1.0", "end")
        self.output_textbox.insert("1.0", output_text)

    def clear_input(self):
        self.input_entry.delete("1.0", "end")

    def clear_output(self):
        self.output_textbox.delete("1.0", "end")

    def copy_output(self):
        output_text = self.output_textbox.get("1.0", "end-1c")
        pyperclip.copy(output_text)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = CharacterTool()
    app.run()
