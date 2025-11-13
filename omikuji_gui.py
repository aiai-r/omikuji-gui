import random
import PySimpleGUI as sg

FORTUNES = [
    ("大吉", "今日は新しいことを始めるのに最適な一日です。思い切って一歩踏み出してみてください。"),
    ("中吉", "落ち着いて行動すれば、良い流れが自然とやってきます。焦らずマイペースで。"),
    ("小吉", "小さな努力が少しずつ積み重なっていく日です。できることから一つずつ進めていきましょう。"),
    ("末吉", "無理をせず、体調と気分を優先すると良い日です。休息も大事な行動の一つです。"),
    ("凶", "今日は慎重さが大切な日です。大きな決断は避けて、確認と見直しを心がけてください。"),
]


def draw_omikuji():
    fortune, message = random.choice(FORTUNES)
    return fortune, message


def main():
    sg.theme("SystemDefault")

    layout = [
        [sg.Text("ワンクリックおみくじ", font=("Yu Gothic UI", 16), justification="center", expand_x=True)],
        [sg.Text("「おみくじを引く」ボタンを押してください。", key="-INFO-", pad=(10, 10))],
        [sg.Text("結果：", size=(6, 1)), sg.Text("まだ引いていません", key="-RESULT-", size=(25, 1))],
        [sg.Multiline(
            "",
            key="-MESSAGE-",
            size=(40, 5),
            disabled=True,
            autoscroll=True,
            no_scrollbar=True,
            wrap_lines=True
        )],
        [sg.Button("おみくじを引く", key="-DRAW-", size=(18, 1)), sg.Button("終了", key="-EXIT-")],
    ]

    window = sg.Window("おみくじツール", layout, finalize=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "-EXIT-"):
            break

        if event == "-DRAW-":
            fortune, message = draw_omikuji()
            window["-RESULT-"].update(fortune)
            window["-MESSAGE-"].update(message)

    window.close()


if __name__ == "__main__":
    main()
