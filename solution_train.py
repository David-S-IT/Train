from PIL import Image, ImageDraw

# from tkinter import *
# Попытка 1
# def train(file_output):
#     # sleep(123)
#     instance_tk = tk.Tk()
#     canvas = tk.Canvas(instance_tk, width=280 * 5, height=200 * 5)
#     canvas.pack()
# 
#     canvas.create_rectangle(5, 5, 1000, 1000, fill='red', outline="blue", width=0)
# 
#     instance_tk.update()
# 
#     # tk.mainloop()
# 
#     canvas.postscript(file="tmp.ps", colormode="color")

# Попытка 2
# def train(file_output):
#     window = Tk()
#     window_width, window_height = 280 * 5, 200 * 5
#
#     window['bg'] = "#ccecff"
#     window.geometry(f'{window_width}x{window_height}')
#
#     canvas = Canvas(window)
#     canvas.pack()
#
#     window.mainloop()

# Попытка 3
# def train(file_output):
#     window = Tk()
#     db = 1  # do_bigger
#     window.title('Паровозик')
#     window_width, window_height = 10, 10
#
#     window['bg'] = "#ccecff"
#     window.geometry(f'{window_width}x{window_height}')
#
#     canvas = Canvas(window, width=window_width, height=window_height, background="#ccecff", highlightthickness=0,
#                     borderwidth=0)
#     canvas.pack()
#
#     canvas.create_rectangle(0, 0, window_width, window_height, fill="#ccecff", outline="")  # Для фона
#
#     # Рисунок
#     canvas.create_rectangle(0, 0, 9, 9, fill="#c55a11", outline="")
#     # canvas.create_rectangle(40, 190, 80, 266, fill="#c55a11", outline="")  # 40, 190-1, 80, 230-1
#     # canvas.create_line(, fill="#c55a11", outline="#ccecff", width=0)
#
#     # Рисунок
#     window.update()
#     canvas.postscript(file='tmp.ps', colormode="color")
#
#     # ps_image = Image.open('tmp.ps')
#     # # print(ps_image.info)
#     # # ps_image.mode = "RGB"
#     # print(ps_image.mode)
#     # # ps_image.show()
#     # # ps_image.save(file_output)
#     #
#     # # png_image = Image.open('out.png')
#     # # ps_image.pilmode = "RGB"
#     # r,g,b = ps_image.split()
#     # ps_image = ps_image.dra
#     # ps_image.save('out.png')
#     # # ps_image.show()
#
#     # window.mainloop()


# Попытка 4
def train(file_output):
    # Заготовки
    # draw.ellipse((0, 0, 50, 50), fill='red')  # круг
    # draw.rectangle((40, 110, 80, 150), fill=(197, 90, 17))  # прямоугольник
    # draw.polygon([(100, 0), (0, 200), (200, 200)], fill='red')  # треугольник

    # фон
    im = Image.new('RGB', (280, 200), '#CCECFF')
    draw = ImageDraw.Draw(im)

    # Рисунок

    draw.rectangle((40, 150, 80, 110), fill='#C55A11')  # коричневый
    draw.rectangle((80, 150, 160, 90), fill='#0070C0')  # синий
    draw.polygon([(40, 110), (60, 75), (80, 110)], fill='#FFC000')  # желтый
    draw.rectangle((80, 90, 110, 60), fill='red')
    draw.polygon([(80, 60), (95, 34), (110, 60)], fill='#FFC000')  # желтый
    draw.rectangle((160, 150, 240, 50), fill='#548235')  # зеленый
    draw.rectangle((150, 50, 250, 40), fill='#C55A11')  # коричневый
    draw.rectangle((185, 100, 215, 60), fill='white')
    draw.ellipse((80, 140, 110, 170), fill='black')
    draw.ellipse((120, 130, 160, 170), fill='black')
    draw.ellipse((180, 130, 220, 170), fill='black')

    # Рисунок

    im.save(file_output, quality=100)
