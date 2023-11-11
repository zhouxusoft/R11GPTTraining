import json
import random

# 打开 options.json 文件并读取内容
with open('options.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 通过随机数，随机从列表中获得一个用户名
random_number = random.randint(0, len(data['user_name_list']) - 1)
user_info_name = data['user_name_list'][random_number]

# 通过随机数，随机从列表中获得一组导航颜色
random_number = random.randint(0, len(data['nav_color_group']) - 1)
nav_color_group = data['nav_color_group'][random_number]

# 打开 config.json 文件并读取内容
with open('config.json', 'r', encoding='utf-8') as f:
    config_data = json.load(f)

# 修改 config.json 字段 中的内容
config_data['soft_name'] = '电子图书设计平台'
config_data['module_list'] = [
    "图书管理",
    "用户管理",
    "分类管理",
    "借阅管理",
    "排名统计",
    "评论管理",
    "图书推荐",
    "阅读器功能",
    "书签管理",
    "收藏夹",
    "搜索功能",
    "图书详情",
    "历史记录",
    "在线阅读",
    "书评功能",
    "借阅规则",
    "购买功能",
    "缓存管理",
    "用户反馈",
    "数据备份与恢复"
]
config_data['top_nav_color'] = nav_color_group[0]
config_data['left_nav_color'] = nav_color_group[1]
config_data['menu_icon_file_name'] = 'menu.svg'
config_data['user_info_name'] = user_info_name



# 将修改后的内容写回 config.json 文件中
with open('config.json', 'w', encoding='utf-8') as f:
    # 写入文件时，默认是使用ASCII编码，因此中文字符会被转换成Unicode编码，故需要添加 ensure_ascii=False
    json.dump(config_data, f, ensure_ascii=False, indent=4)