import sys
import random
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QTextEdit
)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

# 元のコードからおみくじデータを流用
FORTUNES = [
    ("大吉", "今日は新しいことを始めるのに最適な一日です。思い切って一歩踏み出してみてください。"),
    ("中吉", "落ち着いて行動すれば、良い流れが自然とやってきます。焦らずマイペースで。"),
    ("小吉", "小さな努力が少しずつ積み重なっていく日です。できることから一つずつ進めていきましょう。"),
    ("末吉", "無理をせず、体調と気分を優先すると良い日です。休息も大事な行動の一つです。"),
    ("凶", "今日は慎重さが大切な日です。大きな決断は避けて、確認と見直しを心がけてください。"),
]

def draw_omikuji():
    """おみくじの結果をランダムに返す"""
    fortune, message = random.choice(FORTUNES)
    return fortune, message

class OmikujiApp(QMainWindow):
    """おみくじGUIのメインウィンドウ"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("おみくじツール (PySide6版)")
        self.setGeometry(100, 100, 400, 300)  # ウィンドウの初期位置とサイズ

        # --- ウィジェット（部品）の作成 ---

        # 1. タイトルラベル
        self.title_label = QLabel("ワンクリックおみくじ")
        font = self.title_label.font()
        font.setPointSize(16)
        font.setFamily("Yu Gothic UI") # フォントは環境に合わせて調整
        self.title_label.setFont(font)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # 2. 説明ラベル
        self.info_label = QLabel("「おみくじを引く」ボタンを押してください。")
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # 3. 結果表示 (横並び)
        self.result_label_prefix = QLabel("結果：")
        self.result_label_content = QLabel("まだ引いていません")

        # 4. メッセージ表示用のテキストエリア
        self.message_box = QTextEdit()
        self.message_box.setReadOnly(True)  # 編集不可にする
        self.message_box.setFixedHeight(100) # 高さを固定

        # 5. ボタン (横並び)
        self.draw_button = QPushButton("おみくじを引く")
        self.exit_button = QPushButton("終了")

        # --- レイアウト（配置）の設定 ---

        # メインとなるレイアウト (垂直方向)
        main_layout = QVBoxLayout()

        # 結果表示用のレイアウト (水平方向)
        result_layout = QHBoxLayout()
        result_layout.addWidget(self.result_label_prefix)
        result_layout.addWidget(self.result_label_content)
        result_layout.addStretch() # 左寄せにするためのスペーサー

        # ボタン用のレイアウト (水平方向)
        button_layout = QHBoxLayout()
        button_layout.addStretch() # 中央寄せのためのスペーサー
        button_layout.addWidget(self.draw_button)
        button_layout.addWidget(self.exit_button)
        button_layout.addStretch()

        # メインレイアウトに各ウィジェットを追加
        main_layout.addWidget(self.title_label)
        main_layout.addWidget(self.info_label)
        main_layout.addLayout(result_layout) # レイアウトにレイアウトを追加
        main_layout.addWidget(self.message_box)
        main_layout.addLayout(button_layout)

        # --- ウィンドウにレイアウトを適用 ---
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # --- シグナルとスロット（イベント処理）の接続 ---
        self.draw_button.clicked.connect(self.on_draw_click)
        self.exit_button.clicked.connect(self.close) # ウィンドウを閉じる

    def on_draw_click(self):
        """「おみくじを引く」ボタンが押された時の処理"""
        fortune, message = draw_omikuji()
        self.result_label_content.setText(fortune)
        self.message_box.setText(message)

# --- アプリケーションの実行 ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OmikujiApp()
    window.show()
    sys.exit(app.exec())
