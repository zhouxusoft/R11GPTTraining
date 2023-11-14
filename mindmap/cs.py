with open('mermaid.html', 'r', encoding='utf-8') as file:
    html_code = file.read()

with open('config.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

softname = data['name']

html_code = html_code.replace('A[软件名称]', f'A[{softname}]')

print(html_code)

for i in range(0, len(data['moduleList'])):
    pass