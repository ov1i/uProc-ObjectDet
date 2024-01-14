@ECHO OFF

ECHO STARTING DEPENDENCY CHECKUP
winget install -e --id Python.Python.3.10
python.exe init.py

PAUSE