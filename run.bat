@echo off
REM おみくじGUIツールを実行するバッチファイル

call venv\Scripts\activate
if errorlevel 1 (
    echo 仮想環境の有効化に失敗しました。
    pause
    exit /b 1
)

python omikuji_gui.py

echo.
echo プログラムを終了しました。
pause
