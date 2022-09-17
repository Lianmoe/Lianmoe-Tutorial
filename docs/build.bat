@echo off
pip install -r requirements.txt
sphinx-autobuild ./ build/html
pause