@echo off
chcp 65001 > nul

REM 仮想環境 (venv) フォルダが存在しない場合のみ作成
if not exist venv (
    echo 仮想環境 (venv) を作成します...
    python -m venv venv
    if errorlevel 1 (
        echo 仮想環境の作成に失敗しました。
        pause
        exit /b 1
    )
) else (
    echo 仮想環境 (venv) は既に存在します。
)

echo ライブラリをインストールしています (pipのアップグレードとrequirements.txt)...

REM 'activate' を 'call' せず、venv内のpython.exeを直接指定する (こちらが堅牢です)
venv\Scripts\python.exe -m pip install --upgrade pip
venv\Scripts\python.exe -m pip install -r requirements.txt
if errorlevel 1 (
    echo ライブラリのインストールに失敗しました。
    pause
    exit /b 1
)

echo インストールが完了しました。
pause
