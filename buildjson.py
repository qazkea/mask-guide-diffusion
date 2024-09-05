import os
import json

def generate_json(output_file, source_dir, target_dir):
    data = []


    # 获取所有 source 文件夹中的文件名（假设文件名在所有文件夹中是相同的）
    source_files = sorted(os.listdir(source_dir))

    #print("Source files in the first directory:", source_files)
    
    # 确保所有 source 文件夹中的文件数量一致

    # 获取 target 文件名列表
    target_files = sorted(os.listdir(target_dir))

    for file_name in source_files:
        source_file_path = os.path.join(source_dir, file_name)
        target_file_path = os.path.join(target_dir, file_name)
        
        if file_name in target_files:
            item = {
                'source': source_file_path,
                'target': target_file_path,
                'prompt': ''  # 空字符串  以免产生干扰
            }

        data.append(item)
    

    # 写入 JSON 文件
    with open(output_file, 'w') as f:
        for item in data:
            f.write(json.dumps(item) + '\n')

if __name__ == "__main__":
    # 文件夹路径
    base_source_dir = './data'
    target_dir = '/20TB/data/yixue/allimg'  # 替换为实际 target 文件夹路径

    # 读取 prompt 信息
    # prompts = {}
    # with open('/20TB/data/yixue/prompts.txt', 'r') as f:
    #     for line in f:
    #         filename, prompt = line.strip().split(',', 1)
    #         prompts[filename] = prompt

    # 输出 JSON 文件路径
    output_file = './prompt.json'

    # 生成 JSON 文件
    generate_json(output_file, base_source_dir, target_dir)

    print(f"JSON file has been created at: {output_file}")
