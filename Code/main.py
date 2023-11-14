from bs4 import BeautifulSoup
import json
import re


# 打开 options.json 文件并读取内容
with open('config.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

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

    soup.find("div", class_="soft_name").clear()
    soup.find("div", class_="soft_name").append(data['name'])
    soup.find("div", class_="purpose_text").clear()
    soup.find("div", class_="purpose_text").append(data["purpose"])
    soup.find("div", class_="target_text").clear()
    soup.find("div", class_="target_text").append(data["target"])
    soup.find("div", class_="main_text").clear()
    soup.find("div", class_="main_text").append(data["main"])
    soup.find("div", class_="tech_text").clear()
    soup.find("div", class_="tech_text").append(data["tech"])

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