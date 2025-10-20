from pynput import keyboard , mouse
import time 

# Keyboard

last_activity = time.time()

def on_press(key) : 
        global last_activity 
        last_activity= time.time()

listener = keyboard.Listener(on_press=on_press).start()
ideal_time = time.time() - last_activity

# Mouse 

last_mouse_time = time.time()

def on_move(x,y):
       global last_mouse_time
       last_mouse_time = time.time()

def on_scroll (x , y , dx ,dy) : 
       global last_mouse_time
       last_mouse_time = time.time()

def on_click (x , y, button , pressed) : 
       global last_mouse_time
       last_mouse_time = time.time()

mouse_listener = mouse.Listener (
        on_move = on_move,
        on_click = on_click,
        on_scroll = on_scroll
).start()

# Check for Ideal Time

while True : 
       ideal_time = time.time() - last_activity
       if ideal_time > 300 :
               print (f"wasted {int(ideal_time) / 60 : .2f} minutes by being away from the WorkSpace ")
       time.sleep(1)
