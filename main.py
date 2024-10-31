import psutil
import keyboard
import time

def check_process(process_name):
    for proc in psutil.process_iter(['name', 'pid']):
        if proc.info['name'] == process_name:
            return proc.info['pid']
    return None

def on_f10_press():
    process_name = "Unturned.exe"
    pid = check_process(process_name)

    if pid is not None:
        print(f"Finishing the process {process_name} for PID: {pid}")
        psutil.Process(pid).terminate()

def main():
    process_name = "Unturned.exe"

    keyboard.add_hotkey('F10', on_f10_press)
    print(f"Press F10 to finish {process_name}.")

    while True:
        if check_process(process_name) is None:
            print(f"{process_name} not running.")
        time.sleep(2)

if __name__ == '__main__':
    main()
