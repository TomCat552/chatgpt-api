import ctypes

# Windows CMD命令行 字体颜色定义 text colors
STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE= -11
STD_ERROR_HANDLE = -12
FOREGROUND_BLACK = 0x00 # black.
FOREGROUND_DARKBLUE = 0x01 # dark blue. 暗蓝色
FOREGROUND_DARKGREEN = 0x02 # dark green.   暗绿色
FOREGROUND_DARKSKYBLUE = 0x03 # dark skyblue. 暗天蓝色
FOREGROUND_DARKRED = 0x04 # dark red.   暗红色
FOREGROUND_DARKPINK = 0x05 # dark pink. 暗粉红色
FOREGROUND_DARKYELLOW = 0x06 # dark yellow. 暗黄色
FOREGROUND_DARKWHITE = 0x07 # dark white. 暗白色
FOREGROUND_DARKGRAY = 0x08 # dark gray. 暗灰色
FOREGROUND_BLUE = 0x09 # blue.
FOREGROUND_GREEN = 0x0a # green.
FOREGROUND_SKYBLUE = 0x0b # skyblue.
FOREGROUND_RED = 0x0c # red.
FOREGROUND_PINK = 0x0d # pink.
FOREGROUND_YELLOW = 0x0e # yellow.
FOREGROUND_WHITE = 0x0f # white.

# Windows CMD命令行 背景颜色定义 background colors
# BACKGROUND_BLUE = 0x10 # dark blue.
# BACKGROUND_GREEN = 0x20 # dark green.
BACKGROUND_DARKSKYBLUE = 0x30 # dark skyblue.
BACKGROUND_DARKRED = 0x40 # dark red.
BACKGROUND_DARKPINK = 0x50 # dark pink.
BACKGROUND_DARKYELLOW = 0x60 # dark yellow.
BACKGROUND_DARKWHITE = 0x70 # dark white.
BACKGROUND_DARKGRAY = 0x80 # dark gray.
BACKGROUND_BLUE = 0x90 # blue.
BACKGROUND_GREEN = 0xa0 # green.
BACKGROUND_SKYBLUE = 0xb0 # skyblue.
BACKGROUND_RED = 0xc0 # red.
BACKGROUND_PINK = 0xd0 # pink.
BACKGROUND_YELLOW = 0xe0 # yellow.
BACKGROUND_WHITE = 0xf0 # white.


class winColor:
    std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    # 设置字体颜色的代码
    def set_cmd_color(self, color, handle=std_out_handle):
        bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
        return bool
    # 颜色重置
    def reset_color(self):
        self.set_cmd_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)

    # 红色
    def print_red_text(self, print_text):
        self.set_cmd_color(FOREGROUND_RED)
        print(print_text)
        self.reset_color()

    # 绿色
    def print_green_text(self, print_text):
        self.set_cmd_color(FOREGROUND_GREEN)
        print(print_text)
        self.reset_color()

    # 暗蓝色
    def printDarkBlue(self, print_text):
        self.set_cmd_color(FOREGROUND_DARKBLUE)
        print(print_text)
        self.reset_color()

    # 白底黑字
    def printWhiteBlack(self, print_text):
        self.set_cmd_color(FOREGROUND_BLACK | BACKGROUND_WHITE)
        print(print_text)
        self.reset_color()

    # 黄底蓝字
    def printYellowRed(self, print_text):
        self.set_cmd_color(BACKGROUND_YELLOW | FOREGROUND_RED)
        print(print_text)
        self.reset_color()

