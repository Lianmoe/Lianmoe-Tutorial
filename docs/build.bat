@echo off
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
sphinx-autobuild ./ build/html
pause