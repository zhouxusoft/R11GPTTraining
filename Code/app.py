import json
import random
import re

'''
    随机获取各种样式
'''

# 打开 options.json 文件并读取内容
with open('options.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 通过随机数，随机从列表中获得一个用户名
random_number = random.randint(0, len(data['user_name_list']) - 1)
user_info_name = data['user_name_list'][random_number]

# 通过随机数，随机从列表中获得一组导航颜色
random_number = random.randint(0, len(data['nav_color_group']) - 1)
nav_color_group = data['nav_color_group'][random_number]

# 通过随机数，随机从列表中获得一个菜单图标
random_number = random.randint(0, len(data['menu_icon_list']) - 1)
menu_icon = data['menu_icon_list'][random_number]

# 通过随机数，随机从列表中获得一个用户头像
random_number = random.randint(0, len(data['user_info_icon_list']) - 1)
user_info_icon = data['user_info_icon_list'][random_number]

# 打开 config.json 文件并读取内容
with open('config.json', 'r', encoding='utf-8') as f:
    config_data = json.load(f)

# 修改 config.json 字段 中的内容
config_data['top_nav_color'] = nav_color_group[0]
config_data['left_nav_color'] = nav_color_group[1]
config_data['menu_icon'] = menu_icon
config_data['user_info_name'] = user_info_name
config_data['user_info_icon'] = user_info_icon


# 将修改后的内容写回 config.json 文件中
with open('config.json', 'w', encoding='utf-8') as f:
    # 写入文件时，默认是使用ASCII编码，因此中文字符会被转换成Unicode编码，故需要添加 ensure_ascii=False
    json.dump(config_data, f, ensure_ascii=False, indent=4)