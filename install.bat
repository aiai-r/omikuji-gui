@echo off
chcp 65001 > nul

python -m venv venv
if errorlevel 1 (
    echo 仮想環境の作成に失敗しました。
    pause
    exit /b 1
)

call venv\Scripts\activate
if errorlevel 1 (
    echo 仮想環境の有効化に失敗しました。
    pause
    exit /b 1
)

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo インストールが完了しました。
pause
