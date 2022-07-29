@echo off

if [%1]==[] goto usage

COPY .\configs\defaults\embed_config_default.py .\configs\embed_config.py /V
COPY .\configs\defaults\general_config_default.py .\configs\general_config.py /V 

%1\python.exe -m venv .\.venv

.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt

.\.venv\Scripts\activate.bat

goto :eof

:usage
@echo Usage: %0 ^<Python Path^>
