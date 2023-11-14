from bs4 import BeautifulSoup
import json
import re
import random

'''
    随机获取配置
'''

# 打开 options.json 文件并读取内容
with open('./conf/options.json', 'r', encoding='utf-8') as f:
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
with open('./conf/config.json', 'r', encoding='utf-8') as f:
    config_data = json.load(f)

# 修改 config.json 字段 中的内容
config_data['top_nav_color'] = nav_color_group[0]
config_data['left_nav_color'] = nav_color_group[1]
config_data['menu_icon'] = menu_icon
config_data['user_info_name'] = user_info_name
config_data['user_info_icon'] = user_info_icon


# 将修改后的内容写回 config.json 文件中
with open('./conf/config.json', 'w', encoding='utf-8') as f:
    # 写入文件时，默认是使用ASCII编码，因此中文字符会被转换成Unicode编码，故需要添加 ensure_ascii=False
    json.dump(config_data, f, ensure_ascii=False, indent=4)

'''
    修改 html 代码
'''

# 打开 options.json 文件并读取内容
with open('./conf/config.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 读取并修改 index.html 文件
def changeIndex():
    # 打开 index.html 文件并读取内容
    with open('index.html', 'r', encoding='utf-8') as file:
        html_code = file.read()
    # 修改顶部导航栏颜色
    pattern = r"\.topcolor\s*{[^{}]*}"
    html_code = re.sub(pattern, '.topcolor{ background-color: ' + data['top_nav_color'] + ';}', html_code)
    # 修改左侧导航栏颜色
    pattern = r"\.leftcolor\s*{[^{}]*}"
    html_code = re.sub(pattern, '.leftcolor{ background-color: ' + data['left_nav_color'] + ';}', html_code)
    # 修改 script 中的模块列表
    pattern = r"modulelist\s*=\s*\[.*?\]"
    html_code = re.sub(pattern, 'modulelist = ' + str(data['moduleList']), html_code)
    # 修改 script 中的菜单按钮
    pattern = r"menuicon\s*=\s*''"
    html_code = re.sub(pattern, 'menuicon = \'' + data['menu_icon'] + '\'', html_code)
    # 修改 script 中的用户图标
    pattern = r"usericon\s*=\s*''"
    html_code = re.sub(pattern, 'usericon = \'' + data['user_info_icon'] + '\'', html_code)
    # 修改 script 中的顶部导航栏颜色
    pattern = r"topnavcolor\s*=\s*''"
    html_code = re.sub(pattern, 'topnavcolor = \'' + data['top_nav_color'] + '\'', html_code)

    # print(html_code)

    soup = BeautifulSoup(html_code, 'html.parser')
    # 修改 index.html 中的标题
    title_tag = soup.find('title')
    title_tag.string = data['name'] # type: ignore
    # 修改顶部导航栏中的软件名称
    soup.find("div", class_="softnametitle").clear() # type: ignore
    soup.find("div", class_="softnametitle").append(data['name']) # type: ignore
    # 修改顶部导航栏右侧的用户名称
    soup.find("div", class_="userinfoname").clear() # type: ignore
    soup.find("div", class_="userinfoname").append(data['user_info_name']) # type: ignore

    # 将修改后的内容写回 index.html 文件中
    with open('index.html', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())

# 读取并修改 mermaid.html 文件
def changeMindmap():
    # 打开 mindmap.html 文件并读取内容
    with open('mindmap.html', 'r', encoding='utf-8') as file:
        html_code = file.read()
    
    # 获取并修改主题颜色
    color = data['top_nav_color']
    pattern = r"\.color\s*{[^{}]*}"
    html_code = re.sub(pattern, '.color{ color: ' + color + ';}', html_code)

    soup = BeautifulSoup(html_code, 'html.parser')

    # 获取并修改软件相关信息
    soup.find("div", class_="soft_name").clear() # type: ignore
    soup.find("div", class_="soft_name").append(data['name']) # type: ignore

    soup.find("div", class_="purpose_text").clear() # type: ignore
    soup.find("div", class_="purpose_text").append(data["purpose"]) # type: ignore

    soup.find("div", class_="target_text").clear() # type: ignore
    soup.find("div", class_="target_text").append(data["target"]) # type: ignore

    soup.find("div", class_="main_text").clear() # type: ignore
    soup.find("div", class_="main_text").append(data["main"]) # type: ignore

    soup.find("div", class_="tech_text").clear() # type: ignore
    soup.find("div", class_="tech_text").append(data["tech"]) # type: ignore

    # print(soup)
    
    # 将修改后的内容写回 mindmap.html 文件中
    with open('mindmap.html', 'w', encoding='utf-8') as file:
        file.write(soup.prettify()) 

# 读取并修改 mermaid.html 文件
def changeMermaid():
    # 打开 mermaid.html 文件并读取内容
    with open('mermaid.html', 'r', encoding='utf-8') as file:
        html_code = file.read()

    softname = data['name']
    pattern = r"A\[[^\]]*?\]"
    html_code = re.sub(pattern, 'A[' + softname + ']', html_code)


    for i in range(0, len(data['moduleList'])):
        modulename = data['moduleList'][i]['name']
        moduledesc = data['moduleList'][i]['desc']
        if len(moduledesc) > 26:
            moduledesc = moduledesc[0:26] + '\n' + moduledesc[26:]
        # print(moduledesc)
        pattern = rf"M{i + 1}\[[^\]]*?\]"
        html_code = re.sub(pattern, f'M{i + 1}[' + modulename + ']', html_code)
        pattern = rf"D{i + 1}\[[^\]]*?\]"
        html_code = re.sub(pattern, f'D{i + 1}[' + moduledesc + ']', html_code)

    # print(html_code)

    # 将修改后的内容写回 mermaid.html 文件中
    with open('mermaid.html', 'w', encoding='utf-8') as file:
        file.write(html_code)

changeMindmap()
changeMermaid()
changeIndex()