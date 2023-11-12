# R11GPTTraining

### 用于 GPT 生成需求的软件代码的训练

#### 软件外观框架

- 窗口大小建议1280*720

- 将 Code/config_example.json，改为 config.json

- 在 Code/config.json 中配置
  - 软件名称 `可在 app.py 中配置`
  - 功能模块列表  `可在 app.py 中配置`
  - 顶部导航栏颜色 ` 运行 app.py 可自动随机获取`
  - 侧边导航栏颜色 ` 运行 app.py 可自动随机获取`
  - 导航左上角用户名  ` 运行 app.py 可自动获取`
  - 导航左上角用图标  ` 运行 app.py 可自动获取`
  - 侧边菜单图标 ` 运行 app.py 可自动随机获取`

- 在 Code/html 文件夹中，放置 html 代码
  - 以 0.html、1.html... 命名
  - 序号与功能模块列表的下标对应

- 若需添加图标样式、导航颜色组合、用户名列表
  - 按照 options.json 中原有的数据添加或修改即可
  - 添加的图标，需要将图标文件放入 Code/icons 