@echo off
:: Change this to the full path of your cloned repo
cd /d "C:\Users\somsd\daily-counter"

:: Run the Python script
python counter.py >> run_log.txt 2>&1