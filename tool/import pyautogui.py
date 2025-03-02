import pyautogui
import time

# 获取屏幕分辨率
screen_width, screen_height = pyautogui.size()

# 设置屏幕中心位置
center_x = screen_width - screen_width // 4
center_y = screen_height * 0.6

def swipe_up():
    # 模拟鼠标按下（按住在屏幕中间）
    pyautogui.mouseDown(center_x, center_y)
    time.sleep(0.1)  # 按下之后稍等一会

    # 从屏幕中间开始上滑，向上拖动（模拟滑动动作）
    pyautogui.moveTo(center_x, center_y - 600, duration=0.8)  # 向上滑动300像素

    # 松开鼠标
    pyautogui.mouseUp()

def main():
    while True:
        swipe_up()  # 执行上滑操作
        time.sleep(10)  # 休息20秒

if __name__ == "__main__":
    main()
