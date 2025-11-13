@echo off
chcp 65001 > nul
REM おみくじGUIツールを実行するバッチファイル

REM 'activate' を 'call' せず、venv内のpython.exeを直接指定する (こちらが堅牢です)
venv\Scripts\python.exe omikuji_gui.py

echo.
echo プログラムを終了しました。
pause
