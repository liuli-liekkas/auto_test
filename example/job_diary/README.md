# 工作记录

## 文件类型
`Joblog_Panel.py`：工作日志主界面  
`Landing_Panel.py`：登陆界面  
`Link_MySQL.py`：链接数据库  
`Main.py`：执行程序文件  
`Parameter_Panel.py`：配置界面  
`Query_Panel.py`：查询界面  
`resource`：所有ui转py文件    
`ui`：所有界面ui文件

## 每个界面实现主要功能
`Joblog_Panel.py`：工作日志主界面
- 姓名，部门，岗位登陆之后自动填入，不能修改
- 左侧为下拉选择区，规范数据录入内容
- 只需要在右侧文本框中填写内容
- 下方显示临时保存数据
- 右侧按扭区域
  - `保存`：将填写的内容保存到临时表，并在下方显示
  - `修改`：选中下方表中的某行数据，可以对其进行修改
  - `删除`：选中下方表中的某行数据，可以将其删除
  - `提交`：将临时表数据提交到记录表
  - `查询`：显示查询窗口
  - `配置`：显示配置窗口
  
>下方显示数据为临时表数据。临时表数据允许增删改  
>点击提交按钮，将临时表数据转移到记录表，不允许修改，可在查询窗口查询


`Landing_Panel.py`：登陆界面
- 使用姓名和密码登陆
- 姓名不存在，或者密码错误则窗口抖动报错

`Link_MySQL.py`：链接数据库 
- 链接MySQL数据库
- 其他模板直接调用执行SQL语句的方法

`Parameter_Panel.py`：配置界面
- 自定义下拉内容
- 可以调节右侧List条目的顺序

`Query_Panel.py`：查询界面
- 可选定日期进行查询，并导出
- 后台可以控制查询权限
  - 默认只能查询自己的数据
  - 可设置查询数据的部门范围
