#https://pyglet-readthedocs-io.translate.goog/en/latest/modules/shapes.html?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc

import sys
import pyglet
from pyglet import shapes

window = pyglet.window.Window(850, 650)

batch = pyglet.graphics.Batch()

file = 'rbolas.txt'
file = sys.argv[1]
fil = open(file,'r')
ll = fil.readlines()

print(ll)

x0 = 100
y0 = 200
radio = 20

# color=(50, 225, 30)


def Label(x0=0, y0=0, let=''):
  label = pyglet.text.Label(
    let,
    font_name='Times New Roman',
    font_size=24,
    color=(255, 255, 255),
    x= x0, y= y0,
    anchor_x='center', anchor_y='center'
  )
  label.draw()


def Circulo(x0=0, y0=0, let=''):
  circle = shapes.Circle(x0, y0, radio, color=(50, 225, 30), batch=batch)

  label = pyglet.text.Label(
    let,
    font_name='Times New Roman',
    font_size=24,
    color=(0, 0, 0),
    x= x0, y= y0,
    anchor_x='center', anchor_y='center'
  )
  batch.draw()
  label.draw()

  
@window.event

def on_draw():
    window.clear()
    del1 = 40
    y0 = 600
    delx = 100
    x0=350
    n = len(ll)
    for i in range(n):
      Label(x0+delx, y0, ll[i])
      y0 = y0-del1
    color_buffer = pyglet.image.get_buffer_manager().get_color_buffer()
        # Save to file
    color_buffer.save('screenshot.png')

pyglet.app.run()

