import keyboard


def detect_key():
    while True:
        key_event = keyboard.read_event()
        if key_event.event_type == keyboard.KEY_DOWN:
            print(f"\nKey pressed: {key_event.name}\n")


if __name__ == "__main__":
    detect_key()
