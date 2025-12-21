import os
import re

def unmask_tags():
    # 获取当前脚本文件所在的绝对目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 获取输入，如果为空则取脚本所在目录
    input_path = input(f"请输入目录路径 (直接回车则还原脚本所在目录: {script_dir}): ").strip()
    target_dir = input_path if input_path else script_dir

    if not os.path.isdir(target_dir):
        print(f"错误：路径 '{target_dir}' 不存在！")
        return

    # 正则：匹配两个 #，且前后都不是 #
    pattern = re.compile(r'(?<!#)##(?!#)')

    print(f"正在还原目录: {target_dir} ...")
    count = 0

    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.lower().endswith('.md'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                    
                    if lines:
                        # 仅处理第一行
                        new_first_line = pattern.sub('#', lines[0])
                        if new_first_line != lines[0]:
                            lines[0] = new_first_line
                            with open(file_path, 'w', encoding='utf-8') as f:
                                f.writelines(lines)
                            print(f"已还原: {file}")
                            count += 1
                except Exception as e:
                    print(f"无法读取文件 {file}: {e}")

    print(f"\n还原完毕！共处理了 {count} 个文件。")

if __name__ == "__main__":
    unmask_tags()