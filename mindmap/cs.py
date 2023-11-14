import json
import re

with open('mermaid.html', 'r', encoding='utf-8') as file:
    html_code = file.read()

with open('config.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

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

with open('mermaid.html', 'w', encoding='utf-8') as file:
    file.write(html_code)
