import time
from tkinter import *
from tkinter import messagebox

def start_pomodoro(focus_time, break_time):
    root = Tk()
    root.withdraw()

    for i in range(4):
        messagebox.showinfo("Pomodoro Timer", f"开始专注，持续 {focus_time} 分钟")
        time.sleep(focus_time * 60)
        messagebox.showinfo("Pomodoro Timer", f"休息时间，持续 {break_time} 分钟")
        time.sleep(break_time * 60)

    messagebox.showinfo("Pomodoro Timer", "恭喜！你已经完成了4个Pomodoro周期！")
    root.destroy()

if __name__ == "__main__":
    focus_time = 25
    break_time = 5
    start_pomodoro(focus_time, break_time)
