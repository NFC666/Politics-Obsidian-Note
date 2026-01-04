import os

def batch_replace_first_line():
    # 1. 获取当前脚本文件所在的绝对目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 2. 获取目录输入，如果为空则取脚本所在目录
    input_path = input(f"请输入目录路径 (直接回车则处理当前目录: {script_dir}): ").strip()
    target_dir = input_path if input_path else script_dir

    if not os.path.isdir(target_dir):
        print(f"错误：路径 '{target_dir}' 不存在！")
        return

    # 3. 获取替换字符串
    old_str = input("请输入第一行中要被替换的字符串: ")
    new_str = input("请输入替换后的字符串: ")

    print(f"\n正在处理目录: {target_dir} ...")
    count = 0

    # 4. 递归遍历
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.lower().endswith('.md'):
                file_path = os.path.join(root, file)
                try:
                    # 先读取内容
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                    
                    # 5. 仅处理第一行
                    if lines and old_str in lines[0]:
                        # 局部替换第一行中的目标字符串
                        new_first_line = lines[0].replace(old_str, new_str)
                        
                        # 只有在内容真正发生变化时才写入
                        if new_first_line != lines[0]:
                            lines[0] = new_first_line
                            with open(file_path, 'w', encoding='utf-8') as f:
                                f.writelines(lines)
                            
                            # 打印相对路径，方便查看
                            rel_path = os.path.relpath(file_path, target_dir)
                            print(f"已更新: {rel_path}")
                            count += 1
                except Exception as e:
                    print(f"处理文件 {file} 时出错: {e}")

    print(f"\n任务完成！共修改了 {count} 个文件。")

if __name__ == "__main__":
    batch_replace_first_line()