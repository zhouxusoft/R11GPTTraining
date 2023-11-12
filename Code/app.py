import json
import random

'''
    可在此自行配置软件名称以及功能模块列表
'''
name = '基于神经网络和群智算法的智能学习系统'
moduleList = [
    {"name": "智能推荐", "desc": "基于个人喜好和学习情况，为用户推荐个性化学习资源"},
    {"name": "知识图谱", "desc": "建立用户知识体系，呈现知识点间的关联和深度"},
    {"name": "学习路径规划", "desc": "根据用户学习目标和已有知识，制定个性化的学习路径和计划"},
    {"name": "智能测试", "desc": "根据用户学习情况调整题目难度，动态生成适合的测试题"},
    {"name": "学习成效评估", "desc": "评估用户学习成果，为用户提供个性化的学习反馈和建议"},
    {"name": "学习社区", "desc": "提供学习交流和互助平台，促进用户间的学习分享和合作"},
    {"name": "学习记录分析", "desc": "分析用户学习过程和成果，为用户提供学习行为数据的可视化分析"},
    {"name": "情感识别", "desc": "识别用户学习过程中的情感变化，为用户提供情感化的辅助与引导"},
    {"name": "学习动态提醒", "desc": "基于用户学习进度和模式，智能生成学习提醒和激励动态"},
    {"name": "学习资源管理", "desc": "整合各种学习资源，提供个性化推荐、筛选和管理功能"},
    {"name": "多维度知识检索", "desc": "支持用户通过不同维度进行知识检索，提供更多元化的学习资源"},
    {"name": "学习成绩预测", "desc": "通过算法预测用户的学习成绩，帮助用户制定学习计划"},
    {"name": "学习游戏化", "desc": "将学习内容转化为游戏化元素，提高用户学习的趣味性和参与度"},
    {"name": "智能笔记", "desc": "支持用户记录学习笔记，提供智能整理和检索功能"},
    {"name": "学习目标管理", "desc": "帮助用户设定学习目标，并进行有效的管理和跟踪"},
    {"name": "学习社交网络分析", "desc": "分析用户在学习社交网络中的影响力和交互模式"},
    {"name": "多模态学习支持", "desc": "支持文字、图片、音频、视频等多种学习方式，提供全方位的学习支持"},
    {"name": "情境化学习模拟", "desc": "提供真实场景的学习模拟，促进用户在特定情境下的学习体验"},
    {"name": "个性化学习报告", "desc": "生成用户个性化的学习报告，展示学习成绩和成长轨迹"},
    {"name": "智能学习日历", "desc": "智能规划用户学习日程，提供个性化的学习时间安排"}
]

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
config_data['name'] = name
config_data['moduleList'] = moduleList
config_data['top_nav_color'] = nav_color_group[0]
config_data['left_nav_color'] = nav_color_group[1]
config_data['menu_icon'] = menu_icon
config_data['user_info_name'] = user_info_name
config_data['user_info_icon'] = user_info_icon


# 将修改后的内容写回 config.json 文件中
with open('config.json', 'w', encoding='utf-8') as f:
    # 写入文件时，默认是使用ASCII编码，因此中文字符会被转换成Unicode编码，故需要添加 ensure_ascii=False
    json.dump(config_data, f, ensure_ascii=False, indent=4)