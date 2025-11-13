@echo off
REM 仮想環境を作成して必要なライブラリをインストールするバッチファイル

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

pip install --upgrade pip
pip install -r requirements.txt

echo.
echo インストールが完了しました。
pause
