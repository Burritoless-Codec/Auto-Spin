# Overwatch 2 Ana Midnight Sun Gun Skin Auto-Scroll Script
## Overview
This project is a Python-based automation script designed to mimic infinite scrolling using mouse actions. It's built using the ```pyautogui``` and ```keyboard``` libraries, which enable simulated user input and keypress detection.

The purpose of this script is to make the sleep dart gun spin constantly with the mythic skin during a match. There is not other feature to this and does nothing besides a visual effect.

## Features

- **Keybind Activation**: The script activates scrolling when both `8` and `9` are pressed simultaneously on the keyboard. Once activated, the script will continuously scroll downward until deactivated.
  
- **Threaded Scrolling**: The scrolling action runs on a separate thread, allowing the main program to listen for key presses and toggle the scrolling on and off without interrupting the user.

- **Scroll Toggle**: Pressing the `8+9` key combination again will stop the scrolling.


## How It Relates to Overwatch 2's Ana Midnight Sun Gun Skin

Stimming while playing Ana that it just a spinny spin gun animation with a mythic skin.

## How to Use

1. **Clone this repository** to your local machine:
 ```bash
   git clone https://github.com/Burritoless-Codec/Auto-Spin.git
   cd Auto-Spin
```

2. **Install the necessary dependencies:**

```bash
  pip install pyautogui keyboard
```

3. ***Run the script:***

```bash
  python auto_scroll.py
```
4. ***Use the key combination (8 + 9) to toggle the scrolling on or off.***

## Customization
+ You can change the scroll amount by adjusting the value in `pyautogui.scroll(-20000)` inside the `scroll()` function.

+ To modify the activation keybind, change the activate_key variable (currently set to `'8+9'`).

### The Unlicense [License](https://github.com/Burritoless-Codec/Auto-Spin/blob/master/LICENSE)
