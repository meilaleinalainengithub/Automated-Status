@echo off
python -m venv venv
call .\venv\Scripts\activate
pip install requests==2.25.1
python main.py