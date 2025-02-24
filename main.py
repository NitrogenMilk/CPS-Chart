from pynput import mouse
import time
import matplotlib.pyplot as plt

Length = 3

Counter = []
Counter_Time = None

def Detection(x, y, button, pressed):
    if pressed:
        Counter.append(time.time())
listener = mouse.Listener(on_click=Detection)

Counter_Time = time.time()
print("开始计数")
listener.start()
time.sleep(Length)
listener.stop()

relative_times =[t - Counter_Time for t in Counter]
y_values = [0] * len(Counter)

plt.figure(figsize=(10, 1))
plt.scatter(relative_times, y_values, marker='o', s=50, color='cyan', alpha=0.7)
plt.gca().yaxis.set_visible(False)
for i, t in enumerate(relative_times):
    plt.annotate(f'{t:.2f}s', (t, 0), textcoords="offset points",
                 xytext=(0, 15 if i % 2 == 0 else -20), ha='center',
                 arrowprops=dict(arrowstyle="->", lw=1))
print(len(relative_times) / Length)
plt.show()
