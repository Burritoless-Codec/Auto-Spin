import pyautogui
import time
import threading
import keyboard

activate_key = '8+9'
scrolling_active = False


def toggle_scroll():
    global scrolling_active
    scrolling_active = not scrolling_active
    if scrolling_active:
        threading.Thread(target=scroll, daemon=True).start()


def scroll():
    while scrolling_active:
        pyautogui.scroll(-20000)
        time.sleep(0.2)


if __name__ == "__main__":
    while True:
        if keyboard.is_pressed(activate_key):
            toggle_scroll()
            time.sleep(1)  # Debounce to prevent rapid toggling
        time.sleep(0.01)
