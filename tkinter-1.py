import tkinter as tk
import math


def calculate_position(data):

    center_x, center_y, radius, distance, angle, angle_speed, x, y = data

    # calculate new position of object
    x = center_x - distance * math.sin(math.radians(-angle))
    y = center_y - distance * math.cos(math.radians(-angle))

    data[6] = x
    data[7] = y

    x1 = x - radius
    y1 = y - radius
    x2 = x + radius
    y2 = y + radius

    return x1, y1, x2, y2

def create_object(data):
    # calculate oval coordinates
    x1, y1, x2, y2 = calculate_position(data)

    return c.create_oval(x1, y1, x2, y2)

def move_object(object_id, data):
    # calculate oval coordinates
    x1, y1, x2, y2 = calculate_position(data)

    c.coords(object_id, x1, y1, x2, y2)

def animate():
    # move earth - angle += angle_speed
    earth[4] += earth[5]
    move_object(e_id, earth)

    root.after(100, animate)


WIDTH  = 500
HEIGHT = 500

# center of solar system
center_x = WIDTH//2
center_y = HEIGHT//2

# objects data

sun = [center_x, center_y, 30, 0, 0, 0, 0, 0]
earth = [center_x, center_y, 5, 30, 0, 1, 0, 0]



root = tk.Tk()
root.title("Solar System")


c = tk.Canvas(root, width=WIDTH, heigh=HEIGHT)
c.pack()

# create sun and earth
s_id = create_object(sun)
e_id = create_object(earth)

animate()

root.mainloop()