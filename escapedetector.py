import keyboard
import sys

def esc_confirm(prompt):
        key = keyboard.read_event()
        if key.name == "esc":
                print(f"{prompt} Press Esc to confirm or any other key to cancel.")
                return True
        return False

def start_esc_listener(callback):
        keyboard.add_hotkey('esc', lambda: callback())
        callback()

def end():
        sys.exit()
