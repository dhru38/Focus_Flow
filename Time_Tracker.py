import win32gui
import win32process
import psutil
import time
import joblib
import activity

model = joblib.load("window_classifier.pkl")

productive_time = 0
wasted_time = 0 

def get_info():
    hwnd = win32gui.GetForegroundWindow()
    window_title = win32gui.GetWindowText(hwnd)
    _, pid = win32process.GetWindowThreadProcessId(hwnd)

    process = psutil.Process(pid)
    process_name = process.name()

    print(f"Active App: {process_name} | Window Title: {window_title}")
    return window_title

def classify(window_title):
    global productive_time, wasted_time 

    prediction = model.predict([window_title])[0] 
    print(f"Predicted label: {prediction}")

    if prediction == "distracting":
        wasted_time += 5
    else:
        productive_time += 5

# Ideal Time 

input.last_activity 

def ideal () :
    if int(input.last_activity) > 300 : 
        global wasted_time
        wasted_time += int(input.last_activity)


# Main loop
for i in range(3):   # runs 3 times
    title = get_info()
    classify(title)
    ideal()
    time.sleep(5)

print(f"\nTotal productive time: {productive_time / 60:.2f} minutes")
print(f"Total wasted time: {wasted_time / 60:.2f} minutes")
