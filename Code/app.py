import json

# 打开 config.json 文件并读取内容
with open('config.json', 'r', encoding='utf-8') as f:
    config_data = json.load(f)

# 修改 字段 中的内容
config_data['menu_icon_file_name'] = 'menu-4.svg'

# 将修改后的内容写回 config.json 文件中
with open('config.json', 'w', encoding='utf-8') as f:
    # 写入文件时，默认是使用ASCII编码，因此中文字符会被转换成Unicode编码，故需要添加 ensure_ascii=False
    json.dump(config_data, f, ensure_ascii=False, indent=4)