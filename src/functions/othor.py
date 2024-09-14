import time

class Colors:
    # 代表的な色
    INFO_BLUE = '\033[94m'
    INFO_GREEN = '\033[92m'
    WARN = '\033[93m'
    ERR = '\033[91m'

    # フォントスタイル
    MARKER = '\033[7m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    # 末尾制御
    _END = '\033[0m'

class Othor:
    def log(self, text):
        print('{} {} >> {} {}'.format(Colors.INFO_BLUE, time.time(), str(text), Colors._END))
        return

    def error(self, text):
        print('{} {} >> {} {}'.format(Colors.ERR, time.time(), str(text), Colors._END))