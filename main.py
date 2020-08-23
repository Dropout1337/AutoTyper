import os
import pyautogui
import time
import win32gui
import win32con

hwnd = win32gui.GetForegroundWindow()
win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,0,0,500,200,0)


def AutoTyper(text):
    try:
        print('\n[\u001b[31m!\u001b[37m] Typing')
        pyautogui.write(text, interval=0.0)
    except Exception:
        print('\n[\u001b[31m!\u001b[37m] Stopped')
        os.system('pause >NUL')
    except pyautogui.FailSafeException:
       print('\n[\u001b[31m!\u001b[37m] Auto Typer Safety Mode, Your Cursor Was At The Corner Of The Screen')
       os.system('pause >NUL')
    else:
       print(f'\n[\u001b[31m!\u001b[37m] Finished')
       os.system('pause >NUL')

if __name__ == "__main__":
    os.system('cls & title [Auto Typer] By Dropout')
    print(
        '[\u001b[31m1\u001b[37m] Dummy Text',
        '\n[\u001b[31m2\u001b[37m] Custom Text'
    )
    choice = input('\n\u001b[31m>\u001b[37m ')
    if "1" in choice:
        time.sleep(3)
        AutoTyper("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
    elif "2" in choice:
        text = input('\n\u001b[31m>\u001b[37m Text\u001b[31m:\u001b[37m ')
        time.sleep(3)
        AutoTyper(text)
    else:
        print('[\u001b[31m!\u001b[37m] Invalid Option')
        os.system('pause >NUL')

