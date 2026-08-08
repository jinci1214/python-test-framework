# Python Automation Testing Framework

基于 Python + Pytest + Playwright 的自动化测试框架。

## 技术栈

- Python 3.12
- Pytest
- Playwright
- Requests
- Pytest HTML Report

## 项目结构


python-test
├── api
├── pages
├── tests
├── utils
├── config
├── reports
└── pytest.ini


## 已实现功能

- Web UI 自动化测试
- API 接口自动化测试
- Page Object Model (POM)
- 参数化测试
- YAML配置管理
- HTML测试报告
- Git版本管理

## 运行测试

安装依赖：

```bash
pip install -r requirements.txt

执行：

pytest

生成报告：

pytest --html=reports/report.html



