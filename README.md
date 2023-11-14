# R11GPTTraining

### 用于 GPT 生成需求的软件代码的训练

#### 软件外观框架

- 窗口大小建议 1280*720

#### 运行截图配置

- 将 conf/config_example.json，改为 config.json

- 在 conf/config.json 中配置
  - 软件名称
  - 功能模块列表
  - 开发目的
  - 目标用户
  - 主要功能
  - 技术特点
  - 顶部导航栏颜色 ` 运行 main.py 可自动随机获取`
  - 侧边导航栏颜色 ` 运行 main.py 可自动随机获取`
  - 导航左上角用户名  ` 运行 main.py 可自动随机获取`
  - 导航左上角用图标  ` 运行 main.py 可自动随机获取`
  - 侧边菜单图标 ` 运行 main.py 可自动随机获取`

- 在 Code/html 文件夹中，放置 html 代码
  - 以 0.html、1.html... 命名
  - 序号与功能模块列表的下标对应

- 若需添加图标样式、导航颜色组合、用户名列表
  - 按照 options.json 中原有的数据添加或修改即可
  - 添加的图标，需要将图标文件放入 Code/icons 

### 配置好config.json后，运行 main.py 即可自动完善
  - `index.html`
  - `mindmap.html`
  - `mermaid.html`
  
### 运行 `index.html` 即可打开软件

#### 路由 hash
- 功能模块的 hash 为 `#page=0` 至 `#page=19`
- 主思维导图的 hash 为 `#page=20`
- 功能模块图的 hash 为 `#page=21`