import tkinter as tk
import math
from main import solve


def draw_point(canvas: tk.Canvas, x,  y):
    r = 5
    x1, x2 = x-r, x+r
    y1, y2 = y-r, y+r
    canvas.create_oval(x1,  y1,  x2, y2)


r = 300
window = tk.Tk()
window.title("Коло")

canvas_size = int(2 * r + 20)
canvas = tk.Canvas(window, width=canvas_size, height=canvas_size, bg="white")
canvas.pack()


cx = cy = canvas_size // 2
n = 10
step = 2*math.pi/n
# canvas.create_oval(cx - r, cy - r, cx + r, cy + r, outline="blue", width=2)
for i in range(n):
    x = math.cos(i*step)*r
    y = math.sin(i*step)*r
    draw_point(canvas, cx+x, cy+y)
edges = [
    (0, 1, 4), (0, 2, 3), (1, 2, 1), (1, 3, 2),
    (2, 3, 4), (3, 4, 2), (4, 5, 6)
]
cost, ans = solve(edges, None)
print(ans)
for start, end, _ in edges:
    xs = math.cos(start*step)*r
    ys = math.sin(start*step)*r
    xe = math.cos(end*step)*r
    ye = math.sin(end*step)*r
    if (start, end) in ans or (end, start) in ans:
        canvas.create_line(cx+xs, cy+ys, cx+xe, cy+ye, fill='green')
    else:
        canvas.create_line(cx+xs, cy+ys, cx+xe, cy+ye, fill='blue')

window.mainloop()
