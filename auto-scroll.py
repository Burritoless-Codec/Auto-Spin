import pyautogui
import time
import threading
import keyboard


activate_key = '8+9'
scrolling = None
scrolling_active = False


def scroll():
    global scrolling_active
    while scrolling_active:
        pyautogui.scroll(-20000)
        time.sleep(0.2)


def start_scrolling():
    global scrolling, scrolling_active
    if scrolling is None or not scrolling_active:
        scrolling_active = True
        scrolling = threading.Thread(target=scroll)
        scrolling.daemon = True
        scrolling.start()


def stop_scrolling():
    global scrolling_active
    scrolling_active = False


def on_press():
    global scrolling_active
    if keyboard.is_pressed(activate_key):
        if not scrolling_active:
            start_scrolling()
        else:
            stop_scrolling()
        time.sleep(1)


if __name__ == "__main__":
    while True:
        on_press()
        time.sleep(0.01)
