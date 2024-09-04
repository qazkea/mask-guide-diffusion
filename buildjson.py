import os
import json

def generate_json(output_file, source_dirs, target_dir):
    data = []

    # 确保 source_dirs 是一个列表，包含多个 source 文件夹
    if not isinstance(source_dirs, list):
        raise ValueError("source_dirs must be a list of directories.")

    # 获取所有 source 文件夹中的文件名（假设文件名在所有文件夹中是相同的）
    source_files = sorted(os.listdir(source_dirs[0]))

    #print("Source files in the first directory:", source_files)
    
    # 确保所有 source 文件夹中的文件数量一致
    for source_dir in source_dirs[1:]:
        if sorted(os.listdir(source_dir)) != source_files:
            raise ValueError("All source directories must contain the same files.")

    # 获取 target 文件名列表
    target_files = sorted(os.listdir(target_dir))

    for file_name in source_files:
        source_file_paths = [os.path.join(dir, file_name) for dir in source_dirs]
        target_file_path = os.path.join(target_dir, file_name)
        
        if file_name in target_files:
            item = {
                'source': source_file_paths,
                'target': target_file_path,
                'prompt': 'chest x-ray'  # 
            }

        data.append(item)
    

    # 写入 JSON 文件
    with open(output_file, 'w') as f:
        for item in data:
            f.write(json.dumps(item) + '\n')

if __name__ == "__main__":
    # 文件夹路径
    base_source_dir = '/20TB/data/yixue/mask30'
    source_dirs = [os.path.join(base_source_dir, str(i)) for i in range(23)]
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
    generate_json(output_file, source_dirs, target_dir)

    print(f"JSON file has been created at: {output_file}")
