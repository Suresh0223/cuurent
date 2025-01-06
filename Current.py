import os
import tkinter as tk
from time import strftime
from flask import Flask

app = Flask(__name__)

if os.environ.get('DISPLAY', '') == '':
    print('No display found. Using Xvfb.')
    os.system('Xvfb :99 -screen 0 1024x768x16 &')
    os.environ['DISPLAY'] = ':99.0'

root = tk.Tk()
root.title("Clock")
root.geometry("400x300")

clock_label = tk.Label(root, font=("Arial", 50), bg="light green", fg="blue")
clock_label.pack( anchor = "center", fill ="both", expand = True)

@app.route('/')
def update_time():
  current_time = strftime("%H:%M:%S")
  clock_label.config(text=current_time)
  clock_label.after(1000, update_time)

update_time()
root.mainloop()
# main driver function
if __name__ == '__main__':
    app.run()
