import tkinter
import math


def draw_normal_axis(canvas):
    canvas.create_line(400, 0, 400, 400, fill="red", tags="y_axis")
    canvas.create_line(400, 0, 395, 10, fill="red", tags="y_axis")
    canvas.create_line(400, 0, 405, 10, fill="red", tags="y_axis")
    canvas.create_line(0, 200, 800, 200, fill="red", tags="x_axis")
    canvas.create_line(800, 200, 790, 195, fill="red", tags="x_axis")
    canvas.create_line(800, 200, 790, 205, fill="red", tags="x_axis")
    for i in range(15):
        canvas.create_line((i + 1) * 50, 200, (i + 1) * 50, 195, fill="red", tags="x_axis")
        if i == 7:
            canvas.create_text(405, 208, text='0')
        else:
            canvas.create_text((i + 1) * 50, 208, text=str(i - 7))
    for j in range(7):
        canvas.create_line(400, (j + 1) * 50, 405, (j + 1) * 50, fill="red", tags="y_axis")
        if j == 3:
            continue
        canvas.create_text(412, (j + 1) * 50, text=str(3 - j))


def draw_tri_axis(canvas):
    axis_name = ['-3/2π', '-π', '-1/2π', '0', '1/2π', 'π', '3/2π']
    canvas.create_line(400, 100, 405, 100, fill="red", tags="y_axis")
    canvas.create_text(412, 100, text='1')
    canvas.create_line(400, 300, 405, 300, fill="red", tags="y_axis")
    canvas.create_text(412, 300, text='-1')
    for i in range(7):
        canvas.create_line((i + 1) * 100, 200, (i + 1) * 100, 195, fill="red", tags="x_axis")
        if i == 3:
            canvas.create_text(412, 212, text='0')
            continue
        canvas.create_text((i + 1) * 100, 212, text=axis_name[i])


def main():
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, bg='white', width=800, height=400)
    canvas.create_line(400, 0, 400, 400, fill="red", tags="y_axis")
    canvas.create_line(400, 0, 395, 10, fill="red", tags="y_axis")
    canvas.create_line(400, 0, 405, 10, fill="red", tags="y_axis")
    canvas.create_line(0, 200, 800, 200, fill="red", tags="x_axis")
    canvas.create_line(800, 200, 790, 195, fill="red", tags="x_axis")
    canvas.create_line(800, 200, 790, 205, fill="red", tags="x_axis")
    draw_tri_axis(canvas)
    curve_coords = []
    for i in range(40, 760, 1):
        x = (i - 400) / 200 * math.pi
        y = 200 - math.sin(x) * 100
        curve_coords.append((i, y))
    # print(curve_coords)
    for i, coord in enumerate(curve_coords):
        if i == 0:
            continue
        canvas.create_line(curve_coords[i][0], curve_coords[i][1], curve_coords[i - 1][0], curve_coords[i - 1][1], width=2)
        # print(curve_coords[i][0], curve_coords[i][1], curve_coords[i - 1][0], curve_coords[i - 1][1])
    canvas.pack()
    root.mainloop()


if __name__ == '__main__':
    main()
